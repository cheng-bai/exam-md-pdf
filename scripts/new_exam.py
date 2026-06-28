#!/usr/bin/env python3
"""Create a new Chinese-named exam work draft."""

from __future__ import annotations

import argparse
import shutil
import sys
from pathlib import Path


def safe_name(title: str) -> str:
    value = title.strip()
    for char in '/\\:*?"<>|':
        value = value.replace(char, "-")
    value = " ".join(value.split())
    return value or "未命名试卷"


def work_draft_name(title: str) -> str:
    value = safe_name(title)
    return value if value.endswith("-工作稿") else f"{value}-工作稿"


def markdown_template(title: str) -> str:
    return f"""---
title: {title}
geometry: margin=2cm
CJKmainfont: Songti SC
mainfont: Times New Roman
fontsize: 11pt
---

# {title}

## 识别说明

- 原始 PDF：
- OCR 工具：
- 低置信位置：

## 考生注意


## 一、填空题


## 二、选择题


## 三、解答题

"""


def main() -> int:
    parser = argparse.ArgumentParser(description="Create a Chinese-named exam work draft.")
    parser.add_argument("title", help="Exam title, for example: 2026上海市建平中学高三数学一模试卷")
    parser.add_argument("--pdf", help="Optional source PDF to copy into inputs/")
    args = parser.parse_args()

    root = Path.cwd()
    title = safe_name(args.title)
    exam_dir = root / "exams" / work_draft_name(title)
    source_md = exam_dir / "source.md"
    pdf_path = Path(args.pdf).expanduser() if args.pdf else None

    if exam_dir.exists():
        print(f"Exam already exists: {exam_dir}", file=sys.stderr)
        return 1
    if pdf_path and not pdf_path.exists():
        print(f"PDF not found: {pdf_path}", file=sys.stderr)
        return 1

    (exam_dir / "figures").mkdir(parents=True)
    (exam_dir / "outputs").mkdir()
    source_md.write_text(markdown_template(args.title), encoding="utf-8")

    if pdf_path:
        inputs_dir = root / "inputs"
        inputs_dir.mkdir(exist_ok=True)
        target = inputs_dir / f"{title}{pdf_path.suffix.lower()}"
        shutil.copy2(pdf_path, target)
        print(f"Copied source PDF: {target}")

    print(f"Created exam workspace: {exam_dir}")
    print(f"Edit Markdown source: {source_md}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
