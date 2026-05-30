# OpenClaw 集成说明

SkillHub 将 OpenClaw 作为 first-class integration。这个仓库来自真实 OpenClaw 使用经验：多专业 Agent、cron 报告、gateway 修复记录、渠道分发流程，以及散落在本机各处但值得复用的本地 skills。

## 集成模型

SkillHub 不替代 OpenClaw，而是给 OpenClaw 增加一层清晰的 skill 注册中心：

- `skills/openclaw/` 保存 OpenClaw-first skills 和运维手册。
- `skills/hermes/` 保存 Hermes 专用 skills，其中很多会辅助 OpenClaw 邻近流程。
- `skills/general/` 保存可在 OpenClaw、Codex、Claude Code、OpenCode 中复用的通用 skills。
- `registry/` 和 `SKILL_INDEX.md` 用于安装前发现、比较和审查。

## 推荐安装路径

OpenClaw 专用 skill：

```bash
mkdir -p ~/.openclaw/skills
cp -R skills/openclaw/<skill-name> ~/.openclaw/skills/
```

如果某些 skill 只需要被 OpenClaw agent 引用，可以让 SkillHub 保持 source of truth，在 agent prompt 或本地流程里引用 SkillHub 路径，而不是复制。

## 建议本地结构

```text
~/.openclaw/
  skills/
    openclaw-health-check/
    openclaw-agent-routing/
    openclaw-channel-manager/
  agents/
    <agent>/
      agent/
      sessions/
  cron/
    jobs.json
```

不要把 auth 文件、sessions、cookies、tokens 或私人报告输出复制进 SkillHub。

## 更新 Skills

在 SkillHub 仓库中：

```bash
git pull
rsync -av --delete skills/openclaw/ ~/.openclaw/skills/
```

如果 `~/.openclaw/skills` 里有本地改动，先不要用 `--delete`。优先使用：

```bash
rsync -av skills/openclaw/ ~/.openclaw/skills/
```

然后检查：

```bash
find ~/.openclaw/skills -maxdepth 2 -name SKILL.md -print
```

## 在 OpenClaw 中使用 Skill

1. 从 `skills/openclaw/` 选择一个 skill。
2. 阅读 metadata 和 guardrails。
3. 将 skill 路径或摘要指令加入对应 OpenClaw agent prompt。
4. 在启用定时任务或外部渠道写入前，先跑无害检查。

示例：

```bash
sed -n '1,160p' skills/openclaw/openclaw-health-check/SKILL.md
openclaw cron list
```

## 当前 OpenClaw Skills

- `openclaw-health-check`：检查 gateway、cron、模型、进程和输出产物。
- `openclaw-agent-routing`：把任务路由给正确的专业 agent 或 ACP lane。
- `openclaw-channel-manager`：准备并管控 Feishu、Telegram、本地文件夹和公开渠道的交付。
- `openclaw-gateway-foreground-fix`：当 launchd 不可靠时恢复卡死 gateway。
- `rov639-hermes-vs-openclaw`：厘清 Hermes 与 OpenClaw 的职责边界。
- `humanizer`：清理 OpenClaw 生成草稿中的 AI 写作痕迹。

## 常见问题

### Gateway 显示运行，但 cron 失败

先查端口：

```bash
lsof -i :18789
```

如果没有监听，使用 `openclaw-gateway-foreground-fix`。

### 任务被错误 agent 接走

使用 `openclaw-agent-routing`，明确写下：

- 期望产物；
- 所属 agent；
- model/provider；
- 禁止动作；
- 验证命令。

### 渠道发送风险高

使用 `openclaw-channel-manager`。先在本地准备 channel package，再请求人工确认，最后才允许外部发送。

### 本地能用，升级后失效

比较 SkillHub 和本地副本：

```bash
diff -ru skills/openclaw ~/.openclaw/skills | sed -n '1,160p'
```

如果本地副本做过改动，把改进沉淀回 SkillHub，不要让它变成只存在于单台机器上的隐藏 patch。

## 安全规则

- 永远不要提交 `auth-state.json`、`auth-profiles.json`、session dump、cookies、tokens 或 API keys。
- 不要用发布任务作为健康检查。
- 不要让 delegated coding agent 直接修改 OpenClaw cron 或 auth config。
- 全局配置变更前，先做单 agent、单变更测试。
