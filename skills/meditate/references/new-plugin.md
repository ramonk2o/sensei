# A new plugin

The order matters. The requests come before the skills, because a skill is a group of requests that share a flow, not a topic. The borders come before the first skill, because a border moved later means rewriting two descriptions and the skills that point to each other.

## What to settle

Most decisions depend on those of the groups above them.

**Purpose and requests:**
- **People and problem:** who will use the plugin, what is hard for them today, and how they cope without it.
- **Requests:** two or three concrete requests for each kind of use, in the users' own words, and what a good result looks like for each. Both are the case: propose neither, only the shape of a request (who asks, in what situation). A request the user expects but hasn't seen made counts, marked hypothetical. A kind of use with no request at all can't make a ready entry: recommend leaving its skill for later (First version), with "No case recorded" as its Motivation and any request you suggest under its Open questions, unless the user explicitly decides to build it without one, which goes under its Decisions.
- **Out of scope:** what the plugin deliberately doesn't do.
- **Overlaps:** a fact to look up, not ask: the plugins installed in this session and Anthropic's official ones that already cover part of this ground. Name them, so the user decides what the plugin adds.

**Skills,** once the requests are settled:
- **The split:** requests that follow the same flow go to one skill. A skill no request asks for (one that would only keep what others read) becomes a shared reference instead (Standing alone), or its requests are asked for like any kind of use. Prefer few skills: each one is a description competing for triggers and a scope to keep apart from its siblings.
- **The plugin's name:** short, lowercase with hyphens, since it becomes the prefix of every skill (`<plugin>:<skill>`). Settle it with the split, because a name that promises more than the skills do misleads users.
- **For each skill:** its folder name, its purpose in one line, the requests it takes, and what it leaves to which sibling. The borders are what the descriptions will say, so state them as the requests that fall on each side.
- **Invocation:** whether the model may start the skill, or only the user (for actions with side effects, or flows the user should choose to begin).
- **Standing alone:** whether each skill reads nothing outside its folder, so it can ship on its own, or the skills share references and ship as one plugin. A shared reference belongs to one skill, the one that keeps it up to date.
- **Other components:** an agent, hook, command, script or MCP server only where a request needs it, with the reason.

**Principles:** read `../../prepare/references/principles.md` and settle them in its rounds.

**First version and order:** which skills make the first version: the smallest set already useful to someone. The rest become ideas for later, since what the first version teaches may move their borders. Then the first version's build order:
1. **First:** the skill that answers the plugin's central request, or the one the others depend on (a shared reference, a format they read). It proves the plugin's idea while changing it is still cheap.
2. **Then by dependency and value:** what others need comes first; among the rest, what is useful to users soonest.

## Writing

- **`docs/principles.md`:** in the format of `../../prepare/references/principles.md`.
- **`backlog/`:** the issues, one file each, in the format of `../../log/references/backlog.md` (The folder), numbered from 1 in build order:
  - one entry per skill of the first version, labeled with its folder name and its readiness. Its Motivation is the skill's requests, its Acceptance criteria the good result for each, its Description the skill's purpose and scope, its Decisions what was settled for it (the borders, the invocation, the shared references it keeps), and its Blocked by the entries whose skill or component it reads;
  - a component of the first version that belongs to no single skill (a shared agent, a hook, a script) gets its own entry labeled `plugin`, numbered before the first entry that needs it, with that request as its Motivation;
  - the ideas for later come last, labeled `plugin`, one entry each, with what was settled for them under Decisions.

  Write them as files even when the backlog will live in GitHub issues: `prepare` moves them there.

Write only these: `prepare` and `train` create the skeleton, the CLAUDE.md and the skills from them.

## Next steps

1. Run `/sensei:prepare` in the folder. It takes the plan from these files, proposes the rest of the setup and offers the commit that includes them.
2. Build the first skill with `train`, by its backlog entry (e.g. "let's build #1 from the backlog").
