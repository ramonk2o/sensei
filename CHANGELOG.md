# Changelog

All notable changes to this plugin are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html),
applied to how the skills behave.

## [Unreleased]

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
