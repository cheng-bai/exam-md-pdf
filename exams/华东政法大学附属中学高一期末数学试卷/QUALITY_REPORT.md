# 华政高一期末 OCR 审校质量报告

## 产物

- Markdown 主源稿：`source.md`
- 学生版 PDF：`outputs/华政高一期末-OCR审校学生版.pdf`
- MinerU 原始 OCR：`outputs/华政高一期末-MinerU归档/gaoyi-qimo/unzipped/full.md`
- MinerU 归档包：`outputs/华政高一期末-MinerU归档/gaoyi-qimo/result.zip`
- MinerU 摘要：`outputs/华政高一期末-MinerU归档/summary.json`

## 处理说明

- 原始 PDF 共 4 页，A4，来源为 CamScanner 扫描件。
- 源 PDF 含较多手写批注，清理稿已剔除明显手写演算。
- 第 9、18、19 题图按原卷语义重绘，原始 MinerU 裁图保留在 `figures/mineru/` 便于追溯。
- 本稿定位为学生版试卷，不包含答案或解析。

## 已验证

- MinerU 归档状态为 `state: done`，`err_msg: ""`。
- `source.md` 可通过 Pandoc + XeLaTeX 渲染。
- PDF 为 A4，8 页。
- Markdown 图片引用均存在。
- 低置信内容不残留裸 `【待校】`；AI 补全位置使用 `【待校/ai 已润色】` 标记。

## 残余风险

- 本稿已经做了人工视觉核对和清理，但尚未逐题逐字对照原 PDF 完成终审。
- 第 14 题 C 选项已按题目逻辑补全并标记 `【待校/ai 已润色】`；复杂公式题和重绘题图建议在正式发送前再按原卷复核一次。
