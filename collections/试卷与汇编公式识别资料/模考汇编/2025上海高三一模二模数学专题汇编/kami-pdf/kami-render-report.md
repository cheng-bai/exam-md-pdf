---
title: Kami 渲染与验收报告
date: 2026-08-05
status: completed
---

# Kami 渲染与验收报告

## 交付结论

- 已将 15 个专题分册全部渲染为 Kami 风格 PDF。
- 共 671 题、459 页，页面尺寸均为 A4。
- 共检测 15,641 个数学公式节点，15,641 个均完成本地 KaTeX 渲染。
- 共处理 179 个图片引用；输出目录约 61 MB。
- 原专题 Markdown、原始 PDF、原始图片及三份源 Markdown 均未修改。

## 渲染路线

采用 Kami 中文长文档视觉体系：先用 Pandoc 将 Markdown 转换为 HTML，通过薄适配层处理 Obsidian 图片、callout 和标题，再使用本地 KaTeX 预渲染公式，最后由 Headless Chrome 打印为 A4 PDF。答案、解析和疑点分别转换为静态 Kami 卡片，HTML 不依赖外部 HTTP/HTTPS 资源。

## 专项处理

- 移除了 Obsidian 不可见锚点，避免 `#### Qxxxx` 被打印为字面文本。
- Q0671 的 14 张天气图外链已失效，依据尺寸从二模解析资料的本地图片中匹配并复制到本次 Kami 输出；未改动原分册。
- Q0627 的末尾图片曾形成孤立尾页，仅在打印适配层将该图缩至 28 mm，使图片回到所属解析页。
- 立体几何与空间向量第 18 页文字较少，但该页实际承载同一道题的 4 张方案图，目视确认分页合理。

## 验收结果

- 15 份 PDF 均通过 `pdfinfo` 页面尺寸检查，全部为 A4。
- 15 份 PDF 均通过 `qpdf --check`。
- `pdffonts` 检查均包含 TsangerJinKai02 和 KaTeX 字体。
- 文本检查未发现原始 `\\frac`、`\\log`、HTML 标签或 KaTeX 残留。
- 15 份 HTML 均未引用外部 HTTP/HTTPS 资源。
- 每册 HTML 的题目标题数、图片数与对应源分册一致。
- 已检查每册首页、中页、末页，共 45 张预览；数学建模 5 页全部目视检查。
- 三份源 Markdown 的 SHA-256 与渲染前 manifest 一致。

## 审校边界

本报告确认的是渲染完整性、离线资源、字体、公式输出、图片归属、页面尺寸和 PDF 文件结构。此次没有逐题重新证明答案或复核全部数学推导，因此不能把“渲染验收通过”等同于“逐题数学审校通过”。源资料中无法可靠判断或已标注需复核的内容保持原状。

详细逐册统计见 [render-report.json](render-report.json)，抽检页记录见 [sample-report.json](sample-report.json)。
