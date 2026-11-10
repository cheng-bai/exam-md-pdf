#!/usr/bin/env python3
"""Regression tests for preservation, repeat builds, and refusal boundaries."""

from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

from bs4 import BeautifulSoup


SCRIPT = Path(__file__).with_name("prepare_publication.py")


class PrepareTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix="html-publication-test-")
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.source = self.root / "baseline.html"
        self.output = self.root / "教师阅读版.html"
        self.source.write_text('<html lang="zh-CN"><head><title>旧标题</title></head>'
                               '<body><h1>正文标题</h1><h2 id="kept">方法</h2><p>内容不变。</p></body></html>')
        self.original = self.source.read_bytes()

    def run_prepare(self, *extra, output=None):
        return subprocess.run([sys.executable, str(SCRIPT), str(self.source),
                               "--output", str(output or self.output), "--title", "阅读版", *extra],
                              capture_output=True, text=True)

    def test_preserve_and_ascii_entry(self):
        result = self.run_prepare("--density", "compact")
        self.assertEqual(result.returncode, 0, result.stderr)
        doc = BeautifulSoup(self.output.read_text(), "html.parser")
        original = BeautifulSoup(self.source.read_text(), "html.parser")
        self.assertEqual(doc.body.get_text(), original.body.get_text())
        self.assertEqual(doc.select_one("h2")["id"], "kept")
        self.assertTrue(doc.h1.get("id"))
        self.assertEqual(self.source.read_bytes(), self.original)
        self.assertEqual((self.root / "publication-entry.html").resolve(), self.output.resolve())
        self.assertIn("line-height: 1.38", (self.root / "publication-layout.css").read_text())

    def test_repeated_build_requires_replace(self):
        self.assertEqual(self.run_prepare().returncode, 0)
        self.assertNotEqual(self.run_prepare().returncode, 0)
        again = self.run_prepare("--replace")
        self.assertEqual(again.returncode, 0, again.stderr)

    def test_refuse_in_place(self):
        self.assertNotEqual(self.run_prepare("--replace", output=self.source).returncode, 0)
        self.assertEqual(self.source.read_bytes(), self.original)

    def test_refuse_unrendered_math(self):
        self.source.write_text(self.source.read_text().replace("</p>", '</p><span class="math">\\(x^2\\)</span>', 1))
        self.assertNotEqual(self.run_prepare().returncode, 0)
        self.assertFalse(self.output.exists())

    def test_refuse_duplicate_ids(self):
        self.source.write_text(self.source.read_text().replace("<h1>", '<h1 id="kept">'))
        self.assertNotEqual(self.run_prepare().returncode, 0)

    def test_refuse_preexisting_pdf(self):
        pdf = self.output.with_suffix(".pdf")
        pdf.write_bytes(b"existing output")
        self.assertNotEqual(self.run_prepare().returncode, 0)
        self.assertEqual(pdf.read_bytes(), b"existing output")

    def test_refuse_ascii_alias_source_collision(self):
        self.source = self.source.rename(self.root / "publication-entry.html")
        self.assertNotEqual(self.run_prepare("--replace").returncode, 0)
        self.assertEqual(self.source.read_bytes(), self.original)

    def test_refuse_resource_relocation(self):
        (self.root / "other").mkdir()
        self.assertNotEqual(self.run_prepare(output=self.root / "other/edition.html").returncode, 0)


if __name__ == "__main__":
    unittest.main()
