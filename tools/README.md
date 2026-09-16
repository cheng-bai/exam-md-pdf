# 试卷电子化工具库

用途：统一索引本仓库中可公开复用的 Skills、脚本、模板和标准流程，不改变既有目录路径。

## 快速入口

- [Skills](../skills/README.md)：AI Agent 的任务路由、处理边界和验收规范。
- [Scripts](../scripts/README.md)：环境检查、建档、OCR 调用和 PDF 渲染脚本。
- [Templates](../templates/README.md)：A4 试卷源稿和审校记录模板。
- [Workflows](../workflows/README.md)：端到端处理及公开发布检查流程。

## 推荐主链

```text
扫描件/照片/PDF/DOCX
  → OCR 或 DOCX 转换
  → Markdown 逐题审校
  → 可选答案与考点标注
  → A4 PDF 渲染
  → 归档与公开发布验收
```

## 使用 Skills

仓库内的 Skill 可以直接按路径交给 Agent 阅读。需要让 Codex 在其他项目中自动发现时，克隆仓库后把所需 Skill 复制到个人技能目录：

```bash
cp -R skills/<skill-name> "${CODEX_HOME:-$HOME/.codex}/skills/"
```

只安装实际需要的 Skill，避免把整套工具全部加载到个人环境。安装后重新打开 Codex 任务，并用具体任务描述验证触发是否正确。

## 当前状态

| 类别 | 可用资产 | 状态 |
|---|---|---|
| OCR | `paddleocr-text-recognition` | 已引入官方 Skill；运行需要 PaddleOCR CLI 和本机 token |
| 纸质试卷主流程 | `paper-exam-to-md-pdf` | 可用 |
| Word 公式转换 | `math-docx-to-markdown` | 可用；带检查脚本 |
| 答案与考点标注 | `annotating-math-exam-solutions` | 可用 |
| MinerU | `mineru-document-workflow`、`mineru_parse_exam.py` | 默认适配脚本缺失，修复前不列为稳定入口 |
| 渲染 | `render_exam.py` | 可运行；强制 A4 与尺寸验收仍待修复 |
| 归档 | `exam-archive-governance` | 可用 |
| 完成验证 | `verification-before-completion` | 可用 |

## 公开边界

- 不提交 token、cookie、账号配置、本机绝对路径或私有题库原文。
- 原始扫描件、OCR dump、上传回执和预览图默认不进入工具库。
- 第三方资产必须记录来源、固定版本和许可证。
- 本机个人 Skills 只有在资料所有者确认作者权利后才能纳入；首批 3 个个人 Skill 的授权状态已记录在 `provenance.json`。

## 许可证

`skills/`、`scripts/`、`templates/`、`workflows/`、`tools/` 和 `tests/` 中的原创工具资产采用 Apache License 2.0，详见仓库根目录的 [`TOOLKIT_LICENSE.md`](../TOOLKIT_LICENSE.md)。该许可明确不覆盖 `exams/`、`handouts/`、`collections/`、`资料来源/` 等内容目录。

候选筛选和暂缓原因见 [候选资产评估](候选资产评估.md)，第三方来源见 [第三方来源与许可证](第三方来源与许可证.md)。
