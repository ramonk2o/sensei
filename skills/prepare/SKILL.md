---
name: prepare
description: Sets up a Claude Code skill plugin repository, new or existing, for maintenance with sensei. It creates what's missing of the skeleton and the principles, writes the CLAUDE.md, turns off conflicting plugins and skills and the installed copy of the plugin itself for this project (except for sensei itself), adds permissions, and moves an old process document's rules into place. Safe to re-run to refresh. Not for changing skills (train) or releasing (graduate). Run only when the user invokes it.
disable-model-invocation: true
---

# Prepare

Prepares a repository so the plugin it holds can be maintained with sensei's skills: `train` (changing skills), `log` (backlog and changelog) and `graduate` (releases). The cycle lives in those skills. This setup only puts the project's facts and its enforced settings in place, so updating sensei updates every project.

Talk to the user in their language. Write every file in English, unless the user explicitly asks for another language for the project's documents. Then record it in CLAUDE.md.

Nothing is written before the user's OK. When principles are missing, settle them first, in step 2's rounds, because the CLAUDE.md draws facts from them. Then collect the proposals of steps 2 to 6, show them together in step 7, and apply what's approved in step 8.

## 1. Look

Read the repository before proposing anything:
- **Manifests:** `.claude-plugin/plugin.json`, `marketplace.json`.
- **Skills:** `skills/*/SKILL.md`, their `references/`, and any agents, hooks or commands.
- **Documents:** README, LICENSE, CHANGELOG, BACKLOG, `docs/principles.md`, CLAUDE.md.
- **Old process documents:** a pasted project prompt kept in the repo, CONTRIBUTING, or a maintenance doc.
- **Git:** whether it's a repository, its tags, its git log (authors, trailers), its remote.

Then run `python3 ${CLAUDE_PLUGIN_ROOT}/scripts/check.py --no-validate` and `claude plugin validate .` to see where it stands.

If the folder isn't a plugin and the user wants one, it's a new plugin:
- When `docs/principles.md` and BACKLOG.md hold a plan from `/sensei:meditate`, take the name (the principles' title), the purpose (its opening) and the skills (the backlog's areas other than `Plugin`) from them, without asking again.
- Without a plan, recommend running `/sensei:meditate` first when the plugin will have more than one skill or its scope is still open. When the user can state its single skill's purpose in one sentence, or declines `meditate`, propose its name, its first skill's purpose in one sentence and the skeleton. If they agree, stop here and tell them to run `/sensei:meditate`, then `/sensei:prepare` again.

If it's an existing plugin, everything below adapts to what's there.

## 2. Skeleton and principles

Propose only what's missing:
- `.claude-plugin/plugin.json` (name, version `0.1.0`, description, author, license);
- `.claude-plugin/marketplace.json` with an entry whose `source` is `./`, so the plugin installs from its own repository;
- README (what it is, the skills, install, how it's built, contributing, license), drawn from the principles' opening and the backlog's entries when a plan exists, listing the skills as planned. Don't create the skills' folders: each one is built with `train`;
- LICENSE (MIT unless the user says otherwise);
- CHANGELOG.md and BACKLOG.md, in the formats of `../log/references/changelog.md` and `../log/references/backlog.md`;
- `docs/principles.md`.

**Principles,** when `docs/principles.md` is missing, are settled with the user in rounds: read `references/principles.md` and run them now, before drafting anything else. When the file exists, propose only its limits block if it lacks one, from the limits it already states.

**Git:** if it isn't a repository, propose `git init` and a `.gitignore` with OS files (`.DS_Store` and the like), `.claude/settings.local.json` and `evals/**/results/`. If it is, propose only the lines its `.gitignore` is missing.

## 3. CLAUDE.md

Read `references/claude-md.md` and write the draft from its template. The fixed parts are the routing to sensei's skills and the rule that the skills are the object of the work. The facts are discovered first and asked only when the repository doesn't answer.

## 4. Settings

Rules that Claude Code can enforce go in settings, not prose.
- **`.claude/settings.json`,** shared with everyone who clones the repository:
  - `attribution`: `{"commit": "", "pr": ""}` when the project allows no trailers;
  - permissions under `permissions.allow` and `permissions.ask`: read `references/settings.md` for the exact rules.
  - Never add push, reset, deleting branches or files, or publishing. Those keep asking.
  - If the file exists, merge: keep every entry and add only what's missing, except the removals `references/settings.md` names.
- **`.claude/settings.local.json`,** personal to this machine and ignored by git:
  - `enabledPlugins` set to `false` for the installed copy of the plugin being maintained (its `id` from `claude plugin list --json`, as `name@marketplace`), so its released skills don't fire while its source is being changed. When the plugin being maintained is sensei itself (the `name` in its `plugin.json`), write no entry for it, and remove one an earlier run left: there the installed copy is the tool doing the maintenance;
  - the same for each conflicting plugin the user agrees to turn off, and `skillOverrides` for each conflicting skill that has no plugin (step 5).
  - Turning a plugin off in the shared file would turn it off for every contributor, so it goes here.

**Git identity:** when the project fixes a commit author and the environment has none, propose a repo-local `git config user.name` and `user.email`.

## 5. Conflicts

Look at the skills available in this session. List those whose descriptions claim the same work as sensei's skills or as the maintained plugin's own:
- writing or improving skills;
- managing a BACKLOG or CHANGELOG;
- releasing versions;
- reviewing pull requests or changes.

Judge them by what they say they do, never by a fixed list of names. For each, propose turning it off for this project in the local file (step 4), or leaving it and relying on the routing in CLAUDE.md:
- a plugin's skill (`plugin:skill`): its whole plugin, by the `id` that `claude plugin list --json` gives (`name@marketplace`); the prefix is the manifest's name and can differ from that id;
- a skill with no plugin prefix (bundled, user or project): that skill alone, with `"skillOverrides": {"<name>": "off"}`.

Say which you recommend and why.

## 6. Migration and orphans

- **Old process document:** move each rule that still holds:
  - a project fact goes to CLAUDE.md;
  - a principle goes to `docs/principles.md`, with the user's OK;
  - a cycle step is left to sensei's skills, and you say which one owns it;
  - a personal preference is pointed to the user-level CLAUDE.md.

  Show where each rule goes. Then propose removing the document, or keeping it as history if the user prefers.
- **Documents that overlap** BACKLOG or CHANGELOG (TODO.md, ROADMAP.md, HISTORY.md): point them out. Aligning them is `log`'s job.
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
- in existing skills (a description over its limit, a broken reference): offer to record each in BACKLOG.md as Debt, or to fix it with `train`;
- a changelog in another format: offer the alignment with `log`.

Offer a commit with the setup. Don't commit without the OK.

Tell the user that a new session in this folder picks up the settings. To try a change before releasing it, they can start a separate session from another folder, so this repository's CLAUDE.md doesn't steer it: `claude --plugin-dir <this repository>`. For that session it replaces the installed copy, and needs no other setting. When the plugin being maintained is sensei itself, never use it for the session doing the maintenance: a broken change would break the tool making it.

## Re-running

A repository is already set up when its CLAUDE.md has a "Maintenance with sensei" section, whichever skills it routes to (an earlier sensei used other names). Then every step runs, but proposes only what differs from what's there:
- the principles rounds run only if `docs/principles.md` is missing;
- CLAUDE.md is refreshed as `references/claude-md.md` says (sensei's own repository keeps its section as it is);
- both settings files are checked in full, including the removals `references/settings.md` names;
- the conflicts are listed again from what is installed now;
- migration runs only for a process document that appeared since.

Step 7 shows only the differences. When there are none, say so in a line and stop.
