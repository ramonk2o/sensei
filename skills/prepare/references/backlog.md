# The backlog's home

The CLAUDE.md's Backlog fact says where the backlog lives: GitHub issues, or the `backlog/` folder (`github.md` says which to recommend). The formats are `log`'s (`../log/references/backlog.md`, and `../log/references/issues.md` in issues). This file says what setup puts in place and how an older BACKLOG.md moves.

## What setup puts in place

- **GitHub issues:** the `ready` and `needs-clarification` labels (`github.md`, The readiness labels).
- **`backlog/`,** when the Backlog fact ends as `backlog/`: the folder, holding an empty `.gitkeep` while it has no entry, since git doesn't track an empty folder. A declined move leaves BACKLOG.md and creates no folder; nothing records it, so the next run offers the move again.

When entries move, the Backlog fact stays where they are now (in a new CLAUDE.md too) until every entry has moved, then changes: from BACKLOG.md to `backlog/`, or to GitHub issues. Step 7's draft shows the final value, and step 8 writes it after the move, so a move that fails halfway doesn't leave the backlog in two places.

## Moving a BACKLOG.md

The same conversion serves the move into `backlog/` and into issues (`github.md`). Each `###` entry becomes an entry of the current format, in BACKLOG.md's order, so a `meditate` plan keeps its build order. Show it in step 7 as the list of what it creates: for `backlog/`, each file's name, labels and status; for issues, each title and labels.

- **Title, area, type:** the `###` title, the `##` heading as the area in a skill's folder-name form (`Plugin` becomes `plugin`), the Type bullet in lowercase.
- **Body:** each field bullet becomes the body's field of that name, its text unchanged. Where an entry names another by its title, write the number once numbers exist.
- **Readiness and tier:** the readiness by the Ready test (`../log/references/backlog.md`), showing what each entry that needs clarification lacks, and the tier by `../log/references/models.md`, from its Description. A field the old entry lacks and these don't set (acceptance criteria, blocked by) stays out, because the move records what was written.
- **Discarded:** an entry under `## Discarded` becomes `status: discarded` with its Why discarded line ending the body, or an issue closed as not planned (`../log/references/issues.md`). The old file gives it no area, type or Motivation: take the area and type from its Description, write "No case recorded" as its Motivation, and give it no readiness label or tier, since it won't be worked.

Once every entry exists, remove BACKLOG.md in setup's commit.

## A re-run

Look before creating: an existing folder, label or entry stays as it is, and only what's missing is created. An entry has moved when the destination already has one with its exact title: a file of `backlog/`, or an issue, open or closed (`gh issue list --state all --search` finds the candidates); list those in step 7 as already there. After a move that failed halfway, the re-run creates the rest in BACKLOG.md's order, with the next numbers, and removes BACKLOG.md once every entry exists.
