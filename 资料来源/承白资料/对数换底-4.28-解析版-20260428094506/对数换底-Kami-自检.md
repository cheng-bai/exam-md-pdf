# 对数换底 Kami 精排自检

## 输出文件

- 中间稿：`对数换底-注释版讲义-Kami.html`
- 最终 PDF：`对数换底-注释版讲义-Kami.pdf`

## 基本结果

- PDF 页数：15 页。
- PDF 页面规格：A4。
- PDF 生成方式：Playwright / Chromium 从 HTML 打印导出。
- 数学公式渲染方式：HTML 中保留 Pandoc 生成的 `.math` 节点，浏览器端用 KaTeX 渲染后再导出 PDF。
- KaTeX 渲染检查：249 个 `.katex` 节点，0 个 `data-katex-error`。
- 结构检查：11 个题卡，其中母题 3 个、变式 8 个；15 个教师备注框；3 个“需复核”提示保留。

## 版式改进

- 采用 Kami 长文档思路：暖纸底色、墨蓝窄色条、浅色卡片、低对比边框，适合打印和课堂发放。
- 保持原讲义结构：标题、导学说明、知识导图、知识笔记、母题、变式、分层练习、答案解析均保留。
- Mermaid 知识导图改为可打印的 HTML 网格导图，避免原始 Mermaid 代码出现在 PDF。
- 母题/变式标题做成题卡主标题，字号约 20px；教法备注标签约 12.7px，并放入浅色教师备注框，不再抢过题号层级。
- 答案、解析、需复核提示分别做了标签化处理，便于教师快速扫读。

## 验证记录

- `pdfinfo 对数换底-注释版讲义-Kami.pdf`：Pages = 15，Page size = A4，Creator = Chromium。
- `python3 + pypdf`：读取 PDF 成功，页数 15，标题为“对数换底公式的应用与对数式化简证明 - Kami 精排版”。
- `Playwright DOM 检查`：KaTeX = 249，errors = 0，mermaidPre = 0，knowledge_map_code_blocks = 0。
- `pdftotext ... | rg '\log|\frac|\dfrac|flowchart|mermaid|```|katex|<div|</div>|<span|</span>|<p>|</p>'`：无命中。
- `rg 'mermaid|flowchart|```|<pre class="mermaid"' 对数换底-注释版讲义-Kami.html`：无命中。

## 仍需人工复核

- 原讲义中 3 处“需复核”提示已保留，主要涉及 OCR 或题源答案疑似错误：变式题 1-1 的换底分式步骤、挑战题第 3 题答案表达、碳 14 题“87升年/871 年”。
- 本次任务只做排版与渲染，没有改动原始数学内容和答案逻辑。
