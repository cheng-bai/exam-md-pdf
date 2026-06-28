# 松江一中高二期末

## 文件说明

- `source.md`: 由 MinerU OCR 初稿整理出的语义化 Markdown 审校底稿。
- `student.md`: 按原 PDF 人工重建的学生版精校草稿，已去除手写答案和边注。
- `figures/`: 从 MinerU 结果复制出的题图。
- `QUALITY_REPORT.md`: 本轮自查与后续精校任务单。
- `outputs/松江一中高二期末-OCR审校底稿.pdf`: 由 `source.md` 经 Pandoc + XeLaTeX 渲染出的 A4 PDF。
- `outputs/松江一中高二期末-学生版精校草稿.pdf`: 由 `student.md` 经 Pandoc + XeLaTeX 渲染出的 A4 PDF。

## MinerU 解析记录

- 源文件：`inputs/songjiang-yizhong-gaoer-qimo.pdf`，本地保留，不推送。
- 原始 PDF 信息：4 页，A4，约 2.6 MB。
- MinerU 通道：`mineru_parse.py` API 归档通道。
- 解析状态：`state: done`，`err_msg: ""`。
- 本地归档目录：`outputs/松江一中高二期末-MinerU解析/`。

## OCR 底稿质量状态

`source.md` 和 `outputs/松江一中高二期末-OCR审校底稿.pdf` 已完成：

- 标题、分节、题号结构初步整理。
- 9 张题图复制并改为稳定相对路径。
- 基础公式经 XeLaTeX 编译通过。
- PDF 验证为 A4、6 页、文件头 `%PDF-`、尾部 `%%EOF`。

仍需人工精校：

- 原 PDF 含手写痕迹，OCR 已将部分答案或笔迹混入题干。
- `【待校】` 和 `[check]` 标记处需要逐题对照原卷。
- 题号 7、9、15 未作为独立题号稳定识别，需要优先修正。
- OCR 底稿不是最终无误的试卷文本，不适合直接发学生。

## 学生版精校草稿

本轮新增 `student.md` 和学生版 PDF，完成：

- 填空题 1--11 重新按原 PDF 第 1 页转录，删除手写答案和边注。
- 恢复题号 7、9 的独立结构。
- 恢复选择题 13--16 和题号 15 的 A-D 选项。
- 检查解答题 17--21 的公式、表格和小问结构。
- 解答题按页留出书写空间，尽量避免大题跨页。

仍需复核：

- 第 6 题指数位置被手写遮挡，学生版以 $n$ 代称并在题干中标注需校对。

学生版状态：

- 题号 1--21 已覆盖。
- 未保留原扫描中的手写答案和边注。
- PDF 为 A4、7 页。
