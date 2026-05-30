# OpenClaw Integration

SkillHub treats OpenClaw as a first-class integration. The repository grew from real OpenClaw usage: multiple specialist agents, cron-driven reports, gateway recovery notes, channel workflows, and local skills that were too useful to leave scattered across machine-specific folders.

## Integration Model

SkillHub does not replace OpenClaw. It gives OpenClaw a clean registry layer:

- `skills/openclaw/` contains OpenClaw-first skills and operational playbooks.
- `skills/hermes/` contains Hermes skills that often support OpenClaw-adjacent operations.
- `skills/general/` contains reusable skills that can run in OpenClaw, Codex, Claude Code, or OpenCode contexts.
- `registry/` and `SKILL_INDEX.md` help discover and compare skills before installing them.

## Recommended Install Path

For OpenClaw-specific skills:

```bash
mkdir -p ~/.openclaw/skills
cp -R skills/openclaw/<skill-name> ~/.openclaw/skills/
```

For skills that OpenClaw agents should only reference, keep SkillHub as the source of truth and point the agent prompt or local workflow to the SkillHub path instead of copying.

## Suggested Local Layout

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

Do not copy auth files, sessions, cookies, tokens, or private report outputs into SkillHub.

## Updating Skills

From the SkillHub repository:

```bash
git pull
rsync -av --delete skills/openclaw/ ~/.openclaw/skills/
```

If you have local edits under `~/.openclaw/skills`, do not use `--delete` until those edits are reviewed. Prefer:

```bash
rsync -av skills/openclaw/ ~/.openclaw/skills/
```

Then inspect:

```bash
find ~/.openclaw/skills -maxdepth 2 -name SKILL.md -print
```

## Using a Skill in OpenClaw

1. Pick a skill from `skills/openclaw/`.
2. Read the metadata and guardrails.
3. Add the skill path or summarized instruction to the relevant OpenClaw agent prompt.
4. Run a harmless check before enabling scheduled or channel-writing jobs.

Example:

```bash
sed -n '1,160p' skills/openclaw/openclaw-health-check/SKILL.md
openclaw cron list
```

## Operational Skills

Current OpenClaw-first skills:

- `openclaw-health-check`: gateway, cron, model, process, and output checks.
- `openclaw-agent-routing`: route tasks to the right specialist agent or ACP lane.
- `openclaw-channel-manager`: prepare and gate delivery into Feishu, Telegram, local folders, and public channels.
- `openclaw-gateway-foreground-fix`: recover a wedged gateway when launchd is unreliable.
- `rov639-hermes-vs-openclaw`: clarify ownership between Hermes and OpenClaw.
- `humanizer`: clean AI-writing patterns in OpenClaw-generated drafts.

## Common Problems

### Gateway says it is running, but cron fails

Check the port:

```bash
lsof -i :18789
```

If no listener exists, use `openclaw-gateway-foreground-fix`.

### The wrong agent handles a job

Use `openclaw-agent-routing` and write down:

- expected artifact;
- owning agent;
- model/provider;
- forbidden actions;
- verification command.

### Channel delivery is risky

Use `openclaw-channel-manager`. Prepare the package locally first, then request human approval before any external send.

### A skill works locally but not after upgrade

Compare SkillHub and local copies:

```bash
diff -ru skills/openclaw ~/.openclaw/skills | sed -n '1,160p'
```

If the local copy was edited, promote the improvement back into SkillHub rather than leaving it as a hidden machine-only patch.

## Safety Rules

- Never commit `auth-state.json`, `auth-profiles.json`, session dumps, cookies, tokens, or API keys.
- Do not use a publishing job as a health check.
- Do not let delegated coding agents mutate OpenClaw cron or auth config directly.
- Prefer one-agent, one-change testing before global config edits.
