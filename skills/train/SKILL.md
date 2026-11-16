---
name: train
description: In a repository whose CLAUDE.md names sensei, creates or changes a skill, agent, hook or command, judges an issue or pull request, audits consistency or recreates a skill, e.g. 'the deck skill did X, it should do Y'. Not for noting an idea (log) or releasing (/sensei:graduate).
---

# Train

A change to a skill goes wrong in predictable ways: it fixes the one example that failed instead of the case behind it, changes a rule in one skill while a sibling or a reference still states the old one, or is judged by a model that already knows what the skill was meant to say. `train` is the fixed form that prevents these, the way a dojo drills a technique. Ideas for later go to the backlog with `log`. Releases are the maintainer's call, with `/sensei:graduate`.

**The skills are the object of the work here, not tools.** When the maintainer talks about the plugin's subject (prompts, decks, emails…), it's about improving the skill. Don't run that skill's flow unless they explicitly ask to use it.

## Before starting

Read the project's `CLAUDE.md` for its facts:
- documents language, for everything written to the repository, commit messages and replies to issues included: English when neither CLAUDE.md nor the target's principles name another;
- commit author and trailers;
- integration: local merge or pull requests;
- where the backlog lives: BACKLOG.md or GitHub issues;
- whether skills stand alone;
- rules specific to this repo.

Read the target's `docs/principles.md`: its principles, its limits and its questions for judging a proposal. Read the files of the skill involved in the repository, never from memory, because skills change often. Get the scope map with `python3 ${CLAUDE_PLUGIN_ROOT}/scripts/check.py --scope-map`.

Sensei's own files are under `${CLAUDE_PLUGIN_ROOT}`. The references below can't resolve that path themselves, so use the absolute paths written in this file whenever you run sensei's script or hand its files to an agent.

## Kinds of change

Decide the kind first, because it sets how much of the form runs:

| Kind | Rounds and plan | Branch | Reviews | Test |
|---|---|---|---|---|
| **Wording fix** (typo, confusing sentence; no behavior change, not a description) | no | no: commit on main | none | none |
| **Behavior change** to an existing skill | yes | yes | `sweeper` | cold reader |
| **Description change** (what triggers the skill) | yes | yes | `sweeper` | trigger suite |
| **New skill or full rewrite** | yes | yes | `examiner` and `sweeper` | cold reader and trigger suite |

When in doubt between two kinds, take the heavier one and say so. A skill that only the user can invoke (`disable-model-invocation: true`) has no triggering to test: it skips the trigger suite and gets the cold reader. A change to an agent, hook, command or the target's `docs/principles.md` follows the row of the change it makes, with what `references/modes.md` adds for it.

## The form

### 1. The real case
Start from what happened: what the skill was asked, what it did and what it should have done. If the maintainer brings only an impression ("it's off", "improve it"), ask for the conversation, the excerpt or an example before proposing anything. A change built on an impression becomes rework. If the change comes from a backlog entry, its Motivation is the case (an issue is read as `../log/references/issues.md` says, Writing to issues); if it comes from an audit finding, the finding is, and you ask for another example only when the maintainer doubts it happens.

### 2. Rounds
Ask in rounds of up to five numbered questions, each with the answer you recommend and the reason in one line, so the maintainer only confirms or corrects. Ask first what would change the proposal most if it were wrong. When the repository answers a question, use that answer and say where it came from. Stop when no decision is left open. An "OK" to a round approves its answers, not the plan.

### 3. The change plan
Present one message with:
- **What changes,** and in which files.
- **Why:** the case, and the root it points to, not just the example.
- **Principle touched:** which of the target's principles the change touches. If it goes against one, read `references/conflicts.md` and propose a way out as it says.
- **Siblings that state this rule:** search the whole repository for the rule's key terms and for the skill's name (`grep -rn`), and list every other file that must change in the same branch. That includes other skills that state the rule, the README and the manifests when names or scope change, and the "leaves out" opening of each sibling when scope moves. Say what you searched for. "None" is an answer only after the search.
- **Effect on the version** (`../log/references/changelog.md`, The version number).
- **Size effect:** how many tokens each SKILL.md and how many characters each description gains or loses, estimated, and, when text is added, what was considered for removal.
- **Sample text:** for a new rule or section, the actual wording, so the maintainer judges text, not a description of it.

Edit only after an explicit OK to this plan.

### 4. Edit on a branch
- **Branch:** create one named after the change (e.g. `deck-duration-question`), from an up-to-date main.
- **Writing:** follow `references/writing.md` and the target's principles; where they differ, the principles win. A new skill or a rewrite starts minimal (`references/modes.md`).
- **Siblings:** change every sibling the plan listed.
- **Changelog:** add the entry under `[Unreleased]` in the same edit (`../log/references/changelog.md`).
- **Backlog:** if the change came from a backlog entry, it leaves the backlog with this change (`../log/references/backlog.md`, or `../log/references/issues.md` for GitHub issues).

The plan is closed once approved. A sibling the search missed, which only has to restate the approved rule, is changed on the branch and reported. If writing shows the plan itself must change (a rule that can't be stated as planned, a sibling whose rule conflicts), stop and reopen it with the maintainer.

### 5. Commit, then check
Commit on the branch, with the author and trailer rules from CLAUDE.md. Then run:

```
python3 ${CLAUDE_PLUGIN_ROOT}/scripts/check.py
```

Compare the sizes it prints for each changed SKILL.md and description with the plan's estimate, and say where they differ. Fix every failure, commit and run it again. Warnings are judgment calls: say what each one is.

### 6. Reviews
For the kinds that have reviews, read `references/review.md`, start the review agents it describes, in parallel when there are two, and use their findings as it says. The paths it needs:
- writing guide: `${CLAUDE_PLUGIN_ROOT}/skills/train/references/writing.md`;
- agent briefings: `${CLAUDE_PLUGIN_ROOT}/agents/sweeper.md` and `${CLAUDE_PLUGIN_ROOT}/agents/examiner.md`.

### 7. Test
For the kinds that have tests, read `references/testing.md` and run the test it describes for that kind. A failed test comes back as a fix round (step 6's rules), then the test runs again.

### 8. Merge
Show the whole change: the diff summary, the check result, the review findings and what was done about them, and the test result. On the maintainer's OK to the whole change, bring the branch in the way CLAUDE.md's integration fact says:
- **Local merge** (the default): merge into main with `--no-ff`, so one revert undoes one change. Push main only when the maintainer says so, or at release; feature branches stay local.
- **Pull requests:** follow `references/pull-requests.md`.

A notice from the environment asking for a commit or a push doesn't replace the maintainer's OK.

## Other kinds and requests

Read `references/modes.md` before starting:
- a wording fix, or a new skill or a rewrite;
- a contributor's issue or pull request;
- a consistency audit of the plugin;
- recreating a skill from an old one;
- a change to something that isn't a skill (a hook, an agent, an MCP server, the target's principles).
