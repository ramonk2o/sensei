# Backlog

Ideas, bugs and debt for this plugin, managed with sensei's `log` skill. Each entry starts from a real case. Done work leaves this file: what changed goes to CHANGELOG.md.

## Discarded

### A CLAUDE.md under .claude/
- **Description:** Step 1 of `prepare` looks for the CLAUDE.md at the root and in `.claude/`, and the rest of the setup updates whichever exists.
- **Why discarded:** a special case of marketr, not a pattern worth handling in the skill. (2026-11-10)

### Try the cycle on a real plugin
- **Description:** Run `prepare` on an existing plugin and record here what went wrong.
- **Why discarded:** a reminder to test, not a change; the runs so far worked, and a real failure on another plugin will come in as its own entry with its case. (2026-11-10)
