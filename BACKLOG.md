# Backlog

Ideas, bugs and debt for this plugin, managed with sensei's kanban skill. Each entry starts from a real case. Done work leaves this file: what changed goes to CHANGELOG.md.

## hajime

### Git permissions allow destructive variants
- **Type:** Bug
- **Motivation:** a cold reader of hajime (2026-11-07) found that allowing whole commands lets their destructive forms through without a prompt: `git tag*` allows `git tag -d`, `git switch*` allows `--discard-changes`, `git commit*` allows `--amend`, `git archive*` writes files with `-o`. Step 4 says deleting branches or files keeps asking.
- **Description:** Narrow the allowed patterns or add `permissions.deny` rules for the destructive forms, keeping what the cycle uses (kata amends a wording fix; shodan runs `git tag -a`).
- **Open questions:**
  - Narrower allow rules or deny rules.

## Plugin

### Try the cycle on a real plugin
- **Type:** Debt
- **Motivation:** sensei was designed before it was used. Its first runs on itself (a kata change to hajime and the 0.1.0 release, 2026-11-07) worked. It hasn't set up an existing plugin yet.
- **Description:** Run hajime on an existing plugin and record here what went wrong.
- **Open questions:**
  - Whether `Bash(python3 */plugins/cache/*/sensei/*/scripts/check.py*)` matches the command a real session runs, and whether Claude Code warns about it at startup.
  - Whether `claude plugin eval` with a branch checkout target behaves as `testing.md` assumes.
