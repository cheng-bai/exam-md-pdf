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
| `ai-math-question-intake` | 将试卷、讲义或图片整理成可回源、可检索的题目记录，并标明识别与审校状态。 |
| `ai-math-exam-compilation` | 从可追溯母集生成多用途的专题分类汇编，并对账来源、题号、分类和版本。 |
| `ai-math-question-visualization` | 将已有题目转化为以变量、约束和关键关系为中心的教学可视化。 |
| `anatomy` | 制作数学概念、函数图像、几何构造、立体截面和证明步骤的交互可视化；保留原版等轴测插画能力。 |
| `math-solution-style` | 编写或润色中文高中数学解析：以“依据、操作、结论”推进推导，详细讲评不压缩有效步骤。 |
| `lecture-pdf-layout` | 中文高中数学讲义、题集和教师版的 A4 版式：题干框、答案解析层级、分页与阅读密度。 |
| `html-math-pdf-publishing` | 用 HTML、CSS 和本地 KaTeX 出版可离线阅读的数学讲义 PDF，核验公式、分页、目录与书签。 |

## AI Agent 使用顺序

1. 用户只要逐行文字或坐标时使用 `paddleocr-text-recognition`；用户要最终 Markdown/PDF 时使用 `paper-exam-to-md-pdf` 主编排，不默认同时加载所有技能。
2. 需要把材料整理成可回源题目记录时，使用 `ai-math-question-intake`；需要把多套试卷组织成专题分类汇编时，使用 `ai-math-exam-compilation`。
3. 需要答案解析和考点标注时，再使用 `annotating-math-exam-solutions`；新写或润色解析时，用 `math-solution-style` 约束表达与详略。
4. 内容定稿后需要整页 LaTeX 版式时使用 `lecture-pdf-layout`；明确走 HTML 出版路线、需要目录书签或紧凑分页时使用 `html-math-pdf-publishing`。
5. 把文件移动到最终 `exams/` 归档前，使用 `exam-archive-governance`。
6. 提交、推送或汇报完成前，使用 `verification-before-completion`。
7. 需要交互图形、参数探索或离线数学页面时，先用 `ai-math-question-visualization` 明确数学关系与验收目标，再使用 `anatomy` 实现；两者都不承担 OCR、试卷归档或答案审定。

## 数学解析与 PDF 出版链路

新写解析时先保持内容正确，再按 `math-solution-style` 补足关键依据和推导；需要整页 TeX 讲义时交给 `lecture-pdf-layout`，已有 HTML 或需要目录书签与紧凑分页时交给 `html-math-pdf-publishing`。三者分别负责表达、版式和出版，任何一项通过都不能代替数学审校或实际查看成品。

这些技能文件不写入本机 token。认证信息统一通过环境变量或本机 `.env` 配置，不提交到仓库。第三方技能的来源和许可证记录在 `tools/第三方来源与许可证.md`。
