# The settings files

What `prepare` writes in the two settings files (`SKILL.md`, steps 4 and 5):
- **`.claude/settings.json`,** shared with everyone who clones the repository: the attribution and the permissions that allow and ask.
- **`.claude/settings.local.json`,** personal to this machine and ignored by git: what is turned off. Turning a plugin off in the shared file would turn it off for every contributor, so it goes here. Create it only when something goes in it; never write it empty.

If a file exists, merge: keep every entry and add only what's missing, except the removals this file names.

## Attribution

`"attribution": {"commit": "", "pr": ""}` in the shared file when the project allows no trailers.

## Allow

Claude Code checks deny rules first, then ask, then allow, and the first match decides, so an ask rule prompts even when a broader allow rule also matches.

`permissions.allow` lets the commands the cycle runs on every change go through without a prompt:
- sensei's check script. Permission rules don't expand `${CLAUDE_PLUGIN_ROOT}`, and the installed path changes with each version, so write it with wildcards: `Bash(python3 */plugins/cache/*/sensei/*/scripts/check.py*)`;
- `Bash(claude plugin validate*)` and `Bash(claude plugin eval*)`;
- the local git commands the cycle uses: `Bash(git status*)`, `Bash(git diff*)`, `Bash(git log*)`, `Bash(git show*)`, `Bash(git add*)`, `Bash(git commit*)`, `Bash(git switch*)`, `Bash(git merge*)`, `Bash(git branch --list*)`, `Bash(git tag*)`, `Bash(git merge-base*)`, `Bash(git rev-parse*)`.

With pull requests, also the read-only `gh` commands: `Bash(gh auth status*)`, `Bash(gh pr view*)`, `Bash(gh pr list*)`, `Bash(gh pr checks*)`. With the backlog in GitHub issues: `Bash(gh issue view*)`, `Bash(gh issue list*)`, `Bash(gh label list*)`, `Bash(gh repo view*)`. Never the commands that write (`gh repo create`, `gh pr create`, `gh pr merge`, `gh issue create`, `edit`, `close`, `comment`, `gh label create`): they publish, so they keep asking. Never allow push, reset, deleting branches or files, or publishing either: they keep asking too.

`git archive` stays out: `graduate` runs it only to write the release zips, with `-o`, which can overwrite any file, so it asks. The check script runs its own archive without going through these rules. On a re-run, propose removing a `Bash(git archive*)` rule an earlier version of sensei added.

## Ask

`permissions.ask` holds the destructive forms of the commands the allow list opens, so they keep prompting. A short flag is written twice, right after the subcommand and after a space, so a hyphen inside a name (`deck-fix`) doesn't match:
- `Bash(git tag -d*)`, `Bash(git tag * -d*)`, `Bash(git tag *--delete*)`, `Bash(git tag -f*)`, `Bash(git tag * -f*)`, `Bash(git tag *--force*)`;
- `Bash(git switch -f*)`, `Bash(git switch * -f*)`, `Bash(git switch *--force*)`, `Bash(git switch *--discard-changes*)`, `Bash(git switch -C*)`, `Bash(git switch * -C*)`;
- `Bash(git commit *--amend*)`.

These rules cover the forms Claude usually writes, not every way to run git (`git -C . tag -d` slips past), so they guard against slips; they aren't a security boundary.

## Local file

- **The plugin being maintained:** `enabledPlugins` set to `false` for its installed copy, by its `id` from `claude plugin list --json` (`name@marketplace`), so its released skills don't fire while its source is being changed. When that list doesn't include it (a new plugin), write no entry.
- **Conflicts** (step 5), on the user's agreement, by the skill's name as the session lists it:
  - **a prefixed skill** (`<prefix>:<skill>`) alone: `permissions.deny: ["Skill(<prefix>:<skill>)"]`, whatever loads it: an installed plugin, the desktop app, or skills synced from claude.ai. The same skill can load as a plugin skill in one surface and as a synced skill in another, and only the deny rule blocks it in both. The plugin's other skills stay on. Its description stays listed, but loading it is blocked, and the session follows CLAUDE.md's routing. The prefix can differ from the plugin's `id`. Checked in the terminal and the desktop app on 2026-11-19;
  - **a whole plugin,** when all its skills conflict and `claude plugin list --json` lists it: `false` in `enabledPlugins`, by its `id`; otherwise, a deny rule for each of its skills;
  - **a skill with no prefix** (bundled, user or project): `"skillOverrides": {"<name>": "off"}`.

  A `skillOverrides` entry keyed by a prefixed name doesn't reach the skill where it loads as a plugin skill: on a re-run, propose replacing it with the skill's deny rule.
