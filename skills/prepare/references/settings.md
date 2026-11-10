# Permissions in the settings files

The rules `prepare` writes under `permissions`: allow and ask in the shared `.claude/settings.json`, deny in the local one. Claude Code checks deny rules first, then ask, then allow, and the first match decides, so an ask rule prompts even when a broader allow rule also matches.

## Allow

`permissions.allow` lets the commands the cycle runs on every change go through without a prompt:
- sensei's check script. Permission rules don't expand `${CLAUDE_PLUGIN_ROOT}`, and the installed path changes with each version, so write it with wildcards: `Bash(python3 */plugins/cache/*/sensei/*/scripts/check.py*)`. When the plugin being maintained is sensei itself, add `Bash(python3 scripts/check.py*)` for the working copy's script;
- `Bash(claude plugin validate*)` and `Bash(claude plugin eval*)`;
- the local git commands the cycle uses: `Bash(git status*)`, `Bash(git diff*)`, `Bash(git log*)`, `Bash(git show*)`, `Bash(git add*)`, `Bash(git commit*)`, `Bash(git switch*)`, `Bash(git merge*)`, `Bash(git branch --list*)`, `Bash(git tag*)`, `Bash(git merge-base*)`, `Bash(git rev-parse*)`.

`git archive` stays out: `graduate` runs it only to write the release zips, with `-o`, which can overwrite any file, so it asks. The check script runs its own archive without going through these rules. On a re-run, propose removing a `Bash(git archive*)` rule an earlier version of sensei added.

## Ask

`permissions.ask` holds the destructive forms of the commands the allow list opens, so they keep prompting. A short flag is written twice, right after the subcommand and after a space, so a hyphen inside a name (`deck-fix`) doesn't match:
- `Bash(git tag -d*)`, `Bash(git tag * -d*)`, `Bash(git tag *--delete*)`, `Bash(git tag -f*)`, `Bash(git tag * -f*)`, `Bash(git tag *--force*)`;
- `Bash(git switch -f*)`, `Bash(git switch * -f*)`, `Bash(git switch *--force*)`, `Bash(git switch *--discard-changes*)`, `Bash(git switch -C*)`, `Bash(git switch * -C*)`;
- `Bash(git commit *--amend*)`.

These rules cover the forms Claude usually writes, not every way to run git (`git -C . tag -d` slips past), so they guard against slips; they aren't a security boundary.

## Local file

`.claude/settings.local.json` holds what turns things off for this machine only (`SKILL.md`, steps 4 and 5). A plugin's single skill is turned off with `permissions.deny: ["Skill(<plugin>:<skill>)"]`: its description stays listed, but loading it is blocked, and the session follows CLAUDE.md's routing. `skillOverrides` doesn't reach plugin skills. Checked with the CLI on 2026-11-10; Claude Code's docs don't state it.
