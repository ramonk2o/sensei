# CHANGELOG.md format

`CHANGELOG.md`, at the repository root, records what changed in each version for the people who use the plugin. It follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), with [Semantic Versioning](https://semver.org/spec/v2.0.0.html) applied to how the skills behave. kata writes entries with this file; shodan moves them at release; kanban answers direct requests.

## The file

```markdown
# Changelog

All notable changes to this plugin are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html),
applied to how the skills behave.

## [Unreleased]

## [0.2.0] - 2026-11-04

One sentence on what this version is about.

### Added
- ...
```

- Exactly one `## [Unreleased]`, always first, kept even when empty.
- Versions are `## [X.Y.Z] - YYYY-MM-DD`, newest first.
- Groups, in this order and only when they have entries: Added, Changed, Deprecated, Removed, Fixed, Security. A group appears once per version.
- A released version may open with one sentence on what it is about, written at release.

Sensei's check script enforces the structure. When it fails here, fix the file before going on.

## Entries

- **One change, one or two sentences, from the user's side:** what a skill now does, does differently or no longer does. Don't paste the rule itself: the skill holds it, and copies drift.
- **Prefix** the entry with the skill's name when it affects only one skill (`deck: …`), or with all of them when it affects a few (`ai-prompt and ai-knowledge: …`). Entries about the whole plugin (README, principles, manifests, the skeleton) have no prefix.
- **Every change users could notice gets an entry**, the maintainer's or a contributor's, in the same branch as the change. The commit that releases a version gets none.
- **Wording fixes** that don't change behavior go under Fixed only when a user could have noticed them (a wrong instruction, a broken example); a typo needs no entry.
- Follow the file's existing wording style.

## The version number

Semantic Versioning applied to behavior:
- **MINOR:** a new skill, a new capability, or a change to what a skill does that breaks nothing (a new default, a step added or removed).
- **PATCH:** fixes and wording that don't change what a skill does.
- **MAJOR:** a change that breaks how people use the plugin. Before 1.0, the plugin is experimental: a breaking change bumps MINOR, and the version's summary says so.

The number lives in `.claude-plugin/plugin.json` only, unless the project's CLAUDE.md says otherwise. Users receive an update only when it goes up.

## Conflicts after parallel branches

Two branches that both add to `[Unreleased]` conflict there. Keep both sets of entries, merge them into one list per group, keep the groups in the order above, and make sure no group heading is repeated. Run sensei's check script afterwards.

## Release

At release (shodan):
1. Move every `[Unreleased]` entry under `## [X.Y.Z] - YYYY-MM-DD` (today's date), keeping the groups.
2. Add the summary sentence under the heading.
3. Leave `## [Unreleased]` empty above it.
4. Update the links at the end of the file, if it has them:
   - `[Unreleased]` compares the new tag with HEAD;
   - the new version compares the previous tag with the new one.
