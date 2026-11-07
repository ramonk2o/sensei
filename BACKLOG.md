# Backlog

Ideas, bugs and debt for this plugin, managed with sensei's kanban skill. Each entry starts from a real case. Done work leaves this file: what changed goes to CHANGELOG.md.

## hajime

### .gitignore in an existing repository
- **Type:** Bug
- **Motivation:** a cold reader of hajime (2026-11-07) found that only `git init` proposes the `.gitignore`. In a repository that already exists, nothing makes sure `.claude/settings.local.json` and `evals/**/results/` stay out of git.
- **Description:** In step 2, check an existing `.gitignore` and propose the missing lines.

### Re-running hajime on sensei's own repository
- **Type:** Bug
- **Motivation:** the same cold reader found that the template's fixed "Maintenance with sensei" section, refreshed on every re-run, would overwrite what sensei's own CLAUDE.md needs. One example is the fallback without sensei installed, which there points to `skills/kata/SKILL.md`.
- **Description:** Say how the template adapts when the plugin being maintained is sensei itself, or that the re-run keeps that section as it is.

### Which check script counts in sensei's own repository
- **Type:** Debt
- **Motivation:** the same cold reader couldn't tell whether hajime should also allow `python3 scripts/check.py`. sensei's CLAUDE.md runs the local script, and the permission covers only the installed one.
- **Description:** Settle the permission and the wording for that case.

### Trying a change with `--plugin-dir`
- **Type:** Debt
- **Motivation:** the same cold reader asked whether the test session must turn off the installed copy, and whether it should run in another folder so this repository's CLAUDE.md and settings don't load.
- **Description:** Check how `--plugin-dir` behaves against an installed plugin of the same name, and write the answer into step 8.

### Mapping conflicting skills to plugins
- **Type:** Debt
- **Motivation:** the same cold reader found that step 5 doesn't say how to get a skill's plugin id, or what to do with built-in skills that `enabledPlugins` can't turn off.
- **Description:** Add both to step 5.

## Plugin

### Try the cycle on a real plugin
- **Type:** Debt
- **Motivation:** no case recorded yet: sensei was designed, not used. Its first real runs (hajime on an existing plugin, a kata behavior change, a release) will show what the design missed.
- **Description:** Run hajime on an existing plugin, then one kata change and one shodan release, and record what went wrong here.
- **Open questions:**
  - Whether the permission pattern for the check script survives a sensei update.
  - Whether `attribution` with empty strings removes the commit trailer in practice.
  - Whether `claude plugin eval` with a branch checkout target behaves as `testing.md` assumes.
