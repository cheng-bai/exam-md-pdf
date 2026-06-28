#!/usr/bin/env python3
"""Run the MinerU API archive parser with project-local defaults."""

from __future__ import annotations

import argparse
import json
import os
import shlex
import subprocess
import sys
import tempfile
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_ARCHIVE_SCRIPT = Path.home() / ".codex/skills/mineru-document-parser/scripts/mineru_parse.py"
DEFAULT_TOKEN_CONFIG = Path.home() / "MinerU/config.json"


def load_dotenv(path: Path) -> dict[str, str]:
    values: dict[str, str] = {}
    if not path.exists():
        return values
    for raw_line in path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        key = key.strip()
        value = value.strip().strip('"').strip("'")
        if key:
            values[key] = value
    return values


def merged_env() -> dict[str, str]:
    values = load_dotenv(REPO_ROOT / ".env")
    values.update(os.environ)
    return values


def token_config_path(values: dict[str, str]) -> Path:
    configured = values.get("MINERU_TOKEN_CONFIG", "")
    return Path(configured).expanduser() if configured else DEFAULT_TOKEN_CONFIG


def write_temp_token_config(token: str) -> tempfile.NamedTemporaryFile[str]:
    payload = {"config": json.dumps({"state": {"client_api_token": token}}, ensure_ascii=False)}
    handle = tempfile.NamedTemporaryFile("w", encoding="utf-8", suffix=".json", delete=False)
    json.dump(payload, handle, ensure_ascii=False)
    handle.flush()
    handle.close()
    return handle


def default_output_dir(source: Path) -> Path:
    return REPO_ROOT / "outputs" / f"{source.stem}-MinerU归档"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Parse PDFs/images through MinerU API.")
    parser.add_argument("files", nargs="+", help="PDF/image files to parse")
    parser.add_argument("--output-dir", help="Directory to save MinerU archive outputs")
    parser.add_argument("--language", default="ch", help="MinerU language code")
    parser.add_argument("--layout-model", default="doclayout_yolo", help="MinerU layout model")
    parser.add_argument("--no-formula", action="store_true", help="Disable formula recognition")
    parser.add_argument("--no-table", action="store_true", help="Disable table recognition")
    parser.add_argument("--no-ocr", action="store_true", help="Disable OCR")
    parser.add_argument("--poll-interval", type=float, default=5.0, help="Polling interval in seconds")
    parser.add_argument("--max-polls", type=int, default=120, help="Maximum polling attempts")
    parser.add_argument("--archive-script", default=str(DEFAULT_ARCHIVE_SCRIPT), help="MinerU archive script path")
    parser.add_argument("--dry-run", action="store_true", help="Print the sanitized command without calling MinerU")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    sources = [Path(value).expanduser().resolve() for value in args.files]
    for source in sources:
        if not source.exists():
            print(f"Source file not found: {source}", file=sys.stderr)
            return 1

    archive_script = Path(args.archive_script).expanduser().resolve()
    if not archive_script.exists():
        print(f"MinerU archive script not found: {archive_script}", file=sys.stderr)
        return 1

    values = merged_env()
    temp_config: tempfile.NamedTemporaryFile[str] | None = None
    try:
        if args.dry_run:
            if values.get("MINERU_API_TOKEN"):
                config_path = Path("<temporary-token-config>")
            else:
                config_path = token_config_path(values).resolve()
                if not config_path.exists():
                    print(
                        "MinerU token config not found. Set MINERU_TOKEN_CONFIG or MINERU_API_TOKEN in .env.",
                        file=sys.stderr,
                    )
                    return 1
        elif values.get("MINERU_API_TOKEN"):
            temp_config = write_temp_token_config(values["MINERU_API_TOKEN"])
            config_path = Path(temp_config.name)
        else:
            config_path = token_config_path(values).resolve()
            if not config_path.exists():
                print(
                    "MinerU token config not found. Set MINERU_TOKEN_CONFIG or MINERU_API_TOKEN in .env.",
                    file=sys.stderr,
                )
                return 1

        output_dir = Path(args.output_dir).expanduser().resolve() if args.output_dir else default_output_dir(sources[0])
        command = [
            sys.executable,
            str(archive_script),
            *[str(source) for source in sources],
            "--output-dir",
            str(output_dir),
            "--token-config",
            str(config_path),
            "--language",
            args.language,
            "--layout-model",
            args.layout_model,
            "--poll-interval",
            str(args.poll_interval),
            "--max-polls",
            str(args.max_polls),
        ]
        if args.no_formula:
            command.append("--no-formula")
        if args.no_table:
            command.append("--no-table")
        if args.no_ocr:
            command.append("--no-ocr")

        if args.dry_run:
            print(" ".join(shlex.quote(part) for part in command))
            return 0

        return subprocess.run(command, cwd=REPO_ROOT, check=False).returncode
    finally:
        if temp_config is not None:
            Path(temp_config.name).unlink(missing_ok=True)


if __name__ == "__main__":
    sys.exit(main())
