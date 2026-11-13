---
name: meditate
description: Plans a new Claude Code skill plugin from an idea, before any skill exists. It interviews the user about who the plugin serves and the requests it must answer, decides with them which skills it has and where each one's scope ends, settles its principles and picks the first skill, then writes docs/principles.md and BACKLOG.md for prepare and train to pick up. Not for a plugin that already exists (prepare sets it up, train changes or audits it). Run only when the user invokes it.
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
- **Requests:** two or three concrete requests for each kind of use, in the users' own words, and what a good result looks like for each. This question has no recommended answer: give the shape (who asks, in what situation) and ask the user for the wording. They are the case every skill is built and tested from, since no skill has been used yet, and an invented case would test only what the model already expects. When the user has none yet for a kind of use, recommend leaving the skill that would serve it for later (step 5), with "no case recorded" as its Motivation; requests you suggest go to its Open questions, never to its Motivation.
- **Out of scope:** what the plugin deliberately doesn't do.

Look facts up yourself instead of asking: the plugins installed in this session and Anthropic's official ones that already cover part of this ground, and what Claude Code allows (skills, agents, hooks, commands, MCP servers). Name the overlaps you find, so the user decides what the plugin adds.

## 3. Skills

With the requests settled, split them into skills, still in rounds with a recommendation each:
- **The split:** requests that follow the same flow go to one skill. Prefer few skills: each one is a description competing for triggers and a scope to keep apart from its siblings.
- **The plugin's name:** short, lowercase with hyphens, since it becomes the prefix of every skill (`<plugin>:<skill>`). Settle it with the split, because a name that promises more than the skills do misleads users.
- **For each skill:** its folder name, its purpose in one line, the requests it takes, and what it leaves to which sibling. The borders are what the descriptions will say, so state them as the requests that fall on each side.
- **Invocation:** whether the model may start the skill, or only the user (for actions with side effects, or flows the user should choose to begin).
- **Standing alone:** whether each skill reads nothing outside its folder, so it can ship on its own, or the skills share references and ship as one plugin. A shared reference belongs to one skill, the one that keeps it up to date, and that skill is built first.
- **Other components:** an agent, hook, command, script or MCP server only where a request needs it, with the reason.

## 4. Principles

Read `../prepare/references/principles.md` and settle the principles in its rounds. Step 3 already answers whether skills stand alone; use that answer and say so.

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

Wait for the OK; the user may change any part.

## 7. Write

When a file already exists, merge into it: keep every entry and section the plan doesn't change, so nothing the user or `log` added is lost.

- **`docs/principles.md`:** in the format of `../prepare/references/principles.md`. Its title carries the plugin's name, and its opening states the purpose, the people and what's out of scope from step 2.
- **`BACKLOG.md`:** in the format of `../log/references/backlog.md`, one Idea per skill, each in an area named after the skill's folder, the areas in build order. Each entry's Motivation is that skill's requests and good results from step 2. Its Description is the skill's purpose and scope, its Decisions what step 3 settled (the borders, the invocation, the shared references it keeps), its Open questions what is still undecided. Components of the first version that belong to no single skill (a shared agent, a hook, a script) get their own Idea in a `Plugin` area, after the skills, each with the request that needs it as its Motivation. Ideas for later follow them in the same area, each as one entry, never an area of its own. It's a file even for a project that will keep its backlog in GitHub issues: the repository may not exist yet, and `prepare` moves the entries there.

Don't create the skeleton, the CLAUDE.md or the skills: `prepare` and `train` own those, and they read these two files.

## 8. Finish

Tell the user the next steps:
1. Run `/sensei:prepare` in the folder. It takes the name, purpose and skills from the plan, skips the principles rounds, proposes the rest of the setup, and offers the commit that includes these files.
2. Build the first skill with `train`, by its backlog entry (e.g. "let's build the <first skill> skill from the backlog").
