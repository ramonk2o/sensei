# Sensei

A Claude Code plugin that maintains skill plugins: planning (`meditate`), setup (`prepare`), backlog and changelog (`log`), changes to skills (`train`), releases (`graduate`).

## Maintenance with sensei

This repository is maintained with the sensei plugin itself. If sensei is installed:
- creating or changing a skill or agent, judging an issue or pull request, or auditing consistency: the `train` skill;
- the backlog and CHANGELOG.md: the `log` skill (`train` writes its own changelog entries);
- releasing a version: `/sensei:graduate`.

Other skills or plugins that write skills or manage these files don't apply in this repository. Without sensei installed, follow the same cycle by reading `skills/train/SKILL.md`, and check every change against `docs/principles.md`.

**The skills are the object of the work here, not tools.** When the conversation is about maintaining plugins, it's about improving sensei. Don't run a sensei skill's flow on this repository unless explicitly asked to.

## Project facts

- **Documents:** English.
- **Principles:** `docs/principles.md`. Every change is checked against them.
- **Skills stand alone:** no. Sensei installs as a whole plugin, its skills point to each other's references (`../log/references/…`), and releases ship one zip of the whole plugin, not one per skill.
- **Validate:** `python3 scripts/check.py` on every change (it runs `claude plugin validate` on an archive of HEAD); `--release` at release.
- **Commits:** author `Ramon K. <contato@ramonk.com>`; no trailers.
- **Integration:** pull requests: push the branch, open the pull request and merge it with a merge commit, each on the maintainer's OK.
- **Backlog:** GitHub issues.
- **Tags:** `vX.Y.Z`.
- **Maintenance runs on the installed release** of sensei, not on this working copy: `--plugin-dir` is only for trying a change in a separate session. The installed check script doesn't see changes to `scripts/check.py`, so the local one (Validate) always runs too.
- **Generic:** sensei is public, so no skill names a person, a private repository or a specific plugin as part of its behavior (principle 10). Names appear only as examples.
