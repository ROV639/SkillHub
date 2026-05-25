# SkillHub 双机同步流程

## 目标

把两台电脑里的 Agent Skill 统一整理到 GitHub 仓库 `ROV639/SkillHub`。

GitHub 仓库只收整理后的结果，不直接覆盖任何电脑上的正式 Skill 目录。

## 目录角色

- `manifests/`：每台电脑的扫描清单。
- `reports/`：扫描报告、重复项、风险项。
- `skills/lab/`：自写但还未确认的 Skill。
- `skills/external_unverified/`：外部来源或不确定来源的 Skill。
- `skills/ready/`：确认可复用、可安装的正式 Skill。

## 双机流程

1. 每台电脑只读扫描本机 Skill。
2. 扫描结果写入各自的 manifest 和 report。
3. 在主电脑合并两份 manifest。
4. 先处理重复项、敏感风险、外部来源。
5. 确认后再把 Skill 复制到 `skills/ready/` 或 `skills/lab/`。
6. 最后由主电脑提交并推送 GitHub。

## 禁止事项

- 不要让两个 Agent 同时写 `SkillHub` 仓库。
- 不要直接把所有扫描到的 Skill 复制进 `skills/ready/`。
- 不要把完整 API Key、Token、Cookie 写进报告。
- 不要在副电脑上执行 `git push`。
- 不要覆盖正式 Skill 目录。

