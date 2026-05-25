#!/usr/bin/env python3
"""Scan local agent skill folders into a manifest without copying content."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import socket
from datetime import datetime, timezone
from pathlib import Path


SECRET_PATTERNS = [
    re.compile(r"sk-[A-Za-z0-9_-]{20,}"),
    re.compile(r"gh[pousr]_[A-Za-z0-9_]{20,}"),
    re.compile(r"(?i)(api[_-]?key|token|secret|cookie|password)\s*[:=]\s*['\"]?[^'\"\s]{12,}"),
    re.compile(r"-----BEGIN (?:RSA |OPENSSH |EC |DSA )?PRIVATE KEY-----"),
]


DEFAULT_ROOTS = [
    "~/.codex/skills",
    "~/.agents/skills",
    "~/.openclaw/workspace/skills",
    "~/AltmanCodex/_System/skills",
    "~/AltmanCodex/MacBook_Rovin/_System/skills",
]


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def sha256_tree(root: Path) -> str:
    h = hashlib.sha256()
    for path in sorted(p for p in root.rglob("*") if p.is_file()):
        if any(part in {".git", "__pycache__"} for part in path.parts):
            continue
        rel = path.relative_to(root).as_posix()
        h.update(rel.encode("utf-8"))
        h.update(b"\0")
        h.update(sha256_file(path).encode("ascii"))
        h.update(b"\0")
    return h.hexdigest()


def read_text_head(path: Path, limit: int = 12000) -> str:
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


def first_heading(text: str) -> str:
    for line in text.splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return ""


def classify_path(path: Path) -> str:
    s = path.as_posix().lower()
    if "external" in s or "unverified" in s:
        return "external_unverified"
    if "lab" in s or "test" in s or "workspace" in s:
        return "lab"
    return "candidate"


def has_secret_risk(root: Path) -> bool:
    for path in root.rglob("*"):
        if not path.is_file():
            continue
        if path.stat().st_size > 1024 * 1024:
            continue
        text = read_text_head(path)
        if any(p.search(text) for p in SECRET_PATTERNS):
            return True
    return False


def summarize_skill(skill_md: Path) -> dict:
    root = skill_md.parent
    text = read_text_head(skill_md)
    fm = parse_frontmatter(text)
    files = [p for p in root.rglob("*") if p.is_file() and ".git" not in p.parts]
    rel_files = [p.relative_to(root).as_posix() for p in files]
    return {
        "name": fm.get("name") or root.name,
        "title": first_heading(text),
        "description": fm.get("description", ""),
        "path": root.as_posix(),
        "skill_md": skill_md.as_posix(),
        "classification_hint": classify_path(root),
        "tree_sha256": sha256_tree(root),
        "skill_md_sha256": sha256_file(skill_md),
        "file_count": len(files),
        "has_scripts": any(part == "scripts" for p in rel_files for part in Path(p).parts),
        "has_templates": any(part == "templates" for p in rel_files for part in Path(p).parts),
        "has_assets": any(part == "assets" for p in rel_files for part in Path(p).parts),
        "secret_risk": has_secret_risk(root),
        "modified_at": datetime.fromtimestamp(
            max((p.stat().st_mtime for p in files), default=root.stat().st_mtime),
            tz=timezone.utc,
        ).isoformat(),
        "files_sample": sorted(rel_files)[:20],
    }


def find_skill_mds(roots: list[Path]) -> list[Path]:
    found: list[Path] = []
    for root in roots:
        if not root.exists():
            continue
        for path in root.rglob("SKILL.md"):
            if ".git" in path.parts:
                continue
            found.append(path)
    return sorted(set(found))


def build_report(manifest: dict) -> str:
    skills = manifest["skills"]
    duplicate_groups: dict[str, list[dict]] = {}
    for skill in skills:
        duplicate_groups.setdefault(skill["tree_sha256"], []).append(skill)
    duplicates = [v for v in duplicate_groups.values() if len(v) > 1]
    risks = [s for s in skills if s["secret_risk"]]

    lines = [
        "# Skill Scan Report",
        "",
        f"- Machine: `{manifest['machine']}`",
        f"- Generated: `{manifest['generated_at']}`",
        f"- Roots scanned: {len(manifest['roots'])}",
        f"- Skills found: {len(skills)}",
        f"- Duplicate groups: {len(duplicates)}",
        f"- Secret-risk skills: {len(risks)}",
        "",
        "## Duplicate Groups",
        "",
    ]
    if duplicates:
        for i, group in enumerate(duplicates, 1):
            lines.append(f"### Group {i}")
            for skill in group:
                lines.append(f"- `{skill['name']}` — `{skill['path']}`")
            lines.append("")
    else:
        lines.append("- None")
        lines.append("")

    lines.extend(["## Secret Risk", ""])
    if risks:
        for skill in risks:
            lines.append(f"- `{skill['name']}` — `{skill['path']}`")
    else:
        lines.append("- None")
    lines.append("")

    lines.extend(["## Skills", ""])
    for skill in skills:
        risk = " risk" if skill["secret_risk"] else ""
        lines.append(f"- `{skill['name']}` [{skill['classification_hint']}]{risk} — `{skill['path']}`")
    lines.append("")
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--machine", default=socket.gethostname())
    parser.add_argument("--root", action="append", default=[])
    parser.add_argument("--out", required=True)
    parser.add_argument("--report", required=True)
    args = parser.parse_args()

    root_inputs = args.root or DEFAULT_ROOTS
    roots = [Path(os.path.expanduser(p)).resolve() for p in root_inputs]
    skills = [summarize_skill(p) for p in find_skill_mds(roots)]
    manifest = {
        "schema": "skillhub.manifest.v1",
        "machine": args.machine,
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "roots": [p.as_posix() for p in roots],
        "skills": skills,
    }

    out = Path(args.out)
    report = Path(args.report)
    out.parent.mkdir(parents=True, exist_ok=True)
    report.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    report.write_text(build_report(manifest), encoding="utf-8")
    print(f"Wrote {out}")
    print(f"Wrote {report}")


if __name__ == "__main__":
    main()

