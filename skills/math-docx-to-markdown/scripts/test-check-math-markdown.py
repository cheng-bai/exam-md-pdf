#!/usr/bin/env python3
"""Tests for check-math-markdown structural scanners."""

from __future__ import annotations

import importlib.util
import tempfile
from pathlib import Path


SCRIPT = Path(__file__).with_name("check-math-markdown.py")
SPEC = importlib.util.spec_from_file_location("check_math_markdown", SCRIPT)
assert SPEC and SPEC.loader
checker = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(checker)


def test_split_or_and_math_finds_broken_set_builder() -> None:
    text = "答案为$\\{ x|x < -2$或$x > 1\\}$。"

    findings = checker.scan_split_connective_math(text)

    assert findings
    assert findings[0]["type"] == "split_connective_math"
    assert findings[0]["line"] == 1


def test_split_or_and_math_finds_broken_condition_parentheses() -> None:
    text = "函数$y=\\log_a x + a\\left( a>0 \\right.$且$\\left. a\\neq1 \\right)$。"

    findings = checker.scan_split_connective_math(text)

    assert findings
    assert findings[0]["type"] == "split_connective_math"


def test_split_or_and_math_ignores_normal_adjacent_equations() -> None:
    text = "解得$x = 1$或$x = 2$，所以答案为 B。"

    findings = checker.scan_split_connective_math(text)

    assert findings == []


def test_scan_markdown_includes_split_or_and_warning() -> None:
    with tempfile.TemporaryDirectory() as tmpdir:
        path = Path(tmpdir) / "sample.md"
        path.write_text("答案为$\\{ x|x < -2$或$x > 1\\}$。", encoding="utf-8")

        findings = checker.scan_markdown(path, [])

    assert any(f["type"] == "split_connective_math" for f in findings)


if __name__ == "__main__":
    tests = [
        test_split_or_and_math_finds_broken_set_builder,
        test_split_or_and_math_finds_broken_condition_parentheses,
        test_split_or_and_math_ignores_normal_adjacent_equations,
        test_scan_markdown_includes_split_or_and_warning,
    ]
    for test in tests:
        test()
    print(f"{len(tests)} tests passed")
