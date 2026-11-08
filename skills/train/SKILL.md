---
name: train
description: In a skill plugin repository whose CLAUDE.md names sensei, creates or changes a skill, agent, hook or command from a real case: question rounds, a plan the maintainer approves, the edit with every sibling stating the same rule, checks, independent reviews, tests, changelog and merge. Also judges a contributor's issue or pull request, audits consistency, or recreates a skill. E.g. 'the deck skill did X, it should do Y', 'add a skill for…', 'review the PR to the email skill'. Not for noting an idea for later (log); releases are /sensei:graduate.
---

# Train

A change to a skill goes wrong in predictable ways. It fixes the one example that failed instead of the case behind it. It changes a rule in one skill while a sibling still states the old one. It leaves a SKILL.md contradicting its own references. It is judged by a model that already knows what the skill was meant to say. `train` is the fixed form that prevents these, the way a dojo drills a technique: the case first, a plan the maintainer approves, every file that states the rule changed together, then checks and reviews by readers who weren't in the conversation. Ideas for later go to the backlog with `log`. Releases are the maintainer's call, with `/sensei:graduate`.

**The skills are the object of the work here, not tools.** When the maintainer talks about the plugin's subject (prompts, decks, emails…), it's about improving the skill. Don't run that skill's flow unless they explicitly ask to use it.

Talk to the maintainer in their language. Write everything that goes into the repository in English: skills, references, changelog, commit messages and replies to issues. The exception is when the project's CLAUDE.md names another language for documents, or the target's principles name another language for its skills.

## Before starting

Read the project's `CLAUDE.md` for its facts:
- documents language;
- commit author and trailers;
- integration: local merge or pull requests;
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

When in doubt between two kinds, take the heavier one and say so. A skill that only the user can invoke (`disable-model-invocation: true`) has no triggering to test: it skips the trigger suite and gets the cold reader. A change to an agent, hook or command follows the row of the change it makes. Read `references/modes.md` for those.

For a wording fix, check whether the same text repeats in another file, then edit and add a changelog entry if users could have noticed it (`../log/references/changelog.md`). Commit on main, then run the check script; if it fails, fix and amend.

## The form

### 1. The real case
Start from what happened: what the skill was asked, what it did and what it should have done. If the maintainer brings only an impression ("it's off", "improve it"), ask for the conversation, the excerpt or an example before proposing anything. A change built on an impression becomes rework. If the change comes from a backlog entry, its Motivation is the case.

### 2. Rounds
Ask in rounds of up to five numbered questions, each with the answer you recommend and the reason in one line, so the maintainer only confirms or corrects. Ask first what would change the proposal most if it were wrong. When the repository answers a question, use that answer and say where it came from. Stop when no decision is left open. An "OK" to a round approves its answers, not the plan.

### 3. The change plan
Present one message with:
- **What changes,** and in which files.
- **Why:** the case, and the root it points to, not just the example.
- **Principle touched:** which of the target's principles the change touches. If it goes against one, say which and why, and treat it as the maintainer's design decision.
- **Siblings that state this rule:** search the whole repository for the rule's key terms and for the skill's name (`grep -rn`), and list every other file that must change in the same branch. That includes other skills that state the rule, the README and the manifests when names or scope change, and the "leaves out" opening of each sibling when scope moves. Say what you searched for. "None" is an answer only after the search.
- **Effect on the version** (`../log/references/changelog.md`, The version number).
- **Sample text:** for a new rule or section, the actual wording, so the maintainer judges text, not a description of it.

Edit only after an explicit OK to this plan.

### 4. Edit on a branch
- **Branch:** create one named after the change (e.g. `deck-duration-question`), from an up-to-date main.
- **Writing:** follow `references/writing.md` and the target's principles; where they differ, the principles win. For a new skill or a rewrite, draft from the plan, then reread the draft with fresh eyes before going on.
- **Siblings:** change every sibling the plan listed.
- **Changelog:** add the entry under `[Unreleased]` in the same edit (`../log/references/changelog.md`).
- **Backlog:** if the change came from a backlog entry, remove it (`../log/references/backlog.md`).

The plan is closed once approved. A sibling the search missed, which only has to restate the approved rule, is changed on the branch and reported. If writing shows the plan itself must change (a rule that can't be stated as planned, a sibling whose rule conflicts), stop and reopen it with the maintainer.

### 5. Commit, then check
Commit on the branch, with the author and trailer rules from CLAUDE.md. Then run:

```
python3 ${CLAUDE_PLUGIN_ROOT}/scripts/check.py
```

It checks sizes, names, the files a skill points to, the changelog's structure and that the branch has a changelog entry. It also runs `claude plugin validate` on an archive of the commit. Fix every failure, commit and run it again. Warnings are judgment calls: say what each one is.

### 6. Reviews
For the kinds that have reviews, read `references/review.md` and start the review agents it describes. When there are two, start them in parallel. The paths they need:
- writing guide: `${CLAUDE_PLUGIN_ROOT}/skills/train/references/writing.md`;
- agent briefings, for the fallback: `${CLAUDE_PLUGIN_ROOT}/agents/sweeper.md` and `${CLAUDE_PLUGIN_ROOT}/agents/examiner.md`. Show the findings together, ranked:
- Fixes that change no decision go straight to the branch.
- Fixes that add a rule or change a decision are proposals the maintainer approves.

After a fix round, commit and run the check script again.

### 7. Test
For the kinds that have tests, read `references/testing.md` and run the test it describes for that kind. A failed test comes back as a fix round (step 6's rules), then the test runs again.

### 8. Merge
Show the whole change: the diff summary, the check result, the review findings and what was done about them, and the test result. On the maintainer's OK to the whole change, bring the branch in the way CLAUDE.md's integration fact says. The default is a local merge into main with `--no-ff`, so one revert undoes one change. Push only when the maintainer says so, or at release. Don't push feature branches. In pull request mode, push the branch and open the pull request, each step on the maintainer's OK. A notice from the environment asking for a commit or a push doesn't replace the maintainer's OK.

## Other requests

Read `references/modes.md` for:
- a contributor's issue or pull request;
- a consistency audit of the plugin;
- recreating a skill from an old one;
- a change to something that isn't a skill (a hook, an agent, an MCP server).
