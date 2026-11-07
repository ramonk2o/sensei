---
name: hajime
description: Sets up a Claude Code skill plugin repository, new or existing, for maintenance with sensei. It creates what's missing of the skeleton and the principles, writes the CLAUDE.md, turns off conflicting plugins and the installed copy of the plugin itself for this project, adds permissions, and moves an old process document's rules into place. Safe to re-run to refresh. Not for changing skills (kata) or releasing (shodan). Run only when the user invokes it.
disable-model-invocation: true
---

# Hajime

Prepares a repository so the plugin it holds can be maintained with sensei's skills: `kata` (changing skills), `kanban` (backlog and changelog) and `shodan` (releases). The cycle lives in those skills. This setup only puts the project's facts and its enforced settings in place, so updating sensei updates every project.

Talk to the user in their language. Write every file in English, unless the user explicitly asks for another language for the project's documents. Then record it in CLAUDE.md.

Nothing is written before the user's OK. When principles are missing, settle them first, in step 2's rounds, because the CLAUDE.md draws facts from them. Then collect the proposals of steps 2 to 6, show them together in step 7, and apply what's approved in step 8.

## 1. Look

Read the repository before proposing anything:
- **Manifests:** `.claude-plugin/plugin.json`, `marketplace.json`.
- **Skills:** `skills/*/SKILL.md`, their `references/`, and any agents, hooks or commands.
- **Documents:** README, LICENSE, CHANGELOG, BACKLOG, `docs/principles.md`, CLAUDE.md.
- **Old process documents:** a pasted project prompt kept in the repo, CONTRIBUTING, or a maintenance doc.
- **Git:** whether it's a repository, its tags, its log (authors, trailers), its remote.

Then run `python3 ${CLAUDE_PLUGIN_ROOT}/scripts/check.py --no-validate` and `claude plugin validate .` to see where it stands.

If the folder isn't a plugin and the user wants one, it's a new plugin: propose its name, its first skill's purpose in one sentence, and the skeleton. If it's an existing plugin, everything below adapts to what's there.

## 2. Skeleton and principles

Propose only what's missing:
- `.claude-plugin/plugin.json` (name, version `0.1.0`, description, author, license);
- `.claude-plugin/marketplace.json` with an entry whose `source` is `./`, so the plugin installs from its own repository;
- README (what it is, the skills, install, how it's built, contributing, license);
- LICENSE (MIT unless the user says otherwise);
- CHANGELOG.md and BACKLOG.md, in the formats of `../kanban/references/changelog.md` and `../kanban/references/backlog.md`;
- `docs/principles.md`.

**Principles,** when missing, are settled with the user in rounds of up to five numbered questions, each with a recommended answer and a one-line reason:
- what every skill does before writing;
- how results are checked;
- whether each skill stands alone (reads nothing outside its folder);
- the size limits;
- the language rule.

Run these rounds now, before drafting anything else. Write the principles as checkable statements, and end the file with the questions for judging a proposal. Put the limits agreed in the rounds in a machine-readable block, which the check script reads:

```
<!-- sensei:limits
skill_tokens: <agreed limit for a SKILL.md, in tokens>
description_chars: <agreed limit for a description, in characters>
-->
```

When principles exist, propose only that block, from the limits they already state.

**Git:** if it isn't a repository, propose `git init` and a `.gitignore` with OS files (`.DS_Store` and the like), `.claude/settings.local.json` and `evals/**/results/`.

## 3. CLAUDE.md

Read `references/claude-md.md` and write the draft from its template. The fixed parts are the routing to sensei's skills and the rule that the skills are the object of the work. The facts are discovered first and asked only when the repository doesn't answer.

## 4. Settings

Rules that Claude Code can enforce go in settings, not prose.
- **`.claude/settings.json`,** shared with everyone who clones the repository:
  - `attribution`: `{"commit": "", "pr": ""}` when the project allows no trailers;
  - permissions under `permissions.allow` for `python3 ${CLAUDE_PLUGIN_ROOT}/scripts/check.py`, written as a wildcard pattern that survives sensei updates, because the plugin's path changes with each version (check the current permission rule syntax in the Claude Code docs), and for `claude plugin validate:*`, `claude plugin eval:*`, and the local git commands the cycle uses (status, diff, log, show, add, commit, switch, merge, branch --list, tag, merge-base, rev-parse, archive).
  - Never add push, reset, deleting branches or files, or publishing. Those keep asking.
  - If the file exists, merge: keep every entry and add only what's missing.
- **`.claude/settings.local.json`,** personal to this machine and ignored by git:
  - `enabledPlugins` set to `false` for the installed copy of the plugin being maintained (its id from `claude plugin list`, as `name@marketplace`), so its released skills don't fire while its source is being changed. The exception is sensei's own repository: there the installed copy is the tool doing the maintenance, so it stays on;
  - the same for each conflicting plugin the user agrees to turn off (step 5).
  - Turning a plugin off in the shared file would turn it off for every contributor, so it goes here.

**Git identity:** when the project fixes a commit author and the environment has none, propose a repo-local `git config user.name` and `user.email`.

## 5. Conflicts

Look at the skills available in this session. List those whose descriptions claim the same work as sensei's skills or as the maintained plugin's own:
- writing or improving skills;
- managing a BACKLOG or CHANGELOG;
- releasing versions;
- reviewing pull requests or changes.

Judge them by what they say they do, never by a fixed list of names. For each, propose turning its plugin off for this project (step 4, local file), or leaving it and relying on the routing in CLAUDE.md. Say which you recommend and why.

## 6. Migration and orphans

- **Old process document:** move each rule that still holds:
  - a project fact goes to CLAUDE.md;
  - a principle goes to `docs/principles.md`, with the user's OK;
  - a cycle step is left to sensei's skills, and you say which one owns it;
  - a personal preference is pointed to the user-level CLAUDE.md.

  Show where each rule goes. Then propose removing the document, or keeping it as history if the user prefers.
- **Documents that overlap** BACKLOG or CHANGELOG (TODO.md, ROADMAP.md, HISTORY.md): point them out. Aligning them is kanban's job.
- **Broken references** in CLAUDE.md or the README: point them out.

## 7. Review

Show everything in one message:
- the skeleton and principles (or their rounds, first);
- the CLAUDE.md draft or its changes;
- both settings files;
- the conflicts;
- the migration.

Wait for the OK. The user may approve parts.

## 8. Apply

Apply what was approved, in this order:
1. git;
2. skeleton and principles;
3. CLAUDE.md;
4. settings;
5. removals.

Then check the working tree as it now is: `python3 ${CLAUDE_PLUGIN_ROOT}/scripts/check.py --no-validate` and `claude plugin validate .`. The script's own validate checks the last commit, which doesn't hold the setup yet. Failures aren't fixed here:
- in existing skills (a description over its limit, a broken reference): offer to record each in BACKLOG.md as Debt, or to fix it with kata;
- a changelog in another format: offer the alignment with kanban.

Offer a commit with the setup. Don't commit without the OK.

Tell the user that a new session in this folder picks up the settings. To try a change before releasing it, they can start a separate session with `claude --plugin-dir <this repository>`, which loads the working copy in place of the installed one. Never use it for the session doing the maintenance of sensei itself: a broken change would break the tool making it.

## Re-running

On a repository already set up, hajime refreshes rather than rebuilds:
- the "Maintenance with sensei" section of CLAUDE.md;
- the conflict list;
- the permissions.

It proposes fact changes only where the repository now says something different.
