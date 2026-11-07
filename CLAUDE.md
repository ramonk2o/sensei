# Sensei

A Claude Code plugin that maintains skill plugins: setup (hajime), backlog and changelog (kanban), changes to skills (kata), releases (shodan).

## Maintenance with sensei

This repository is maintained with the sensei plugin itself. If sensei is installed:
- creating or changing a skill or agent, judging an issue or pull request, or auditing consistency: the `kata` skill;
- BACKLOG.md and CHANGELOG.md: the `kanban` skill (kata writes its own changelog entries);
- releasing a version: `/sensei:shodan`.

Other skills or plugins that write skills or manage these files don't apply in this repository. Without sensei installed, follow the same cycle by reading `skills/kata/SKILL.md`, and check every change against `docs/principles.md`.

**The skills are the object of the work here, not tools.** When the conversation is about maintaining plugins, it's about improving sensei. Don't run a sensei skill's flow on this repository unless explicitly asked to.

## Project facts

- **Documents:** English.
- **Principles:** `docs/principles.md`. Every change is checked against them.
- **Skills stand alone:** no. Sensei installs as a whole plugin, its skills point to each other's references (`../kanban/references/…`), and releases ship no per-skill zips.
- **Validate:** `python3 scripts/check.py` on every change (it runs `claude plugin validate` on an archive of HEAD); `--release` at release.
- **Commits:** author `Ramon K. <contato@ramonk.com>`; no trailers.
- **Integration:** local merge with `--no-ff`; push main when the maintainer says so or at release.
- **Tags:** `vX.Y.Z`.
- **Maintenance runs on the installed release** of sensei, not on this working copy: `--plugin-dir` is only for trying a change in a separate session. The installed check script doesn't see changes to `scripts/check.py`, so the local one (Validate) always runs too.
- **Generic:** sensei is public, so no skill names a person, a private repository or a specific plugin as part of its behavior (principle 10). Names appear only as examples.
