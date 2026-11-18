# Backlog in GitHub issues

When the project's CLAUDE.md gives GitHub issues as its Backlog fact, the backlog lives in the repository's issues instead of `backlog/`. It shows what's wanted as it changes, without waiting for a merge, and a contributor's report is already in it. CHANGELOG.md stays a file, since it changes in the same commit as the skills.

Everything in `backlog.md` still holds (each entry starts from its case, what each field is for, when an entry is ready, write only what the maintainer said) except where entries are stored, which this file replaces. Use `gh`, signed in (`gh auth status`). If it isn't, or the repository has issues turned off, stop and tell the maintainer: falling back to `backlog/` would split the backlog in two places.

## Mapping

| `backlog/` | Issues |
|---|---|
| An entry's file and its number | An open issue and its number |
| `title` | The issue's title |
| The body | The issue's body |
| `labels`: the area and the readiness | The same labels: the skill's folder name or `plugin`, and `ready` or `needs-clarification` |
| `type` | A label: `idea`, `bug` or `debt` |
| Blocked by | GitHub's blocked-by relationship when `gh issue list --limit 1 --json blockedBy` succeeds; otherwise the Blocked by field in the body |
| `status: discarded` | Closed as not planned, with a comment giving the reason and the date |
| Done: the file is removed | `Closes #<number>` in the pull request's body, or in the merge commit's message with local merge, so the issue closes when the change reaches the default branch |

A label that doesn't exist yet (`gh label list`) is created on first use (`gh label create <name>`).

## Writing to issues

Everyone who can see the repository sees an issue as soon as it's written. The table in `log`'s SKILL.md ("What needs an OK first") applies as it does to `backlog/`: an entry the maintainer dictated is the OK to create its issue, and a capture that interprets the conversation shows the draft first. Changing the body of an issue someone else opened shows the change and waits for the OK, since it rewrites their text.

Read an issue again before using it (`gh issue view <number> --comments`): others comment on it. When a newer comment changes what the body says (a decision, the scope), ask the maintainer which holds, then update the body so it stays the entry.

Write issues and comments in the documents' language (`log`'s SKILL.md), as `backlog/` is.

Nothing about the backlog is committed in this mode: the issue is the record.

## Operations

- **Capture:** as in `backlog.md`, then `gh issue create --title "<title>" --body-file <file> --label <area>,<type>,<readiness>`, adding `--blocked-by <numbers>` when it has blockers and the relationship is available. Give the maintainer the link.
- **Change readiness or blockers:** `gh issue edit <number> --add-label <readiness> --remove-label <the other>`; `--add-blocked-by` or `--remove-blocked-by <numbers>`.
- **Check for duplicates:** `gh issue list --state all --search "<key words>"`. A closed issue is done or discarded (closed as not planned): handle it as `backlog.md` handles an implemented or a discarded entry.
- **List:** `gh issue list --state open --limit 200 --json number,title,labels`, grouped by area label, each with its number, type and readiness.
- **What's next:** `gh issue list --state open --limit 200 --json number,title,labels,body,blockedBy`, then as `backlog.md` says. An entry's blockers are the open issues in `blockedBy` and any Blocked by line in its body.
- **Discard:** only on the maintainer's word: `gh issue close <number> --reason "not planned" --comment "<why discarded> (YYYY-MM-DD)"`.
- **Clean up and reorganize:** as in `backlog.md`, plan first; moving entries between areas is a change of labels.
- **A contributor's issue:** once the maintainer accepts it as an entry, add its area, type and readiness labels. It isn't copied anywhere: the issue is the entry. When it lacks the case, ask for it in a comment, on the maintainer's OK to the text.

## Migrate from the repository

When a project moves its backlog to issues and `backlog/` or a BACKLOG.md has entries (a plan from `meditate`, or an older backlog):
1. List the issues to create, one per entry, with title and labels. Say that they become visible to everyone who can see the repository as soon as they're created. Wait for the OK, which also covers creating the labels they need.
2. Create them in number order, or a BACKLOG.md's order, so a `meditate` plan keeps its build order in the issue numbers. Discarded entries become issues closed as not planned, with their Why discarded as the comment. Once all exist, set each entry's blockers to the new numbers.
3. Once every issue exists, remove `backlog/` or BACKLOG.md, in the commit of the change that moved the backlog. If a creation fails, stop with the files still in place and say which issues exist, so the backlog isn't left in two places.
