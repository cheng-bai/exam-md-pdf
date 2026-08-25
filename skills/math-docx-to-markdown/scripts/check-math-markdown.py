#!/usr/bin/env python3
"""Check math-heavy Markdown converted from DOCX."""

from __future__ import annotations

import argparse
import json
import re
import shutil
import subprocess
import sys
import zipfile
from pathlib import Path


RAW_PATTERNS = [
    ("error", "broken_left_right_bar", r"\\left\|\s*\\right\."),
    ("error", "bare_geqslant_after_dollar", r"\$\\geqslant"),
    ("error", "omml_xml_residue", r"</?m:|<m:oMath|OMML"),
    ("error", "replacement_character", "\ufffd"),
    ("warning", "possible_lost_subset_before_set", r"[A-Z]\\s*\\left\\\{"),
    ("warning", "possible_word_gt_as_angle", r"\\right\\rangle\s*[-+0-9A-Za-z]"),
]

MATH_PATTERNS = [
    ("error", "broken_left_right_bar", r"\\left\|\s*\\right\."),
    ("error", "unbalanced_left_right", None),
    ("warning", "cjk_text_inside_math", r"[\u4e00-\u9fff]"),
    ("warning", "possible_word_gt_as_angle", r"\\right\\rangle\s*[-+0-9A-Za-z]"),
]


def run(cmd: list[str]) -> subprocess.CompletedProcess[str]:
    return subprocess.run(cmd, text=True, capture_output=True, check=False)


def require_pandoc() -> None:
    if not shutil.which("pandoc"):
        raise SystemExit("FAIL: pandoc not found in PATH")


def count_docx_omml(path: Path) -> tuple[int, dict[str, int]] | tuple[None, dict[str, int]]:
    if not path:
        return None, {}
    counts: dict[str, int] = {}
    with zipfile.ZipFile(path) as zf:
        for name in sorted(zf.namelist()):
            if not (name.startswith("word/") and name.endswith(".xml")):
                continue
            xml = zf.read(name).decode("utf-8", errors="replace")
            count = len(re.findall(r"<m:oMath(?:Para)?\b", xml))
            if count:
                counts[name] = count
    return sum(counts.values()), counts


def pandoc_math_items(md_path: Path) -> tuple[list[str], str]:
    proc = run(["pandoc", str(md_path), "-t", "json"])
    if proc.returncode != 0:
        raise SystemExit(f"FAIL: pandoc JSON parse failed\n{proc.stderr}")
    data = json.loads(proc.stdout)

    def walk(node):
        if isinstance(node, dict):
            if node.get("t") == "Math":
                yield node
            for value in node.values():
                yield from walk(value)
        elif isinstance(node, list):
            for item in node:
                yield from walk(item)

    math_items = [node["c"][1] for node in walk(data)]
    return math_items, proc.stdout


def mathml_check(md_path: Path, html_out: Path | None) -> tuple[int, list[str]]:
    cleanup = html_out is None
    html_path = html_out or Path(str(md_path) + ".math-check.tmp.html")

    proc = run(["pandoc", str(md_path), "--mathml", "-s", "-o", str(html_path)])
    if proc.returncode != 0:
        raise SystemExit(f"FAIL: pandoc MathML export failed\n{proc.stderr}")

    html = html_path.read_text(encoding="utf-8", errors="replace")
    errors = ["merror"] if re.search(r"<merror\b", html) else []
    if cleanup:
        html_path.unlink(missing_ok=True)
    return len(re.findall(r"<math\b", html)), errors


def non_code_lines(text: str):
    in_fence = False
    for line_no, line in enumerate(text.splitlines(), start=1):
        if re.match(r"^\s*(```|~~~)", line):
            in_fence = not in_fence
            continue
        if not in_fence:
            yield line_no, line


def add_finding(
    findings: list[dict[str, object]], severity: str, kind: str, text: str, line: int | None = None
) -> None:
    item: dict[str, object] = {"severity": severity, "type": kind, "text": text.strip()[:200]}
    if line is not None:
        item["line"] = line
    findings.append(item)


def has_open_set_without_close(math: str) -> bool:
    return bool(re.search(r"(\\left\\\{|\\\{|(?<!\\)\{)", math)) and not bool(
        re.search(r"(\\right\\\}|\\\}|(?<!\\)\})", math)
    )


def has_close_set_without_open(math: str) -> bool:
    return bool(re.search(r"(\\right\\\}|\\\}|(?<!\\)\})", math)) and not bool(
        re.search(r"(\\left\\\{|\\\{|(?<!\\)\{)", math)
    )


def has_split_left_right_boundary(left_math: str, right_math: str) -> bool:
    return (
        bool(re.search(r"\\right\.\s*$", left_math))
        or bool(re.search(r"^\s*\\left\.", right_math))
    )


def scan_split_connective_math(text: str) -> list[dict[str, object]]:
    findings: list[dict[str, object]] = []
    inline_math = re.compile(r"(?<!\\)\$(.*?)(?<!\\)\$")

    for line_no, line in non_code_lines(text):
        spans = list(inline_math.finditer(line))
        for left, right in zip(spans, spans[1:]):
            between = line[left.end() : right.start()]
            if "或" not in between and "且" not in between:
                continue

            left_math = left.group(1)
            right_math = right.group(1)
            if not (
                has_open_set_without_close(left_math)
                or has_close_set_without_open(right_math)
                or has_split_left_right_boundary(left_math, right_math)
            ):
                continue

            snippet = line[left.start() : right.end()]
            add_finding(findings, "warning", "split_connective_math", snippet, line_no)

    return findings


def scan_markdown(md_path: Path, math_items: list[str]) -> list[dict[str, object]]:
    text = md_path.read_text(encoding="utf-8", errors="replace")
    findings: list[dict[str, object]] = []

    for severity, name, pattern in RAW_PATTERNS:
        regex = re.compile(pattern)
        for line_no, line in non_code_lines(text):
            if regex.search(line):
                add_finding(findings, severity, name, line, line_no)

    total_dollar_count = sum(
        len(re.findall(r"(?<!\\)\$", line)) for _, line in non_code_lines(text)
    )
    if total_dollar_count % 2 == 1:
        add_finding(
            findings,
            "error",
            "odd_dollar_count",
            f"total unescaped dollar count is odd: {total_dollar_count}",
        )

    findings.extend(scan_split_connective_math(text))

    for math in math_items:
        left_count = len(re.findall(r"\\left\b", math))
        right_count = len(re.findall(r"\\right\b", math))
        if left_count != right_count:
            add_finding(findings, "error", "unbalanced_left_right", math)
        for severity, name, pattern in MATH_PATTERNS:
            if name == "unbalanced_left_right":
                continue
            if pattern and re.search(pattern, math):
                add_finding(findings, severity, name, math)

    return findings


def main() -> int:
    parser = argparse.ArgumentParser(description="Verify Markdown math converted from DOCX.")
    parser.add_argument("markdown", type=Path)
    parser.add_argument("--source-docx", type=Path)
    parser.add_argument("--html-out", type=Path)
    parser.add_argument("--accept-count-delta", action="store_true")
    parser.add_argument("--allow-warnings", action="store_true")
    args = parser.parse_args()

    require_pandoc()
    if not args.markdown.exists():
        raise SystemExit(f"FAIL: Markdown not found: {args.markdown}")
    if args.source_docx and not args.source_docx.exists():
        raise SystemExit(f"FAIL: source DOCX not found: {args.source_docx}")

    source_count, source_parts = count_docx_omml(args.source_docx) if args.source_docx else (None, {})
    math_items, _ = pandoc_math_items(args.markdown)
    markdown_count = len(math_items)
    mathml_count, mathml_errors = mathml_check(args.markdown, args.html_out)
    findings = scan_markdown(args.markdown, math_items)

    if source_count is not None and source_count != markdown_count:
        add_finding(
            findings,
            "warning",
            "source_markdown_math_count_delta",
            f"source OMML count {source_count}, Markdown math count {markdown_count}",
        )

    report = {
        "markdown": str(args.markdown),
        "source_docx": str(args.source_docx) if args.source_docx else None,
        "source_omml_count": source_count,
        "source_omml_parts": source_parts,
        "markdown_math_count": markdown_count,
        "mathml_count": mathml_count,
        "mathml_errors": mathml_errors,
        "findings": findings,
    }
    print(json.dumps(report, ensure_ascii=False, indent=2))

    errors = [f for f in findings if f.get("severity") == "error"]
    warnings = [f for f in findings if f.get("severity") == "warning"]
    count_delta_unaccepted = any(
        f.get("type") == "source_markdown_math_count_delta" for f in warnings
    ) and not (args.accept_count_delta or args.allow_warnings)
    effective_warnings = [
        f
        for f in warnings
        if not (
            args.accept_count_delta
            and f.get("type") == "source_markdown_math_count_delta"
        )
    ]
    warning_failure = bool(effective_warnings) and not args.allow_warnings

    if mathml_errors or errors or markdown_count != mathml_count or count_delta_unaccepted or warning_failure:
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
