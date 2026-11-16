# When the plugin is sensei itself

Sensei is maintained with sensei: the copy installed in Claude Code is the tool doing the maintenance, while the repository holds the source being changed. That changes three steps:
- **Step 3, CLAUDE.md:** keep its "Maintenance with sensei" section as it is, on every run. It is adapted to a plugin that maintains itself: its fallback points to the repository's own `skills/train/SKILL.md`.
- **Step 4, shared settings:** besides the installed check script, allow the working copy's: `Bash(python3 scripts/check.py*)`.
- **Step 4, local settings:** write no `enabledPlugins` entry for sensei, and remove one an earlier run left, so the installed copy stays on.
- **Step 8, trying a change:** never use `--plugin-dir` for the session doing the maintenance: a broken change would break the tool making it.
