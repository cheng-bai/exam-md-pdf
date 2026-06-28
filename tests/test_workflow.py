#!/usr/bin/env python3
"""Regression tests for the local exam workflow scripts."""

from __future__ import annotations

import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]


class WorkflowTests(unittest.TestCase):
    def test_new_exam_missing_pdf_does_not_leave_exam_directory(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            result = subprocess.run(
                [
                    sys.executable,
                    str(REPO_ROOT / "scripts" / "new_exam.py"),
                    "2026-上海-高三数学-一模",
                    "--pdf",
                    str(tmp_path / "missing.pdf"),
                ],
                cwd=tmp_path,
                check=False,
                capture_output=True,
                text=True,
            )

            self.assertNotEqual(result.returncode, 0)
            self.assertFalse((tmp_path / "exams").exists())

    def test_render_exam_fails_when_expected_pages_do_not_match(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            markdown = tmp_path / "source.md"
            markdown.write_text(
                "---\n"
                "title: Page Check\n"
                "geometry: margin=2cm\n"
                "CJKmainfont: Songti SC\n"
                "---\n\n"
                "# Page Check\n\n"
                "Only one page.\n",
                encoding="utf-8",
            )

            result = subprocess.run(
                [
                    sys.executable,
                    str(REPO_ROOT / "scripts" / "render_exam.py"),
                    str(markdown),
                    "--expect-pages",
                    "2",
                ],
                cwd=tmp_path,
                check=False,
                capture_output=True,
                text=True,
            )

            self.assertNotEqual(result.returncode, 0)
            self.assertIn("Expected 2 pages", result.stderr)


if __name__ == "__main__":
    unittest.main()

