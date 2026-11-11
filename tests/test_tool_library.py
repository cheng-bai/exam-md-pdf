from __future__ import annotations

import hashlib
import json
import re
import shutil
import subprocess
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PUBLIC_SKILLS = [
    "paper-exam-to-md-pdf",
    "annotating-math-exam-solutions",
    "math-docx-to-markdown",
    "paddleocr-text-recognition",
]
LIBRARY_ROOTS = [ROOT / "tools", ROOT / "templates", ROOT / "workflows"] + [
    ROOT / "skills" / name for name in PUBLIC_SKILLS
]


class ToolLibraryTests(unittest.TestCase):
    def test_public_skills_have_matching_frontmatter_names(self) -> None:
        for name in PUBLIC_SKILLS:
            skill_file = ROOT / "skills" / name / "SKILL.md"
            self.assertTrue(skill_file.is_file(), skill_file)
            text = skill_file.read_text(encoding="utf-8")
            match = re.search(r"(?m)^name:\s*(.+?)\s*$", text)
            self.assertIsNotNone(match, skill_file)
            self.assertEqual(match.group(1), name)

    def test_public_library_has_no_machine_absolute_paths(self) -> None:
        mac_path = re.compile(r"(?:^|[\s`\"'])(/Users/[^\s`\"']+)")
        windows_path = re.compile(r"(?:^|[\s`\"'])([A-Za-z]:[\\/][^\s`\"']*)")
        findings: list[str] = []
        for root in LIBRARY_ROOTS:
            for path in root.rglob("*"):
                if not path.is_file() or path.suffix not in {".md", ".py", ".yaml", ".yml", ".txt"}:
                    continue
                text = path.read_text(encoding="utf-8", errors="replace")
                for line_no, line in enumerate(text.splitlines(), start=1):
                    without_urls = re.sub(r"https?://\S+", "", line)
                    if mac_path.search(without_urls) or windows_path.search(without_urls):
                        findings.append(f"{path.relative_to(ROOT)}:{line_no}")
        self.assertEqual(findings, [])

    def test_tool_library_markdown_links_resolve(self) -> None:
        broken: list[str] = []
        link_pattern = re.compile(r"(?<!!)\[[^\]]+\]\(([^)]+)\)")
        for folder in (ROOT / "tools", ROOT / "templates", ROOT / "workflows"):
            for path in folder.rglob("*.md"):
                text = path.read_text(encoding="utf-8")
                for raw in link_pattern.findall(text):
                    link = raw.strip().split()[0].strip("<>")
                    if re.match(r"^(?:https?:|mailto:|#)", link):
                        continue
                    target = (path.parent / link.split("#", 1)[0]).resolve()
                    if not target.exists():
                        broken.append(f"{path.relative_to(ROOT)} -> {link}")
        self.assertEqual(broken, [])

    def test_exam_template_declares_a4(self) -> None:
        template = (ROOT / "templates" / "高中数学试卷A4模板.md").read_text(encoding="utf-8")
        self.assertIn("papersize: a4", template)
        self.assertIn("geometry: a4paper,margin=2cm", template)

    def test_exam_template_renders_to_a4_when_toolchain_is_available(self) -> None:
        required = ["pandoc", "xelatex", "pdfinfo"]
        if any(shutil.which(command) is None for command in required):
            self.skipTest("Pandoc/XeLaTeX/pdfinfo toolchain is unavailable")
        with tempfile.TemporaryDirectory() as tmpdir:
            output = Path(tmpdir) / "高中数学试卷A4模板.pdf"
            result = subprocess.run(
                [
                    "python3",
                    str(ROOT / "scripts" / "render_exam.py"),
                    str(ROOT / "templates" / "高中数学试卷A4模板.md"),
                    "--output",
                    str(output),
                    "--min-pages",
                    "1",
                ],
                capture_output=True,
                text=True,
                check=False,
            )
            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
            info = subprocess.run(["pdfinfo", str(output)], capture_output=True, text=True, check=False)
            self.assertEqual(info.returncode, 0, info.stderr)
            self.assertRegex(info.stdout, r"(?m)^Page size:\s+59[45]\..* x 84[12]\..*\(A4\)")

    def test_paddleocr_provenance_and_local_integrity(self) -> None:
        provenance = json.loads((ROOT / "tools" / "provenance.json").read_text(encoding="utf-8"))
        paddle = next(
            item for item in provenance["assets"]
            if item["path"] == "skills/paddleocr-text-recognition/SKILL.md"
        )
        self.assertEqual(paddle["source_repo"], "PaddlePaddle/PaddleOCR")
        self.assertEqual(paddle["source_path"], "skills/paddleocr-text-recognition/SKILL.md")
        self.assertEqual(paddle["source_commit"], "1e5aa0ad31bc8a82cd8e1daef7adc24e577d2534")
        self.assertEqual(
            paddle["source_sha256"],
            "7696b3c79521d71c483391904524b0da2fd4051e574566140c72ec023dbfe1b3",
        )
        local_skill = ROOT / paddle["path"]
        self.assertEqual(
            hashlib.sha256(local_skill.read_bytes()).hexdigest(),
            "cd6b328b8bf40ec7639fb24a0be690ac91cb4b81fc5e0534831a0554ecb7dc85",
        )
        self.assertEqual(
            hashlib.sha256((ROOT / "tools" / "licenses" / "Apache-2.0.txt").read_bytes()).hexdigest(),
            "3840c5c0c61c294264d2dd77b8777be6ddd90121ef4e0e64abcd22edea581d6e",
        )

    def test_toolkit_license_scope_excludes_content_directories(self) -> None:
        license_text = (ROOT / "TOOLKIT_LICENSE.md").read_text(encoding="utf-8")
        for tool_dir in ("skills/", "scripts/", "templates/", "workflows/", "tools/", "tests/"):
            self.assertIn(f"`{tool_dir}`", license_text)
        for content_dir in ("exams/", "handouts/", "collections/", "资料来源/", "inputs/", "outputs/", "work/"):
            self.assertIn(f"`{content_dir}`", license_text)
        self.assertIn("明确排除", license_text)

    def test_personal_skill_authorizations_are_resolved(self) -> None:
        provenance = json.loads((ROOT / "tools" / "provenance.json").read_text(encoding="utf-8"))
        personal = [item for item in provenance["assets"] if item.get("source") == "user-local-personal-skill"]
        self.assertEqual(len(personal), 3)
        for item in personal:
            self.assertEqual(item.get("license"), "Apache-2.0")
            self.assertEqual(item.get("authorization"), "confirmed-by-repository-owner")
            self.assertRegex(item.get("confirmed_at", ""), r"^\d{4}-\d{2}-\d{2}$")

    def test_paper_exam_skill_references_only_packaged_ocr_routes(self) -> None:
        text = (ROOT / "skills" / "paper-exam-to-md-pdf" / "SKILL.md").read_text(encoding="utf-8")
        self.assertNotIn("ppocrv5", text)
        for dependency in ("paddleocr-text-recognition", "mineru-document-workflow"):
            self.assertIn(dependency, text)
            self.assertTrue((ROOT / "skills" / dependency / "SKILL.md").is_file())

    def test_public_library_has_no_embedded_secret_values(self) -> None:
        assignment = re.compile(
            r"(?i)(?:api[_-]?key|access[_-]?token|password|secret|cookie)\s*[:=]\s*[\"']([^\"']+)[\"']"
        )
        findings: list[str] = []
        for root in LIBRARY_ROOTS:
            for path in root.rglob("*"):
                if not path.is_file() or path.suffix not in {".md", ".py", ".yaml", ".yml", ".json"}:
                    continue
                for line_no, line in enumerate(path.read_text(encoding="utf-8", errors="replace").splitlines(), 1):
                    match = assignment.search(line)
                    if match and not match.group(1).startswith(("${", "<")):
                        findings.append(f"{path.relative_to(ROOT)}:{line_no}")
        self.assertEqual(findings, [])


if __name__ == "__main__":
    unittest.main()
