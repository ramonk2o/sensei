# BACKLOG.md format

`BACKLOG.md`, at the repository root, holds what may come: ideas, bugs and debt left for later. Each entry starts from the real case that produced it, because a change judged without its case gets built wrong. Done work leaves the file. It lives on in the changelog and in git history.

## The file

```markdown
# Backlog

Ideas, bugs and debt for this plugin, managed with sensei's `log` skill. Each entry starts from a real case. Done work leaves this file: what changed goes to CHANGELOG.md.

## <skill name>

### <Entry title>
- **Type:** Idea | Bug | Debt
- **Motivation:** <the real case: what was asked, what the skill did, what it should have done; or a review finding: the text and the request it breaks>
- **Description:** <the change wanted, from the user's side>
- **Decisions:**
  - <a choice already made>
- **Open questions:**
  - <what is still undecided>

## Plugin

### <Entry about the whole plugin>
...

## Discarded

### <Entry title>
- **Description:** ...
- **Why discarded:** ... (YYYY-MM-DD)
```

- **Areas (`##`):** one per skill, by its folder name, plus `Plugin` for whatever spans the plugin (README, principles, manifests, tooling). Remove an area as soon as it's empty.
- **Discarded** is always last, so a discarded idea isn't proposed again. Omit it while empty.
- **Fields:** Type, Motivation and Description are always present. Omit any other field with nothing to say.
- **Type:**
  - Idea: new behavior.
  - Bug: a skill does something wrong; the Description says how to reproduce it.
  - Debt: a change that keeps behavior, such as trimming, reorganizing or aligning skills.
- **Motivation** is the case, condensed: the request, what happened, what should have happened. For a skill not built yet, it's the concrete requests the skill must serve, quoted whole since they are its test cases, and what a good result looks like for each. Quote only key phrases. If no case exists, write "no case recorded", which is itself a reason to ask before doing it.
- **Write only what the maintainer said or decided.** An assumption is an open question.

## Operations

- **Capture:** when the maintainer states an idea, a bug or a debt, record it in the right area.
  - When the case is missing, ask one or two short questions about it.
  - "Just note it" skips the questions.
  - Look first for a similar entry, including in Discarded. If one exists, show it and ask whether to merge.
- **List:** by area, each entry's title and type. Give details only when asked.
- **Discard:** only on the maintainer's word. Move the entry to Discarded, keeping its Description and adding a Why discarded line with the reason and the date.
- **Clean up:** look for entries that are duplicated, already done (check the skills and CHANGELOG.md) or dropped. Show the plan and wait for the OK.
- **Done:** when `train` finishes a change that came from an entry, the entry leaves the file in that change's commit. `train` does this.
- **Create:** `meditate` or `prepare` creates the file with the title and the legend. `log` creates it when it's missing and the maintainer asks for it.
