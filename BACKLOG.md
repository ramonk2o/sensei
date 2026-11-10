# Backlog

Ideas, bugs and debt for this plugin, managed with sensei's `log` skill. Each entry starts from a real case. Done work leaves this file: what changed goes to CHANGELOG.md.

## Plugin

### Try the cycle on a real plugin
- **Type:** Debt
- **Motivation:** sensei was designed before it was used. Its first runs on itself (a `train` change to `prepare` and the 0.1.0 release, 2026-11-07) worked. It hasn't set up an existing plugin yet.
- **Description:** Run `prepare` on an existing plugin and record here what went wrong.
- **Open questions:**
  - Whether `Bash(python3 */plugins/cache/*/sensei/*/scripts/check.py*)` matches the command a real session runs, and whether Claude Code warns about it at startup.
  - Whether `claude plugin eval` with a branch checkout target behaves as `testing.md` assumes.
