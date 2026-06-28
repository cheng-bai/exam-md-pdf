#!/usr/bin/env python3
"""Check tools needed by the exam digitization workflow."""

from __future__ import annotations

import shutil
import subprocess
import sys
from pathlib import Path


REQUIRED = ["git", "gh", "pandoc", "xelatex", "python3"]
RECOMMENDED = ["magick", "pdfinfo", "pdftotext", "qpdf"]

VERSION_ARGS = {
    "pdfinfo": ["-v"],
    "pdftotext": ["-v"],
}


def find_command(command: str) -> str | None:
    path = shutil.which(command)
    if path:
        return path

    poppler_bins = Path.home().glob(".cache/codex-runtimes/*/dependencies/native/poppler/poppler/bin")
    for directory in poppler_bins:
        candidate = directory / command
        if candidate.exists() and candidate.is_file():
            return str(candidate)
    return None


def command_version(command: str, path: str) -> str:
    version_args = VERSION_ARGS.get(command, ["--version"])
    try:
        result = subprocess.run(
            [path, *version_args],
            check=False,
            capture_output=True,
            text=True,
            timeout=10,
        )
    except Exception as exc:  # pragma: no cover - diagnostic path
        return f"version check failed: {exc}"
    first_line = (result.stdout or result.stderr).splitlines()
    return first_line[0] if first_line else "installed"


def print_check(command: str, required: bool) -> bool:
    path = find_command(command)
    label = "required" if required else "recommended"
    if not path:
        print(f"FAIL {command:<10} missing ({label})")
        return not required
    print(f"OK   {command:<10} {path} - {command_version(command, path)}")
    return True


def check_gh_auth() -> bool:
    if not shutil.which("gh"):
        return False
    result = subprocess.run(
        ["gh", "auth", "status"],
        check=False,
        capture_output=True,
        text=True,
        timeout=15,
    )
    if result.returncode == 0:
        print("OK   gh auth    GitHub CLI is logged in")
        return True
    print("FAIL gh auth    run: gh auth login")
    return False


def main() -> int:
    ok = True
    for command in REQUIRED:
        ok = print_check(command, required=True) and ok
    for command in RECOMMENDED:
        print_check(command, required=False)
    ok = check_gh_auth() and ok
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
