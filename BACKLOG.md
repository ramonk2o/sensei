# Backlog

Ideas, bugs and debt for this plugin, managed with sensei's `log` skill. Each entry starts from a real case. Done work leaves this file: what changed goes to CHANGELOG.md.

## graduate

### Open feature pull requests at release
- **Type:** Idea
- **Motivation:** cold reader on `graduate` in pull request mode (2026-11-13): with a feature pull request still open, the release is proposed without it, or stops with nothing to release, and nothing tells the maintainer.
- **Description:** in pull request mode, list the open pull requests at step 1 so the maintainer decides whether to wait for them before releasing.

## Discarded

### A CLAUDE.md under .claude/
- **Description:** Step 1 of `prepare` looks for the CLAUDE.md at the root and in `.claude/`, and the rest of the setup updates whichever exists.
- **Why discarded:** a special case of marketr, not a pattern worth handling in the skill. (2026-11-10)

### Try the cycle on a real plugin
- **Description:** Run `prepare` on an existing plugin and record here what went wrong.
- **Why discarded:** a reminder to test, not a change; the runs so far worked, and a real failure on another plugin will come in as its own entry with its case. (2026-11-10)
