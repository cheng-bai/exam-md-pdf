#!/usr/bin/env python3
"""Render an exam Markdown file to PDF with Pandoc and XeLaTeX."""

from __future__ import annotations

import argparse
import shutil
import subprocess
import sys
from pathlib import Path


def run(command: list[str], cwd: Path) -> subprocess.CompletedProcess[str]:
    return subprocess.run(command, cwd=cwd, check=False, text=True)


def pdf_page_count(pdf_path: Path) -> int | None:
    pdfinfo = shutil.which("pdfinfo")
    if not pdfinfo:
        return None
    result = subprocess.run(
        [pdfinfo, str(pdf_path)],
        check=False,
        capture_output=True,
        text=True,
    )
    for line in result.stdout.splitlines():
        if line.startswith("Pages:"):
            return int(line.split(":", 1)[1].strip())
    return None


def main() -> int:
    parser = argparse.ArgumentParser(description="Render Markdown exam source to PDF.")
    parser.add_argument("markdown", help="Path to source.md")
    parser.add_argument("--output", help="Optional output PDF path")
    parser.add_argument("--expect-pages", type=int, help="Fail if the rendered PDF page count differs")
    parser.add_argument("--min-pages", type=int, help="Fail if the rendered PDF has fewer pages")
    args = parser.parse_args()

    source = Path(args.markdown).expanduser().resolve()
    if not source.exists():
        print(f"Markdown not found: {source}", file=sys.stderr)
        return 1
    if shutil.which("pandoc") is None:
        print("pandoc is not installed or not on PATH", file=sys.stderr)
        return 1
    if shutil.which("xelatex") is None:
        print("xelatex is not installed or not on PATH", file=sys.stderr)
        return 1

    output = Path(args.output).expanduser().resolve() if args.output else source.parent / "outputs" / f"{source.stem}.pdf"
    output.parent.mkdir(parents=True, exist_ok=True)

    command = [
        "pandoc",
        source.name,
        "-o",
        str(output),
        "--pdf-engine=xelatex",
    ]
    result = run(command, cwd=source.parent)
    if result.returncode != 0:
        print(f"Pandoc failed with exit code {result.returncode}", file=sys.stderr)
        return result.returncode

    size_kb = output.stat().st_size / 1024
    pages = pdf_page_count(output)
    if args.expect_pages is not None:
        if pages is None:
            print("Cannot verify expected pages because pdfinfo is unavailable", file=sys.stderr)
            return 1
        if pages != args.expect_pages:
            print(f"Expected {args.expect_pages} pages, got {pages}: {output}", file=sys.stderr)
            return 1
    if args.min_pages is not None:
        if pages is None:
            print("Cannot verify minimum pages because pdfinfo is unavailable", file=sys.stderr)
            return 1
        if pages < args.min_pages:
            print(f"Expected at least {args.min_pages} pages, got {pages}: {output}", file=sys.stderr)
            return 1
    print(f"Rendered PDF: {output}")
    print(f"Size: {size_kb:.1f} KB")
    print(f"Pages: {pages if pages is not None else 'unknown'}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
