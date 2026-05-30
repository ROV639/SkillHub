# SkillHub

![GitHub Repo stars](https://img.shields.io/github/stars/ROV639/SkillHub?style=social)
![License](https://img.shields.io/badge/license-MIT-green)
![OpenClaw](https://img.shields.io/badge/platform-OpenClaw-2563eb)
![Codex](https://img.shields.io/badge/platform-Codex-111827)
![Claude Code](https://img.shields.io/badge/platform-Claude%20Code-6b7280)

SkillHub 是一个面向 AI 编程 Agent 的策划型 skill 注册中心，适用于 OpenClaw、Codex、Claude Code 和 OpenCode 等运行环境。

这个项目会收集、规范化、测试和索引可复用的 agent skills，让独立开发者能够发现高信号工作流，而不是把未经审查的 prompt 直接复制进生产环境。

SkillHub 收录来自社区和本地实践的优质 agent skills，并由维护者进行筛选、测试和格式统一。所有收录内容保留原始来源和 license 信息。

## 背景

SkillHub 来自长期真实使用 OpenClaw 的维护经验。从 OpenClaw 早期发布开始，我就在多 Agent、cron 定时任务、本地报告和渠道分发工作流中持续使用它。使用时间越长，一个问题越明显：有价值的 skills 分散在本地目录、agent prompt、Hermes 笔记、Claude skills 和临时修复文档里，难以发现、难以版本管理，也容易在升级或换机器时丢失。

SkillHub 把这些维护痛点整理成一个注册中心：统一 skill 格式，按平台分类，记录来源 metadata，做安全审查，并让安装、比较和复用变得更简单。OpenClaw 在 SkillHub 中是 first-class integration, actively maintained；同时，SkillHub 也支持 Codex、Claude Code 和 OpenCode 工作流。

## 为什么需要 SkillHub

Agent skills 正在变成 AI 辅助软件工作的“小型操作单元”：仓库审查、文档整理、内容生产、办公资产、发布准备、证据研究和平台工作流都可以沉淀为 skill。

多数 skill 集合难以比较，因为每个仓库的 metadata、风险标签和兼容性假设都不一样。SkillHub 解决这些问题：

- 统一 `SKILL.md` metadata 格式。
- 提供可检索的 registry index。
- 使用 lab-to-ready 流程，在晋升前测试 skill。
- 为社区改编 skill 保留清晰来源。
- 对 key、账号、发布、外部服务等风险提供 guardrails。

## 核心功能

- Skill 发布：每个 skill 都有可预测目录、frontmatter、状态、风险级别和测试引用。
- 搜索发现：通过 `SKILL_INDEX.md`、`registry/skills_index.json` 和来源雷达文件浏览。
- 跨平台兼容：标注 OpenClaw、Codex、Claude Code、OpenCode 的适用方式。
- 版本管理：追踪 skill version、updated date、review date 和 test report。
- 策展记录：保留社区来源、license 和改编说明。

## 支持平台

- OpenClaw：first-class integration, actively maintained
- Codex
- Claude Code
- OpenCode

## 快速开始

浏览人工可读目录：

```bash
open SKILL_INDEX.md
```

查看机器可读 registry：

```bash
jq '.skills[] | {id, status, risk_level, path}' registry/skills_index.json
```

查看某个 skill：

```bash
sed -n '1,120p' skills/openclaw/openclaw-health-check/SKILL.md
```

使用时，将选中的 skill 目录复制到你的 agent 环境支持的 skill 路径，然后先阅读 metadata 和 guardrails，再调用。

## 目录结构

```text
skills/
  openclaw/              # OpenClaw-first 本地和集成 skills
  hermes/                # Hermes 专用运维 skills
  general/               # 跨 agent runtime 的通用 skills
  ready/                 # 已审查、可安装或同步的 skills
  lab/                   # 正在适配、测试或本地审查的 skills
  external_unverified/   # 未验证第三方来源隔离区
registry/
  skills_index.json      # 机器可读 skill 注册表
  sources_index.json     # 外部来源雷达和审查状态
manifests/               # 不同机器扫描输出
reports/                 # 审查、测试和策展报告
scorecards/              # skill 评估记录
scripts/                 # registry 和 inventory 工具
docs/                    # 操作指南和审查流程文档
test_cases/              # skill 验证 prompts 和产物
```

## Metadata 标准

每个 `SKILL.md` 以 frontmatter 开头：

```yaml
---
name: rubin-example-skill
version: 1.0.0
author: Community source, curated by Roven
maintainer: Roven <https://github.com/ROV639>
description: One sentence describing what the skill does.
tags: [agent-ops, content-pipeline]
platforms: [codex, claude-code, openclaw]
updated: 2026-05-25
curated-by: Roven <https://github.com/ROV639>
original-source: https://github.com/example/source
license: MIT
notes: Curated and adapted for SkillHub registry
---
```

原创 SkillHub skill 可以省略 `original-source`，并使用 `author: Roven`。

## 策展策略

SkillHub 不会把所有发现的 skill 直接放进 `skills/ready/`。

默认流程：

1. 在 `registry/sources_index.json` 记录外部来源。
2. 将未验证内容隔离保存。
3. 改写为 SkillHub metadata 和 guardrail 格式。
4. 用 `test_cases/` 中的真实 prompts 测试。
5. 从 `reports/` 或 `scorecards/` 链接测试结果。
6. 只把完成审查的 skill 晋升到 `skills/ready/`。

策展来源见 [CREDITS.md](CREDITS.md)。

## 贡献

欢迎改进发现质量、metadata 一致性、测试覆盖和平台兼容性。

提交新 skill：

1. 在 `skills/lab/<source-class>/<skill-name>/` 下创建目录。
2. 添加带标准 metadata 的 `SKILL.md`。
3. 如果需要机器可读状态、风险、来源或测试字段，添加 `skill.meta.json`。
4. 在 `test_cases/` 或 `reports/` 添加测试或审查记录。
5. 使用仓库 PR 模板提交。

命名规范：

- skill 目录使用 lowercase kebab-case。
- 优先使用动作导向命名，如 `repo-review-workflow` 或 `markdown-publish-cleaner`。
- 不提交 API keys、cookies、tokens 或私人账号数据。

## Roadmap

- 基于 `registry/skills_index.json` 生成可搜索静态目录。
- 将已测试 LAB skills 晋升到 `skills/ready/` 并附发布说明。
- 为每个 skill 增加 OpenClaw、Codex、Claude Code、OpenCode 兼容性 badge。
- 增加 `SKILL.md` metadata 自动校验。
- 发布 research、office docs、publishing、visual workflows 等策展合集。

## License

SkillHub 仓库代码、registry 文件和原创文档采用 MIT License。

第三方策展 skill 保留其原始来源和 license 信息。见 [CREDITS.md](CREDITS.md)。

作者与维护者：Roven，[https://github.com/ROV639](https://github.com/ROV639)
