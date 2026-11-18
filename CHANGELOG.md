# Changelog

All notable changes to this plugin are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html),
applied to how the skills behave.

## [Unreleased]

### Added

- `log`'s backlog format defines when an entry is ready: it has its case (or the maintainer's explicit decision to go without one), the expected behavior, acceptance criteria and no open questions; any other entry needs clarification. `train` asks for what keeps an entry from being ready before its plan, and `meditate` leaves for later a skill whose entry couldn't be ready.
- `log` labels each backlog entry `ready` or `needs-clarification` by that test and tells the maintainer what an unready entry lacks. Entries gain three fields: acceptance criteria, the entries they're blocked by (GitHub's own blocked-by relationship when it's available) and a model tier (light, medium or strong), which one reference maps to current models.
- Asked "what's next?", `log` shows the ready entries in the order to take them (blockers first, then bugs, ideas and debt, oldest first) with their tier and open blockers, then the entries that need clarification and what each lacks, and suggests the one to take next.
- `meditate` also plans a change to an existing plugin, not only a new one: it reads the project's facts, principles, the skills involved and the backlog entries about the change, settles its case and every decision it needs, and writes the issues where the project keeps its backlog, rewriting in place an entry the change came from. The model can now start it, so asking to plan a plugin or to think a change through before building it is enough.

### Changed

- `meditate` keeps an explicit tree of decisions: each round asks the decisions whose prerequisites are settled, up to five, each worded as a recommendation that "yes" accepts, and facts about the repository or the environment are looked up instead of asked. It then splits what was settled into issues that `train` builds one run and one pull request at a time, usable on their own, preparatory work first and expand–migrate–contract for a change across the whole plugin, each with acceptance criteria, blockers and a model tier, and one OK covers the understanding and the split. A new plugin's plan is written as numbered `backlog/` files in build order instead of BACKLOG.md.
- Sensei prefers a real case instead of requiring one. When the maintainer has only an account of what happened or a request they expect, `train`, `log` and `meditate` accept it as a hypothetical case and record it as such, so the first real case can overturn it; going without any case is the maintainer's explicit decision. An impression still only leads to asking for the case, and `train` asks for a missing case without proposing one, not even as an example request.
- Outside GitHub issues, `log` keeps the backlog in a `backlog/` folder instead of one BACKLOG.md: one numbered file per entry, with its title, type, labels and status in frontmatter, mirroring an issue, so entries refer to each other by number the same way in both. A discarded entry keeps its file with `status: discarded`. An existing BACKLOG.md is still followed as it is until it's moved. `meditate` puts the good result for each request of a new skill under the entry's acceptance criteria.

## [0.10.0] - 2026-11-18

Train settles what a skill's model really has when it runs, and its light paths stay light: wording fixes reach main in pull request mode, and agent descriptions are held to the skills' limit.

### Changed

- A wording fix in `train` starts from an up-to-date main. In a project that integrates through pull requests, it goes on a short branch and pull request, and the one OK to the reported fix covers the push, the pull request and the merge. A typo in a description is now a wording fix.
- The `sweeper`'s and `examiner`'s descriptions say only what each agent does and when it's used (149 and 192 characters, down from 528 and 613); what each review checks stays in its body. The check script now holds agent descriptions to the same `description_chars` limit as skills, and `train`'s writing guide states the rule for the agents of maintained plugins.
- `train` settles once what the model running a skill has: the skill's SKILL.md and what its text sends the model to read, with a project's CLAUDE.md counting only for the facts the skill names there, never the plugin repository's own. The one-source test uses it, so a cut no longer leans on a CLAUDE.md the skill's users don't have, and the cold reader gets it for the case's path, so a change to a reference alone is tested with the SKILL.md that routes to it and the project facts it reads, nothing more. The `sweeper` also reads the SKILL.md of every skill whose references changed.

## [0.9.0] - 2026-11-16

Skills get leaner: train writes and checks text against sentence-level tests and proposes cuts from the examiner, and every SKILL.md is shorter with the same behavior.

### Added

- The check script prints each changed SKILL.md's and description's size and growth against main, and `train`'s change plan states the size effect and, when text is added, what was considered for removal.
- The `examiner` lists, apart from its findings, the sentences that fail the writing guide's no-op or one-source test, and `train` shows them as cuts the maintainer picks. Every consistency audit runs the `examiner` on each skill as a pruning pass; the cuts picked for a skill are their own case and plan, and go through a branch, the sweeper's review and a cold reader that compares the cut text with main, putting back a cut that changed the answer.

### Changed

- `train` writes and changes skill text against six tests run on each sentence (no-op, branch, one source, positive, one word, why) instead of general advice to cut. A reason is kept where the model must generalize a judgment and dropped from mechanical steps, and the `examiner` asks for reasons accordingly.
- Descriptions are shorter: what the skill does, one trigger per kind of request and the sibling that takes neighboring requests, without the flow; a skill only the user can invoke gets one line for the menu. `prepare` now recommends a 300-character limit instead of 600, and sensei's own five descriptions follow the rule.
- `train`'s SKILL.md is over a fifth shorter, with the same behavior: the steps for a wording fix and for a new skill or a rewrite moved to its `modes.md` reference, the ways out of a conflict with a principle to a new `conflicts.md`, and text that restated its references or the project's CLAUDE.md was removed.
- `prepare`'s SKILL.md is about a fifth shorter, with the same behavior: what differs when the plugin is sensei itself moved to a new `sensei-itself.md` reference, the exact settings rules (attribution, what never to allow, the local file's entries) to `settings.md`, and each step's behavior on a re-run is stated once, in that step.
- `meditate`'s and `graduate`'s SKILL.md are shorter, with the same behavior: text that restated their references (`backlog.md`, `principles.md`, `pull-requests.md`, the check script's output) or another step was removed, and `graduate` states once how it finishes a release that stopped before tagging and when the zips or the release page are left out.
- `train` builds a new skill or a rewrite minimal first: the first draft holds only the flow, the gates before costly or irreversible actions, what the model can't know and a step that checks the result, and a cold reader run on each request from the plan decides what else earns text. After a failure, it sharpens or replaces the sentence that is there before adding one.

## [0.8.0] - 2026-11-13

Sensei works with GitHub: pull requests and issues for the backlog become the recommended flow, and prepare and graduate handle new plugins, general code-review skills and open pull requests with more care.

### Added

- `log` can keep the backlog in the repository's GitHub issues instead of BACKLOG.md: areas and types become labels, discarding closes the issue as not planned, and a done entry closes with `Closes #N`; a contributor's accepted issue is the entry itself.
- `prepare` offers to create a private GitHub repository when the project has no remote and `gh` is signed in, and moves an existing BACKLOG.md to issues when the backlog goes there.
- `train` and `graduate` follow a written pull request flow: push the branch, open the pull request and merge it with a merge commit, each step on the maintainer's OK; `graduate` stops before tagging when a release pull request is left open, and finishes that release on its next run once it's merged.

### Changed

- `prepare` recommends pull requests and a backlog in GitHub issues when the repository is on GitHub and `gh` is signed in, keeping local merge and BACKLOG.md otherwise; a re-run on a project set up for local merge offers the switch.
- `prepare` recommends that skills don't stand alone when the plugin has no skills yet, writes no `enabledPlugins` entry (and no empty local settings file) for a plugin that isn't installed, and no longer counts general code-review skills as conflicts.
- `graduate`, in pull request mode, lists the open pull requests: it asks whether to wait for them before proposing a release, and names them when there is nothing to release.
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
