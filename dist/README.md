# 可分发压缩包

用途：存放可直接发给同事或上传到聊天窗口的成品压缩包，免去对方克隆仓库。

## 文件

| 文件 | 说明 |
|---|---|
| `exam-md-pdf-skills-share-20261110.zip` | 数学解析与 PDF 出版技能分享包，解压后得到 `exam-md-pdf-skills-share/`，内含 `README.md`、`LICENSE` 和三个技能目录 |

## 维护方式

`skills-share/` 是分享包的源目录，本目录里的 ZIP 只是它的打包产物。改动技能后按 `skills-share/README.md` 里的命令重新生成，并把新版压缩包一并提交；不要只改 ZIP 不改源目录。

压缩包内不含试卷、讲义成品、学生材料或本机配置，仅含技能说明、模板、样式和检查脚本，许可为 Apache License 2.0。
