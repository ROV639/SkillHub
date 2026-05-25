# Rubin SkillHub 总索引

更新时间：2026-05-25  
维护人：Robin / Codex  
仓库：ROV639/SkillHub  
用途：所有 Agent 共用的 Skill 总目录

## 当前状态

- ready skills：0
- lab skills：1
- external_unverified：0
- blocked_prod：0
- 最近一次扫描：2026-05-25
- 最近一次晋升：无

## 快速使用

如果你是 Agent：

1. 优先读取本文件。
2. 只自动调用 `状态=READY` 且 `风险<=R2` 的 skill。
3. `R3` 以上必须提示 Robin 确认。
4. `BLOCKED_PROD` 只能研究，不能执行。
5. 不要从 `external_unverified/` 直接安装。

如果你是 Robin：

- 想找能马上用的，看“即拿即用”。
- 想看正在测试的，看“候选测试区”。
- 想看外部学习来源，看“外部仓库雷达”。
- 想看高风险能力，看“封存/受限区”。

## 状态定义

| 状态 | 含义 | Agent 是否可自动调用 |
|---|---|---|
| READY | 已测试，可复用 | 可以，受风险等级限制 |
| LAB | 正在测试或改写 | 不自动调用，除非任务明确要求测试 |
| ADAPTING | 正在从外部改写成 Rubin 版本 | 不自动调用 |
| REFERENCE | 只读参考 | 不调用 |
| BLOCKED_PROD | 禁止生产执行 | 不调用 |
| DEPRECATED | 已废弃 | 不调用 |

## 风险等级

| 风险 | 含义 | 规则 |
|---|---|---|
| R0 | 纯提示词/纯文档 | 可自动调用 |
| R1 | 读取本地普通文件或公开网页 | 可自动调用 |
| R2 | 调 API / 生图 / 下载公开内容 | 需要成本提示或环境检查 |
| R3 | 浏览器登录态 / Cookie / 账号草稿 | 必须人工确认 |
| R4 | 真实发布 / 删除 / 互动 / 远程执行 | 禁止无人值守 |

## 即拿即用

| 中文名 | 目录名 | 状态 | 风险 | 版本 | 加入日期 | 更新日期 | 最近测试 | 适合做什么 | 推荐 Agent |
|---|---|---|---|---|---|---|---|---|---|
| 暂无 | - | - | - | - | - | - | - | - | - |

## 候选测试区

| 中文名 | 原型来源 | 目录名 | 当前动作 | 加入日期 | 更新日期 | 测试重点 | 负责人 | 下一步 |
|---|---|---|---|---|---|---|---|---|
| 证据研究所 | Rubin 原创 | `rubin-evidence-lab` | LAB 回测中 | 2026-05-25 | 2026-05-25 | 仓库评估、工具调研、内容事实核查 | Codex | 继续做工具/API 和内容事实核查回测 |

## 外部仓库雷达

| 仓库 | 类型 | 当前判断 | 放置位置 | 最近核查 | 下一步 |
|---|---|---|---|---|---|
| JimLiu/baoyu-skills | 内容生产 skill 池 | 第一外部样本池 | 待放入 `external_unverified/baoyu-skills` | 2026-05-25 | 测 7 个低风险 skill |
| freestylefly/canghe-skills | 个人 skill repo | 本地化对照 | 待放入 `external_unverified/canghe-skills` | 2026-05-25 | 只参考改写方式 |
| laolaoshiren/claude-code-skills-zh | 中文代码类 skill | 轻量对照组 | 待放入 `external_unverified/claude-code-skills-zh` | 2026-05-25 | 测 `zh-readme` |
| Jst-Well-Dan/Skill-Box | 技能市场/分类目录 | 学分类，不安装 | `docs/source_radar.md` 候选 | 2026-05-25 | 吸收标签体系 |
| yzfly/awesome-claude-skills-zh | 中文资料索引 | 资料雷达 | `docs/source_radar.md` 候选 | 2026-05-25 | 只读参考 |
| yzfly/awesome-mcp-zh | MCP 中文资料索引 | 工具雷达 | `docs/source_radar.md` 候选 | 2026-05-25 | 只读参考 |
| NanmiCoder/MediaCrawler | 社媒样本采集工具 | 另开工具沙盒 | `tools_lab/` 候选 | 2026-05-25 | 不进 ready |
| dreammis/social-auto-upload | 社媒自动上传 | 技术储备，高风险 | `blocked_prod/` 候选 | 2026-05-25 | 提取发布包 schema |

## 封存 / 受限区

| 名称 | 来源 | 原因 | 允许动作 | 禁止动作 |
|---|---|---|---|---|
| 社媒自动发布器 | social-auto-upload | R4，真实发布风险 | 研究字段、生成本地发布包 | 无人值守发布 |
| danger / post 类 skill | baoyu-skills 等 | Cookie、登录态、账号写操作 | 研究结构、草稿链路 | 读取真实 token、自动互动 |

## 最近更新

| 日期 | 动作 | Skill / 来源 | 说明 |
|---|---|---|---|
| 2026-05-25 | 新建索引 | SkillHub | 建立人类与 Agent 共读总索引 |
| 2026-05-25 | 新增候选 | `rubin-evidence-lab` | 进入 `skills/lab/rubin-original/` |
| 2026-05-25 | 完成回测 | `rubin-evidence-lab` | 用 `JimLiu/baoyu-skills` 完成一次 GitHub 仓库评估回测 |
| 2026-05-25 | 新增阶段报告 | SkillHub | 输出初始化盘点与 MiniMax agent 可执行任务分流 |
| 2026-05-25 | 新增流程 | 新仓库接收评估 | 后续 Robin 丢新仓库时，按固定流程分析、分类、评价、推荐 |
| 2026-05-25 | 新增批量管线 | SkillHub | 新增 inventory/classify 脚本，生成外部候选批量盘点和自动分类报告 |
| 2026-05-25 | 新增 Agent 配置 | MiniMax Coder | 定义 Coder 可使用的 SkillHub 能力、禁止项和默认输出格式 |

## 更新规则

每次发生以下动作，都必须更新本文件：

1. 新增、删除、晋升、降级 skill。
2. 风险等级、适配 Agent、依赖、登录态、发布能力变化。
3. `SKILL.md`、workflow、template、example 任一文件变化。
4. 外部来源重新核查、license 变化、维护状态变化。
5. 测试结果变化。

同步更新：

- `registry/skills_index.json`
- `CHANGELOG.md`
- 对应 skill 的 `skill.meta.json`
- 对应评分卡
