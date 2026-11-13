# Pull requests, issues and the GitHub repository

Where the repository lives sets two facts of the CLAUDE.md: the integration and where the backlog lives. On GitHub, pull requests keep each change reviewable on its own page, and issues show the backlog as it changes and take contributors' reports directly. Both need `gh` installed and signed in, so without it the project keeps local merge and BACKLOG.md, which need nothing beyond git.

## What step 1 reads

- the remote (`git remote -v`): on GitHub, on another host, or none;
- whether `gh` is installed and signed in (`gh auth status`);
- on GitHub, whether issues are on (`gh repo view --json hasIssuesEnabled`). A repository created here has them on.

## The recommendation

- **On GitHub, `gh` signed in:** pull requests; the backlog in issues when they're on, BACKLOG.md otherwise.
- **No remote, `gh` signed in:** offer to create the repository (below). Yes brings pull requests and issues; no keeps local merge and BACKLOG.md.
- **Otherwise** (another host, or no `gh`): local merge and BACKLOG.md, without asking.

Say the recommendation and its reason in step 7's review, like the other facts. The user may pick otherwise at that review. Issues without pull requests work too: `Closes #<number>` then goes in the merge commit's message and closes the issue when main is pushed.

## Creating the repository

**Propose** it in step 7: its name (the folder's), its owner (the signed-in account, unless the user names an organization) and its visibility, recommending private, since the code leaves this machine but nobody else sees it until the user decides. If the user declines, redo the integration and backlog proposals for local merge and BACKLOG.md and show them again.

**Create** it in step 8, right after git:
1. `gh repo create <owner>/<name> --private --source . --remote origin` (`--public` if chosen), without `--push`. Give the user the link.
2. If it fails (the name is taken, no right to create in that organization), show the error and ask: another name or owner, or local merge and BACKLOG.md. Don't write a pull request CLAUDE.md for a repository that doesn't exist.
3. The remote has no main branch yet, so setup's commit goes on main. Then push it (`git push -u origin <main branch>`) on an OK of its own, apart from the commit's: the first pull request needs it there. If the user declines, say that the first pull request will need main pushed.

## Moving the backlog to issues

When the backlog goes to issues and BACKLOG.md has entries (a `meditate` plan, or an older backlog), show in step 7 the list of issues to create, as `../log/references/issues.md` says (Migrate from BACKLOG.md). In step 8, migrate after the CLAUDE.md and the settings. Until every issue exists, the CLAUDE.md's Backlog fact stays BACKLOG.md; switch it once the migration is done, so a failed migration doesn't leave the backlog in two places. Take a `meditate` plan's name, purpose and skills from BACKLOG.md before it's removed.

## Setup's own commit

Setup's commit goes on main when the repository is new or the remote was just created. When it uses pull requests and main already exists on the remote, main only takes pull requests: start a `sensei-setup` branch (`git switch -c`, which carries the uncommitted changes), commit there and bring it in as `../train/references/pull-requests.md` says, each step on the user's OK.

## Re-running on a repository already set up

When the CLAUDE.md says local merge and the repository is on GitHub with `gh` signed in, offer the switch to pull requests, and to issues when they're on, in step 7, with the migration list if BACKLOG.md has entries. A decline leaves the CLAUDE.md as it is. Nothing records it, so the next run offers the switch again, in one line.
