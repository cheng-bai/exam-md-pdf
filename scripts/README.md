# 自动化脚本

用途：保存环境检查、建档、OCR 解析和 PDF 渲染脚本。

这里保存试卷归档流程中可复用的自动化脚本。

- `check_environment.py`：检查 Git、GitHub CLI、Pandoc、XeLaTeX、PDF 工具和 MinerU 配置。
- `new_exam.py`：创建新试卷工作目录。
- `render_exam.py`：把 Markdown 渲染成可打印 PDF。
- `mineru_parse_exam.py`：调用 MinerU 解析试卷并保存可追溯归档。

