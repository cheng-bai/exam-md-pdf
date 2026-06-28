---
name: exam-archive-governance
description: Use when preparing final exam Markdown/PDF archives for GitHub, enforcing Chinese naming, directory structure, and public repository safety checks.
---

# Exam Archive Governance

Use this skill before committing or pushing final exam products.

## Directory Rule

Each exam gets one final directory:

```text
exams/年份学校标准名考试名称/
```

Work drafts stay local:

```text
exams/年份学校标准名考试名称-工作稿/
```

## Final File Rule

The final directory must contain top-level `.md` and `.pdf` files named:

```text
学段-学校标准名年级学科考试类型版本类型提交日期.md
学段-学校标准名年级学科考试类型版本类型提交日期.pdf
```

Example:

```text
exams/2026上海市建平中学高一期末数学试卷/
├── 高中-上海市建平中学高一数学2026春期末解析版20260625.md
├── 高中-上海市建平中学高一数学2026春期末解析版20260625.pdf
└── figures/
```

## Commit Gate

Before committing:

```bash
git status --short
find exams -maxdepth 2 -type f \( -name '*.md' -o -name '*.pdf' \) ! -path '*-工作稿/*' -print | sort
for f in exams/20*/*.pdf; do echo "$f"; pdfinfo "$f" | awk '/^Pages:|^Page size:/ {print "  "$0}'; done
git diff --cached --check
git diff --cached --name-only | rg '(^|/)(result\.zip|summary\.json|upload-response\.json|result\.json|full\.md|source\.md|student\.md|QUALITY_REPORT\.md)$|(^|/)(page-previews|final-previews)(/|$)|-工作稿/' || true
```

The last command should print nothing for final archive commits.

## Public Repository Safety

Before making a repository public or pushing exam files:

- Confirm copyright permission for redistribution.
- Check Markdown and PDF for student names, IDs, phone numbers, teacher contact details, and internal watermarks.
- Confirm raw PDFs and OCR archives are not tracked.
- Keep the repository private unless public distribution is intentional.
