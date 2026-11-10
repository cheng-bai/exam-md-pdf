# 构建、检测与故障分支

## 前置条件

输入为已有 HTML 或从已授权的 Markdown 内容源生成的 HTML。先用原有脚本完成本地 KaTeX/MathJax 渲染，再准备出版；两个 helper 不承担 OCR、补解或动态公式渲染。

Python 脚本依赖 BeautifulSoup；验收另需 PyMuPDF，可选预览还需 Pillow。运行前检测现有依赖，缺失时优先使用宿主已配置运行时，不每个文档建一套环境。Node CLI 复用已有项目的绝对路径。

已验证版本是 Vivliostyle CLI 11.4.0 / Core 2.45.2 与本机 Chrome 155，不代表只能用这些版本或它们仍是最新版。版本变化后重跑代表性分页、符号和导航检查。新项目确需安装时，用该项目包管理器和锁文件；已有 lock 后 `npm ci`，不直接滚动安装 latest。

## 准备普通/紧凑出版版

在新工作目录中放入已渲染基线和必要本地资源，或直接在原目录生成不同名的兄弟文件。`prepare_publication.py` 要求输出与基线同目录，避免移动 HTML 后图片与字体相对路径失效。别复制 node_modules；不要往已有成品上覆盖。

```bash
SKILL="${CODEX_HOME:-$HOME/.codex}/skills/html-math-pdf-publishing"
python3 "$SKILL/scripts/prepare_publication.py" 已渲染底稿.html \
  --output 教师紧凑阅读版.html --title '本讲标题' \
  --density compact --prefix teacher-compact
```

脚本保留正文和公式节点，补缺失的标题 ID、拒绝重复 ID，添加覆盖 CSS、作者元数据和构建配置。它不会自动猜测题块结束边界，也不自动测量步骤高度；按 SKILL.md 在工作副本建立完整 `.problem-unit` / `.keep-step`，再保真核验。已有包装会保留。

生成中文用户入口、相对 ASCII 构建别名、`teacher-compact-layout.css`、`teacher-compact.config.mjs`；CSS 不依赖 skill 内部路径，可随成品离线分发。别名使用相对符号链接，本机有效；跨机/ZIP 分享若不能保留 symlink，应将别名物化为一份普通 HTML，再检查资源和目录跳转。

重复生成默认拒绝覆盖。只有确认这些命名文件确为本轮生成文件时使用 `--replace`；原始输入始终不可覆盖。保留基线普通版作为回滚点，不必备份整目录。

## 调用现有 Vivliostyle

定位实际可用 CLI：先 `command -v vivliostyle`；若没有则找项目中已经安装的 `node_modules/.bin/vivliostyle`。CLI 可以位于另一处，构建工作目录仍是当前 HTML 的目录。

```bash
"$CLI" --version
"$CLI" build -c teacher-compact.config.mjs \
  --executable-browser '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'
```

优先指定已安装 Chrome，避免额外下载 Chromium。若本地调试连接被代理干扰，先核验故障；单次构建可 `env -u HTTP_PROXY -u HTTPS_PROXY -u http_proxy -u https_proxy`，或正确设置 NO_PROXY。不要修改全局代理配置。

## 机器验收

```bash
python3 "$SKILL/scripts/audit_publication.py" \
  --baseline 已渲染底稿.html --html 教师紧凑阅读版.html \
  --pdf 教师紧凑阅读版.pdf --require-outline \
  --report 验收报告.json --preview-dir 验证预览
```

知道实际预期页数后才传 `--expect-pages`；不能因为案例为 6 页就把任意新讲义固定成 6 页。使用 helper 的 `--help` 查看可用的附加导航检查参数。

正文比较忽略空白，不可忽略文字、题目或公式；比较要求两份基线使用相同静态渲染表示。跨渲染器重新渲染时改为逐项数学源码对账，不能把 HTML 序列化不同误判为数学错误，也不能忽略原始源码变化。保留原图路径和来源，图片改路径时核对实际字节而非仅文件名。

报告中“有书签”只是结构检查；另从正文实际标题页建立期望页表。打印目录、点击链接、书签三者要分别验证。机器报告标注视觉检查未进行时，必须实际打开最终预览并另记已查页码。数学审校不在本脚本范围内。

脚本的正文保真是两份 HTML 的对比，不等于 PDF 全文保真已经自动通过；PDF 可提取公式顺序尤其不可靠。检查实际章节/题号、关键起止段落，并使用可比较的文本或字符序列对账，不能只看总字数。单独运行 `python3 "$SKILL/scripts/test_prepare.py"` 可复测准备脚本的保真和拒绝覆盖等边界。

CSS 字体的 `src` 往往列出 woff2/woff/ttf 多个备选：当前浏览器能加载其中一种，不等于全部候选文件都存在。检查要区分“所有引用齐全”与“有可用的离线字体候选”；缺失备用格式可以列警告，全部缺失或普通图片/CSS缺失则失败。静态候选检查仍不能取代浏览器 `document.fonts.ready` / `document.fonts.check()` 与最终字形目视核验。

运行 `python3 "$SKILL/scripts/test_audit.py"` 可复测字体候选与普通资源的 8 项成功/失败边界。测试自建临时 PDF 并在结束时清除，不依赖本次项目或 `/tmp` 历史文件。

## 已观察到的故障及处理顺序

| 症状 | 处理 | 防止过度外推 |
|---|---|---|
| PDF 书签为空 | 给缺少 ID 的标题加唯一锚点，重建核验 | 不是所有无书签都由此引起 |
| 书签全部跳末页、目录外观却正常 | 尝试 ASCII 构建入口，保留中文成品名；逐项目的页复验 | 11.4.0 的本案现象，不称为官方确认的通用缺陷 |
| 不等号斜线丢失 | 先检查实际字体/渲染节点及版本；必要时局部等价显示修补，再看最终 PDF | 不把案例 NEQMARK 替换无条件套用到所有文档 |
| 公式编号换行或游离 | 检查静态公式容器；按渲染器能力安排关系式与编号布局 | 不用简单正则重写嵌套 `\\tag` |
| 小问结果落到下一页 | 包装有限的关键步骤及结论，防止 break 避免链无限延长 | 不强包超长整题 |
| 文末有留白 | 先查内容是否结束及整体换页约束；按用途决定密度 | 不缩字到不可读、不把所有空白当失败 |
| 手机上整页横向溢出 | 单独做屏幕媒体规则，行间公式可局部滚动；打印版另检 | 手机通过不代表 PDF 无裁切 |

## 可逆清理

只认领本轮生成的 `.vivliostyle*` / `.prefix-cache`、重复编译文件、测试运行目录。保留依赖、源图、内容底稿、已交付 PDF 和必要证据。压缩归档后逐文件校验哈希，再移除原缓存；记录原路径、字节数、归档大小和恢复命令。释放量以原占用减去归档占用计算，注明逻辑大小与文件系统分配大小，不承诺即时物理释放（快照等可能影响）。
