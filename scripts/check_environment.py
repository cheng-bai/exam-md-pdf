#!/usr/bin/env python3
"""Check tools needed by the exam digitization workflow."""

from __future__ import annotations

import json
import os
import shutil
import subprocess
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
REQUIRED = ["git", "gh", "pandoc", "xelatex", "python3"]
RECOMMENDED = ["magick", "pdfinfo", "pdftotext", "qpdf"]
MINERU_ARCHIVE_SCRIPT = Path.home() / ".codex/skills/mineru-document-parser/scripts/mineru_parse.py"
DEFAULT_MINERU_TOKEN_CONFIG = Path.home() / "MinerU/config.json"

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


def load_dotenv(path: Path) -> dict[str, str]:
    values: dict[str, str] = {}
    if not path.exists():
        return values
    for raw_line in path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        values[key.strip()] = value.strip().strip('"').strip("'")
    return values


def check_mineru_api() -> bool:
    values = load_dotenv(REPO_ROOT / ".env")
    values.update(os.environ)

    if MINERU_ARCHIVE_SCRIPT.exists():
        print(f"OK   mineru api script {MINERU_ARCHIVE_SCRIPT}")
    else:
        print(f"WARN mineru api script missing: {MINERU_ARCHIVE_SCRIPT}")

    if values.get("MINERU_API_TOKEN"):
        print("OK   mineru api token configured via MINERU_API_TOKEN")
        return True

    config_path = Path(values.get("MINERU_TOKEN_CONFIG", str(DEFAULT_MINERU_TOKEN_CONFIG))).expanduser()
    if not config_path.exists():
        print(f"WARN mineru api token config missing: {config_path}")
        return False

    try:
        outer = json.loads(config_path.read_text(encoding="utf-8"))
        inner = json.loads(outer.get("config", "{}"))
        token = inner.get("state", {}).get("client_api_token", "")
    except Exception as exc:  # pragma: no cover - diagnostic path
        print(f"WARN mineru api token config unreadable: {config_path} ({exc})")
        return False
    if not token:
        print(f"WARN mineru api token missing in config: {config_path}")
        return False
    print(f"OK   mineru api token configured via {config_path}")
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
    check_mineru_api()
    ok = check_gh_auth() and ok
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
