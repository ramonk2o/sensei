# Backlog

Ideas, bugs and debt for this plugin, managed with sensei's `log` skill. Each entry starts from a real case. Done work leaves this file: what changed goes to CHANGELOG.md.

## prepare

### A conflicting skill inside a large plugin
- **Type:** Debt
- **Motivation:** a cold reader of `prepare` (2026-11-10) found that the main conflict in a typical session, a skill-writing skill shipped inside a large plugin of unrelated skills, can only be handled by turning off the whole plugin (losing the unrelated skills) or by relying on the routing. Step 5 allows `skillOverrides` only for skills with no plugin prefix, and two readers would recommend differently.
- **Description:** Say how to weigh turning off a whole plugin against relying on the routing, and use a per-skill override for a plugin's skill if Claude Code supports one.
- **Open questions:**
  - Whether a `plugin:skill` name works anywhere: Claude Code's skills docs (2026-11-10) say plugin skills aren't affected by `skillOverrides`, and don't say whether a `Skill(plugin:skill)` deny rule works.
  - Whether a conflict also covers skills that overlap the maintained plugin's subject (a slides skill for a deck plugin), or only sensei's own work.
  - What to do with a prefixed skill whose plugin doesn't appear in `claude plugin list --json` (a bundle that ships with the app).
  - Whether a re-run proposes again a conflict the user declined before, since nothing records the decline (a cold reader of a re-run, 2026-11-10).

## Plugin

### Try the cycle on a real plugin
- **Type:** Debt
- **Motivation:** sensei was designed before it was used. Its first runs on itself (a `train` change to `prepare` and the 0.1.0 release, 2026-11-07) worked. It hasn't set up an existing plugin yet.
- **Description:** Run `prepare` on an existing plugin and record here what went wrong.
- **Open questions:**
  - Whether `Bash(python3 */plugins/cache/*/sensei/*/scripts/check.py*)` matches the command a real session runs, and whether Claude Code warns about it at startup.
  - Whether `claude plugin eval` with a branch checkout target behaves as `testing.md` assumes.
