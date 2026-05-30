# SkillHub 更新记录

## 2026-05-31

- 新增 `skills/openclaw/`、`skills/hermes/`、`skills/general/` 三个本地策展目录。
- 收录 23 个本地自建或深度定制 skill，统一 metadata 为 `source: locally-developed`。
- 新增 3 个 OpenClaw-first skill：`openclaw-health-check`、`openclaw-agent-routing`、`openclaw-channel-manager`。
- 将 OpenClaw 设为 first-class integration，更新 `README.md` 并新增 `README.zh.md`。
- 新增 `docs/openclaw-integration.md` 和 `docs/openclaw-integration.zh.md`。
- 敏感信息处理：未收录 auth/session/secret 文件，`minimax-img-bot` 中的真实 Telegram Bot Token 已改为占位符。

## 2026-05-25

- 新增 `SKILL_INDEX.md`，作为人类与 Agent 共读的 Skill 总索引。
- 新增 `registry/skills_index.json`，作为结构化 Skill 索引。
- 新增 `scorecards/_template_skill_scorecard.md`，作为入库评分卡模板。
- 新增原创候选 Skill：`skills/lab/rubin-original/rubin-evidence-lab/`。
- 使用 `rubin-evidence-lab` 回测 `JimLiu/baoyu-skills`，新增回测报告和评分卡。
- 新增 `reports/04_REPORT_skillhub_初始化盘点与可执行任务分流_v1.md`，明确当前可用资产、MiniMax agent 可执行任务、下一步批量盘点方向。
- 新增 `docs/03_GUIDE_skillhub_新仓库接收评估流程_v1.md`，作为后续新仓库/Skill/工作流的默认分析、分类、评价和推荐流程。
- 新增 `scripts/inventory_skills.py`、`scripts/classify_skills.py`、`registry/sources_index.json`，生成批量盘点和自动分类结果。
- 新增 `registry/skills_inventory.json`、`registry/skills_classification.json`、`reports/05_REPORT_skillhub_外部候选批量盘点_v1.md`、`reports/06_REPORT_skillhub_自动分类结果_v1.md`。
- 新增 `configs/minimax/coder.md`，定义 MiniMax Coder agent 可使用的 SkillHub 能力、禁止项和输出格式。
- 新增 12 个 P0/P1 `rubin-adapted` 候选 Skill，并新增逐个测试计划。
- 完成 `rubin-diagram-workshop` 测试 01，新增 SkillHub 入库流程 SVG 和测试报告。
- 新增第二批 8 个 LAB 候选 Skill，并新增 AltmanCodex 项目适配图谱。
- 完成 `rubin-publish-format-workshop` 测试 01，新增发布前 Markdown 包和测试报告。
- 完成 21 个 LAB Skill 批量测试，新增总报告、测试样例和结构化测试结果。
- 完成 `rubin-skill-builder` 和 `rubin-knowledge-base-builder` 项目测试 02，新增候选 Skill 包样例和 SkillHub 知识地图。
