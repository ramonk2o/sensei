# A change to a plugin

The plugin exists, and the change is planned here and built by `train`, one issue at a time. The rounds settle every decision `train` would otherwise have to ask the user for before planning (`../log/references/backlog.md`, Ready).

## Before the first round

Read:
- the project's CLAUDE.md, for its facts (the documents' language, where the backlog lives), and its `docs/principles.md`;
- the skills the change touches, and every other skill or listing (README, manifests) that states the same rule: search for its key terms;
- the backlog entries about it, including any the change came from. In GitHub issues, find them and read them as `../log/references/issues.md` says (Operations, Check for duplicates; Writing to issues).

When the CLAUDE.md doesn't name sensei, say that `/sensei:prepare` sets the project up for `train`, which builds the issues. While it gives no Backlog fact, they go to `backlog/`.

## What to settle

The case comes first: the rest depends on it.
- **The case:** what the skill was asked, what it did and what it should have done, from a conversation or an excerpt; for a new skill, the requests it must serve and the good result for each. The user's account of what happened, or a request they expect, counts, marked hypothetical. An impression ("it's off") is a reason to ask for the case. Going without one is the user's explicit decision, recorded under the issue's Decisions.
- **The behavior wanted:** what each skill involved does after the change, for each request of the case.
- **The border:** what the change leaves out and, when scope moves between skills, which requests fall on each side.
- **Skills:** for a new skill, a scope that moves, or a reference several skills will share, also settle what applies of the Skills group in `references/new-plugin.md` (What to settle): the split, the folder and borders, the invocation, which skill keeps a shared reference.
- **Principles:** a change that goes against one of the project's principles is a design decision. Name the principle and recommend a way out, weighed as `../train/references/conflicts.md` says.

## Writing

Write the issues where the CLAUDE.md's Backlog fact says, as `log` does: in the format of `../log/references/backlog.md`, and through `../log/references/issues.md` (Operations) when they live in GitHub issues. In issues, say before the OK that they're visible to everyone who can see the repository once created.
- **An entry the change came from** becomes one of the issues, rewritten in place, so it keeps its number and discussion. When no issue matches it, discard it with "split into #…" as the reason.
- **In `backlog/`,** commit only the entry files, on the branch you're on ("Backlog: plan <the change>").

## Next step

Build the first issue with no open blocker with `train` (e.g. "let's build #12"), on its tier's model (`../log/references/models.md`). `log` shows what's next.
