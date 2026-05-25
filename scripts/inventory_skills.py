#!/usr/bin/env python3
"""Build a SkillHub inventory from local skills, manifests, and source registry."""

from __future__ import annotations

import json
from datetime import datetime
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
OUT = REPO / "registry/skills_inventory.json"
REPORT = REPO / "reports/05_REPORT_skillhub_外部候选批量盘点_v1.md"


def read_json(path: Path) -> dict:
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def read_text(path: Path, limit: int = 12000) -> str:
    try:
        return path.read_text(encoding="utf-8", errors="replace")[:limit]
    except OSError:
        return ""


def parse_frontmatter(text: str) -> dict[str, str]:
    if not text.startswith("---"):
        return {}
    end = text.find("\n---", 3)
    if end == -1:
        return {}
    data: dict[str, str] = {}
    for line in text[3:end].splitlines():
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        data[key.strip()] = value.strip().strip("'\"")
    return data


def source_type_from_path(path: Path) -> str:
    parts = set(path.parts)
    if "rubin-original" in parts:
        return "rubin-original"
    if "rubin-adapted" in parts:
        return "rubin-adapted"
    if "external-sandbox" in parts:
        return "external-sandbox"
    if "external_unverified" in parts:
        return "external-reference"
    return "unknown"


def collect_local_skills() -> list[dict]:
    rows = []
    for skill_md in sorted((REPO / "skills").rglob("SKILL.md")):
        root = skill_md.parent
        text = read_text(skill_md)
        fm = parse_frontmatter(text)
        meta = read_json(root / "skill.meta.json")
        rows.append(
            {
                "kind": "local-skill",
                "id": meta.get("id") or fm.get("name") or root.name,
                "display_name": meta.get("display_name") or root.name,
                "path": root.relative_to(REPO).as_posix(),
                "source_type": meta.get("source_type") or source_type_from_path(root),
                "status": meta.get("status") or "LAB",
                "risk_level": meta.get("risk_level"),
                "version": meta.get("version"),
                "added_at": meta.get("added_at"),
                "updated_at": meta.get("updated_at"),
                "last_tested": meta.get("last_tested"),
                "summary": meta.get("summary") or fm.get("description", ""),
                "requires_api_key": bool(meta.get("requires_api_key")),
                "requires_login": bool(meta.get("requires_login")),
                "writes_external_platform": bool(meta.get("writes_external_platform")),
            }
        )
    return rows


def collect_manifest_skills() -> list[dict]:
    rows = []
    for manifest_path in sorted((REPO / "manifests").glob("*.json")):
        data = read_json(manifest_path)
        for raw in data.get("skills", []):
            rows.append(
                {
                    "kind": "manifest-skill",
                    "id": raw.get("name") or Path(raw.get("path", "")).name,
                    "display_name": raw.get("title") or raw.get("name") or Path(raw.get("path", "")).name,
                    "path": raw.get("path"),
                    "machine": data.get("machine") or manifest_path.stem,
                    "source_type": raw.get("classification_hint", "unknown"),
                    "status": "DISCOVERED",
                    "risk_level": None,
                    "summary": raw.get("description", ""),
                    "secret_risk": bool(raw.get("secret_risk")),
                    "has_scripts": bool(raw.get("has_scripts")),
                    "has_assets": bool(raw.get("has_assets")),
                    "has_templates": bool(raw.get("has_templates")),
                }
            )
    return rows


def collect_sources() -> list[dict]:
    data = read_json(REPO / "registry/sources_index.json")
    return data.get("sources", [])


def table(rows: list[list[str]]) -> str:
    if not rows:
        return "- 无\n"
    lines = [
        "| " + " | ".join(rows[0]) + " |",
        "| " + " | ".join(["---"] * len(rows[0])) + " |",
    ]
    for row in rows[1:]:
        lines.append("| " + " | ".join(str(x).replace("\n", " ") for x in row) + " |")
    return "\n".join(lines) + "\n"


def build_report(inventory: dict) -> str:
    local = inventory["local_skills"]
    manifests = inventory["manifest_skills"]
    sources = inventory["sources"]
    lines = [
        "# SkillHub 外部候选批量盘点 v1",
        "",
        f"生成时间：{inventory['generated_at']}",
        "",
        "## 结论",
        "",
        "- 当前 SkillHub 已有本地候选 skill，可继续扩展批量盘点。",
        "- 外部来源先进入 source radar，不直接复制到 `skills/ready/`。",
        "- 下一步由 `classify_skills.py` 自动打风险等级和推荐动作。",
        "",
        "## 总览",
        "",
        table(
            [
                ["类型", "数量"],
                ["本地 Skill", str(len(local))],
                ["manifest 发现记录", str(len(manifests))],
                ["外部来源", str(len(sources))],
            ]
        ),
        "## 本地 Skill",
        "",
    ]
    lines.append(
        table(
            [["Skill", "中文名", "状态", "风险", "路径"]]
            + [[s["id"], s["display_name"], s.get("status", ""), s.get("risk_level") or "", s.get("path", "")] for s in local]
        )
    )
    lines += ["## 外部来源", ""]
    lines.append(
        table(
            [["来源", "类型", "优先级", "建议动作", "风险提示"]]
            + [[s["name"], s["type"], s.get("priority", ""), s.get("recommended_action", ""), s.get("risk_hint", "")] for s in sources]
        )
    )
    lines += ["## 下一步", "", "1. 运行 `scripts/classify_skills.py` 自动分类。", "2. 让 MiniMax agent 生成外部来源卡和使用卡初稿。", "3. Codex 抽样复核 Top 7。", ""]
    return "\n".join(lines)


def main() -> None:
    inventory = {
        "schema_version": "0.1.0",
        "generated_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "local_skills": collect_local_skills(),
        "manifest_skills": collect_manifest_skills(),
        "sources": collect_sources(),
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    REPORT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(inventory, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    REPORT.write_text(build_report(inventory), encoding="utf-8")
    print(OUT)
    print(REPORT)


if __name__ == "__main__":
    main()

