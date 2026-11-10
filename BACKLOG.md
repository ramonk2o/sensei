# Backlog

Ideas, bugs and debt for this plugin, managed with sensei's `log` skill. Each entry starts from a real case. Done work leaves this file: what changed goes to CHANGELOG.md.

## prepare

### A CLAUDE.md under .claude/
- **Type:** Bug
- **Motivation:** re-running `prepare` on marketr (2026-11-10), its CLAUDE.md was at `.claude/CLAUDE.md`. Step 1 says only "CLAUDE.md", so a reader who looks at the root concludes there is none and proposes a second one.
- **Description:** Step 1 looks for the CLAUDE.md at the root and in `.claude/`, and the rest of the setup updates whichever exists.

## Plugin

### Try the cycle on a real plugin
- **Type:** Debt
- **Motivation:** sensei was designed before it was used. Its first runs on itself (a `train` change to `prepare` and the 0.1.0 release, 2026-11-07) worked. On 2026-11-10 `prepare` re-ran on marketr, a plugin already set up by an earlier sensei: its three differences (removing `git archive`, the ask rules, a deny rule for `anthropic-skills:skill-creator`) came out right, and the deny rule worked on a skill whose bundle isn't in `claude plugin list`. No `train` or `graduate` has run on another plugin yet.
- **Description:** Run `prepare` on an existing plugin and record here what went wrong.
- **Open questions:**
  - Whether `Bash(python3 */plugins/cache/*/sensei/*/scripts/check.py*)` matches the command a real session runs, and whether Claude Code warns about it at startup.
  - Whether `claude plugin eval` with a branch checkout target behaves as `testing.md` assumes.
  - How `graduate` finds the last version in a plugin with released versions in its changelog and no git tags (marketr: 0.1.0 to 0.4.0, no tags).
  - The marketr run was made from a session in sensei's folder, so the conflicts came from the wrong session; the next run starts a session in the plugin's own folder.
