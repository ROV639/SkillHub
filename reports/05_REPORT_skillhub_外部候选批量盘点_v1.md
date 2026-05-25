# SkillHub 外部候选批量盘点 v1

生成时间：2026-05-25 22:01:11

## 结论

- 当前 SkillHub 已有本地候选 skill，可继续扩展批量盘点。
- 外部来源先进入 source radar，不直接复制到 `skills/ready/`。
- 下一步由 `classify_skills.py` 自动打风险等级和推荐动作。

## 总览

| 类型 | 数量 |
| --- | --- |
| 本地 Skill | 1 |
| manifest 发现记录 | 523 |
| 外部来源 | 8 |

## 本地 Skill

| Skill | 中文名 | 状态 | 风险 | 路径 |
| --- | --- | --- | --- | --- |
| rubin-evidence-lab | 证据研究所 | LAB | R1 | skills/lab/rubin-original/rubin-evidence-lab |

## 外部来源

| 来源 | 类型 | 优先级 | 建议动作 | 风险提示 |
| --- | --- | --- | --- | --- |
| JimLiu/baoyu-skills | external-skill-pool | P0 | SANDBOX | mixed |
| freestylefly/canghe-skills | external-skill-pool | P1 | REFERENCE | mixed |
| laolaoshiren/claude-code-skills-zh | external-skill-pool | P1 | SANDBOX | low |
| Jst-Well-Dan/Skill-Box | external-index | P1 | REFERENCE | low |
| yzfly/awesome-claude-skills-zh | external-index | P2 | REFERENCE | low |
| yzfly/awesome-mcp-zh | external-index | P2 | REFERENCE | mixed |
| NanmiCoder/MediaCrawler | external-tool | P2 | RESEARCH-SANDBOX | R3 |
| dreammis/social-auto-upload | external-tool | P2 | SCHEMA-ONLY | R4 |

## 下一步

1. 运行 `scripts/classify_skills.py` 自动分类。
2. 让 MiniMax agent 生成外部来源卡和使用卡初稿。
3. Codex 抽样复核 Top 7。
