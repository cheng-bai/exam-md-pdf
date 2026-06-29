# 试卷 MD/PDF 云端归档工作流

这个仓库用于把试卷 PDF、扫描件或图片版材料整理成可维护的 Markdown 和可阅读 PDF，并用 GitHub 做版本管理。

目标不是保存 OCR 中间文件，而是保存最终可复用产物：

- 一份试卷一个中文目录。
- 每份最终试卷至少包含一个规范命名的 `.md` 和 `.pdf`。
- 必要题图放在同目录 `figures/`。
- 原始 PDF、MinerU 归档包、预览图、上传回执和工作稿默认不提交。

## 给同事和 AI 的入口

先读这三个 skill，再开始处理试卷：

| Skill | 何时使用 | 文件 |
|---|---|---|
| MinerU 文档工作流 | PDF/扫描件转 OCR 初稿、清理成试卷 Markdown | `skills/mineru-document-workflow/SKILL.md` |
| 试卷归档治理 | 整理最终目录、命名、GitHub 提交前检查 | `skills/exam-archive-governance/SKILL.md` |
| 交付前验证 | 提交、推送或声明完成前做证据检查 | `skills/verification-before-completion/SKILL.md` |

AI agent 执行顺序：

1. 读 `AGENTS.md`。
2. 读本 README。
3. 按任务读取 `skills/` 下对应 `SKILL.md`。
4. 只把最终归档目录提交到 GitHub。
5. 交付前运行验证命令，并报告证据。

## 目录结构

```text
.
├── AGENTS.md                  # 本仓库 AI 工作规则
├── README.md                  # 人类和 AI 的复现手册
├── skills/                    # 可复用 AI skills
├── inputs/                    # 原始 PDF / 扫描图片，默认不提交
├── outputs/                   # MinerU 解析包和上传回执，默认不提交
├── work/                      # 裁图、预览、临时文件，默认不提交
├── exams/                     # 最终试卷归档目录
├── handouts/                  # 专题讲义、教师版材料和习题册归档
├── scripts/                   # 环境检查、建工作稿、MinerU、渲染脚本
├── tests/                     # 工作流脚本测试
└── examples/                  # 最小示例
```

## 最终归档规则

最终归档统一放在 `exams/` 下。

目录名使用中文试卷名称：

```text
exams/年份学校标准名考试名称/
```

目录内最终 `.md` 和 `.pdf` 必须使用完整字段命名：

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

字段说明：

| 字段 | 示例 | 说明 |
|---|---|---|
| 学段 | `高中` | 小学 / 初中 / 高中等 |
| 学校标准名 | `上海市建平中学` | 优先使用标准校名，不随意简称 |
| 年级 | `高一` | 高一 / 高二 / 高三等 |
| 学科 | `数学` | 语文 / 数学 / 英语等 |
| 考试类型 | `2026春期末` | 年份 + 学期/考试类型 |
| 版本类型 | `解析版` | 学生版 / 解析版 / OCR审校学生版等 |
| 提交日期 | `20260625` | 实际提交到 GitHub 的日期，格式 `YYYYMMDD` |

## 不提交的内容

默认不要提交：

- `inputs/` 里的原始 PDF、扫描图片。
- `outputs/` 里的 `result.zip`、`summary.json`、`upload-response.json`、`result.json`。
- `work/` 里的裁图、预览页、调试输出。
- `exams/*-工作稿/` 审校现场。
- `source.md`、`student.md`、`QUALITY_REPORT.md` 这类工作稿文件。
- `page-previews/`、`final-previews/`。
- `.env`、API token、签名上传 URL。

公开仓库前必须确认试卷版权和隐私风险。

## 环境准备

检查环境：

```bash
python3 scripts/check_environment.py
```

建议具备：

- `git`
- `gh`
- `pandoc`
- `xelatex`
- `pdfinfo`
- `pdftotext`
- ImageMagick `magick`
- MinerU API token 或本地 MinerU CLI

项目支持 `.env`：

```bash
cp .env.example .env
```

`.env` 不提交。可配置：

```text
MINERU_API_TOKEN=...
MINERU_TOKEN_CONFIG=/path/to/mineru/config.json
```

## 一次完整复现流程

### 1. 新建工作稿

```bash
python3 scripts/new_exam.py "2026上海市建平中学高三数学一模试卷" --pdf "/path/to/source.pdf"
```

脚本会创建：

```text
exams/2026上海市建平中学高三数学一模试卷-工作稿/
├── source.md
├── figures/
└── outputs/
```

如果没有原始 PDF，也可以先只建工作稿：

```bash
python3 scripts/new_exam.py "2026上海市建平中学高三数学一模试卷"
```

### 2. 获取 OCR 初稿

扫描版或图片版 PDF 使用 MinerU：

```bash
python3 scripts/mineru_parse_exam.py \
  inputs/2026上海市建平中学高三数学一模试卷.pdf \
  --output-dir "outputs/2026上海市建平中学高三数学一模试卷-MinerU归档"
```

可复制文字 PDF 可先用：

```bash
mkdir -p work/2026上海市建平中学高三数学一模试卷
pdftotext -layout \
  inputs/2026上海市建平中学高三数学一模试卷.pdf \
  work/2026上海市建平中学高三数学一模试卷/raw.txt
```

### 3. 人工审校 Markdown

把 OCR 初稿整理到：

```text
exams/2026上海市建平中学高三数学一模试卷-工作稿/source.md
```

审校要求：

- 保留题号、分值、选项、小问。
- 数学公式写成标准 LaTeX：行内 `$...$`，独立 `$$...$$`。
- 题图放入 `figures/`，并确保 Markdown 引用可用。
- 不直接把 MinerU `full.md` 当最终稿。
- 未逐题对照原卷前，不声称内容完全准确。

### 4. 渲染 PDF

```bash
python3 scripts/render_exam.py \
  exams/2026上海市建平中学高三数学一模试卷-工作稿/source.md \
  --min-pages 1
```

知道页数时使用：

```bash
python3 scripts/render_exam.py \
  exams/2026上海市建平中学高三数学一模试卷-工作稿/source.md \
  --expect-pages 8
```

### 5. 整理最终归档

建立最终目录：

```text
exams/2026上海市建平中学高三数学一模试卷/
```

把最终 Markdown、PDF 和必要题图移动进去，并命名为：

```text
高中-上海市建平中学高三数学2026一模学生版20260629.md
高中-上海市建平中学高三数学2026一模学生版20260629.pdf
```

### 6. 提交前验证

```bash
python3 -m unittest discover -s tests
git diff --check
find exams -maxdepth 2 -type f \( -name '*.md' -o -name '*.pdf' \) ! -path '*-工作稿/*' -print | sort
for f in exams/20*/*.pdf; do echo "$f"; pdfinfo "$f" | awk '/^Pages:|^Page size:/ {print "  "$0}'; done
git ls-files | rg '(^|/)(result\.zip|summary\.json|upload-response\.json|result\.json|full\.md|source\.md|student\.md|QUALITY_REPORT\.md)$|(^|/)(page-previews|final-previews)(/|$)|-工作稿/' || true
```

最后一条命令如果输出文件名，说明有中间物被 Git 跟踪，需要先清理。

### 7. 提交和推送

```bash
git status --short
git add README.md AGENTS.md skills scripts tests exams/<最终试卷目录>
git commit -m "docs: add normalized exam archive"
git push origin main
```

## GitHub 公开前检查

公开或分享仓库前确认：

- 试卷版权允许公开或二次整理传播。
- Markdown 和 PDF 中没有学生姓名、准考证号、电话、内部水印。
- `inputs/` 原始 PDF 没有被强制提交。
- `outputs/` MinerU 包和上传回执没有被提交。
- `exams/*-工作稿/` 没有被提交。
- `.env` 没有被提交。

## 当前仓库内容

当前 `exams/` 下已经有 5 份最终归档，文件名均按：

```text
学段-学校标准名年级学科考试类型版本类型提交日期.md/pdf
```

进行管理。
