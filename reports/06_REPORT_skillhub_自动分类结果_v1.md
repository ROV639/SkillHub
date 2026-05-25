# SkillHub 自动分类结果 v1

生成时间：2026-05-25 22:02:24

## 总览

| 风险 | 数量 |
| --- | --- |
| R0 | 3 |
| R1 | 1 |
| R2 | 3 |
| R3 | 1 |
| R4 | 1 |

| 建议动作 | 数量 |
| --- | --- |
| LAB-TEST | 1 |
| REFERENCE | 4 |
| RESEARCH-SANDBOX | 1 |
| SANDBOX | 2 |
| SCHEMA-ONLY | 1 |

## 分类结果

| 名称 | 类型 | 风险 | 建议动作 | 备注 |
| --- | --- | --- | --- | --- |
| 证据研究所 | local-skill | R1 | LAB-TEST | 用于外部仓库评估、AI 工具调研、内容事实核查和决策卡输出。 |
| JimLiu/baoyu-skills | external-source | R2 | SANDBOX | 内容生产第一外部样本池，优先测试 diagram、infographic、xhs-images、url-to-markdown、markdown-to-html、youtube-transcript。 |
| freestylefly/canghe-skills | external-source | R2 | REFERENCE | 个人 skills repo 对照，主要学习本地化改写方式。 |
| laolaoshiren/claude-code-skills-zh | external-source | R0 | SANDBOX | 中文代码类对照组，优先测试 zh-readme。 |
| Jst-Well-Dan/Skill-Box | external-source | R0 | REFERENCE | 学习分类体系和 Curated / Community 标签，不直接安装。 |
| yzfly/awesome-claude-skills-zh | external-source | R0 | REFERENCE | 中文 Claude Skills 资料雷达。 |
| yzfly/awesome-mcp-zh | external-source | R2 | REFERENCE | MCP 中文资料雷达，涉及账号/平台的 MCP 需独立评估。 |
| NanmiCoder/MediaCrawler | external-source | R3 | RESEARCH-SANDBOX | 内容样本研究工具，不进入 skills/ready，不碰主账号，不做批量抓取。 |
| dreammis/social-auto-upload | external-source | R4 | SCHEMA-ONLY | 社媒自动上传技术储备，只提取发布包 schema，不做无人值守实发。 |

## MiniMax agent 可接任务

- 为 `SANDBOX` 和 `REFERENCE` 项生成使用卡初稿。
- 为 `BLOCK-PROD` 项整理字段和限制，不做运行。
- 为 R0-R2 项提取依赖、输入、输出、失败点。

## Codex / Robin 保留判断

- 是否晋升 READY。
- 是否接账号、API key、cookie、登录态。
- 是否执行外部脚本或真实发布。
