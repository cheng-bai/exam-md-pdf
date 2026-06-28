# 试卷 PDF 电子化工作流

这个仓库用于把试卷 PDF 整理成可维护的 Markdown，再渲染成可打印 PDF，并用 Git 记录版本，最后推送到 GitHub。

## 当前目标

1. 原始 PDF 放入 `inputs/`。
2. 每份试卷在 `exams/<试卷名>/` 下维护 Markdown 源稿。
3. 用 Pandoc + XeLaTeX 把 Markdown 渲染成 PDF。
4. 用 Git 保存每次校对和排版修改。
5. 配好 GitHub 远程仓库后推送。

## 目录结构

```text
.
├── AGENTS.md                  # Codex 在本项目里的工作规则
├── README.md                  # 项目说明和 Git 教程
├── inputs/                    # 原始 PDF，默认不提交到 Git
├── exams/                     # 每份试卷的 Markdown、图片和输出 PDF
├── scripts/                   # 自动化脚本
└── examples/                  # 可运行示例
```

## 一次完整流程

### 1. 检查环境

```bash
python3 scripts/check_environment.py
```

需要看到 `git`、`gh`、`pandoc`、`xelatex` 都通过。`magick` 和 `pdfinfo` 用于图片/PDF 验证，建议保留。

### 2. 新建一份试卷

```bash
python3 scripts/new_exam.py "2026-上海-高三数学-一模"
```

如果已有原始 PDF，可以复制到项目里：

```bash
python3 scripts/new_exam.py "2026-上海-高三数学-一模" --pdf "/path/to/source.pdf"
```

脚本会创建：

```text
exams/2026-shanghai-gaosan-shuxue-yimo/
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
mkdir -p work/2026-shanghai-gaosan-shuxue-yimo
pdftotext -layout inputs/2026-shanghai-gaosan-shuxue-yimo.pdf work/2026-shanghai-gaosan-shuxue-yimo/raw.txt
open work/2026-shanghai-gaosan-shuxue-yimo/raw.txt
```

然后把 `raw.txt` 里的题目结构整理进：

```text
exams/2026-shanghai-gaosan-shuxue-yimo/source.md
```

整理时要做三件事：

1. 保留题号、分值、选项、小问和留空。
2. 把错乱换行合并成自然段。
3. 把数学公式改成 LaTeX，不保留 OCR 产生的乱码。

#### 路线 B：扫描版 PDF 用 MinerU

MinerU 适合扫描件、复杂版式、公式和表格较多的 PDF。官方 CLI 支持本地 PDF 输入并输出 Markdown/JSON。

建议先建独立虚拟环境，避免污染系统 Python：

```bash
uv venv .venv-mineru --python 3.12
source .venv-mineru/bin/activate
uv pip install -U "mineru[all]"
mineru -p inputs/2026-shanghai-gaosan-shuxue-yimo.pdf -o work/mineru -b pipeline
```

如果你的机器支持 GPU 或 Apple Silicon 加速，也可以先尝试：

```bash
mineru -p inputs/2026-shanghai-gaosan-shuxue-yimo.pdf -o work/mineru
```

完成后，在 `work/mineru/` 里找到生成的 `.md`，把可用内容复制并校对到 `exams/<slug>/source.md`。

#### 路线 C：扫描版 PDF 用 Marker

Marker 适合快速把 PDF 转成 Markdown，并会抽取图片。它需要 Python 3.10+ 和 PyTorch。

```bash
uv venv .venv-marker --python 3.12
source .venv-marker/bin/activate
uv pip install marker-pdf
marker_single inputs/2026-shanghai-gaosan-shuxue-yimo.pdf --output_dir work/marker --output_format markdown
```

如果数学行内公式识别差，可以强制 OCR：

```bash
marker_single inputs/2026-shanghai-gaosan-shuxue-yimo.pdf --output_dir work/marker --output_format markdown --force_ocr
```

完成后，把 `work/marker/` 生成的 Markdown 和图片整理进 `exams/<slug>/source.md` 与 `exams/<slug>/figures/`。

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
python3 scripts/render_exam.py exams/2026-shanghai-gaosan-shuxue-yimo/source.md
```

如果你知道原卷页数，可以强制检查页数：

```bash
python3 scripts/render_exam.py exams/2026-shanghai-gaosan-shuxue-yimo/source.md --expect-pages 8
```

如果只想避免生成空白或明显缺页 PDF：

```bash
python3 scripts/render_exam.py exams/2026-shanghai-gaosan-shuxue-yimo/source.md --min-pages 1
```

输出文件会写到同级 `outputs/` 目录，例如：

```text
exams/2026-shanghai-gaosan-shuxue-yimo/outputs/source.pdf
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

以后每整理完一份试卷，推荐这样提交：

```bash
git add exams/<试卷名>/source.md exams/<试卷名>/figures exams/<试卷名>/outputs
git commit -m "docs: digitize <试卷名>"
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
