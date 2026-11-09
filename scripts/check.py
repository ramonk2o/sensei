#!/usr/bin/env python3
"""Sensei's consistency checks for a skill plugin repository.

Usage:
    check.py [ROOT] [--release] [--scope-map] [--no-validate]
             [--skill-tokens N] [--description-chars N]

ROOT defaults to the current directory. Exit code 1 when any check fails;
warnings are printed but don't fail. Standard library only.
"""

import argparse
import json
import os
import re
import shutil
import subprocess
import sys
import tarfile
import tempfile
from pathlib import Path

errors = []
warnings = []


def err(msg):
    errors.append(msg)


def warn(msg):
    warnings.append(msg)


def run(cmd, cwd):
    try:
        out = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True)
    except FileNotFoundError:
        return None
    return out


# ---------- discovery ----------

def load_json(path):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        return None
    except json.JSONDecodeError as e:
        err(f"{path}: invalid JSON ({e})")
        return None


def plugin_dirs(root):
    """Plugin folders in this repo: the root itself, or the marketplace's local sources."""
    dirs = []
    if (root / ".claude-plugin" / "plugin.json").exists():
        dirs.append(root)
    market = load_json(root / ".claude-plugin" / "marketplace.json")
    if market:
        for p in market.get("plugins", []):
            src = p.get("source")
            if isinstance(src, str) and src.startswith("./"):
                d = (root / src).resolve()
                if d != root.resolve() and (d / ".claude-plugin" / "plugin.json").exists():
                    dirs.append(d)
    if not dirs and (root / "skills").is_dir():
        dirs.append(root)
    return dirs


def parse_frontmatter(text):
    """Minimal YAML frontmatter reader: scalar keys, quoted values, and | or > blocks."""
    if not text.startswith("---"):
        return None, text
    end = text.find("\n---", 3)
    if end == -1:
        return None, text
    block = text[3:end].strip("\n")
    body = text[end + 4:]
    data = {}
    lines = block.split("\n")
    i = 0
    while i < len(lines):
        m = re.match(r"^([A-Za-z0-9_-]+):\s*(.*)$", lines[i])
        if not m:
            i += 1
            continue
        key, value = m.group(1), m.group(2).strip()
        if value in ("|", ">", "|-", ">-"):
            parts = []
            i += 1
            while i < len(lines) and (lines[i].startswith(" ") or not lines[i].strip()):
                parts.append(lines[i].strip())
                i += 1
            sep = "\n" if value.startswith("|") else " "
            data[key] = sep.join(p for p in parts).strip()
            continue
        if len(value) >= 2 and value[0] == value[-1] and value[0] in "\"'":
            value = value[1:-1]
        data[key] = value
        i += 1
    return data, body


def read_limits(root, args):
    limits = {"skill_tokens": None, "description_chars": None}
    p = root / "docs" / "principles.md"
    if p.exists():
        m = re.search(r"<!--\s*sensei:limits(.*?)-->", p.read_text(encoding="utf-8"), re.S)
        if m:
            for line in m.group(1).splitlines():
                kv = re.match(r"\s*([a-z_]+)\s*:\s*(\d+)", line)
                if kv and kv.group(1) in limits:
                    limits[kv.group(1)] = int(kv.group(2))
    if args.skill_tokens:
        limits["skill_tokens"] = args.skill_tokens
    if args.description_chars:
        limits["description_chars"] = args.description_chars
    return limits


# ---------- checks ----------

REF_RE = re.compile(r"(?<![\w/.-])((?:\.\./[\w-]+/)?(?:references|scripts|assets|agents)/[\w./-]*[\w-]\.[a-z]{1,5})")


def check_skills(plugin, limits, rel):
    skills = []
    sdir = plugin / "skills"
    if not sdir.is_dir():
        return skills
    for skill_md in sorted(sdir.glob("*/SKILL.md")):
        folder = skill_md.parent
        text = skill_md.read_text(encoding="utf-8")
        fm, body = parse_frontmatter(text)
        where = rel(skill_md)
        if fm is None:
            err(f"{where}: no frontmatter")
            continue
        name = fm.get("name", "")
        desc = fm.get("description", "")
        if name != folder.name:
            err(f"{where}: name '{name}' doesn't match folder '{folder.name}'")
        if not desc:
            err(f"{where}: no description")
        tokens = len(text) // 4
        if limits["skill_tokens"] and tokens > limits["skill_tokens"]:
            err(f"{where}: ~{tokens} tokens, over the {limits['skill_tokens']} limit")
        if limits["description_chars"] and len(desc) > limits["description_chars"]:
            err(f"{where}: description has {len(desc)} characters, over the {limits['description_chars']} limit")
        pointers = [(where, body, None)]
        for extra in sorted(folder.glob("references/**/*.md")):
            pointers.append((rel(extra), extra.read_text(encoding="utf-8"), extra.parent))
        for src, text_, here in pointers:
          for ref in sorted(set(REF_RE.findall(text_))):
            if "<" in ref or "*" in ref:
                continue
            if here is not None and (here / ref).exists():
                continue
            if (plugin / ref).exists():
                continue
            if not (folder / ref).exists():
                owners = [d.name for d in sdir.iterdir() if d.is_dir() and d != folder and (d / ref).exists()]
                if owners:
                    warn(f"{src}: names {ref}, which exists only in {', '.join(owners)} "
                         f"(fine if the text says whose it is; a path to read is ../{owners[0]}/{ref})")
                else:
                    err(f"{src}: names {ref}, which doesn't exist")
        skills.append({"name": name or folder.name, "description": desc, "body": body,
                       "tokens": tokens, "path": where, "manual": fm.get("disable-model-invocation") == "true"})
    return skills


def check_listings(root, plugin, skills, rel):
    readme = root / "README.md"
    if not readme.exists():
        readme = plugin / "README.md"
    if readme.exists():
        text = readme.read_text(encoding="utf-8")
        for s in skills:
            if not re.search(rf"(?<![\w-]){re.escape(s['name'])}(?![\w-])", text):
                err(f"{rel(readme)}: doesn't mention the skill '{s['name']}'")
    else:
        warn("no README.md")
    pj = load_json(plugin / ".claude-plugin" / "plugin.json")
    market = load_json(root / ".claude-plugin" / "marketplace.json")
    if pj and market:
        entry = next((p for p in market.get("plugins", []) if p.get("name") == pj.get("name")), None)
        if entry is None:
            err(f"marketplace.json: no entry named '{pj.get('name')}'")
        elif entry.get("description") and pj.get("description") and entry["description"] != pj["description"]:
            warn("plugin.json and marketplace.json describe the plugin differently")
    if pj and not re.match(r"^\d+\.\d+\.\d+$", str(pj.get("version", ""))):
        err(f"{rel(plugin / '.claude-plugin' / 'plugin.json')}: version '{pj.get('version')}' isn't X.Y.Z")


VERSION_RE = re.compile(r"^## \[(Unreleased|\d+\.\d+\.\d+)\](?: - (\d{4}-\d{2}-\d{2}))?\s*$")
GROUPS = {"Added", "Changed", "Deprecated", "Removed", "Fixed", "Security"}


def check_changelog(root, release):
    p = root / "CHANGELOG.md"
    if not p.exists():
        err("no CHANGELOG.md")
        return
    lines = p.read_text(encoding="utf-8").splitlines()
    versions, current, groups, unreleased_items = [], None, set(), 0
    for n, line in enumerate(lines, 1):
        if line.startswith("## "):
            m = VERSION_RE.match(line)
            if not m:
                err(f"CHANGELOG.md:{n}: heading isn't '## [X.Y.Z] - YYYY-MM-DD' or '## [Unreleased]'")
                current = None
                continue
            current, groups = m.group(1), set()
            if current != "Unreleased" and not m.group(2):
                err(f"CHANGELOG.md:{n}: version {current} has no date")
            versions.append((current, n))
        elif line.startswith("### ") and current:
            g = line[4:].strip()
            if g not in GROUPS:
                err(f"CHANGELOG.md:{n}: unknown group '{g}'")
            if g in groups:
                err(f"CHANGELOG.md:{n}: group '{g}' repeated in [{current}]")
            groups.add(g)
        elif current == "Unreleased" and re.match(r"^\s*[-*] ", line):
            unreleased_items += 1
    names = [v for v, _ in versions]
    if names.count("Unreleased") != 1:
        err(f"CHANGELOG.md: {names.count('Unreleased')} [Unreleased] sections, expected 1")
    elif names[0] != "Unreleased":
        err("CHANGELOG.md: [Unreleased] isn't the first version")
    nums = [tuple(int(x) for x in v.split(".")) for v in names if v != "Unreleased"]
    if nums != sorted(nums, reverse=True) or len(set(nums)) != len(nums):
        err("CHANGELOG.md: versions aren't in strictly descending order")
    if release and unreleased_items == 0:
        err("CHANGELOG.md: [Unreleased] is empty: nothing to release")
    return nums[0] if nums else None


def main_branch(root):
    out = run(["git", "symbolic-ref", "--quiet", "--short", "refs/remotes/origin/HEAD"], root)
    if out and out.returncode == 0 and out.stdout.strip():
        return out.stdout.strip().split("/", 1)[-1]
    for b in ("main", "master"):
        out = run(["git", "rev-parse", "--verify", "--quiet", b], root)
        if out and out.returncode == 0:
            return b
    return None


def check_git(root):
    if not (root / ".git").exists():
        warn("not a git repository: branch and archive checks skipped")
        return False
    has_head = run(["git", "rev-parse", "--verify", "--quiet", "HEAD"], root)
    committed = bool(has_head and has_head.returncode == 0)
    status = run(["git", "status", "--porcelain"], root)
    if committed and status and status.stdout.strip():
        warn("uncommitted changes: the validator checks the last commit, not them")
    if not committed:
        warn("no commits yet: the validator checks the working tree")
    branch = run(["git", "rev-parse", "--abbrev-ref", "HEAD"], root)
    branch = branch.stdout.strip() if branch and branch.returncode == 0 else None
    main = main_branch(root)
    if branch and main and branch != main and branch != "HEAD":
        diff = run(["git", "diff", "--name-only", f"{main}...HEAD"], root)
        files = diff.stdout.split() if diff and diff.returncode == 0 else []
        plugin_parts = ("skills/", "agents/", "hooks/", "commands/", ".mcp.json", ".claude-plugin/")
        touches_plugin = any(any(part in f for part in plugin_parts) for f in files)
        touches_log = any(f.endswith("CHANGELOG.md") for f in files)
        if touches_plugin and not touches_log:
            err(f"branch '{branch}' changes the plugin but not CHANGELOG.md")
    return committed


def validate(root, plugins, release, committed):
    if shutil.which("claude") is None:
        warn("claude CLI not found: validate skipped")
        return
    tmp = tempfile.mkdtemp(prefix="sensei-check-")
    try:
        if committed:
            archive = os.path.join(tmp, "head.tar")
            out = run(["git", "archive", "--format=tar", "-o", archive, "HEAD"], root)
            if not out or out.returncode != 0:
                err("git archive failed: " + (out.stderr.strip() if out else "git not found"))
                return
            dest = os.path.join(tmp, "repo")
            with tarfile.open(archive) as t:
                t.extractall(dest)
            # The validator finds the repository root by its .git; without one,
            # files at the root (such as a README) are missed for plugins in sub-folders.
            init = run(["git", "init", "-q"], dest)
            if not init or init.returncode != 0:
                err("git init in the archive copy failed: " + (init.stderr.strip() if init else "git not found"))
                return
            base = Path(dest)
        else:
            base = root
        targets = [base / p.relative_to(root) if p != root else base for p in plugins]
        for t in targets:
            cmd = ["claude", "plugin", "validate", str(t)]
            if release:
                cmd += ["--profile", "directory"]
            out = run(cmd, root)
            if out is None:
                warn("claude CLI not found: validate skipped")
                return
            if out.returncode != 0:
                text = (out.stdout + out.stderr).strip().splitlines()
                err("claude plugin validate failed:\n    " + "\n    ".join(text[-25:]))
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


def scope_map(skills):
    print("Scope map")
    for s in skills:
        mode = " (manual)" if s["manual"] else ""
        print(f"\n## {s['name']}{mode} (~{s['tokens']} tokens)")
        print(f"Description: {s['description']}")
        paras = [p.strip() for p in re.split(r"\n\s*\n", s["body"]) if p.strip() and not p.strip().startswith("#")]
        if paras:
            opening = " ".join(paras[0].split())
            print(f"Opening: {opening[:700]}{'…' if len(opening) > 700 else ''}")


def main():
    ap = argparse.ArgumentParser(description="Consistency checks for a skill plugin repository.")
    ap.add_argument("root", nargs="?", default=".")
    ap.add_argument("--release", action="store_true", help="release checks: non-empty [Unreleased], validate --profile directory")
    ap.add_argument("--scope-map", action="store_true", help="print each skill's description and opening, then exit")
    ap.add_argument("--no-validate", action="store_true", help="skip claude plugin validate")
    ap.add_argument("--skill-tokens", type=int)
    ap.add_argument("--description-chars", type=int)
    args = ap.parse_args()

    root = Path(args.root).resolve()
    rel = lambda p: os.path.relpath(p, root)
    plugins = plugin_dirs(root)
    if not plugins:
        print(f"{root}: no plugin found (.claude-plugin/plugin.json or skills/)")
        return 1
    limits = read_limits(root, args)
    skills = []
    for p in plugins:
        found = check_skills(p, limits, rel)
        check_listings(root, p, found, rel)
        skills += found

    if args.scope_map:
        scope_map(skills)
        return 0

    check_changelog(root, args.release)
    committed = check_git(root)
    if not args.no_validate:
        validate(root, plugins, args.release, committed)

    if not limits["skill_tokens"] or not limits["description_chars"]:
        warn("no size limits found (a sensei:limits block in docs/principles.md, or flags): sizes not checked")
    for w in warnings:
        print(f"warning: {w}")
    for e in errors:
        print(f"FAIL: {e}")
    total = sum(s["tokens"] for s in skills)
    print(f"{len(skills)} skills, ~{total} tokens in SKILL.md files; "
          f"{len(errors)} failures, {len(warnings)} warnings")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
