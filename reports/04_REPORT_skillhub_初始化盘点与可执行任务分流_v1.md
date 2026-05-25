# SkillHub 初始化盘点与可执行任务分流 v1

日期：2026-05-25  
阶段：SkillHub 初始化后第一次盘点  
目标：说明当前 SkillHub 已经能做什么、哪些可以马上使用、哪些适合交给 MiniMax agent 执行、下一步如何批量盘点外部 Skill / 工作流。

## 0. 结论

SkillHub 已从“空仓库/扫描仓库”进入“可维护的技能系统”阶段。

当前已经具备：

1. 人类与 Agent 共读索引：`SKILL_INDEX.md`
2. 结构化索引：`registry/skills_index.json`
3. 更新记录：`CHANGELOG.md`
4. 评分卡模板：`scorecards/_template_skill_scorecard.md`
5. 第一个原创候选 Skill：`rubin-evidence-lab`
6. 第一次真实回测报告：`baoyu-skills` 仓库评估

现在还不是“很多 Skill 可以直接自动调用”的阶段，而是“规则、索引、评分、回测流程已经打通”的阶段。

## 1. 现在可以马上使用什么

### 1.1 可以马上使用的流程

| 名称 | 状态 | 用途 | 谁来用 |
|---|---|---|---|
| SkillHub 总索引 | 可用 | 人和 Agent 快速判断 Skill 状态、风险、分类 | 所有 Agent |
| 评分卡模板 | 可用 | 每个 Skill 入库前评分 | Codex / Claude |
| 证据研究所流程 | LAB 可用 | 仓库评估、工具调研、事实核查 | Codex 优先 |
| 决策卡格式 | 可用 | 小调研快速结论 | 所有 Agent |
| R0-R4 风险等级 | 可用 | 判断是否能自动执行 | 所有 Agent |

### 1.2 可以马上拿来做的任务

| 任务 | 推荐执行者 | 原因 |
|---|---|---|
| 外部仓库初筛 | Codex | 需要判断、分级、风险识别 |
| README/Skill 文档摘要 | MiniMax agent | 流程固定，只需提取结构 |
| Skill 元数据补全 | MiniMax agent | 字段固定，可批量执行 |
| 评分卡初稿 | MiniMax agent | 可按模板填写，Codex 最后复核 |
| 风险关键词初筛 | MiniMax agent | 机械判断：cookie/key/login/post/delete/publish |
| 最终入库判断 | Codex / Robin | 需要综合判断 |

## 2. MiniMax agent 可以承担的任务

MiniMax agent 适合做“低判断、强流程、可模板化”的任务。建议先让它们做批量准备，不让它们做最终晋升。

### 2.1 适合交给 MiniMax 的任务

| 任务 | 输入 | 输出 |
|---|---|---|
| README 摘要 | 仓库 README / SKILL.md | 200-500 字摘要 |
| Skill 字段提取 | skill 目录 | 名称、用途、依赖、风险词 |
| 风险关键词扫描 | 文档和源码 | R0-R4 初判 |
| 使用卡初稿 | Skill 文档 | 适合做什么、不适合做什么 |
| 评分卡初稿 | 使用卡 + 简单测试结果 | 分项评分草稿 |
| 外部来源卡 | GitHub URL | stars、license、活跃度、风险点 |
| 发布包 schema 整理 | 社媒工具 README | 平台、标题、正文、标签、素材、发布时间字段 |

### 2.2 不适合交给 MiniMax 自动决定的任务

| 任务 | 原因 |
|---|---|
| 是否晋升 READY | 需要最终责任判断 |
| 是否允许账号/登录态/发布 | 高风险 |
| 是否写入正式 Skill 路径 | 需要人工确认 |
| 是否推送 GitHub | 需要主控确认 |
| 是否调用真实 API key | 成本和安全风险 |
| 是否执行外部脚本 | 供应链风险 |

### 2.3 MiniMax agent 批量任务模板

```text
任务：为候选 Skill 生成初筛卡

输入：
- 仓库 URL：
- Skill 路径：
- README / SKILL.md 内容：

只做：
1. 摘要用途。
2. 提取依赖。
3. 扫描风险词。
4. 初判 R0-R4。
5. 标记是否可能适合 Rubin。
6. 输出使用卡草稿。

禁止：
- 不安装。
- 不运行。
- 不登录。
- 不调用 API key。
- 不发布。
- 不写入 ready。

输出：
- 使用卡草稿
- 风险标签
- 建议动作：REFERENCE / SANDBOX / ADAPT-CANDIDATE / BLOCK-PROD
```

## 3. 下一次批量盘点应该怎么做

下一次不要一个个手工回测。建议做批量管线：

```text
搜索候选仓库
→ 批量抓取 README / SKILL.md / manifest
→ 自动生成 inventory
→ 自动初筛分类和风险
→ MiniMax agent 生成使用卡初稿
→ Codex 抽样复核
→ 只挑 Top 7 做真实回测
→ 产出推荐清单
```

## 4. 批量盘点输出物

每次临时盘点任务应该输出：

```text
registry/skills_inventory.json
registry/sources_index.json
reports/NN_REPORT_skillhub_候选盘点_vX.md
scorecards/<skill>.md
test_cases/<batch>/
```

报告必须回答：

1. 哪些可以马上使用？
2. 哪些适合沙盒测试？
3. 哪些值得改写成 Rubin 版本？
4. 哪些只能只读参考？
5. 哪些禁止进入生产？
6. 哪些任务可以交给 MiniMax agent？
7. 哪些必须由 Codex / Robin 判断？

## 5. 当前推荐优先级

### P0：继续完善原创核心 Skill

| Skill | 动作 |
|---|---|
| `rubin-evidence-lab` | 再做工具/API 调研回测、内容事实核查回测 |
| `rubin-skill-vetter` | 新建，用于批量入库评分和风险识别 |
| `rubin-decision-card` | 新建，用于所有小调研统一输出 |

### P1：批量盘点外部内容生产 Skill

优先仓库：

1. `JimLiu/baoyu-skills`
2. `freestylefly/canghe-skills`
3. `laolaoshiren/claude-code-skills-zh`
4. `Jst-Well-Dan/Skill-Box`

优先 skill 类型：

1. diagram / SVG 图解
2. infographic / 信息图
3. xhs images / 小红书图卡
4. url to markdown / 网页取证
5. markdown to html / 微信 HTML
6. youtube transcript / 视频字幕
7. zh readme / 中文 README

### P2：社媒发布类只做 schema

| 类型 | 当前动作 |
|---|---|
| social-auto-upload | 提取本地发布包字段，不实发 |
| baoyu-post-to-wechat | 研究草稿/预览/API 字段，不实发 |
| xhs 自动发布 | 研究草稿和预览，不碰主账号 |
| danger / cookie 类 | 只读结构，不接真实 token |

## 6. 当前可用清单

| 项目 | 状态 | 是否即拿即用 | 备注 |
|---|---|---|---|
| `SKILL_INDEX.md` | 可用 | 是 | 人类和 Agent 共读入口 |
| `registry/skills_index.json` | 可用 | 是 | Agent / 脚本读取 |
| `scorecards/_template_skill_scorecard.md` | 可用 | 是 | 入库评分卡模板 |
| `rubin-evidence-lab` | LAB | 可用于回测，不自动调用 | 已完成一次仓库评估回测 |
| `baoyu-skills` 候选池 | REFERENCE | 否 | 需批量盘点和沙盒测试 |

## 7. 下一步建议

建议下一步不是继续手工测单个 Skill，而是创建批量盘点工具：

1. `scripts/inventory_skills.py`
2. `scripts/classify_skills.py`
3. `registry/skills_inventory.json`
4. `reports/05_REPORT_skillhub_外部候选批量盘点_v1.md`

同时新建第二个原创 Skill：

```text
skills/lab/rubin-original/rubin-skill-vetter/
```

它负责把“盘点、评分、风险识别、晋升建议”标准化。

