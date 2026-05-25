# 给副电脑 Claude 的扫描指令

你现在只做本机 Skill 扫描，不做 Git 操作，不删除、不覆盖、不移动正式 Skill。

## 输出目录

请把所有输出写入：

```text
/Users/robin/AltmanCodex/MacBook_Rovin/_workspace/skillhub_sync/claude_exports/
```

如果这台电脑不是 MacBook_Rovin，请改成该电脑本地存在的临时整理目录，例如：

```text
~/SkillHub_claude_exports/
```

## 任务

1. 查找本机所有包含 `SKILL.md` 的 Skill 目录。
2. 优先扫描这些目录：

```text
~/.codex/skills
~/.agents/skills
~/.openclaw/workspace/skills
~/AltmanCodex/_System/skills
~/AltmanCodex/MacBook_Rovin/_System/skills
```

3. 生成：

```text
skills_manifest.json
01_REPORT_skill_scan_v1.md
```

4. 每个 Skill 记录：

```text
name
description
path
SKILL.md hash
整个 Skill 目录 hash
文件数量
是否包含 scripts/templates/assets
是否疑似重复
是否疑似外部来源
是否疑似包含敏感信息
最后修改时间
```

5. 敏感信息处理：

- 不要输出完整 API Key、Token、Cookie、私钥。
- 只标记 `secret_risk: true/false`。
- 如果必须写证据，只写文件路径和脱敏片段，例如 `前6...后4`。

6. 完成后只汇报输出文件路径，不要提交 Git，不要复制到正式 Skill 目录。

## 可直接使用的命令

如果本机已经有 `SkillHub/scripts/scan_skills.py`，可运行：

```bash
python3 /path/to/SkillHub/scripts/scan_skills.py \
  --machine 副电脑名称 \
  --out ~/SkillHub_claude_exports/skills_manifest.json \
  --report ~/SkillHub_claude_exports/01_REPORT_skill_scan_v1.md
```

