#!/usr/bin/env python3
"""Create a new exam workspace."""

from __future__ import annotations

import argparse
import re
import shutil
import sys
from pathlib import Path


PINYIN_HINTS = {
    "上海": "shanghai",
    "高三": "gaosan",
    "高二": "gaoer",
    "高一": "gaoyi",
    "数学": "shuxue",
    "语文": "yuwen",
    "英语": "yingyu",
    "物理": "wuli",
    "化学": "huaxue",
    "生物": "shengwu",
    "一模": "yimo",
    "二模": "ermo",
    "期中": "qizhong",
    "期末": "qimo",
}


def slugify(title: str) -> str:
    value = title.strip().lower()
    for chinese, pinyin in PINYIN_HINTS.items():
        value = value.replace(chinese, f"-{pinyin}-")
    value = re.sub(r"[^a-z0-9]+", "-", value)
    value = re.sub(r"-+", "-", value).strip("-")
    return value or "exam"


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
    parser = argparse.ArgumentParser(description="Create an exam workspace.")
    parser.add_argument("title", help="Exam title, for example: 2026-上海-高三数学-一模")
    parser.add_argument("--pdf", help="Optional source PDF to copy into inputs/")
    args = parser.parse_args()

    root = Path.cwd()
    slug = slugify(args.title)
    exam_dir = root / "exams" / slug
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
        target = inputs_dir / f"{slug}{pdf_path.suffix.lower()}"
        shutil.copy2(pdf_path, target)
        print(f"Copied source PDF: {target}")

    print(f"Created exam workspace: {exam_dir}")
    print(f"Edit Markdown source: {source_md}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
