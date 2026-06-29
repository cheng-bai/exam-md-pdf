# AI 工作技能

用途：保存 AI 处理试卷、归档成品和交付验证时遵循的操作规范。

这里保存本仓库使用的可复用 AI 操作说明，用于稳定地产出、审校和维护试卷归档。

## 已包含技能

| 技能 | 用途 |
|---|---|
| `mineru-document-workflow` | 将扫描版试卷转换为 Markdown 和 PDF 的 OCR 与审校流程。 |
| `exam-archive-governance` | 最终命名、目录整理、GitHub 提交和公开仓库风险规则。 |
| `verification-before-completion` | 在声明完成、提交或推送前进行证据优先的验证。 |

## AI Agent 使用顺序

1. 解析或清理原始试卷前，先读 `skills/mineru-document-workflow/SKILL.md`。
2. 把文件移动到最终 `exams/` 归档前，先读 `skills/exam-archive-governance/SKILL.md`。
3. 提交、推送或汇报完成前，先读 `skills/verification-before-completion/SKILL.md`。

这些技能文件不写入本机 token。认证信息统一通过 `.env` 配置，不提交到仓库。
