# AI 工作技能

用途：保存 AI 处理试卷、归档成品和交付验证时遵循的操作规范。

这里保存本仓库使用的可复用 AI 操作说明，用于稳定地产出、审校和维护试卷归档。

## 已包含技能

| 技能 | 用途 |
|---|---|
| `paper-exam-to-md-pdf` | 将纸质或扫描试卷编排成交付级 Markdown 与 A4 PDF。 |
| `paddleocr-text-recognition` | 使用 PaddleOCR 官方 CLI 提取扫描件的行级文字和坐标。 |
| `math-docx-to-markdown` | 将公式密集 Word 文档转换为 Markdown，并检查公式结构。 |
| `annotating-math-exam-solutions` | 为高中数学试卷补答案、解析、考点和学生易卡点。 |
| `mineru-document-workflow` | 将扫描版试卷转换为 Markdown 和 PDF 的 OCR 与审校流程。 |
| `exam-archive-governance` | 最终命名、目录整理、GitHub 提交和公开仓库风险规则。 |
| `verification-before-completion` | 在声明完成、提交或推送前进行证据优先的验证。 |

## AI Agent 使用顺序

1. 用户只要逐行文字或坐标时使用 `paddleocr-text-recognition`；用户要最终 Markdown/PDF 时使用 `paper-exam-to-md-pdf` 主编排，不默认同时加载所有技能。
2. 需要答案解析和考点标注时，再使用 `annotating-math-exam-solutions`。
3. 把文件移动到最终 `exams/` 归档前，使用 `exam-archive-governance`。
4. 提交、推送或汇报完成前，使用 `verification-before-completion`。

这些技能文件不写入本机 token。认证信息统一通过环境变量或本机 `.env` 配置，不提交到仓库。第三方技能的来源和许可证记录在 `tools/第三方来源与许可证.md`。
