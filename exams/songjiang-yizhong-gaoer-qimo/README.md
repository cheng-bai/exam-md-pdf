# 松江一中高二期末

## 文件说明

- `source.md`: 由 MinerU OCR 初稿整理出的语义化 Markdown 清理稿。
- `figures/`: 从 MinerU 结果复制出的题图。
- `outputs/松江一中高二期末-OCR清理稿.pdf`: 由 `source.md` 经 Pandoc + XeLaTeX 渲染出的 A4 PDF。

## MinerU 解析记录

- 源文件：`inputs/songjiang-yizhong-gaoer-qimo.pdf`，本地保留，不推送。
- 原始 PDF 信息：4 页，A4，约 2.6 MB。
- MinerU 通道：`mineru_parse.py` API 归档通道。
- 解析状态：`state: done`，`err_msg: ""`。
- 本地归档目录：`outputs/松江一中高二期末-MinerU解析/`。

## 质量状态

本稿已完成：

- 标题、分节、题号结构整理。
- 9 张题图复制并改为稳定相对路径。
- 基础公式经 XeLaTeX 编译通过。
- PDF 验证为 A4、6 页、文件头 `%PDF-`、尾部 `%%EOF`。

仍需人工精校：

- 原 PDF 含手写痕迹，OCR 已将部分答案或笔迹混入题干。
- `【待校】` 和 `[check]` 标记处需要逐题对照原卷。
- 未声明本稿为最终无误的试卷文本。

