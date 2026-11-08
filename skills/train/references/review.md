# Independent reviews

Two read-only agents review a change. Neither sees the conversation or the plan, so neither is anchored on the reasoning that produced the text:
- **sweeper** checks cohesion: leftovers, contradictions, redundancy, drift between siblings, broken references, inconsistent terms, vague instructions and scope overlap.
- **examiner** checks architecture: whether the skill is well built, against the target's principles and `train`'s writing guide.

Which kinds of change get which review is in SKILL.md's "Kinds of change" table.

## Starting them

They ship with sensei as the agents `sensei:sweeper` and `sensei:examiner`. Start each with a message that holds only:
- **Base:** the commit the branch started from (`git merge-base main HEAD`). The agent reads the change with `git diff <base>`. When there is no usable base (an audit, or a repository whose first commit holds the skill), say "none" and list every file to read in full.
- **Changed files:** the paths in the diff.
- **Siblings:** the SKILL.md path of every other skill in the plugin, plus every file the plan listed as stating the same rule.
- **Principles:** the path to the target's `docs/principles.md`.
- **Writing guide** (`examiner` only): the absolute path given in SKILL.md, step 6.
- **Scope map:** the output of the check script's `--scope-map`, pasted in.

Don't add what the change is for, what you think of it, or what to look for. Its job is to read the change without your view of it.

If the plugin's agents aren't available, start a general agent with the same message, prefixed by the body of the agent's briefing file (path in SKILL.md, step 6), without its frontmatter. If the session can't start agents at all, say so to the maintainer and offer the review as a prompt for a new conversation.

## Using the findings

Each agent returns findings ranked by severity, each with:
- where it is (file and section);
- what is wrong;
- a suggested fix.

Before showing them, drop every finding that fails the bar in the agents' briefings ("What to leave out", written the same in `sweeper.md` and `examiner.md`; a change to it reaches both). A finding passes when the model would do the wrong thing, stop or guess between readings on a realistic request, when it is a copy of a rule that will drift, or when it is a principle conflict that changes what the skill does. Drop the rest even when an agent reported it, and don't list or count what you dropped. When both agents ran, show the remaining findings together, merging duplicates. For each one, say whether you agree and what you'd do:
- **Fixes that change no decision:** a leftover, a broken reference, a term made consistent, a sibling the plan missed. These go straight to the branch.
- **Fixes that add a rule or change a decision:** proposals, applied only on the maintainer's OK.
- **Findings you disagree with:** say why. The maintainer decides.

After a fix round, commit, run the check script, and rerun only the review whose findings led to changes in behavior. Don't loop over wording.
