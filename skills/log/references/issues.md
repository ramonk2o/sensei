# Backlog in GitHub issues

When the project's CLAUDE.md gives GitHub issues as its Backlog fact, the backlog lives in the repository's issues instead of BACKLOG.md. It shows what's wanted as it changes, without waiting for a merge, and a contributor's report is already in it. CHANGELOG.md stays a file, since it changes in the same commit as the skills.

Everything in `backlog.md` still holds (each entry starts from a real case, what each field is for, write only what the maintainer said) except where entries are stored, which this file replaces. Use `gh`, signed in (`gh auth status`). If it isn't, or the repository has issues turned off, stop and tell the maintainer: falling back to BACKLOG.md would split the backlog in two places.

## Mapping

| BACKLOG.md | Issues |
|---|---|
| An entry | An open issue titled with the entry's title; its body holds Motivation, Description, Decisions and Open questions, as in `backlog.md` |
| The area (`## <skill>`, `## Plugin`) | A label with the skill's folder name, or `plugin` |
| Type | A label: `idea`, `bug` or `debt` |
| Discarded | Closed as not planned, with a comment giving the reason and the date |
| Done: the entry leaves the file | `Closes #<number>` in the pull request's body, or in the merge commit's message with local merge, so the issue closes when the change reaches the default branch |

A label that doesn't exist yet (`gh label list`) is created on first use (`gh label create <name>`).

## Writing to issues

Everyone who can see the repository sees an issue as soon as it's written. The table in `log`'s SKILL.md ("What needs an OK first") applies as it does to BACKLOG.md: an entry the maintainer dictated is the OK to create its issue, and a capture that interprets the conversation shows the draft first. Changing the body of an issue someone else opened shows the change and waits for the OK, since it rewrites their text.

Read an issue again before using it (`gh issue view <number> --comments`): others comment on it. When a newer comment changes what the body says (a decision, the scope), ask the maintainer which holds, then update the body so it stays the entry.

Write issues and comments in the documents' language (`log`'s SKILL.md), as BACKLOG.md is.

Nothing about the backlog is committed in this mode: the issue is the record.

## Operations

- **Capture:** as in `backlog.md`, then `gh issue create --title "<title>" --body-file <file> --label <area>,<type>`. Give the maintainer the link.
- **Check for duplicates:** `gh issue list --state all --search "<key words>"`. A closed issue is done or discarded (closed as not planned): handle it as `backlog.md` handles an implemented or a Discarded entry.
- **List:** `gh issue list --state open --limit 200 --json number,title,labels`, grouped by area label, each with its number and type.
- **Discard:** only on the maintainer's word: `gh issue close <number> --reason "not planned" --comment "<why discarded> (YYYY-MM-DD)"`.
- **Clean up and reorganize:** as in `backlog.md`, plan first; moving entries between areas is a change of labels.
- **A contributor's issue:** once the maintainer accepts it as an entry, add its area and type labels. It isn't copied anywhere: the issue is the entry. When it lacks the case, ask for it in a comment, on the maintainer's OK to the text.

## Migrate from BACKLOG.md

When a project moves its backlog to issues and BACKLOG.md has entries (a plan from `meditate`, or an older backlog):
1. List the issues to create, one per entry, with title and labels. Say that they become visible to everyone who can see the repository as soon as they're created. Wait for the OK, which also covers creating the labels they need.
2. Create them in the file's order, so a `meditate` plan keeps its build order in the issue numbers. Entries under Discarded become issues closed as not planned, with their Why discarded as the comment.
3. Once every issue exists, remove BACKLOG.md, in the commit of the change that moved the backlog. If a creation fails, stop with BACKLOG.md still in place and say which issues exist, so the backlog isn't left in two places.
