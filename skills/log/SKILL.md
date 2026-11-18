---
name: log
description: In a repository whose CLAUDE.md names sensei, notes ideas, bugs and debt in the backlog (backlog/ or GitHub issues), shows what's next, keeps CHANGELOG.md, e.g. 'note this idea for the deck skill', 'what's next?', 'fix the changelog'. Not for changing a skill (train) or releasing (/sensei:graduate).
---

# Log

Two records describe a plugin over time, like a training log: what is left to practice and what each version earned. `log` owns their formats: it notes what may come, shows what to take next and keeps the changelog. A change to a skill belongs to `train`, which writes its own changelog entry, and planning one that isn't settled to `meditate`; `log` only records ideas for later. A release belongs to the maintainer, who runs `/sensei:graduate`; `log` doesn't cut versions.

| Where | Holds | Time |
|---|---|---|
| `backlog/`, or GitHub issues | What may come: ideas, bugs and debt, each from its case | future |
| `CHANGELOG.md` | What changed in each version, for the plugin's users | past |

The skills themselves are the present: they say how the plugin works today, so no other document repeats them. `meditate`, `train` and `graduate` don't load this skill. They read the formats directly from `references/`, so the formats have one owner and every reader writes the same way.

Talk to the maintainer in their language. Write the files in English, unless the project's CLAUDE.md names another language for its documents.

## Before writing

- For the backlog, read `references/backlog.md`. When CLAUDE.md gives GitHub issues as its Backlog fact, read `references/issues.md` too: the entries live there instead of `backlog/`.
- For CHANGELOG.md, read `references/changelog.md`.
- Read the current entry or file before changing it.
- If a file follows another structure, don't rewrite it on your own. Show how it differs, propose the alignment and wait for the OK. Until then, follow the structure that's there.

## What needs an OK first

| Operation | Before writing |
|---|---|
| Capture a clear idea, bug or debt; "just note it" | Write it, then tell them what was written |
| Capture that needed interpretation (from a long discussion) | Show the draft and its area, then wait |
| Discard | On the maintainer's word only |
| Clean up, reorganize areas, align a file's format | Show the plan, then wait |
| Fix a slip in an already-aligned changelog (a failed check, a merge conflict) | Fix it, then tell them |
| A changelog in another format (the check fails on its whole structure) | It's an alignment: show the plan, then wait |

Never implement what's recorded. A change to a skill starts with `train`, from the entry's case.

## Commits

Backlog changes kept in issues aren't committed. Otherwise, commit the changed files on their own, on the branch you're on, with a short message ("Backlog: note deck duration idea"). Commit only these files, never other pending changes. When the change is part of `train`'s or `graduate`'s work, it goes in that commit instead.
