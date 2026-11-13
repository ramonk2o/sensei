# Pull request mode

When the project's CLAUDE.md says its integration is pull requests, a change reaches main through a pull request on GitHub instead of a local merge. Each step below that leaves the machine (the push, the pull request, the merge) waits for the maintainer's OK of its own: the OK to the whole change approves the change, not what's published about it. Use `gh`, signed in (`gh auth status`); if it isn't, stop and give the maintainer the commands.

1. **Push the branch:** `git push -u origin <branch>`.
2. **Open the pull request:** `gh pr create --base main --title "<what the change does>" --body-file <file>`. The body is the summary shown for the merge: what changed and why, the check result, the review findings and what was done about them, and the test result. When the change came from a backlog issue, the body ends with `Closes #<number>`, so the issue closes on merge. Give the maintainer the link.
3. **Merge:** wait for the pull request's checks if the repository has any (`gh pr checks <number> --watch`). Then `gh pr merge <number> --merge --delete-branch`: a merge commit, so one revert undoes one change, as a local `--no-ff` merge does. If the repository requires a review the maintainer can't give themselves, or the maintainer prefers to merge on GitHub, leave it open and say so.
4. **Update main:** `git switch main` and `git pull --ff-only`, then delete the local branch (`git branch -d <branch>`).

A contributor's pull request is merged the same way, from step 3, keeping its author. A fix commit added on top of it goes to its branch only when the contributor allowed edits from maintainers; otherwise, ask them for it in a comment, on the maintainer's OK to the text.
