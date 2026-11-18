---
name: meditate
description: Plans a new skill plugin from an idea: who it serves, its skills and their borders, its principles.
disable-model-invocation: true
---

# Meditate

Takes a plugin from an idea to a plan: the people it serves and the requests they'll make are understood, the skills are split with clear borders, the principles are agreed, and the skills are lined up in the order to build them. From there, sensei's cycle takes over: `prepare` sets up the repository from the plan, and `train` builds each skill from its backlog entry.

The order matters. The requests come before the skills, because a skill is a group of requests that share a flow, not a topic. The borders come before the first skill, because a border moved later means rewriting two descriptions and the skills that point to each other.

Talk to the user in their language. Write the files in English, unless the user explicitly asks for another language for the plugin's documents.

Nothing is written before the user's OK on the plan (step 6).

## 1. Look at the folder

This skill is for a plugin that doesn't exist yet:
- **Empty, or only notes** (a README, a sketch, a `.git` with no plugin): go on. Read the notes first; what they already decide isn't asked again.
- **Already a plugin** (`.claude-plugin/plugin.json` or a `skills/` folder): say so. Point to `/sensei:prepare` to set it up for sensei, and to `train` to change, audit or recreate its skills. Stop.
- **An unrelated folder** (the home folder, another project): ask where the new plugin should live, and work there.

## 2. Purpose and requests

Interview in rounds of up to five numbered questions, each with your recommended answer and a one-line reason, riskiest first. Ask only what can be decided now; a question that depends on an open one waits for a later round. Cover:
- **People and problem:** who will use the plugin, what is hard for them today, and how they cope without it.
- **Requests:** two or three concrete requests for each kind of use, in the users' own words, and what a good result looks like for each. This question has no recommended answer: give only the shape (who asks, in what situation), because these requests are the case every skill is built and tested from, and an invented one tests only what the model already expects. A request the user expects but hasn't seen made counts, marked hypothetical. A kind of use with no request at all can't make a ready entry (`../log/references/backlog.md`, Ready): recommend leaving its skill for later (step 5), with "no case recorded" as its Motivation and any request you suggest under its Open questions, unless the user explicitly decides to build it without one, which goes under its Decisions.
- **Out of scope:** what the plugin deliberately doesn't do.

Look facts up yourself instead of asking: the plugins installed in this session and Anthropic's official ones that already cover part of this ground, and what Claude Code allows. Name the overlaps you find, so the user decides what the plugin adds.

## 3. Skills

With the requests settled, split them into skills, still in rounds with a recommendation each:
- **The split:** requests that follow the same flow go to one skill. Prefer few skills: each one is a description competing for triggers and a scope to keep apart from its siblings.
- **The plugin's name:** short, lowercase with hyphens, since it becomes the prefix of every skill (`<plugin>:<skill>`). Settle it with the split, because a name that promises more than the skills do misleads users.
- **For each skill:** its folder name, its purpose in one line, the requests it takes, and what it leaves to which sibling. The borders are what the descriptions will say, so state them as the requests that fall on each side.
- **Invocation:** whether the model may start the skill, or only the user (for actions with side effects, or flows the user should choose to begin).
- **Standing alone:** whether each skill reads nothing outside its folder, so it can ship on its own, or the skills share references and ship as one plugin. A shared reference belongs to one skill, the one that keeps it up to date.
- **Other components:** an agent, hook, command, script or MCP server only where a request needs it, with the reason.

## 4. Principles

Read `../prepare/references/principles.md` and settle the principles in its rounds.

## 5. Order

First ask which skills make the first version: the smallest set already useful to someone. The rest become ideas for later, since their borders aren't settled yet. Then put the first version's skills in the order to build them:
1. **First:** the skill that answers the plugin's central request, or the one the others depend on (a shared reference, a format they read). It proves the plugin's idea while changing it is still cheap.
2. **Then by dependency and value:** what others need comes first; among the rest, what is useful to users soonest.

## 6. Review the plan

Show everything in one message:
- **Purpose:** the plugin's name, the people, the problem and what's out of scope, in a few sentences, plus the overlaps found.
- **Skills,** in build order: name, purpose, invocation, the requests each takes and what each leaves to its siblings.
- **Principles:** the draft of `docs/principles.md`.
- **Files:** what will be written (step 7). When `docs/principles.md` or BACKLOG.md already exists, show the changes section by section: what's added, what the new text replaces, what stays.

Wait for the OK.

## 7. Write

When a file already exists, merge into it: keep every entry and section the plan doesn't change, so nothing the user or `log` added is lost.

- **`docs/principles.md`:** in the format of `../prepare/references/principles.md`.
- **`BACKLOG.md`:** in the format of `../log/references/backlog.md`, one Idea per skill of the first version, in its skill's area, the areas in build order. Each entry's Motivation is the skill's requests and good results from step 2, its Description the skill's purpose and scope, its Decisions what step 3 settled (the borders, the invocation, the shared references it keeps). Components of the first version that belong to no single skill (a shared agent, a hook, a script) get their own Idea under `Plugin`, with the request that needs it as its Motivation. Ideas for later follow them under `Plugin`, one entry each, not an area of their own. Write it as a file even when the backlog will live in GitHub issues: `prepare` moves the entries there.

Write only these two files: `prepare` and `train` create the skeleton, the CLAUDE.md and the skills from them.

## 8. Finish

Tell the user the next steps:
1. Run `/sensei:prepare` in the folder. It takes the plan from these two files, proposes the rest of the setup and offers the commit that includes them.
2. Build the first skill with `train`, by its backlog entry (e.g. "let's build the <first skill> skill from the backlog").
