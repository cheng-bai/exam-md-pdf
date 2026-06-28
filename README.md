# 试卷 PDF 电子化工作流

这个仓库用于把试卷 PDF 整理成可维护的 Markdown，再渲染成可打印 PDF，并用 Git 记录版本，最后推送到 GitHub。

## 当前目标

1. 原始 PDF 放入 `inputs/`。
2. 每份最终试卷在 `exams/<年份学校标准名考试名称>/` 下维护 Markdown 源稿和 PDF。
3. 用 Pandoc + XeLaTeX 把 Markdown 渲染成 PDF。
4. 用 Git 保存每次校对和排版修改。
5. 配好 GitHub 远程仓库后推送。

## 目录结构

```text
.
├── AGENTS.md                  # Codex 在本项目里的工作规则
├── README.md                  # 项目说明和 Git 教程
├── inputs/                    # 原始 PDF / 扫描图片输入，默认不提交到 Git
├── outputs/                   # MinerU 全局解析输出 / 上传回执 / 归档包，中间物
├── work/                      # 本地裁图 / 预览页 / 临时处理目录，中间物
├── exams/                     # 试卷 Markdown、题图和 PDF
│   ├── 2026上海市敬业中学高一期末数学试卷/               # 最终归档
│   ├── 2026上海市晋元高级中学高二数学期末试卷/           # 最终归档
│   ├── 2026上海市松江一中高一数学期末试卷/               # 最终归档
│   ├── 2026上海市松江一中高二数学期末试卷/               # 最终归档
│   ├── 2026华东政法大学附属中学高一期末数学试卷/         # 最终归档
│   └── 2026上海市敬业中学高一期末数学试卷-工作稿/        # 审校现场
├── scripts/                   # 自动化脚本
├── tests/                     # 工作流测试
└── examples/                  # 可运行示例
```

## 目录导航

| 路径 | 用途 | 是否建议提交 | 说明 |
|---|---|---:|---|
| `inputs/` | 原始 PDF / 扫描图片输入 | 否 | 默认包含版权或隐私材料，只保留目录说明文件 |
| `outputs/` | MinerU 解析包、上传回执、中间输出 | 否 | 用于追溯 OCR 过程，不作为最终交付 |
| `work/` | 裁图、预览、临时处理文件 | 否 | 可按需重建，不进入云端归档 |
| `exams/<年份学校标准名考试名称>/` | 最终云端规范归档 | 是 | 每份试卷一个目录，包含中文语义化 `.md` + `.pdf` |
| `exams/<年份学校标准名考试名称>-工作稿/` | 审校工作稿 | 视情况 | 不要作为最终归档整体直接推送 |
| `scripts/` | 自动化脚本 | 是 | 环境检查、建目录、渲染和 MinerU 解析 |
| `tests/` | 自动化测试 | 是 | 验证脚本和工作流约定 |
| `examples/` | 示例材料 | 是 | 用于演示最小可运行流程 |

## 云端归档规则

推送到 GitHub 管理的最终试卷，统一放在 `exams/` 下，并采用“一份试卷一个文件夹”。`exams/` 下的文件夹使用中文试卷名称：

```text
年份学校标准名考试名称
```

文件夹名只描述试卷本身。目录内最终 `.md` 和 `.pdf` 文件名必须同时包含完整归档字段：

```text
exams/年份学校标准名考试名称/
├── 学段-学校标准名年级学科考试类型版本类型提交日期.md
├── 学段-学校标准名年级学科考试类型版本类型提交日期.pdf
└── figures/                  # 仅当 Markdown 引用题图时保留
```

示例：

```text
exams/2026上海市建平中学高一期末数学试卷/
├── 高中-上海市建平中学高一数学2026春期末解析版20260625.md
└── 高中-上海市建平中学高一数学2026春期末解析版20260625.pdf
```

命名字段说明：

- `学段`：如 `高中`。
- `学校标准名`：优先参考本机资料 `/Users/thj/Documents/Codex/2026-06-24/jp/outputs/上海各区高中学校层次分类表_2026官方版.xlsx`，不要随意使用简称。
- `年级`：如 `高一`、`高二`、`高三`。
- `学科`：如 `数学`。
- `考试类型`：如 `2026春期末`、`2026春期终`、`2026一模`。
- `版本类型`：如 `学生版`、`解析版`、`OCR审校学生版`、`学生版精校草稿`。
- `提交日期`：实际提交到 GitHub 的日期，格式为 `YYYYMMDD`。
- `-工作稿`：如果同一份试卷还要保留审校现场，在规则目录名后追加 `-工作稿`。

不要把 `source.md`、`student.md`、`QUALITY_REPORT.md`、`full.md`、`summary.json`、`result.zip`、`page-previews/`、`final-previews/`、原始扫描 PDF 或 MinerU 归档包作为最终云端归档提交。若 Markdown 引用题图，必须提交必要的 `figures/`，否则 GitHub 上阅读 Markdown 时图片会断链。

## 一次完整流程

### 1. 检查环境

```bash
python3 scripts/check_environment.py
```

需要看到 `git`、`gh`、`pandoc`、`xelatex` 都通过。`magick` 和 `pdfinfo` 用于图片/PDF 验证，建议保留。

### 2. 新建一份试卷

```bash
python3 scripts/new_exam.py "2026上海市建平中学高三数学一模试卷"
```

如果已有原始 PDF，可以复制到项目里：

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

### 3. PDF 转 Markdown

推荐策略是“工具 OCR + 人工校对”：

- 可复制文字的 PDF：先用 `pdftotext -layout` 导出文本，再整理进 `source.md`。
- 扫描版或复杂版式 PDF：优先用成熟开源 OCR 工具，如 MinerU 或 Marker，生成初稿后逐题校对。
- 数学公式：不要完全信 OCR，最终以人工校对后的 LaTeX 为准。

#### 路线 A：可复制文字 PDF

适合从学校网站、教研系统下载的文字型 PDF。

```bash
mkdir -p work/2026上海市建平中学高三数学一模试卷
pdftotext -layout inputs/2026上海市建平中学高三数学一模试卷.pdf work/2026上海市建平中学高三数学一模试卷/raw.txt
open work/2026上海市建平中学高三数学一模试卷/raw.txt
```

然后把 `raw.txt` 里的题目结构整理进：

```text
exams/2026上海市建平中学高三数学一模试卷-工作稿/source.md
```

整理时要做三件事：

1. 保留题号、分值、选项、小问和留空。
2. 把错乱换行合并成自然段。
3. 把数学公式改成 LaTeX，不保留 OCR 产生的乱码。

#### 路线 B：扫描版 PDF 用 MinerU API

MinerU 适合扫描件、复杂版式、公式和表格较多的 PDF。本项目优先复用本机已经配置好的 MinerU API 归档脚本，保留 `summary.json`、`result.zip`、`full.md` 等可追溯原始结果。

先确认 MinerU API 配置可用：

```bash
python3 scripts/check_environment.py
```

项目默认读取 `/Users/thj/MinerU/config.json`。如果要改成项目本地配置，复制 `.env.example` 为 `.env`，设置 `MINERU_TOKEN_CONFIG` 或 `MINERU_API_TOKEN`；`.env` 已被 Git 忽略，不要提交真实 token。

解析扫描版 PDF：

```bash
python3 scripts/mineru_parse_exam.py \
  inputs/2026上海市建平中学高三数学一模试卷.pdf \
  --output-dir "outputs/2026-上海-高三数学-一模-MinerU归档"
```

完成后，把归档目录里的 `full.md` 当作 OCR 初稿，复制并校对到 `exams/<年份学校标准名考试名称>-工作稿/source.md`。不要直接把原始 OCR dump 当最终稿。

#### 路线 B2：本地 MinerU CLI

如果 API 不可用，再考虑本地 CLI。建议先建独立虚拟环境，避免污染系统 Python：

```bash
uv venv .venv-mineru --python 3.12
source .venv-mineru/bin/activate
uv pip install -U "mineru[all]"
mineru -p inputs/2026上海市建平中学高三数学一模试卷.pdf -o work/mineru -b pipeline
```

#### 路线 C：扫描版 PDF 用 Marker

Marker 适合快速把 PDF 转成 Markdown，并会抽取图片。它需要 Python 3.10+ 和 PyTorch。

```bash
uv venv .venv-marker --python 3.12
source .venv-marker/bin/activate
uv pip install marker-pdf
marker_single inputs/2026上海市建平中学高三数学一模试卷.pdf --output_dir work/marker --output_format markdown
```

如果数学行内公式识别差，可以强制 OCR：

```bash
marker_single inputs/2026上海市建平中学高三数学一模试卷.pdf --output_dir work/marker --output_format markdown --force_ocr
```

完成后，把 `work/marker/` 生成的 Markdown 和图片整理进 `exams/<年份学校标准名考试名称>-工作稿/source.md` 与 `exams/<年份学校标准名考试名称>-工作稿/figures/`。

Markdown 公式约定：

```md
行内公式写作 $x^2 + y^2 = 1$。

独立公式写作：

$$
\dfrac{a}{b} + \sqrt{x}
$$
```

### 4. Markdown 渲染 PDF

```bash
python3 scripts/render_exam.py exams/2026上海市建平中学高三数学一模试卷-工作稿/source.md
```

如果你知道原卷页数，可以强制检查页数：

```bash
python3 scripts/render_exam.py exams/2026上海市建平中学高三数学一模试卷-工作稿/source.md --expect-pages 8
```

如果只想避免生成空白或明显缺页 PDF：

```bash
python3 scripts/render_exam.py exams/2026上海市建平中学高三数学一模试卷-工作稿/source.md --min-pages 1
```

输出文件会写到同级 `outputs/` 目录，例如：

```text
exams/2026上海市建平中学高三数学一模试卷-工作稿/outputs/source.pdf
```

渲染后人工检查：

1. PDF 页数和预期一致。
2. 每个题号都在 Markdown 和 PDF 中出现。
3. 公式没有黑框、乱码或漏掉分式根号。
4. 题图能显示，且没有丢失关键标注。

### 5. Git 基础操作

第一次查看状态：

```bash
git status
```

把文件加入暂存区：

```bash
git add README.md AGENTS.md scripts examples .gitignore
```

提交：

```bash
git commit -m "chore: initialize exam digitization workflow"
```

以后每整理完一份试卷，先整理成“云端归档规则”里的最终目录，再只提交该规范目录：

```bash
git add exams/2026上海市建平中学高一期末数学试卷
git diff --cached --name-only | rg 'result\.zip|summary\.json|full\.md|source\.md$|student\.md$|page-previews|final-previews|_origin\.pdf' || true
git diff --cached --check
git commit -m "docs: add normalized exam markdown and pdf archives"
```

### 6. 推送到 GitHub

本机已经安装 GitHub CLI。试卷内容通常涉及版权、学校信息或学生隐私，默认推荐先创建私有仓库：

```bash
gh repo create exam-md-pdf --private --source=. --remote=origin --push
```

只有确认试卷内容允许公开传播时，才使用 `--public`。

如果你已经在 GitHub 创建了仓库，用：

```bash
git remote add origin https://github.com/<你的用户名>/<仓库名>.git
git push -u origin main
```

推送一份或多份最终试卷前，建议按顺序检查：

```bash
gh repo view <owner>/<repo> --json nameWithOwner,visibility,isPrivate,url
find exams -maxdepth 2 -type f \( -name '*.md' -o -name '*.pdf' \) ! -path '*-工作稿/*' -print | sort
for f in exams/20*/*.pdf; do echo "$f"; pdfinfo "$f" | awk '/^Pages:|^Page size:/ {print "  "$0}'; done
git status --short
```

暂存时只加入最终归档目录：

```bash
git add exams/2026上海市建平中学高一期末数学试卷
git diff --cached --name-only | rg 'result\.zip|summary\.json|full\.md|source\.md$|student\.md$|page-previews|final-previews|_origin\.pdf' || true
git diff --cached --check
git commit -m "docs: add normalized exam markdown and pdf archives"
git push origin main
```

如果第二条 `rg` 命令输出了文件名，说明暂存区混入了中间文件或旧工作稿，应先取消暂存并重新选择要提交的最终目录。

## Git 学习路径

### 必会命令

```bash
git status                  # 看当前改了什么
git add <文件>              # 准备提交
git commit -m "说明"        # 保存一个版本
git log --oneline           # 查看历史版本
git diff                    # 查看未暂存的改动
git diff --staged           # 查看已暂存的改动
git remote -v               # 查看远程仓库
git push                    # 推送到 GitHub
git pull                    # 拉取远程更新
```

### 你需要形成的习惯

- 每次只提交一个清晰变化：比如“整理一份试卷”或“修正某页公式”。
- 提交前先跑渲染，确认 PDF 能生成。
- 原始 PDF 如果版权或体积不适合公开，放在 `inputs/`，默认不提交。
- 即使不提交原始 PDF，`source.md` 和 `outputs/*.pdf` 也可能包含版权内容；公开前要检查。
- Markdown 是主源文件，PDF 是可再生成的交付文件。

## 公开前检查清单

在把仓库改成 public 或发给别人之前，逐项确认：

- 原卷版权允许公开或二次整理传播。
- Markdown 和 PDF 中没有学生姓名、准考证号、学校内部水印、教师联系方式。
- `inputs/` 原始 PDF 没有被 `git add -f` 强制加入。
- `work/` 中间 OCR 文件没有被提交。
- GitHub 仓库如果只是个人资料库，保持 private。

## 推荐工具

- PDF/OCR 到 Markdown：[MinerU](https://github.com/opendatalab/MinerU)、[Marker](https://github.com/datalab-to/marker)。
- Markdown 到 PDF：[Pandoc](https://pandoc.org/MANUAL.html) + XeLaTeX。
- 图片裁剪和增强：ImageMagick。
- GitHub 操作：GitHub CLI `gh`。
