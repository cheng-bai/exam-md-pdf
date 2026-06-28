# 晋元高级中学高二数学期末 OCR 审校质量报告

## 产物

- Markdown 主源稿：`晋元高级中学高二数学期末-OCR审校学生版.md`
- 学生版 PDF：`outputs/晋元高级中学高二数学期末-OCR审校学生版.pdf`
- MinerU 原始 OCR：`outputs/晋元高级中学高二数学期末-MinerU归档/jinyuan-gaoer-shuxue-qimo/unzipped/full.md`
- MinerU 归档包：`outputs/晋元高级中学高二数学期末-MinerU归档/jinyuan-gaoer-shuxue-qimo/result.zip`
- MinerU 摘要：`outputs/晋元高级中学高二数学期末-MinerU归档/summary.json`

## 处理说明

- 原始 PDF 共 4 页，A4，来源为 CamScanner 扫描件。
- 本稿由 MinerU OCR 草稿整理为学生版试卷，不包含答案或解析。
- 表格和题图使用 MinerU 原始裁图，保留印刷卷风格。
- 低置信内容不残留裸 `【待校】`；AI 补全位置使用 `【待校/ai 已润色】` 标记。

## 已验证

- MinerU 归档状态为 `state: done`，`err_msg: ""`。
- `晋元高级中学高二数学期末-OCR审校学生版.md` 可通过 Pandoc + XeLaTeX 渲染。
- 图片引用均已复制到 `figures/mineru/`。
- 第 16 题已强制整体排在同一页，避免题干与图像、选项跨页。

## 残余风险

- 第 14 题的指数与选项细节已按数学关系补全并标记 `【待校/ai 已润色】`，正式发送前建议按原卷局部复核。
- 第 20、21 题公式密集，已按原图人工修正 OCR 错误，但尚未逐字终审。
