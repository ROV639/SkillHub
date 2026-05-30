# Rubin SkillHub 总索引

更新时间：2026-05-25  
维护人：Robin / Codex  
仓库：ROV639/SkillHub  
用途：所有 Agent 共用的 Skill 总目录

## 当前状态

- ready skills：0
- local curated skills：26
- lab skills：21
- external_unverified：0
- blocked_prod：0
- 最近一次扫描：2026-05-31
- 最近一次晋升：2026-05-31（local curated）

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

## Local Curated / OpenClaw First

| Name | Platform | Directory | Status | Language treatment | Source |
|---|---|---|---|---|---|
| `humanizer` | OpenClaw | `skills/openclaw/humanizer` | READY | English, metadata normalized | `~/.openclaw/skills/humanizer` |
| `openclaw-gateway-foreground-fix` | OpenClaw | `skills/openclaw/openclaw-gateway-foreground-fix` | READY | Mixed CN/EN -> English | `~/.hermes/skills/devops/openclaw-gateway-foreground-fix` |
| `rov639-hermes-vs-openclaw` | OpenClaw | `skills/openclaw/rov639-hermes-vs-openclaw` | READY | Mixed CN/EN -> English | `~/.hermes/skills/productivity/rov639-hermes-vs-openclaw` |
| `openclaw-health-check` | OpenClaw | `skills/openclaw/openclaw-health-check` | READY | English, newly authored | SkillHub |
| `openclaw-agent-routing` | OpenClaw | `skills/openclaw/openclaw-agent-routing` | READY | English, newly authored | SkillHub |
| `openclaw-channel-manager` | OpenClaw | `skills/openclaw/openclaw-channel-manager` | READY | English, newly authored | SkillHub |

## Local Curated / Hermes

| Name | Directory | Status | Language treatment | Source |
|---|---|---|---|---|
| `kanban-codex-lane` | `skills/hermes/kanban-codex-lane` | READY | English, metadata normalized | `~/.hermes/skills/autonomous-ai-agents/kanban-codex-lane` |
| `hermes-upgrade-workflow` | `skills/hermes/hermes-upgrade-workflow` | READY | English, metadata normalized | `~/.hermes/skills/productivity/hermes-upgrade-workflow` |
| `hermes-compression-debug` | `skills/hermes/hermes-compression-debug` | READY | Mixed CN/EN -> English | `~/.hermes/skills/productivity/hermes-compression-debug` |
| `hermes-telegram-buttons` | `skills/hermes/hermes-telegram-buttons` | READY | Mixed CN/EN -> English | `~/.hermes/skills/productivity/hermes-telegram-buttons` |
| `hermes-telegram-inline-keyboard` | `skills/hermes/hermes-telegram-inline-keyboard` | READY | Mixed CN/EN -> English | `~/.hermes/skills/hermes-extension/hermes-telegram-inline-keyboard` |
| `nomos-ops` | `skills/hermes/nomos-ops` | READY | Mixed CN/EN -> English | `~/.hermes/skills/nomos-ops` |
| `nomos-deep-reasoning` | `skills/hermes/nomos-deep-reasoning` | READY | Pure Chinese -> bilingual | `~/.hermes/skills/nomos/nomos-deep-reasoning` |
| `nomos-skill-review` | `skills/hermes/nomos-skill-review` | READY | Mixed CN/EN -> English | `~/.hermes/skills/nomos/nomos-skill-review` |
| `minimax-img-bot` | `skills/hermes/minimax-img-bot` | READY | Mixed CN/EN -> English, token redacted | `~/.hermes/skills/productivity/minimax-img-bot` |
| `minimax-bot-ecosystem` | `skills/hermes/minimax-bot-ecosystem` | READY | Mixed CN/EN -> English | `~/.hermes/skills/bot-development/minimax-bot-ecosystem` |
| `minimax-api-retry-pattern` | `skills/hermes/minimax-api-retry-pattern` | READY | Mixed CN/EN -> English | `~/.hermes/skills/bot-development/minimax-api-retry-pattern` |

## Local Curated / General

| Name | Directory | Status | Language treatment | Source |
|---|---|---|---|---|
| `content-creation-platform-playbook` | `skills/general/content-creation-platform-playbook` | READY | Pure Chinese -> bilingual | `~/.hermes/skills/content-creation-platform-playbook` |
| `social-card-design` | `skills/general/social-card-design` | READY | Mixed CN/EN -> English | `~/.hermes/skills/content-creation/social-card-design` |
| `hyperframes-html-to-video` | `skills/general/hyperframes-html-to-video` | READY | Mixed CN/EN -> English | `~/.hermes/skills/media/hyperframes-html-to-video` |
| `notebooklm` | `skills/general/notebooklm` | READY | Mixed CN/EN -> English | `~/.hermes/skills/research/notebooklm` |
| `qwen-research-2026` | `skills/general/qwen-research-2026` | READY | Mixed CN/EN -> English | `~/.hermes/skills/research/qwen-research-2026` |
| `youtube-clipper` | `skills/general/youtube-clipper` | READY | Mixed CN/EN -> English | `~/.hermes/skills/youtube-clipper` |
| `youtube-playlist-extractor` | `skills/general/youtube-playlist-extractor` | READY | Mixed CN/EN -> English | `~/.hermes/skills/youtube-playlist-extractor` |
| `redbook-creator-publish` | `skills/general/redbook-creator-publish` | READY | Mixed CN/EN -> English | `~/.claude/skills/redbook-creator-publish` |
| `film-creator` | `skills/general/film-creator` | READY | Mixed CN/EN -> English | `~/.claude/skills/film-creator` |

## 候选测试区

| 中文名 | 原型来源 | 目录名 | 当前动作 | 加入日期 | 更新日期 | 测试重点 | 负责人 | 下一步 |
|---|---|---|---|---|---|---|---|---|
| 证据研究所 | Rubin 原创 | `rubin-evidence-lab` | LAB 回测中 | 2026-05-25 | 2026-05-25 | 仓库评估、工具调研、内容事实核查 | Codex | 继续做工具/API 和内容事实核查回测 |
| Rubin 图解工坊 | baoyu-diagram | `rubin-diagram-workshop` | LAB 测试 | 2026-05-25 | 2026-05-25 | SVG 准确性、中文显示、流程/架构表达 | Codex | 已完成测试 01，待浏览器渲染复核 |
| Rubin 小红书图卡工坊 | baoyu-xhs-images | `rubin-xhs-card-workshop` | LAB 测试 | 2026-05-25 | 2026-05-25 | 中文排版、卡片密度、发布包完整度 | Codex/MiniMax | 批量测试完成，待项目实测 |
| Rubin 信息图工坊 | baoyu-infographic | `rubin-infographic-workshop` | LAB 测试 | 2026-05-25 | 2026-05-25 | 信息结构、图面密度、可读性 | Codex/MiniMax | 批量测试完成，待项目实测 |
| Rubin 发布格式工坊 | baoyu-markdown-to-html / format-markdown | `rubin-publish-format-workshop` | LAB 测试 | 2026-05-25 | 2026-05-25 | Markdown/HTML 清理、发布前 QC | Codex/MiniMax | 已完成测试 01，待 HTML 转换复测 |
| Rubin 网页资料入口 | baoyu-url-to-markdown | `rubin-url-markdown-intake` | LAB 测试 | 2026-05-25 | 2026-05-25 | 公开网页提取、来源卡、登录门禁 | Codex/MiniMax | 批量测试完成，待 live fetch 复测 |
| Rubin 办公资产工作台 | anthropics document skills | `rubin-office-asset-workbench` | LAB 测试 | 2026-05-25 | 2026-05-25 | docx/pdf/pptx/xlsx 资产验收 | Codex/MiniMax | 批量测试完成，待 docx/pptx 复测 |
| Rubin 封面图工坊 | baoyu-cover-image | `rubin-cover-image-workshop` | ADAPTING | 2026-05-25 | 2026-05-25 | 封面方向、构图、提示词 | Codex/MiniMax | 批量测试完成，待项目实测 |
| Rubin 文章配图规划器 | baoyu-article-illustrator | `rubin-article-illustration-planner` | ADAPTING | 2026-05-25 | 2026-05-25 | 长文配图点识别、成本控制 | Codex/MiniMax | 批量测试完成，待项目实测 |
| Rubin 内容复用器 | OneWave content-repurposer | `rubin-content-repurposer` | ADAPTING | 2026-05-25 | 2026-05-25 | 多平台改写、事实边界 | MiniMax/Codex | 批量测试完成，待项目实测 |
| Rubin 品牌语气门禁 | OneWave brand-voice-analyzer | `rubin-brand-voice-gate` | ADAPTING | 2026-05-25 | 2026-05-25 | AI 味、语气一致、事实跳跃 | MiniMax/Codex | 批量测试完成，待项目实测 |
| Rubin 社媒草稿改写器 | OneWave social-repurposer | `rubin-social-draft-repurposer` | ADAPTING | 2026-05-25 | 2026-05-25 | 平台草稿、发布包 schema、门禁 | MiniMax/Codex | 批量测试完成，待 ONE_SPARK 实测 |
| Rubin MiniMax 办公适配器 | VoltAgent MiniMax radar | `rubin-minimax-office-adapter` | ADAPTING | 2026-05-25 | 2026-05-25 | MiniMax 任务拆分、输入包、验收 | Codex/MiniMax | 批量测试完成，待 MiniMax 实测 |

| Rubin Google 工作区闸门 | VoltAgent/awesome-agent-skills | `rubin-google-workspace-gate` | LAB-TEST | 2026-05-25 | 2026-05-25 | 项目适配、权限边界、真实任务测试 | Codex/MiniMax | 批量测试完成，待项目实测 |
| Rubin MiniMax 语音工坊 | VoltAgent/awesome-agent-skills | `rubin-minimax-tts-workshop` | LAB-TEST | 2026-05-25 | 2026-05-25 | 项目适配、权限边界、真实任务测试 | Codex/MiniMax | 批量测试完成，待项目实测 |
| Rubin Skill 建造器 | anthropics/skills | `rubin-skill-builder` | LAB-TEST | 2026-05-25 | 2026-05-26 | 项目适配、权限边界、真实任务测试 | Codex/MiniMax | 项目测试 02 PASS，适合新仓库入库默认工具 |
| Rubin 营销文案实验室 | VoltAgent/awesome-agent-skills | `rubin-marketing-copy-lab` | ADAPTING | 2026-05-25 | 2026-05-25 | 项目适配、权限边界、真实任务测试 | Codex/MiniMax | 批量测试完成，待项目实测 |
| Rubin 知识漫画工坊 | JimLiu/baoyu-skills | `rubin-comic-card-workshop` | ADAPTING | 2026-05-25 | 2026-05-25 | 项目适配、权限边界、真实任务测试 | Codex/MiniMax | 批量测试完成，待项目实测 |
| Rubin 漫画视频规划器 | freestylefly/canghe-skills | `rubin-manga-video-planner` | ADAPTING | 2026-05-25 | 2026-05-25 | 项目适配、权限边界、真实任务测试 | Codex/MiniMax | 批量测试完成，待项目实测 |
| Rubin 知识库建造器 | OneWave-AI/claude-skills | `rubin-knowledge-base-builder` | ADAPTING | 2026-05-25 | 2026-05-26 | 项目适配、权限边界、真实任务测试 | Codex/MiniMax | 项目测试 02 PASS，适合 SkillHub 知识地图 |
| Rubin 多 Agent 编排参考 | OneWave-AI/claude-skills | `rubin-agent-orchestration-reference` | REFERENCE | 2026-05-25 | 2026-05-25 | 项目适配、权限边界、真实任务测试 | Codex/MiniMax | 批量测试完成，待项目实测 |

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

| 2026-05-25 | 新增候选 | P0/P1 Rubin 改写版 | 新增 12 个 `rubin-adapted` 候选 Skill，并加入逐个测试计划 |

| 2026-05-25 | 完成测试 | `rubin-diagram-workshop` | 生成 SkillHub 入库流程 SVG，结构测试通过，待浏览器渲染复核 |

| 2026-05-25 | 新增候选 | 第二批 Rubin 改写版 | 新增 8 个 LAB 候选 Skill，并补充 AltmanCodex 项目适配图谱 |

| 2026-05-25 | 完成测试 | `rubin-publish-format-workshop` | 生成 SkillHub 第二批候选发布前 Markdown 包，QC 通过，待 HTML 转换复测 |

| 2026-05-25 | 完成批量测试 | 21 个 LAB Skill | 生成批量测试总报告和每个 Skill 的测试样例；全部保持 LAB，待项目实测后再晋升 |

| 2026-05-26 | 完成项目测试 | `rubin-skill-builder` / `rubin-knowledge-base-builder` | 生成候选 Skill 包样例和 SkillHub 知识地图，两个测试均 PASS |
| 2026-05-31 | 新增本地策展 | `skills/openclaw` / `skills/hermes` / `skills/general` | 收录 23 个本地自建/深度定制 skill，并新增 3 个 OpenClaw 深度集成 skill |
| 2026-05-31 | 新增文档 | OpenClaw integration | README 增加 OpenClaw 背景，新增中英文 README 与 OpenClaw 集成指南 |

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
