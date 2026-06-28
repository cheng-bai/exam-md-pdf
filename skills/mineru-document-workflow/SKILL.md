---
name: mineru-document-workflow
description: Use when converting scanned PDFs, image PDFs, or Chinese math exams into Markdown and printable PDFs with MinerU, manual review, and GitHub archiving.
---

# MinerU Document Workflow

This is the reproducible AI workflow used by this repository for exam digitization.

## When To Use

Use this skill when the input is a PDF, scan, image PDF, or OCR-heavy Chinese math exam and the target is a reviewed Markdown source plus a printable PDF archive.

## Repository Chain

1. Put source files in `inputs/`.
2. Create a work draft:
   ```bash
   python3 scripts/new_exam.py "2026上海市建平中学高三数学一模试卷" --pdf "/path/to/source.pdf"
   ```
3. Parse with MinerU when OCR is needed:
   ```bash
   python3 scripts/mineru_parse_exam.py \
     inputs/2026上海市建平中学高三数学一模试卷.pdf \
     --output-dir "outputs/2026上海市建平中学高三数学一模试卷-MinerU归档"
   ```
4. Treat MinerU output as a draft only. Copy useful text, formulas, tables, and figure references into `exams/<试卷名>-工作稿/source.md`.
5. Manually review every problem against the source PDF. Do not claim mathematical correctness from OCR alone.
6. Render and verify:
   ```bash
   python3 scripts/render_exam.py exams/<试卷名>-工作稿/source.md --min-pages 1
   ```
7. Move the final reviewed `.md`, final `.pdf`, and required `figures/` into `exams/<中文试卷名称>/`.

## Final Archive Naming

Final archive files must use:

```text
学段-学校标准名年级学科考试类型版本类型提交日期.md
学段-学校标准名年级学科考试类型版本类型提交日期.pdf
```

Example:

```text
高中-上海市建平中学高一数学2026春期末解析版20260625.md
高中-上海市建平中学高一数学2026春期末解析版20260625.pdf
```

## OCR Review Rules

- Keep problem numbers, scores, options, subquestions, formulas, tables, and necessary figures.
- Use Markdown LaTeX: inline `$...$`, display `$$...$$`.
- Do not leave bare OCR uncertainty markers as final content.
- If AI inference was used to repair low-confidence OCR, mark it in the work draft and review before final archive.
- Do not publish raw OCR dumps, `summary.json`, `result.zip`, `full.md`, page previews, or upload responses as final archive files.

## Privacy And Tokens

- Never commit `.env`, API tokens, signed upload URLs, or raw authentication headers.
- Public repositories should not include source scans unless copyright and privacy have been checked.
- Keep `inputs/`, `outputs/`, `work/`, and `exams/*-工作稿/` local by default.
