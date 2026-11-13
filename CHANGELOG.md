# Changelog

All notable changes to this plugin are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html),
applied to how the skills behave.

## [Unreleased]

### Added

- `log` can keep the backlog in the repository's GitHub issues instead of BACKLOG.md: areas and types become labels, discarding closes the issue as not planned, and a done entry closes with `Closes #N`; a contributor's accepted issue is the entry itself.
- `prepare` offers to create a private GitHub repository when the project has no remote and `gh` is signed in, and moves an existing BACKLOG.md to issues when the backlog goes there.
- `train` and `graduate` follow a written pull request flow: push the branch, open the pull request and merge it with a merge commit, each step on the maintainer's OK; `graduate` stops before tagging when a release pull request is left open, and finishes that release on its next run once it's merged.

### Changed

- `prepare` recommends pull requests and a backlog in GitHub issues when the repository is on GitHub and `gh` is signed in, keeping local merge and BACKLOG.md otherwise; a re-run on a project set up for local merge offers the switch.
- The principles recommend the remote host's CLI when it's installed and signed in, instead of treating it only as an option.

## [0.7.0] - 2026-11-10

A new skill, meditate, plans a plugin from an idea, and prepare builds on its plan and handles already set-up repositories and conflicting skills with more care.

### Added

- `meditate` plans a new plugin from an idea: it interviews the user about who the plugin serves and the requests it must answer, decides the skills and their borders, settles the principles and the build order, and writes `docs/principles.md` and one backlog entry per skill. Run it with `/sensei:meditate`.

### Changed

- `prepare` gives each fact the repository doesn't answer a recommended value in its review (the author from git config, no trailers, `vX.Y.Z` tags, local merge) and recommends size limits of 4000 tokens and 600 characters, with the reason.
- `prepare` re-runs every step on an already set-up repository and proposes only what differs, including both settings files; it keeps the project's subject wording and every fact line as written, proposing only what the current template adds, and stops in a line when nothing differs.
- `prepare` takes a new plugin's name, purpose and skills from a `meditate` plan when there is one, and recommends `meditate` first for a plugin with more than one skill or an open scope.
- `prepare` turns off a conflicting skill inside a plugin on its own, with a deny rule in the local settings, instead of the whole plugin; a skill that only overlaps the maintained plugin's subject is mentioned but not a conflict, and a re-run lists the conflicts still on by name, without recommending them again, so the user can turn off one installed since.
- A skill not built yet starts from concrete requests it must serve, in its users' words: `train` asks for them for a new skill, and backlog entries for planned skills record them as their Motivation.

### Fixed

- `prepare` adds ask rules for the destructive forms of the git commands it allows (deleting or forcing tags, forcing or discarding changes on switch, amending a commit), so they keep prompting, and no longer allows `git archive`. `graduate`'s release zips and `train`'s amend of a wording fix now ask once.

## [0.6.0] - 2026-11-09

Releases publish their GitHub page with the zips attached by default.

### Changed

- `graduate` creates the GitHub release page with the zips attached as part of the release, instead of offering it, and leaves the zips or the page out only when the user asks.

## [0.5.1] - 2026-11-09

The check script's release validation finds the repository root again for plugins in sub-folders.

### Fixed

- The check script's release validation no longer reports a missing README for a plugin in a sub-folder whose README is at the repository root.

## [0.5.0] - 2026-11-08

Principle conflicts are weighed instead of defaulting to an exception, and releases of plugins whose skills don't stand alone ship a zip of the whole plugin.

### Changed

- When a change goes against a principle, `train` weighs changing the proposal, changing the principle or an exception by what the principle protects, and recommends one, instead of defaulting to an exception. Audits, contributor reviews and the reviews of a change weigh their principle conflicts the same way, and a change to the target's principles goes through a plan, a branch and the sweeper's review.
- `graduate` ships one zip of the whole plugin with each release when the skills don't stand alone, instead of none.

## [0.4.0] - 2026-11-08

Reviews and audits report only what changes how a skill runs, and an audit can review architecture too.

### Changed

- A consistency audit that asks about architecture or design also runs the examiner on each skill. A fix picked from an audit uses the finding as its real case, without asking the maintainer for another example.
- Reviews report only what changes how a skill runs on a realistic request. The sweeper, the examiner and the cold reader leave out wording, style, cost that breaks no limit and edge cases no real user would send, and `train` drops any finding below that bar before showing the review or an audit to the maintainer.

## [0.3.0] - 2026-11-08

Skills and agents get English names that keep the dojo analogy, a breaking change: the old commands no longer work.

### Changed

- Skills and agents have English names: hajime → prepare, kanban → log, kata → train, shodan → graduate, shihan → examiner, soji → sweeper. The old names no longer work: the commands are now `/sensei:prepare` and `/sensei:graduate`. In a repository set up with an earlier version, run `/sensei:prepare` again to refresh its CLAUDE.md.

## [0.2.0] - 2026-11-07

hajime sets up existing repositories and sensei's own repository correctly, with a check script permission that works.

### Fixed

- hajime: writes the check script's permission with a wildcard path that matches every installed version, because permission rules don't expand `${CLAUDE_PLUGIN_ROOT}`.
- hajime: adds missing lines to an existing `.gitignore`, turns off a conflicting skill that has no plugin with `skillOverrides`, keeps the maintenance section of sensei's own CLAUDE.md on a re-run, and suggests trying a change from another folder.
- The check script accepts a pointer to a file at the plugin's root, such as `scripts/check.py`.
- hajime: in sensei's own repository, keeps the installed copy on, because it does the maintenance, and suggests `--plugin-dir` only for trying a change.

## [0.1.0] - 2026-11-07

The first version: the whole maintenance cycle, from setup to release.

### Added

- First version of the plugin: hajime (setup), kanban (backlog and changelog), kata (creating and changing skills), shodan (releases), the shihan and soji review agents, and the check script.
