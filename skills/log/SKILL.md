---
name: log
description: In a skill plugin repository whose CLAUDE.md names sensei, keeps the backlog (ideas, bugs and debt left for later, each from a real case, in BACKLOG.md or the repository's GitHub issues) and CHANGELOG.md (what changed in each version) when the maintainer asks directly, e.g. 'note this idea for the deck skill', 'what's in the backlog?', 'discard that idea', 'fix the changelog'. Not for changing a skill (that's train, which writes its own changelog entry) or releasing a version (the user runs /sensei:graduate), and not for repositories that aren't set up for sensei.
---

# Log

Two files describe a plugin over time, like a training log: what is left to practice and what each version earned. `log` owns their formats. A change to a skill belongs to `train`, which writes its own changelog entry. A release belongs to the maintainer, who runs `/sensei:graduate`; `log` doesn't cut versions.

| File | Holds | Time |
|---|---|---|
| `BACKLOG.md`, or GitHub issues | What may come: ideas, bugs and debt, each from a real case | future |
| `CHANGELOG.md` | What changed in each version, for the plugin's users | past |

The skills themselves are the present: they say how the plugin works today, so no other document repeats them. `train` and `graduate` don't load this skill. They read the formats directly from `references/`, so the formats have one owner and every reader writes the same way.

Talk to the maintainer in their language. Write the files in English, unless the project's CLAUDE.md names another language for its documents.

## Before writing

- For the backlog, read `references/backlog.md`. When CLAUDE.md gives GitHub issues as its Backlog fact, read `references/issues.md` too: the entries live there instead of BACKLOG.md.
- For CHANGELOG.md, read `references/changelog.md`.
- Read the current file before changing it.
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

Backlog changes kept in issues aren't committed. Otherwise, commit the file on its own, on the branch you're on, with a short message ("Backlog: note deck duration idea"). Commit only these files, never other pending changes. When the change is part of `train`'s or `graduate`'s work, it goes in that commit instead.
