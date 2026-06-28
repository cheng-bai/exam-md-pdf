# 松江一中高一期末质量报告

## 产物

- Markdown 主源稿：`source.md`
- 学生版 PDF：`outputs/松江一中高一期末-学生版精校草稿.pdf`
- MinerU 原始 OCR：`../../outputs/松江一中高一期末-MinerU解析/1/unzipped/full.md`
- MinerU 归档包：`../../outputs/松江一中高一期末-MinerU解析/1/result.zip`
- MinerU 摘要：`../../outputs/松江一中高一期末-MinerU解析/summary.json`

## 处理说明

- 原始 PDF 共 4 页，A4，来源为 CamScanner 扫描件。
- MinerU OCR 已识别出 21 题和 5 张题图；清理稿按原 PDF 页面重新核对了明显 OCR 错字、符号、选项、题图图注和卷首信息。
- 本稿定位为学生版试卷，不包含答案或解析。
- 解答题加入书写留白，并用分页尽量避免大题跨页；因此 PDF 页数多于 4 页原卷，属于带书写留白版。

## 已验证

- MinerU 归档状态为 `state: done`，`err_msg: ""`。
- `source.md` 可通过 Pandoc + XeLaTeX 渲染。
- Markdown 图片引用均存在。
- 题号覆盖 1--21。
- `source.md` 清理稿未残留裸 `【待校】`、`[check]`、`OCR` 标记。

## 残余风险

- 本稿已按原 PDF 页面做视觉核对，并修正过命题教师姓名与第 12 题图注，但尚未逐题逐字完成终审。
- 第 16 题中的“当 $(\vec a,\vec b)$ 取到最大值时”按原卷转录；该处符号可能表示向量夹角，正式发送前建议人工复核原卷印刷含义。
