---
name: paper-exam-to-md-pdf
description: 当拍照或扫描的纸质试卷需要编排成交付级 Markdown 和可打印 PDF，并保留题号、分值、公式、选项、图形和验证证据时使用。它负责成品主编排；如果用户只要行级 OCR 文本或坐标，应改用文字识别 Skill。
---

# 纸质试卷转 Markdown/PDF

## 概览

把纸质试卷照片或扫描件整理成电子稿：先形成可维护的 Markdown，再渲染 PDF。结构正确优先于 OCR 原始顺序，完成前必须有可见验证。

## 配套 skill

- 普通题干文字草稿优先使用脚本完整的 `paddleocr-text-recognition`；它不负责可靠恢复公式、表格或复杂版面，这些内容必须按原图校对。
- 用户明确要求 MinerU、完整 MinerU 归档，或复杂公式/表格/版面需要自动解析时，先运行环境检查；只有 `mineru-document-workflow` 的适配脚本可用时才走 MinerU，否则明确报告不可用并采用 OCR 初稿加人工校对。
- 生成和检查 PDF 时优先使用项目内 `scripts/render_exam.py`、`pdfinfo` 和 `qpdf`；拆分或合并时使用当前环境里经过验证的 PDF 工具。
- 声称交付完成前，直接执行本 skill 的检查清单，不依赖外部完成验证 skill。

## 流程

1. **建立产物**
   - 原始照片保持只读。
   - 中间裁剪、增强图放入 `work/`。
   - 最终 `.md`、最终 `.pdf` 和必要题图放入符合项目命名规则的 `exams/<年份学校标准名考试名称>/`。
   - 最终 Markdown 必须按内容含义使用中文语义化文件名；审校报告如需保留，应放在工作稿目录，不默认进入最终归档。不要把 `source.md`、`cleaned.md`、`QUALITY_REPORT.md` 这类泛名或英文名作为公开成品。

2. **检查和预处理图片**
   - 用 `magick identify` 检查尺寸和方向。
   - 需要时旋转页面、裁剪左右半页、增强对比度和锐度。
   - 关键题图先放入工作目录；定稿后复制到最终归档的 `figures/`，再用相对路径嵌入 Markdown，不凭记忆重画。

3. **OCR 后按图校正**
   - 如果 OCR 可用就运行；中文 OCR 不可用或质量差时，说明 OCR 只是辅助。
   - 公式、中文题干、分值、选项标签必须结合图像人工核对。
   - OCR 文本不转写手写痕迹或相机界面叠加信息；原始照片保持只读，不得擦除、覆盖或模糊其中的真实来源标识或水印。
   - 不能确认的内容放到 `识别说明`，不要静默猜测。

4. **编写 Markdown**
   - 保留原始结构，如 `考生注意`、`填空题`、`选择题`、`解答题`。
   - 保留题号、分值、留空、A-D 选项和全部小问。
   - 数学使用标准 Markdown LaTeX：行内 `$...$`，必要时使用 `$$...$$`。
   - 中文高中数学记号优先用 `\mathbf R`、`\mathbf Z`、`\mathbf N^*`、`\dfrac{}`、`\vec a`、`\overline{AB}`。
   - Markdown 本身必须可作为源文件阅读，不能只是 PDF 构建临时文件。

5. **生成 PDF**
   - 中文/数学密集 Markdown 默认优先用 Pandoc + XeLaTeX：

     ```bash
     pandoc input.md -o output.pdf --pdf-engine=xelatex
     ```

   - 需要时加入 YAML 元数据：

     ```yaml
     ---
     title: 试卷标题
     papersize: a4
     geometry: a4paper,margin=2cm
     CJKmainfont: FandolSong-Regular.otf
     mainfont: texgyretermes-regular.otf
     fontsize: 11pt
     ---
     ```

   - 从 Markdown 和图片所在目录运行 `pandoc`，或确保图片路径能正确解析。

6. **完成前验证**
   - 确认 Markdown 和 PDF 存在且大小合理。
   - 确认最终 Markdown 是中文语义化文件名；可选审校报告只保留在工作稿目录。
   - 用 `pdfinfo` 检查页数和 A4 页面尺寸，用 `qpdf --check` 检查 PDF 结构。
   - 核对 Markdown 中出现所有预期题号。
   - PDF 中若有题图，检查 `/Image` 对象或渲染预览。
   - 尽量用 Quick Look、浏览器或其他渲染器至少查看一页预览。

## 常见失败

- **中文 OCR 不可用**：继续按图转录，不要假装 OCR 高置信。
- **PDF 丢图**：从 Markdown/图片目录重跑 `pandoc`，或修正图片路径。
- **照片边缘缺字**：保留最可靠的可读重建，并在 `识别说明` 里标注。
- **公式字形问题**：PDF-bound Markdown 里用 LaTeX 命令，不用 Unicode 上下标。
- **只停在 Markdown**：如果用户要 PDF，也要编译并验证 PDF，除非用户明确暂停。

## 完成汇报

最终回复应包含：

- 最终 Markdown 和 PDF 路径。
- 验证证据：文件存在/大小、PDF 页数、预览或渲染状态。
- 低置信 OCR 或转录位置。
