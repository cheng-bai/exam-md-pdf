# Project Instructions

本项目用于试卷 PDF 电子化：原始 PDF -> Markdown 源稿 -> 可打印 PDF -> Git/GitHub 管理。

## 工作原则

- Markdown 是主源文件，PDF 是渲染产物。
- 原始 PDF、扫描图和 OCR 中间文件默认视为大文件或版权敏感文件，不主动提交，除非用户明确要求。
- `source.md` 和 `outputs/*.pdf` 也可能包含版权或隐私信息；推送公开仓库前必须提醒用户确认。
- 数学公式必须使用标准 Markdown LaTeX：行内 `$...$`，独立 `$$...$$`。
- OCR 只能作为初稿来源，最终内容必须按原卷逐题校对。
- 交付前必须验证 Markdown 和 PDF 文件存在，PDF 页数合理，Pandoc 渲染无报错。

## 目录约定

- `inputs/`: 原始 PDF，默认被 `.gitignore` 忽略。
- `exams/<slug>/source.md`: 单份试卷的 Markdown 源稿。
- `exams/<slug>/figures/`: 从试卷中裁出的题图。
- `exams/<slug>/outputs/`: 渲染出的 PDF。
- `scripts/`: 项目自动化脚本。
- `examples/`: 示例材料。

## 命令约定

检查环境：

```bash
python3 scripts/check_environment.py
```

新建试卷：

```bash
python3 scripts/new_exam.py "试卷标题"
```

渲染 PDF：

```bash
python3 scripts/render_exam.py exams/<slug>/source.md
```

带页数验收：

```bash
python3 scripts/render_exam.py exams/<slug>/source.md --expect-pages 8
```

## Git 约定

- 提交信息优先使用 Conventional Commits。
- 初始化类提交使用 `chore: ...`。
- 试卷内容提交使用 `docs: ...`。
- 脚本修复使用 `fix: ...`。
- GitHub 远程默认使用 private，除非用户明确确认可以公开。
