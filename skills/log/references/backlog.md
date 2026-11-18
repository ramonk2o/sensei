# Backlog format

The backlog holds what may come: ideas, bugs and debt left for later. Each entry starts from the case that produced it, because a change judged without its case gets built wrong. Done work leaves the backlog. It lives on in the changelog and in git history.

The entries live in GitHub issues when the project's CLAUDE.md gives them as its Backlog fact (`issues.md`), and otherwise in a `backlog/` folder at the repository root, one file per entry, mirroring an issue.

## An entry

- **Number:** an issue's number, or the file's (The folder). Entries refer to each other as `#<number>`.
- **Type:**
  - `idea`: new behavior.
  - `bug`: a skill does something wrong; the Description says how to reproduce it.
  - `debt`: a change that keeps behavior, such as trimming, reorganizing or aligning skills.
- **Area:** the skill's folder name, or `plugin` for whatever spans the plugin (README, principles, manifests, tooling).
- **Readiness:** `ready` or `needs-clarification` (Ready).
- **Body:**

```markdown
**Motivation:** <the case: what was asked, what the skill did, what it should have done; or a review finding: the text and the request it breaks>

**Description:** <the change wanted, from the user's side>

**Acceptance criteria:**
- <how to tell the change works>

**Decisions:**
- <a choice already made>

**Blocked by:** #<number>, #<number>

**Model:** <light | medium | strong>

**Open questions:**
- <what is still undecided>
```

- **Fields:** Motivation and Description are always present. Omit any other field with nothing to say.
- **Motivation** is the case, condensed: the request, what happened, what should have happened. For a skill not built yet, it's the concrete requests the skill must serve, quoted whole since they are its test cases. Quote only key phrases. When the case, or a request in it, is only the maintainer's account of what happened, with no conversation or excerpt, or a request they expect, mark it "(hypothetical)", since the first real case can overturn what's built on it. With no case at all, write "No case recorded".
- **Acceptance criteria:** what a good result looks like for each request of the case, or another way to tell the change works.
- **Blocked by:** the entries that must be done before this one.
- **Model:** the tier of model the change needs (`models.md`).
- **Write only what the maintainer said or decided.** An assumption is an open question. The type, area, readiness and tier are yours to set from what was said.

## Ready

An entry is ready when a change plan can be written from it without asking the maintainer for a decision. It has:
- **The case:** real or hypothetical, in Motivation, or the maintainer's explicit decision to go without one, in Decisions. "No case recorded" alone isn't a case.
- **The expected behavior:** what the skill should do after the change, in Description.
- **Acceptance criteria**, in their field.
- **No open questions.**

Any other entry needs clarification. Set the readiness by this test each time an entry is written or changed, and when it needs clarification, tell the maintainer what it lacks.

## The folder

Each entry is a file `backlog/<number>-<slug>.md`, the slug a few words of the title in lowercase with hyphens (`backlog/7-deck-duration-question.md`). A new entry takes one more than the highest number the folder has ever used, counting files removed since and files on other branches (`git log --all --format= --name-only -- backlog/`), so a number never points to two entries.

```markdown
---
title: <Entry title>
type: <idea | bug | debt>
labels: [<area>, <readiness>]
status: open
---

<the body>
```

- **Status:** `open`, or `discarded`. A discarded entry keeps its file, so it isn't proposed again, and its body ends with a `**Why discarded:** <reason> (YYYY-MM-DD)` line.
- **Done:** the file is removed.

A project may still keep its backlog in one `BACKLOG.md` at the root: `## <area>` headings, a `### <title>` per entry with its type and fields as bullets (`- **Type:** Idea`), and discarded entries under a last `## Discarded`. It has no numbers or labels: refer to an entry by its title, and judge its readiness when reading it. Write to it in that form until `prepare` moves it into `backlog/`.

## Operations

- **Capture:** when the maintainer states an idea, a bug or a debt, write it as a new entry.
  - When the case is missing, ask one or two short questions about it.
  - "Just note it" skips the questions.
  - Look first for a similar entry, including discarded ones. If one exists, show it and ask whether to merge.
- **List:** by area, each entry's number, title, type and readiness. Give details only when asked.
- **What's next:** read the open entries and show, without changing anything:
  1. a table of the ready ones in the order to take them: first those with no open blocker, then those still blocked, each after its blockers; within each group, bugs, then ideas, then debt, oldest (lowest number) first. Columns: number, title, area, type, tier, open blockers;
  2. the entries that need clarification, oldest first, each with what it lacks;
  3. the one to take next: the first in the table with no open blocker, with its tier's model (`models.md`). When there's none, the entry to clarify first: one that blocks a ready entry, or else the oldest.

  Place an entry with no readiness label by the Ready test, say which ones they are, and offer to label them (Clean up).
- **Discard:** only on the maintainer's word: set `status: discarded` and add the Why discarded line.
- **Clean up:** look for entries that are duplicated, already done (check the skills and CHANGELOG.md) or dropped, and for readiness labels the Ready test no longer gives. Show the plan and wait for the OK.
- **Done:** when `train` finishes a change that came from an entry, the entry leaves the backlog in that change's commit. `train` does this.
