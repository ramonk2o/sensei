# Backlog

Ideas, bugs and debt for this plugin, managed with sensei's `log` skill. Each entry starts from a real case. Done work leaves this file: what changed goes to CHANGELOG.md.

## prepare

### Skills stand alone, before any skill exists
- **Type:** Bug
- **Motivation:** cold reader on `prepare` for a new plugin from a `meditate` plan (2026-11-13): when the principles don't say whether skills stand alone, `claude-md.md` says to take "the value that matches the skills as they are", but no skill exists yet, so one reading writes "yes" and another has no basis. The value decides one zip per skill or one of the whole plugin.
- **Description:** say what to recommend for this fact when the plugin has no skills yet.

### The local settings file with no installed copy
- **Type:** Bug
- **Motivation:** cold reader on `prepare` for a new plugin (2026-11-13): step 4 sets `enabledPlugins` to `false` for the installed copy from `claude plugin list --json`, but a new plugin has none, and nothing says to write no entry or whether to create the local file when it would be empty.
- **Description:** say what step 4 does when the plugin being maintained isn't installed.

### General code-review skills as conflicts
- **Type:** Bug
- **Motivation:** cold reader on `prepare` (2026-11-13): bundled skills like `code-review`, `simplify` and `security-review` literally match step 5's "reviewing pull requests or changes", though they are general code tools, not sensei's work. One reading turns them off for the whole project with `skillOverrides`; the other only mentions them.
- **Description:** make step 5 say whether general code-review skills count as conflicts.

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
