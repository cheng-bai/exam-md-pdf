# 题目 ID 与数学交互作品的绑定规范 v1

绑定描述“某题或某小问，使用哪个固定版本作品、哪个场景、以什么初始参数打开”。它是作品之外的多对多关联，不是作品身份，也不是用户交互日志。新增题目关联不重封作品；`entrypoints.component` 仍仅是组件文件入口，不意味着跨框架运行 API 已统一。

## 身份、字段与事实源

完整交换格式见 [question-bindings-v1.schema.json](../schemas/question-bindings-v1.schema.json)：`{"schema_version":"1.0","bindings":[记录...]}`。

| 字段 | 含义 |
|---|---|
| `binding_id` | 关联 UUID，永久且不可用相同 ID 改写内容 |
| `question_namespace` | 题库命名空间，如 `demo.anatomy`；不同来源的相同题目 ID 不混淆 |
| `question_id` | 来源系统的稳定题目 ID，字符串，保留前导零，不用临时题号冒充 |
| `subquestion_id` | 可选小问 ID；缺省表示整题 |
| `question_revision` / `question_content_sha256` | 可选题目修订号/约定内容字节的 SHA-256，用于检测题目漂移；本工具不读取外部题库验证 |
| `asset_id` / `asset_version` | 作品 UUID 与精确三段版本，不允许 latest 或版本范围 |
| `asset_manifest_sha256` | 作品 manifest 原始字节指纹，校验是否确为同一封存内容 |
| `scene_id` | 可选、须存在于该版本作品的稳定场景 ID |
| `initial_state` | 参数覆盖，分 `math`、`view`、`lesson`；可省略组，不接受未知参数 |
| `created_at` / `created_by` | UTC 创建时间与创建者标识，不能捏造人名 |
| `note` | 可选说明，如教学用途、示例标记 |

`bind` 接受单条草稿，自动补全 UUID、时间、空覆盖和实际 manifest 指纹。`created_by` 由调用方提供。正式记录保存在 `<数据库完整路径>.bindings/<binding_id>.json`，SQLite `question_bindings` 是可重建索引；移动作品后通过固定身份重新解析位置。复制/迁移整个库应携带数据库旁的 `.bindings` 目录；也可使用显式 JSON 导出再导入。修改绑定须新建 ID；v1 不含删除/撤销历史语义。

记录按 UUID 不可变。JSON 对象字段顺序不影响记录身份；数组顺序和数值表示仍保留。重导入相同记录幂等，不同内容的同 ID 拒绝。每次解析、导出和导入重新校验作品文件与指纹。事实文件写入采用临时文件和原子创建，普通异常清理本次新增文件，数据库事务回滚；断电/进程强杀不保证跨文件系统与 SQLite 原子性，残留事实可用于显式重建。不得自行扫描其他目录寻找题目。

## 状态契约与实际恢复

新制作品使用 [manifest 1.1](../schemas/manifest-v1.1.schema.json)，声明 `state_link:"hash-json-v1"`、完整 `default_state` 与 `state_contract`。每个参数声明 `number`、`integer`、`boolean` 或 `string` 类型，可加 `minimum`、`maximum`、`enum`。默认和场景状态都必须完整符合契约；覆盖允许部分字段。合并顺序：**默认 → 场景 → 题目绑定覆盖**，各组按参数名浅合并。

`resolve-binding` 返回入口 URL `#scene=<id>&state=<URL编码JSON>` 及合并状态。HTML 必须实际解析、验证并应用参数，监听 hashchange；非法链接明确提示并恢复默认，不能悄悄截断。数学定义域、展示范围与可输入状态范围分开：`display_range` 是滑块展示范围，不自动限制数学参数。页面内“全部重置”恢复作品默认值。

旧 manifest 1.0 可以绑定整件作品或已存在场景；**拒绝非空参数覆盖**，避免假装旧页面能恢复任意状态。规范/结构通过不等于浏览器恢复通过；交互验收要检查实际控件、图形、公式和模型结果。

## CLI

以下命令中的路径由用户资料库决定；本次默认仍是任务输出目录。命令返回 JSON，不执行导入包代码。

```sh
python3 scripts/resources.py migrate --db <现有库.sqlite>
python3 scripts/resources.py bind --file <单条绑定草稿.json> --db <库.sqlite>
python3 scripts/resources.py bindings --question-namespace demo.anatomy --question-id tetrahedron-section-001 --db <库.sqlite>
python3 scripts/resources.py bindings --reference 'anatomy:<uuid>@1.1.0' --db <库.sqlite>
python3 scripts/resources.py resolve-binding <binding_uuid> --db <库.sqlite>
python3 scripts/resources.py bindings-export --out <绑定集合.json> --db <库.sqlite>
python3 scripts/resources.py bindings-import <绑定集合.json或事实目录> --db <库.sqlite>
python3 scripts/resources.py rebuild <作品归档目录> --bindings <绑定集合.json或事实目录> --db <新库.sqlite>
python3 scripts/resources.py export 'anatomy:<uuid>@1.1.0' --with-bindings --out <作品与绑定.zip> --db <库.sqlite>
python3 scripts/resources.py import <作品与绑定.zip> <新作品目录> --db <目标库.sqlite>
```

`bindings` 可加 `--subquestion-id` 精确筛选小问；不加返回该题整题与所有小问的关联。作品反查可加 `#scene=` 限定场景。已有库先 `migrate`，自动做 SQLite 一致备份再添加表，保留现有作品；新库直接含关联表。读命令使用只读连接，不占写锁。

普通 ZIP 仍只有原作品包；`--with-bindings` 生成传输封套：`transfer.json`、`package/`、`question-bindings.json`。清单记录原 manifest 和绑定 JSON 的 SHA-256，原作品字节不改。只携带该固定作品版本的关联；导入需先通过 ZIP 路径/CRC/大小/文件类型、作品、关联目标、场景及状态校验。重复绑定幂等；导入目标目录已存在时拒绝，需选新的目录。导入的外部题目 ID 不代表外部题库已接入或已核实。

## 演示草稿

下面是演示，`demo.anatomy` 与 `tetrahedron-section-001` 不是真实题库映射：

```json
{
  "question_namespace": "demo.anatomy",
  "question_id": "tetrahedron-section-001",
  "subquestion_id": "2",
  "asset_id": "ee8d0713-4f88-44d6-88da-57e9d25aef21",
  "asset_version": "1.1.0",
  "scene_id": "rectangle",
  "initial_state": {"math":{"t":10},"view":{"azimuth":130},"lesson":{"step":2}},
  "created_by": "Codex demo",
  "note": "仅演示绑定；t=10 时截面为长方形，面积为 3000。"
}
```
