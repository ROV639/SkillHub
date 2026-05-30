# SkillHub

![GitHub Repo stars](https://img.shields.io/github/stars/ROV639/SkillHub?style=social)
![License](https://img.shields.io/badge/license-MIT-green)
![OpenClaw](https://img.shields.io/badge/platform-OpenClaw-2563eb)
![Codex](https://img.shields.io/badge/platform-Codex-111827)
![Claude Code](https://img.shields.io/badge/platform-Claude%20Code-6b7280)

SkillHub is a curated registry for agent skills used by AI coding agents such as OpenClaw, Codex, Claude Code, and OpenCode.

The project collects, normalizes, tests, and indexes reusable skills so independent developers can discover high-signal workflows without copying unreviewed prompts directly into production environments.

SkillHub 是一个策划型 skill 注册中心，收录来自社区的优质 agent skills，并由维护者进行筛选、测试和格式统一。所有收录内容保留原始来源和 license 信息。

## Background

SkillHub grew out of long-term, day-to-day OpenClaw use. After running OpenClaw from its early release period across multiple specialist agents, cron jobs, local reports, and channel workflows, one recurring problem became obvious: useful skills were scattered across local folders, agent prompts, Hermes notes, Claude skills, and ad hoc repair documents. They were hard to discover, hard to version, and easy to lose after upgrades or machine changes.

SkillHub turns that lived maintenance pain into a registry: skills are normalized, grouped by platform, given source metadata, reviewed for safety, and made easier to install or compare. OpenClaw is treated as a first-class integration, actively maintained, while the same registry also supports Codex, Claude Code, and OpenCode workflows.

## Why SkillHub

Agent skills are becoming small operational units for AI-assisted software work: repository review, documentation, content production, office assets, publishing preparation, research evidence, and platform-specific workflows.

Most skill collections are hard to compare because each repository uses different metadata, risk labels, and compatibility assumptions. SkillHub solves that by providing:

- A consistent `SKILL.md` metadata format.
- A registry index for discovery and review.
- A lab-to-ready workflow for testing skills before promotion.
- Clear source attribution for adapted community skills.
- Practical guardrails around keys, accounts, publishing, and external services.

## Core Features

- Skill publishing: store each skill in a predictable directory with frontmatter, status, risk level, and test references.
- Search and discovery: browse `SKILL_INDEX.md`, `registry/skills_index.json`, and source radar files.
- Cross-platform compatibility: document expected use across Codex, Claude Code, OpenClaw, and OpenCode.
- Version management: track skill version, update date, review date, and test report links.
- Curation records: preserve original source, license, and adaptation notes for community-derived skills.

## Supported Platforms

- OpenClaw: first-class integration, actively maintained
- Codex
- Claude Code
- OpenCode

## Quick Start

Browse the human-readable catalog:

```bash
open SKILL_INDEX.md
```

Inspect machine-readable registry data:

```bash
jq '.skills[] | {id, status, risk_level, path}' registry/skills_index.json
```

Review a skill:

```bash
sed -n '1,120p' skills/lab/rubin-adapted/rubin-diagram-workshop/SKILL.md
```

Use a skill by copying the selected skill directory into the skill location supported by your agent environment, then read the metadata and guardrails before invoking it.

## Directory Structure

```text
skills/
  openclaw/              # OpenClaw-first local and integration skills
  hermes/                # Hermes-specific operational skills
  general/               # universal skills useful across agent runtimes
  ready/                 # reviewed skills ready for installation or sync
  lab/                   # skills under adaptation, testing, or local review
  external_unverified/   # third-party sources kept isolated before review
registry/
  skills_index.json      # machine-readable skill registry
  sources_index.json     # external source radar and review status
manifests/               # per-machine skill scan outputs
reports/                 # review, test, and curation reports
scorecards/              # skill evaluation notes
scripts/                 # registry and inventory tooling
docs/                    # operating guides and review process docs
test_cases/              # skill validation prompts and outputs
```

## Metadata Standard

Each `SKILL.md` begins with frontmatter:

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

Original SkillHub skills may omit `original-source` and use `author: Roven`.

## Curation Policy

SkillHub does not promote every discovered skill directly into `skills/ready/`.

The default workflow is:

1. Record the external source in `registry/sources_index.json`.
2. Keep unverified material isolated.
3. Adapt the skill into SkillHub metadata and guardrail format.
4. Test with realistic prompts in `test_cases/`.
5. Link the result from `reports/` or `scorecards/`.
6. Promote only reviewed skills to `skills/ready/`.

See [CREDITS.md](CREDITS.md) for curated community sources.

## Contributing

Contributions are welcome when they improve discovery quality, metadata consistency, test coverage, or platform compatibility.

To submit a new skill:

1. Create a folder under `skills/lab/<source-class>/<skill-name>/`.
2. Add a `SKILL.md` with the standard metadata block.
3. Include `skill.meta.json` when status, risk, source, or test fields need machine-readable tracking.
4. Add a test case or review note under `test_cases/` or `reports/`.
5. Open a pull request using the repository PR template.

Naming conventions:

- Use lowercase kebab-case for skill directories.
- Prefer action-oriented names such as `repo-review-workflow` or `markdown-publish-cleaner`.
- Do not include API keys, cookies, tokens, or private account data.

## Roadmap

- Add a searchable static catalog generated from `registry/skills_index.json`.
- Promote tested LAB skills into `skills/ready/` with clear release notes.
- Add compatibility badges for Codex, Claude Code, OpenClaw, and OpenCode per skill.
- Add automated metadata validation for every `SKILL.md`.
- Publish curated collections for research, office docs, publishing, and visual workflows.

## License

SkillHub repository code, registry files, and original SkillHub documentation are released under the MIT License.

Curated third-party skill content keeps its original source and license notes. See [CREDITS.md](CREDITS.md).

Author and maintainer: Roven, [https://github.com/ROV639](https://github.com/ROV639)
