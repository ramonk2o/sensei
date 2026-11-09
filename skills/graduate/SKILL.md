---
name: graduate
description: Releases a version of a Claude Code skill plugin maintained with sensei. It proposes the number from the changelog's unreleased entries, runs the release checks, then moves the entries, bumps plugin.json, tags, pushes and builds the release zips: one per skill when the skills stand alone, one of the whole plugin otherwise. Not for changing skills (train) or editing the changelog (log). Run only when the user invokes it.
disable-model-invocation: true
---

# Graduate

Releases what has reached main since the last version. People who installed the plugin get an update only when the version number in `plugin.json` goes up, so a release is what turns merged changes into something users receive.

Talk to the user in their language. Write the changelog and commit messages in the project's documents language (English unless its CLAUDE.md says otherwise).

## 1. Read the state

- Read the project's CLAUDE.md for its tag format, its integration (local merge or pull requests), its commit rules and whether skills stand alone.
- Switch to main and make sure it's clean and up to date with its remote, if it has one.
- Read `CHANGELOG.md` and `../log/references/changelog.md`.
- If `[Unreleased]` is empty, say there is nothing to release and stop.

## 2. Check

Run `python3 ${CLAUDE_PLUGIN_ROOT}/scripts/check.py --release`. Besides the usual checks, it requires a non-empty `[Unreleased]` and runs `claude plugin validate --profile directory`, which catches what the plugin directory would refuse. Fix failures through `train`, or for a changelog structure problem through `log`'s format, before going on. Don't release over a failure.

## 3. Propose

Show in one message:
- **The number,** from the entries, by the rules in the changelog reference's "The version number", with the reason ("a new capability in deck: MINOR").
- **The date:** today.
- **The summary sentence** for the version's heading.
- **The entries** that go into it.
- **What will happen:** the commit, the tag, the push, and the release page with the zips attached.

The user's OK to the number and the summary covers the whole release flow below, the release page included. If they asked for no zips or no release page, when invoking or here, leave that part out. Anything else they change goes back to this step.

## 4. Release

1. **Commit on main**, one commit:
   - move the entries under `## [X.Y.Z] - YYYY-MM-DD` with the summary, leaving `[Unreleased]` empty above it (changelog reference, Release);
   - bump `version` in `.claude-plugin/plugin.json`.

   Message: `Release X.Y.Z`. In pull request mode, make the commit on a `release-X.Y.Z` branch and bring it in the way the project integrates. Then go on from the merged commit.
2. **Tag** it in the project's format:
   - `vX.Y.Z` by default, as an annotated tag;
   - `{name}--v{version}`: create it with `claude plugin tag --dry-run` and then `claude plugin tag`, which also checks that the manifests agree.
3. **Push** main and the tag (`git push`, `git push origin <tag>`). The push asks for permission. If it's refused, stop and give the user the commands.
4. **Confirm** with `git log origin/main -1` and `git ls-remote --tags origin <tag>`, and give the hash.

## 5. Zips and the release page

The release page carries the zips by default. Leave the zips out only when the user explicitly asked for that; if they asked for no release page, skip this step.

Build the zips from the tagged commit, in a temporary folder outside the repository:
- **When the skills stand alone** (CLAUDE.md says so): one zip per skill, named `<skill>.zip`, with the skill's folder at the root of the zip:
  ```
  git archive --format=zip --prefix=<skill>/ -o <tmp>/<skill>.zip <tag>:skills/<skill>
  ```
  Check that each zip lists `<skill>/SKILL.md`.
- **When they don't:** one zip of the whole plugin, named after `name` in `.claude-plugin/plugin.json`, with the plugin's files at the root of the zip:
  ```
  git archive --format=zip -o <tmp>/<plugin>.zip <tag>
  ```
  It holds every tracked file except paths marked `export-ignore` in `.gitattributes`. Check that it lists `.claude-plugin/plugin.json` and every `skills/<skill>/SKILL.md`.

If the session can publish a release on GitHub (`gh` is available and signed in), create it with the version's changelog entries as notes and the zips attached. If a release for the tag already exists, attach the zips to it with `gh release upload <tag> <zips>` instead. Otherwise, deliver the notes ready to paste, the command, and the zips' paths.

## 6. Close

Say what was released, the version, the tag, the hash, and what's still for the user to do (publishing the release page, if it wasn't done). Remind them that users who installed the plugin get the update when Claude Code next refreshes the marketplace, or when they update by hand.
