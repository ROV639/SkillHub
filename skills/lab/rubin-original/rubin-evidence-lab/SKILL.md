---
name: rubin-evidence-lab
description: Use this skill for Rubin evidence research: evaluating external GitHub repositories, researching AI tools or APIs, checking facts for content, producing claim tables, source notes, and short decision cards. Trigger when the user asks whether a tool, repository, claim, workflow, or content idea is worth using, migrating, writing about, or investing in.
---

# 证据研究所

用于把“这个东西值不值得用/写/迁移/投入”变成可复查的证据和决策卡。

## 触发场景

- 外部仓库是否值得学习或迁移。
- AI 工具、API、平台能力是否真实可用。
- 公众号、视频、图文内容需要事实依据。
- 需要判断某个 workflow 是否能进入 Rubin / Codex / MiniMax 体系。

## 默认输出

优先输出短决策卡，不默认写长报告。

```text
结论：
证据等级：强 / 中 / 弱 / 不足
可用价值：
商业价值：
内容转化：
系统迁移：
风险：
建议动作：SHIP / FIX-FIRST / HOLD / BLOCK
下一步：
```

## 任务分级

| 等级 | 用途 | 输出 |
|---|---|---|
| L1 快速判断 | 仓库、工具、想法是否值得继续看 | 决策卡 |
| L2 标准调研 | 工具选型、仓库评估、选题依据 | 决策卡 + 证据表 |
| L3 深度证据 | 公众号、项目部署、高风险判断 | 证据表 + 完整报告 |

## Workflow 选择

- GitHub 仓库评估：读 `workflows/github_repo_review.md`
- AI 工具/API 调研：读 `workflows/tool_research.md`
- 内容事实核查：读 `workflows/content_fact_check.md`

## 证据规则

- 区分事实、判断、推测、证据不足。
- 关键事实必须有来源 URL。
- 重要 claim 尽量绑定原文 quote。
- quote 必须二次确认上下文是否支持。
- 没有证据的内容不能进入正式结论。

## 安全边界

允许：

- 搜索公开资料。
- 读取公开 GitHub、README、源码、issues、release。
- 生成决策卡、证据表、迁移建议。

禁止：

- 安装外部依赖。
- 运行不明脚本。
- 接入账号、cookie、session、API key。
- 直接发布内容或自动互动。
- 把外部 skill 直接写入正式 ready。

## Rubin 真实目标

每次研究最后要回答：

1. 能不能做内容？
2. 能不能做教程？
3. 能不能做工具流？
4. 能不能变成产品或服务？
5. 能不能提升现有生产效率？
6. 能不能降低试错成本？
7. 值不值得继续投入？
8. 下一步由谁执行：ChatGPT、Codex、MiniMax、人工，还是暂缓？

