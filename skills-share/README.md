# 数学解析与 PDF 出版技能分享包

用途：把「写好解析 → 排成讲义 → 出版 PDF」这条链路上的三个技能装在一起，方便整包复制给同事或其他 AI 助手使用。

这个包只包含技能说明、模板和检查脚本，不包含任何试卷、讲义成品、学生材料或本机配置。包内三个技能与仓库 `skills/` 下的同名目录内容一致，需要单独使用时可直接取其中一个目录。

## 包内内容

| 技能 | 负责什么 | 什么时候用 |
|---|---|---|
| `math-solution-style` | 中文高中数学解析的文风与详略：以「依据 → 操作 → 结论」推进，关键转化处补选择理由 | 新写解析、补解析、教师讲评稿润色 |
| `lecture-pdf-layout` | A4 讲义版式：题干框、答案与解析层级、分页、教师版与学生版差异 | 已有内容需要整页 LaTeX 排版或重排 |
| `html-math-pdf-publishing` | 用 HTML + CSS + 本地 KaTeX 出版 PDF，含目录、书签、分页单元和结构检查脚本 | 明确走 HTML 路线，或需要目录书签与紧凑分页 |

## 推荐使用顺序

1. 先定内容：用 `math-solution-style` 把解析写到可跟算、可讲解的程度。
2. 再定版式：整页 TeX 路线交给 `lecture-pdf-layout`；HTML 路线交给 `html-math-pdf-publishing`。
3. 最后验收：导出的 PDF 要实际打开看页数、分页、公式和图形；三者任何一项通过都不能替代数学复核。

## 安装

技能目录是纯文本，安装就是把目录放进宿主读取技能的位置，不需要构建。

```bash
# Codex
cp -R math-solution-style lecture-pdf-layout html-math-pdf-publishing ~/.codex/skills/

# 其他宿主（路径按实际技能目录调整）
cp -R math-solution-style lecture-pdf-layout html-math-pdf-publishing ~/.agents/skills/
```

每个技能都以 `SKILL.md` 为入口；`agents/openai.yaml` 是给支持该清单的宿主的元数据，缺失也不影响阅读。

## 依赖

- `math-solution-style`：无代码依赖，只需要能读 Markdown。
- `lecture-pdf-layout`：XeLaTeX（TeX Live 或 MacTeX），模板使用 `ctexart`（`fontset=fandol`）、`tcolorbox`、`enumitem`、`fancyhdr`、`hyperref`；校样用 `pdfinfo` 核对页数与 A4 尺寸。
- `html-math-pdf-publishing`：Python 3，`beautifulsoup4`（脚本解析 HTML）、`PyMuPDF`（`import fitz`，生成预览与页数检查）；导出 PDF 需要本地 Chrome/Chromium 或 Vivliostyle，公式依赖本地 KaTeX 或 MathJax 资源。

先跑自检，确认环境可用：

```bash
python3 html-math-pdf-publishing/scripts/test_prepare.py -v
python3 html-math-pdf-publishing/scripts/test_audit.py
```

## 重新打包

修改技能后从仓库根目录重新生成压缩包，避免包内文件与 `skills/` 脱节：

```bash
cd skills-share
rm -f ../exam-md-pdf-skills-share.zip
zip -r ../exam-md-pdf-skills-share.zip . -x '*.DS_Store' -x '__pycache__/*'
```

解压后应能看到本文件、`LICENSE` 和三个技能目录；`SKILL.md` 的 YAML 头要能解析。

## 许可与边界

- 包内技能、模板和脚本采用 Apache License 2.0，全文见 `LICENSE`。
- 不附带任何试卷、讲义、题库、图片或学生信息；这些内容的版权归各自来源，仓库公开可见不代表可以再分发。
- 技能中的作者元数据（`chengbai`）只写入 PDF 属性，不在页面可见位置署名；接收方按自己的交付规范可覆盖。
- 技能提供的是流程约束，不是数学正确性的保证；交付前仍需逐题核对原卷与解答。
