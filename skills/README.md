# AI Skills

This directory contains the reusable AI operating instructions used to produce and maintain this repository.

## Skills Included

| Skill | Purpose |
|---|---|
| `mineru-document-workflow` | OCR and review chain for turning scanned exams into Markdown and PDF. |
| `exam-archive-governance` | Final naming, directory, GitHub, and public repository safety rules. |
| `verification-before-completion` | Evidence-first checks before claiming a task is complete. |

## How AI Agents Should Use Them

1. Read `skills/mineru-document-workflow/SKILL.md` before parsing or cleaning a source exam.
2. Read `skills/exam-archive-governance/SKILL.md` before moving files into final `exams/` archives.
3. Read `skills/verification-before-completion/SKILL.md` before committing, pushing, or reporting completion.

These skills are written without local machine tokens. Configure credentials through `.env`, not through committed files.
