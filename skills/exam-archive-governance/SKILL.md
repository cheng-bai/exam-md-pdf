---
name: exam-archive-governance
description: Use when preparing final exam Markdown/PDF archives for GitHub, enforcing Chinese naming, directory structure, Chinese commit messages, and public repository safety checks.
---

# 试卷归档治理

提交或推送最终试卷、专题讲义和相关成品前，先使用本 skill。

## 目录规则

每份试卷使用一个最终归档目录：

```text
exams/年份学校标准名考试名称/
```

工作稿留在本地或工作目录中：

```text
exams/年份学校标准名考试名称-工作稿/
```

## 最终文件规则

最终目录必须包含顶层 `.md` 和 `.pdf`，文件名使用：

```text
学段-学校标准名年级学科考试类型版本类型提交日期.md
学段-学校标准名年级学科考试类型版本类型提交日期.pdf
```

示例：

```text
exams/2026上海市建平中学高一期末数学试卷/
├── 高中-上海市建平中学高一数学2026春期末解析版20260625.md
├── 高中-上海市建平中学高一数学2026春期末解析版20260625.pdf
└── figures/
```

## 中文提交规则

- 提交信息必须使用中文。
- 提交标题可以保留 `docs:`、`fix:`、`chore:` 等类型前缀，但说明必须是中文。
- 提交正文要写清本次完成的任务、提交的主要内容和校验结果。
- 不使用 `update`、`misc`、`docs` 这类无法说明内容的泛名。
- 若希望 GitHub 文件夹列表右侧显示某个英文目录的用途，应单独提交该目录的 `README.md`，提交标题写成该目录的中文用途说明。

示例：

```text
docs: 入库函数单调性教师版讲义

本次完成：整理函数单调性教师版讲义的 Markdown、PDF 和知识导图。

校验：Markdown 图片引用缺失数为 0；PDF 可读取页数。
```

## GitHub 可读性规则

- 每个根目录都应有中文 `README.md`。
- README 开头应有一句 `用途：...`，直接说明该英文目录的作用。
- 目录说明必须根据目录真实内容编写，避免空泛表述。
- Markdown 图片引用必须使用仓库内相对路径，必要图片放入同级 `figures/` 并一起提交。

## 提交前检查

提交前执行：

```bash
git status --short
find exams -maxdepth 2 -type f \( -name '*.md' -o -name '*.pdf' \) ! -path '*-工作稿/*' -print | sort
for f in exams/20*/*.pdf; do echo "$f"; pdfinfo "$f" | awk '/^Pages:|^Page size:/ {print "  "$0}'; done
git diff --cached --check
git diff --cached --name-only | rg '(^|/)(result\.zip|summary\.json|upload-response\.json|result\.json|full\.md|source\.md|student\.md|QUALITY_REPORT\.md)$|(^|/)(page-previews|final-previews)(/|$)|-工作稿/' || true
```

最后一条命令在最终归档提交中应无输出。

## 公开仓库安全

公开仓库或推送试卷文件前：

- 确认材料允许公开传播。
- 检查 Markdown 和 PDF 中是否包含学生姓名、证件号、电话、教师联系方式和内部水印。
- 确认原始 PDF、扫描件和 OCR 归档包没有被跟踪。
- 除非明确要公开分发，否则仓库保持 private。
