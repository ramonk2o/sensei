# Other requests

## A contributor's issue or pull request

- Read it in full: the issue and its comments, or the pull request's diff and description.
- Judge it with the target's questions for judging a proposal (`docs/principles.md`):
  - which real case it comes from;
  - whether it changes behavior or only wording;
  - whether it conflicts with a principle;
  - whether it fits an existing skill;
  - what it costs in size or turns.
- Say what's missing for a decision: the case, the version where it happened, an example.

Draft the reply in the repository's documents language (English by default). Publish nothing (comment, label, close, merge) without the maintainer's OK to that exact text and action.

An accepted pull request still goes through the form from step 3: the plan lists the siblings its change must reach, then come the checks, the reviews and the test for its kind. When it lacks a changelog entry or misses a sibling, add a commit on top of it with what's missing. Bring it in the way the project integrates (local merge with `--no-ff` by default), keeping its author. The project's commit-author rule applies only to commits made here.

## Consistency audit

When the maintainer asks to check the whole plugin ("audit the plugin", "is everything consistent?"):
1. Run the check script (its path is in SKILL.md, step 5), plain and with `--scope-map`.
2. Start `sensei:sweeper` on each skill, or on the whole plugin when it is small. The base is "none", the files to read in full are all the skill's files, and the siblings are the other skills (see `review.md`, Starting them). When the maintainer also asks about architecture or design ("cohesion and architecture", "is it well built?"), start `sensei:examiner` on each skill too, with the same message plus the writing guide (path in SKILL.md, step 6).
3. Read the scope map yourself for overlap: two skills whose descriptions claim the same request, or a skill whose opening doesn't say what it leaves to a sibling.
4. List what you found that passes the bar in `review.md` (Using the findings), grouped by skill and ranked, with a proposed fix for each. Edit nothing before the maintainer picks what to fix.

Each fix then goes through the form for its kind. The finding is its real case: it names the file, the text and what goes wrong, so don't ask the maintainer for another example unless they doubt it happens.

## Recreating a skill from an old one

When the maintainer brings an older skill to rebuild (from another plugin or an earlier design), treat it as a reference, not text to copy.
- Read all of it. Say what works, what is surplus and what weighs too much.
- Decide with the maintainer, in rounds, what goes into the new version.
- Settle the new skill's name with them. The name is the `skills/<name>/` folder and the frontmatter `name`, which must match. The new text doesn't mention the old name.

Then it's a new skill: plan, edit, check, both reviews, the cold reader and the trigger suite.

## Something that isn't a skill

For a hook, an agent, a command or an MCP server, load the matching skill of Anthropic's official plugin-dev when the session has it (hook-development, agent-development, command-development, mcp-integration), for the format and its rules. Keep the target's principles above its style advice. The form is the same: case, plan, branch, checks (validate covers these components), review by `sweeper`, and a test that fits the component. A change to the README or the manifests alone is a wording fix, or a behavior change when it alters what the plugin promises. When plugin-dev isn't available, use the current Claude Code documentation for the format, never memory.
