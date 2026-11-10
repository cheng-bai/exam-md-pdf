# Anatomy · 数学交互与等轴测插画

用途：把数学概念、函数图像、几何构造、立体截面、参数轨迹和证明步骤做成可独立打开的交互页面；同时保留原版精细等轴测技术插画能力。

本目录是 **数学优先的本地修订版**，基于 [wheresryan22/anatomy](https://github.com/wheresryan22/anatomy) 的 MIT 技能整理，不是上游仓库的字节副本。数学分支、中文使用说明和反馈回归规范有本地修订；原版机械插画流程、示例和工具库继续保留。实际执行规范以 [`SKILL.md`](SKILL.md) 为准，本文件只说明安装、范围和验证方式。

## 适合做什么

| 目标 | 建议表达 |
|---|---|
| 函数、平面解析几何、单位圆、数列、概率 | 等比例二维 SVG，图形与公式、表格联动 |
| 空间位置、截面、投影、向量、旋转体 | 三维数学模型＋正交投影 SVG，必要时使用成熟 3D 渲染器 |
| 尺规构造、拉绳椭圆等机制本身有数学意义 | 适量仪器结构＋准确的数学对象 |
| 明确要求精细机械技术插画 | 原版等轴测绘图流程 |

数学作品先建立可复算的纯模型，再让图形、公式、读数和讲解步骤读取同一份状态。视角变化不得改写数学参数；临界值、退化情形和空集要有诚实展示。详细规范见 [`references/math-teaching.md`](references/math-teaching.md)、[`references/math-design.md`](references/math-design.md) 和 [`references/math-validation.md`](references/math-validation.md)。

## 安装

这是一个标准 Agent Skill：目录根部有 `SKILL.md`。按使用的 Agent 选择安装位置。

### Codex

```sh
mkdir -p "${CODEX_HOME:-$HOME/.codex}/skills"
cp -R skills/anatomy "${CODEX_HOME:-$HOME/.codex}/skills/anatomy"
```

安装后重新打开 Codex 任务，让技能索引刷新。

### Claude Code

```sh
mkdir -p ~/.claude/skills
cp -R skills/anatomy ~/.claude/skills/anatomy
```

也可以只装到某个项目：把目录复制到项目内的 `.claude/skills/anatomy` 或 `.codex/skills/anatomy`。安装时复制整个目录，不要只复制 `SKILL.md`，因为数学规范、示例和 kit 都在子目录中。

## 快速开始

在 Codex 或 Claude Code 中直接描述数学任务，例如：

```text
用 Anatomy 做一个正四面体平行截面的交互页面：
可调截面高度，显示截面形状和面积，桌面与手机都能操作。
```

技能会先确认数学对象、参数范围和验收目标，再建立模型、交互与离线页面。普通函数图像不需要机械底座、零件配额或实体装配审计。

## 示例

`examples/` 中有 9 个完整示例。数学分支从 `math-tetrahedron` 开始；其余示例保留原版机械插画与 WebGL/3D 能力。

| 示例 | 内容 | 运行 |
|---|---|---|
| [`math-tetrahedron`](examples/math-tetrahedron/CONCEPT.md) | 正四面体平行截面：独立数学模型、截面高度、视角、讲解步骤、正交投影和等比例截面图；原生 MathML，无远程资源 | `node examples/math-tetrahedron/build.mjs --out <输出目录>` |
| [`dial-indicator`](examples/dial-indicator) | 百分表、表座和量块滑架，最小的机械示例 | `node examples/dial-indicator/build.mjs` |
| [`desk-computer`](examples/desk-computer) | 1984 风格桌面电脑，可敲击键盘，CRT 显示输入内容 | `node examples/desk-computer/build.mjs` |
| [`arcade-cabinet`](examples/arcade-cabinet) | 侧板打开的街机柜：投币、币道、开关脉冲和 CRT 自检 | `node examples/arcade-cabinet/build.mjs` |
| [`raptor-engine`](examples/raptor-engine) | 试验台中的 Raptor 2 发动机，可拆成 11 个组件，含 WebGL 尾焰 | `node examples/raptor-engine/build.mjs` |
| [`ripple-tank`](examples/ripple-tank) | 学校水波槽，两层 WebGL 与色散、光学模型联动 | `node examples/ripple-tank/build.mjs` |
| [`test-rig`](examples/test-rig) | React/Next.js 中的玻璃按钮、探针和百分表 | 无构建脚本，复制到 React 项目使用 |
| [`spot-plate`](examples/spot-plate) | React 示例：六对玻璃液滴随探片张开而融合 | 无构建脚本，复制到 React 项目使用 |
| [`turning-dial`](examples/turning-dial) | 3D beta：组合拨盘、机械手和可脱落部件 | `node examples/turning-dial/build.mjs` |

机械示例加 `--light` 可生成浅色主题。`raptor-engine` 构建需要几分钟；`--audit` 会额外运行几何审计。

### 正四面体小样

```sh
node examples/math-tetrahedron/check.mjs
node examples/math-tetrahedron/build.mjs --out <输出目录>
```

输出 `tetrahedron-section.html`，可直接离线打开。页面内联 kit、数学模块和展示代码，不依赖远程字体、脚本或图片。模型接受任意有限截面高度；演示范围为 `t ∈ [-50, 50]`，并覆盖正方形、长方形、退化棱和空集状态。

需要标准作品包时：

```sh
node examples/math-tetrahedron/package.mjs --out <空目录>
```

该命令生成可移植作品包草稿和实际模型检查证据；其他验收项保持 `pending`，完成检查后再按 [`references/resource-package.md`](references/resource-package.md) 封存。

## 目录

```text
anatomy/
├── SKILL.md                 技能入口：工作流、分支选择和验收规则
├── kit/                     SVG、WebGL、3D 与 React 绘图工具
├── references/              数学、机械、渲染、验证和资源规范
├── examples/                9 个完整示例
├── scripts/                 截图、驱动、几何检查和资源封存脚本
├── schemas/                 作品清单与状态契约 schema
├── evals/                   技能评测提示
├── tests/                   资源与数学检查测试
└── CHANGELOG.md             本地修订记录
```

## 依赖

| 依赖 | 用途 | 说明 |
|---|---|---|
| Node.js 20.10+ | 构建、kit、检查脚本 | 只用 Node 内置模块，无需 `npm install` |
| Chrome 或 Chromium | 截图、驱动、几何与 3D 检查 | 无头运行并开启 WebGL；可用 `CHROME_PATH` 指定 |
| Python 3.10+ | `scripts/resources.py` 资源封存与索引 | 仅标准库 |
| React 18+ | 仅 React 输出 | `kit/react/` 与两个 React 示例 |

## 验证

在技能目录运行：

```sh
PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s tests -v
node examples/math-tetrahedron/check.mjs
node examples/math-tetrahedron/build.mjs --out <输出目录>
```

验证应覆盖数学模型、临界值与两侧邻域、空集和非法输入、场景深链接、离线打开、桌面与约 390 px 手机截图，以及公式真实渲染。通过结构检查不等于完成数学证明；截图和浏览器检查必须实际读过。

## 边界

- 不是通用图表库：没有坐标轴、数据系列和统计图封装；需要统计图时使用专门工具。
- 数学分支优先二维 SVG 和可复算模型；只有空间关系确实需要时才使用三维投影或 3D 运行时。
- 原版 `kit/audit.mjs` 的零件、线端和遮挡规则只适用于机械插画，不要求数学曲线、坐标轴和虚线通过机械审计。
- 3D 模式仍是 beta；性能与稳定性按具体示例和实测环境说明。
- 构建需要 Node，打开生成页面不需要 Node；数学作品不依赖 CDN。

## 来源与许可证

- 上游项目：[wheresryan22/anatomy](https://github.com/wheresryan22/anatomy)
- 参考提交：`1482e8469b0a9e0d8cc18ea2740a01423d29ae80`
- 许可证：MIT，原始版权行保留在 [`LICENSE`](LICENSE)
- 本地修订：数学分支、中文使用说明、反馈回归规范及数学示例；不是上述提交的字节副本

本目录继续按 MIT 许可证提供。再分发时请保留 [`LICENSE`](LICENSE) 中的版权与许可声明，并注明本地修订。
