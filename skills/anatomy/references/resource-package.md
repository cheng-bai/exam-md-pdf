# 数学交互资源规范 v1：作品包与数据库索引

适用：通过 Anatomy 交付的数学交互作品。普通数学任务默认交付标准作品包；用户明确只要图或组件时尊重其范围，说明尚未归档。数据库路径使用用户已有资料库；没有指定时放在本次输出目录，不隐式建立共享服务或扫描其他资料。

## 身份、版本与引用

- `asset_id` 是创建作品时生成的规范小写 UUID。标题、文件夹、存储设备或作者变化不改变它。新作者编辑同一作品保留 ID；独立改编、分叉或新作品生成新 ID，用 `derived_from` 记录来源。
- `version` 为三段非负整数 `major.minor.patch`，不使用隐式 `latest`。修正文字/样式升 patch；兼容地增加场景/交互升 minor；改变数学任务、参数含义或场景语义升 major。升级时保留旧版本包。
- `schema_version: "1.0"` 是清单格式版本，与作品版本独立。
- 封存后，同 ID＋版本必须对应完全相同的 `manifest.json` 字节和全部载荷哈希。修改文件、元数据、验证结论乃至重排清单，都应生成新作品版本；不要通过更新哈希覆盖旧版。同版本的完整副本可以共存。
- 场景 ID 使用稳定英文 slug，例如 `degenerate`；它标识一组数学、视角、讲解初始状态。场景含义不随标题或顺序变化，删除/改变语义按重大版本处理。使用可选 `extensions` 保存未标准化字段，不擅自增加顶层字段。

引用为可解析的文本标识：

```text
anatomy:ee8d0713-4f88-44d6-88da-57e9d25aef21@1.0.0
anatomy:ee8d0713-4f88-44d6-88da-57e9d25aef21@1.0.0#scene=degenerate
```

这不是已经注册的浏览器协议。`resolve` 将它转换成当前机器可打开的 `file:` URL；讲义或网站可以保存上述标识，在打开时调用解析层。静态文件链接只适用于当前位置。v1 不提供联网短链接、跨机器自动同步或 PDF 自动改链。

## 作品包结构

```text
tetrahedron-1.0.0/
  manifest.json             身份、描述、入口、文件清单、场景及验证
  index.html                可离线打开的入口
  source/                   模型、必要源码、构建依赖及许可
  previews/                 按需：实际预览图
  evidence/                 数学、交互、视觉、离线检查的证据
```

目录名可变化；入口与资源由清单确定。运行载荷、必要源码和依赖必须带齐，不能引用制作人的私有绝对路径。清单中的包内文件路径是相对 POSIX 路径，不允许 `..`、绝对路径、反斜杠、符号链接或大小写冲突。完整列出所有文件，`manifest.json` 自身不进入 `files`，避免递归哈希；数据库、临时脚本和编辑草稿放到包外。

## 清单契约

机器规范在 [manifest-v1.schema.json](../schemas/manifest-v1.schema.json)。`scripts/resources.py` 使用 Python 3.10+，不依赖第三方库，按该文件使用的 JSON Schema 子集检查格式，并补充哈希、路径、证据、重复 ID 等语义检查；其他实现可用完整 JSON Schema 2020-12 验证器，然后执行相同语义检查。

| 字段 | 内容 |
|---|---|
| `schema_version / asset_id / version / slug / title / language` | 格式、身份、固定版本与可搜索标题 |
| `created_at / updated_at` | UTC `Z` 时间；更新时间不能早于创建时间 |
| `contributors / rights` | 实际作者/修改人/复核者；许可与署名要求。不把调用者自动登记成作者，不擅自授予公开使用权 |
| `math` | 主题、受众、对象、条件、教学目标、参数定义及近似说明；参数显示范围不等于数学定义域 |
| `entrypoints` | 必需的 HTML 预览入口；可选 SVG/组件入口，都须列为 runtime 文件 |
| `files` | 每个文件的相对路径、角色、SHA-256、字节数；可附 MIME 与许可 |
| `scenes` | 稳定 ID、标题及 `state.math / view / lesson` 初始状态；无场景时可为空数组 |
| `provenance.sources` | 原题、文献或创作来源；可附 URI 与说明 |
| `provenance.relations` | `derived_from / uses / cites` 指向其他作品的固定版本或场景 |
| `validation` | mathematics、interaction、visual、offline 四类分别记录，不能合并成一个“已验收” |
| `extensions` | 非标准扩展对象，可为空 |

所有时间、作者、来源与验证范围据实填写；未知项用说明或 `pending`，不编造。验证状态可为 `pass / fail / pending / not_applicable`；后者写明理由。`pass` 和 `fail` 必须包含实际检查时间、包内证据路径和 `tested_files` 的受检文件哈希。封存工具不会自动生成通过记录。证据的内容与充分性仍须人工/数学/浏览器复核，结构检查只能证明文件和声明一致。

场景状态以清单和运行时共享的模型数据为准。HTML 应支持 `#scene=<id>`，离线打开即恢复该场景；同页面切换 hash 也要生效。未知 ID 显示明确提示并恢复默认状态。场景只定义初始状态；用户随后拖动参数不会回写封存清单。检验脚本不能只比较清单文字，要实际打开每个场景确认参数与结果。

## 制作与封存

1. 先完成并验证数学作品，准备包内文件。新建作品用 `python3 -c 'import uuid; print(uuid.uuid4())'` 生成 ID。
2. 在包外准备元数据草稿 JSON，字段遵循 schema；`files` 可先列路径和角色，`seal` 会补齐 SHA-256 与字节数。已完成的验证需要另行提供真实 `tested_files` 哈希。
3. 实测包内入口，保存证据并将其加入 `files`；更新四类验证记录。再封存：

```sh
python3 scripts/resources.py seal /path/to/package --metadata /path/to/metadata.json
python3 scripts/resources.py validate /path/to/package
python3 scripts/resources.py index /path/to/package --db /path/to/library.sqlite
```

`seal` 拒绝覆盖已有清单。校验失败会停止，不将未列出文件默默丢弃。包中 `pending` 可保存，但不能称为全面验收。

四面体完整草稿生成例：

```sh
node examples/math-tetrahedron/package.mjs --out /path/to/tetrahedron-1.0.0
```

它输出包与同级 `.metadata.json`，运行真实数学检查并记录，其他三类保持 pending；完成实际浏览器/视觉验收后再封存。该例默认使用固定示例 ID；可用 `--asset-id <uuid> --version 1.1.0` 指定身份与版本。新作品应更换 ID；继续维护同一示例应保留 ID 并升级版本。

## 数据库、查询与引用关系

SQLite 索引保存 releases、locations、files、scenes、relations。元数据来自清单，机器路径只在 locations 中；目录搬迁不改变作品身份。索引能存多个作者、版本和副本。相同 ID＋版本且不同清单会拒绝入库，批量入库在一个事务内完成。

```sh
python3 scripts/resources.py list --db /path/to/library.sqlite --query 截面
python3 scripts/resources.py list --db /path/to/library.sqlite --topic 立体几何
python3 scripts/resources.py resolve 'anatomy:<uuid>@1.0.0#scene=degenerate' --db /path/to/library.sqlite
python3 scripts/resources.py refs 'anatomy:<uuid>@1.0.0' --db /path/to/library.sqlite
```

`resolve` 重新检查当前载荷与入库清单的哈希，返回入口路径、实际 URL、场景状态和不可用副本说明；没有有效副本就报错。`refs` 返回入库作品的出引用和入引用，未入库目标明确标记 `target_indexed:false`。外部讲义/PDF/网站只有显式登记成资源并记录关系后才会出现在此查询中，不声称自动发现使用者。

索引丢失时，从明确指定的资料根目录建立新数据库：

```sh
python3 scripts/resources.py rebuild /path/to/packages --db /path/to/new-library.sqlite
```

重建要求新数据库路径，保留旧索引；遇到损坏、冲突清单会停止并回滚导入。不会扫描未指定目录，也不自动决定哪个版本“最新”。

## 移动、跨设备与打包

同一文件系统中移动整个作品包并更新位置索引：

```sh
python3 scripts/resources.py move /old/package /new/package --db /path/to/library.sqlite
```

目的地须不存在，目录与索引变更失败会尝试回滚；同 ID＋版本引用保持不变。直接用 Finder 移动后，可以重新 `index /new/package`；失效旧路径不删除历史作品，解析时跳过不可用副本。数据库必须放在被移动包外。

跨文件系统或跨机器使用导出/导入，原包保留，确认新包有效后再由用户决定旧副本去留：

```sh
python3 scripts/resources.py export 'anatomy:<uuid>@1.0.0' --db /path/to/library.sqlite --out /path/to/package.zip
python3 scripts/resources.py import /path/to/package.zip /path/to/new-package --db /path/to/target-library.sqlite
```

ZIP 中根目录即作品包内容；导出检查 CRC 和逐文件回读，并返回 ZIP SHA-256。导入不执行代码，拒绝越界、重复、特殊文件和超限内容，先在临时目录校验，再放到目标位置并入库。v1 导入上限为 5001 个文件、解压总大小 256 MiB；目标路径不能存在。ZIP 包含可独立打开的作品与清单，不携带原数据库中的私有绝对路径。

完整验收还应从导出 ZIP 解压后的文件直接打开，实际检查公式、场景与关键操作。归档校验通过不代表数学正确、许可已授权或浏览器已验收。

## 题目关联扩展

题目关联采用独立的[题目绑定规范 v1](question-bindings.md)，不修改已封存作品清单。新作品 manifest 1.1 增加状态恢复契约，旧 manifest 1.0 保留兼容；两种 schema 不混用。标准作品 ZIP 可用 `export --with-bindings` 置于传输封套，携带该精确版本的关联记录。关联事实与 SQLite 索引均可查询、迁移与显式重建。
