# Project Instructions

本项目用于试卷 PDF 电子化：原始 PDF -> Markdown 源稿 -> 可打印 PDF -> Git/GitHub 管理。

## 工作原则

- Markdown 是主源文件，PDF 是渲染产物。
- 最终交付的 Markdown 和 PDF 文件名必须按试卷内容使用中文语义化命名，不要把最终交付文件命名为 `source.md`、`cleaned.md`、`student.md`、`QUALITY_REPORT.md` 这类泛名或英文名。
- 原始 PDF、扫描图和 OCR 中间文件默认视为大文件或版权敏感文件，不主动提交，除非用户明确要求。
- Markdown 主源稿和 `outputs/*.pdf` 也可能包含版权或隐私信息；推送公开仓库前必须提醒用户确认。
- 数学公式必须使用标准 Markdown LaTeX：行内 `$...$`，独立 `$$...$$`。
- OCR 只能作为初稿来源，最终内容必须按原卷逐题校对。
- 交付前必须验证 Markdown 和 PDF 文件存在，PDF 页数合理，Pandoc 渲染无报错。

## 云端归档命名规则

- 推送到 GitHub 管理的最终试卷产物必须采用“一份试卷一个文件夹”。
- `exams/` 下的试卷文件夹命名统一使用：
  `年份学校标准名考试名称`
- 最终 `.md` 和 `.pdf` 文件名必须使用：
  `学段-学校标准名年级学科考试类型版本类型提交日期`
- 示例：
  `2026上海市建平中学高一期末数学试卷/`
  `2026上海市建平中学高一期末数学试卷/高中-上海市建平中学高一数学2026春期末解析版20260625.md`
  `2026上海市建平中学高一期末数学试卷/高中-上海市建平中学高一数学2026春期末解析版20260625.pdf`
- 文件夹名只描述试卷本身；版本类型和提交日期必须写在目录内最终文件名里，例如 `学生版`、`解析版`、`OCR审校学生版`。
- 学校标准名优先参考 `/Users/thj/Documents/Codex/2026-06-24/jp/outputs/上海各区高中学校层次分类表_2026官方版.xlsx`。该表只作为本机校名参考资料，不默认提交到本仓库。
- 如果表格无法直接读取或校名不在表中，先用原卷抬头、质量报告或用户确认的学校名；不要随意缩写为“松江一中”“华政”等非标准名，除非用户明确要求。
- 如果同一份试卷同时保留最终归档和审校现场，最终归档使用纯规则名，审校现场目录在同一规则名后追加 `-工作稿`。
- 最终归档目录内至少包含 `.md` 和 `.pdf` 两个顶层文件。若 Markdown 引用题图，必须同时提交必要的 `figures/`，保证 GitHub 上 Markdown 图片不失效。
- 不把 MinerU 原始归档、OCR dump、上传回执、布局 JSON、预览截图、原始扫描 PDF 等中间物放入云端归档目录；除非用户明确要求，不提交 `result.zip`、`summary.json`、`full.md`、`source.md`、`student.md`、`QUALITY_REPORT.md`、`page-previews/`、`final-previews/`。

## 目录约定

- `inputs/`: 原始 PDF，默认被 `.gitignore` 忽略。
- `exams/<年份学校标准名考试名称>/`: 推送到 GitHub 的最终试卷归档目录。
- `exams/<年份学校标准名考试名称>-工作稿/`: 本地审校现场或历史工作稿目录。
- `exams/<归档目录>/<学段-学校标准名年级学科考试类型版本类型提交日期>.md`: 最终 Markdown 主源稿。
- `exams/<归档目录>/<学段-学校标准名年级学科考试类型版本类型提交日期>.pdf`: 最终可打印 PDF。
- `exams/<归档目录>/figures/`: 最终 Markdown 引用的必要题图。
- 旧的 `exams/<英文或拼音临时目录>/source.md`、`outputs/`、MinerU 归档目录只作为本地工作现场或历史兼容目录；整理云端交付时不要主动纳入提交。
- `scripts/`: 项目自动化脚本。
- `examples/`: 示例材料。

## 命令约定

检查环境：

```bash
python3 scripts/check_environment.py
```

新建试卷：

```bash
python3 scripts/new_exam.py "试卷标题"
```

渲染 PDF：

```bash
python3 scripts/render_exam.py exams/<年份学校标准名考试名称>/<中文语义文件名>.md
```

带页数验收：

```bash
python3 scripts/render_exam.py exams/<年份学校标准名考试名称>/<中文语义文件名>.md --expect-pages 8
```

## Git 约定

- 提交信息优先使用 Conventional Commits。
- 初始化类提交使用 `chore: ...`。
- 试卷内容提交使用 `docs: ...`。
- 脚本修复使用 `fix: ...`。
- GitHub 远程默认使用 private，除非用户明确确认可以公开。
- 推送试卷到云端前必须确认 GitHub 仓库是 private，或用户已明确确认可以公开。
- 每次推送试卷内容时只暂存最终归档目录和必要题图；不要把未审阅的旧目录、脚本改动、OCR 中间文件混入同一提交。
- 提交前至少验证：目录名格式、同名 `.md`/`.pdf` 存在、PDF 可打开且页数/A4 合理、Markdown 图片引用存在、暂存区没有 `result.zip`、`summary.json`、`full.md`、`*_origin.pdf`、`page-previews/`。
