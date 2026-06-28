---
name: verification-before-completion
description: Use before claiming the exam workflow, archive, commit, push, or documentation is complete.
---

# Verification Before Completion

Do not claim completion until fresh verification has been run and read.

## Required Pattern

1. Identify the command that proves the claim.
2. Run the full command.
3. Read the output and exit code.
4. Report the evidence.
5. Only then claim completion.

## Exam Archive Verification

Use these checks for this repository:

```bash
python3 -m unittest discover -s tests
git diff --check
find exams -maxdepth 2 -type f \( -name '*.md' -o -name '*.pdf' \) ! -path '*-工作稿/*' -print | sort
for f in exams/20*/*.pdf; do echo "$f"; pdfinfo "$f" | awk '/^Pages:|^Page size:/ {print "  "$0}'; done
git ls-files | rg '(^|/)(result\.zip|summary\.json|upload-response\.json|result\.json|full\.md|source\.md|student\.md|QUALITY_REPORT\.md)$|(^|/)(page-previews|final-previews)(/|$)|-工作稿/' || true
```

Expected results:

- Unit tests pass.
- No whitespace errors.
- Final `.md` and `.pdf` files are visible under `exams/<中文试卷名称>/`.
- PDFs are readable and page sizes are reasonable.
- The final command prints no tracked OCR intermediates.
