---
name: math-docx-to-markdown
description: Use when converting math-heavy Word .docx files, Chinese high-school handouts, teacher editions, exam materials, or formula-dense documents to Markdown.
---

# Math DOCX to Markdown

## Overview

Convert formula-heavy `.docx` teaching materials into Markdown, then verify conversion smoke checks and review mathematical content. Pandoc output is a draft, not a finished answer.

## Workflow

1. Confirm the source is a valid OOXML file:

```bash
file "<source.docx>"
unzip -t "<source.docx>"
unzip -l "<source.docx>" | rg 'word/document.xml'
```

2. Convert with Pandoc:

```bash
pandoc --track-changes=all --wrap=none -t markdown+tex_math_dollars \
  --extract-media "<output-dir>/media" \
  "<source.docx>" -o "<output.md>"
```

3. Run the checker:

```bash
python3 skills/math-docx-to-markdown/scripts/check-math-markdown.py \
  "<output.md>" --source-docx "<source.docx>"
```

The checker finds hard failures and review warnings; it does not prove all math content is correct. Fix errors. Investigate warnings. Only after manual review, rerun with `--accept-count-delta` or `--allow-warnings` and disclose why.

4. Read the Markdown and inspect likely Word-conversion failures:

- `>` converted to `\right\rangle`.
- Set-builder bars split as `\left| \right.` or broken across `$...$`.
- Chinese connectives split one formula across two math spans, such as `$\{x|x<0$或$x>1\}$` or `$\left(a>0\right.$且$\left.a\ne1\right)$`. The checker reports these as `split_connective_math`.
- Lost relation symbols between adjacent formulas.
- Chinese text swallowed into math unexpectedly.
- Answer line contradicts the explanation.
- Range/set descriptions are syntactically valid but mathematically incomplete.

5. For answer keys, teacher editions, or requests that formulas be correct, ask a subagent for an independent formula/content review before final delivery.

6. Final response must include output path, source/Markdown/MathML formula counts, checker result, warning decisions, and content-level corrections.

## Correction Boundary

Only modify mathematical content when the source DOCX or its rendered meaning makes the error clear. If unsure whether a problem is source error or conversion error, mark it as a疑点 in the final response instead of silently changing the answer.

## Formula Style

- Use inline math `$...$` for ordinary formulas.
- Use display math only for displayed derivations or long formulas.
- Prefer `\mid` for set-builder notation: `$\{x\mid x \in A\}$`.
- Preserve teacher/student strategy: teacher editions may include answers; student editions must not leak answers.

## Completion Gate

Do not report completion until:

- Markdown exists and has reasonable size.
- Pandoc can parse Markdown JSON and export MathML.
- The checker has no unhandled errors or warnings.
- Manual or subagent review covered content-level formula issues.
