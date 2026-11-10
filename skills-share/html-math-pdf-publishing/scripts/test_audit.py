#!/usr/bin/env python3
"""Regression checks for conservative offline font fallback handling."""
import json
import subprocess
import sys
import tempfile
from pathlib import Path
import fitz

AUDIT = Path(__file__).with_name("audit_publication.py")


def main():
    with tempfile.TemporaryDirectory(prefix="html-math-audit-test-") as temp:
        root = Path(temp)
        valid_pdf = root / "valid.pdf"
        doc = fitz.open()
        doc.new_page(width=595, height=842).insert_text((50, 50), "fixture")
        doc.set_metadata({"author": "chengbai"})
        doc.save(valid_pdf)
        doc.close()
        (root / "available.woff2").write_bytes(b"fixture-font")
        cases = {
            "usable_fallback": ('@font-face { src: url("available.woff2"), url("missing.woff"); }', 0, "missing_fallback"),
            "external_fallback": ('@font-face { src: url("available.woff2"), url("missing.woff"); }', 0, "missing_fallback"),
            "all_missing": ('@font-face { src: url("missing.woff2"), url("missing.woff"); }', 1, "missing"),
            "remote_candidate": ('@font-face { src: url("https://example.invalid/font.woff2"), url("available.woff2"); }', 1, "remote"),
            "ordinary_resource": ('p { background: url("absent.png"); }', 1, "missing"),
            "single_missing": ('@font-face { src: url("missing.woff"); }', 1, "missing"),
            "duplicate_url_outside_font": ('@font-face { src: url("available.woff2"), url("missing.woff"); } p { background: url("missing.woff"); }', 1, "missing"),
            "multiple_src": ('@font-face { src: url("available.woff2"); src: url("missing.woff"); }', 1, "missing"),
        }
        for name, (css, expected_exit, expected_status) in cases.items():
            source = root / f"{name}.html"
            report = root / f"{name}.json"
            head = f"<style>{css}</style>"
            if name == "external_fallback":
                (root / "external.css").write_text(css, encoding="utf-8")
                head = '<link rel="stylesheet" href="external.css">'
            source.write_text(f"<html><head>{head}</head><body>fixture</body></html>", encoding="utf-8")
            result = subprocess.run(
                [sys.executable, str(AUDIT), "--html", str(source), "--pdf", str(valid_pdf), "--report", str(report)],
                capture_output=True, text=True, check=False,
            )
            assert result.returncode == expected_exit, (name, result.returncode, result.stdout, result.stderr)
            checks = json.loads(report.read_text(encoding="utf-8"))["checks"]["offline_static_resources"]
            statuses = {item["status"] for item in checks["resources"]}
            assert expected_status in statuses, (name, statuses)
            if name in ("usable_fallback", "external_fallback"):
                assert len(checks["warnings"]) == 1, checks["warnings"]
        print(f"PASS: {len(cases)} offline font/resource boundary regressions")


if __name__ == "__main__":
    main()
