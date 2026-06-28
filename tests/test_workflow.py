#!/usr/bin/env python3
"""Regression tests for the local exam workflow scripts."""

from __future__ import annotations

import subprocess
import os
import sys
import tempfile
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]


class WorkflowTests(unittest.TestCase):
    def test_mineru_parse_dry_run_with_token_does_not_write_temp_config(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            source = tmp_path / "source.pdf"
            source.write_bytes(b"%PDF-1.4\n")
            archive_script = tmp_path / "mineru_parse.py"
            archive_script.write_text("#!/usr/bin/env python3\n", encoding="utf-8")
            before = {path.name for path in tmp_path.iterdir()}
            env = {
                **os.environ,
                "MINERU_API_TOKEN": "fake-token-for-dry-run",
                "TMPDIR": str(tmp_path),
            }
            env.pop("MINERU_TOKEN_CONFIG", None)

            result = subprocess.run(
                [
                    sys.executable,
                    str(REPO_ROOT / "scripts" / "mineru_parse_exam.py"),
                    str(source),
                    "--archive-script",
                    str(archive_script),
                    "--dry-run",
                ],
                cwd=tmp_path,
                env=env,
                check=False,
                capture_output=True,
                text=True,
            )

            after = {path.name for path in tmp_path.iterdir()}
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertEqual(before, after)
            self.assertIn("<temporary-token-config>", result.stdout)
            self.assertNotIn("fake-token-for-dry-run", result.stdout)

    def test_mineru_parse_dry_run_uses_config_without_calling_api(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            source = tmp_path / "source.pdf"
            source.write_bytes(b"%PDF-1.4\n")
            archive_script = tmp_path / "mineru_parse.py"
            archive_script.write_text("#!/usr/bin/env python3\n", encoding="utf-8")
            token_config = tmp_path / "mineru-config.json"
            token_config.write_text('{"config":"{\\"state\\":{\\"client_api_token\\":\\"fake-token\\"}}"}', encoding="utf-8")
            env = {**os.environ, "MINERU_TOKEN_CONFIG": str(token_config)}

            result = subprocess.run(
                [
                    sys.executable,
                    str(REPO_ROOT / "scripts" / "mineru_parse_exam.py"),
                    str(source),
                    "--archive-script",
                    str(archive_script),
                    "--dry-run",
                ],
                cwd=tmp_path,
                env=env,
                check=False,
                capture_output=True,
                text=True,
            )

            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertIn("mineru_parse.py", result.stdout)
            self.assertIn("--token-config", result.stdout)
            self.assertNotIn("Bearer", result.stdout)
            self.assertNotIn("MINERU_API_TOKEN", result.stdout)

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

    def test_new_exam_uses_chinese_work_draft_directory(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            result = subprocess.run(
                [
                    sys.executable,
                    str(REPO_ROOT / "scripts" / "new_exam.py"),
                    "2026上海市建平中学高三数学一模试卷",
                ],
                cwd=tmp_path,
                check=False,
                capture_output=True,
                text=True,
            )

            exam_dir = tmp_path / "exams" / "2026上海市建平中学高三数学一模试卷-工作稿"
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertTrue((exam_dir / "source.md").exists())
            self.assertTrue((exam_dir / "figures").is_dir())
            self.assertTrue((exam_dir / "outputs").is_dir())

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
