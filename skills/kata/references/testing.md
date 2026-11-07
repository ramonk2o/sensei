# Testing a change

A skill is read by a model whose failures its author can't see from inside the conversation, so the test always runs where the conversation can't help: a fresh agent or a fresh process. The test is scaled to the kind of change, because most changes are small and a heavy test on each one costs more than it catches. This guidance is adapted in part from Anthropic's skill-creator (Apache 2.0).

## Behavior change or new skill: the cold reader

The cold reader tests what happens once the skill is running; the trigger suite below tests only whether it starts. A new skill or a full rewrite gets both, the cold reader first, so the description is tested on a flow that already works. Use one case per main path of the skill.

Start a fresh agent with no access to this conversation. Give it only:
- the changed `SKILL.md` and every changed reference (most contradictions are between a SKILL.md and a reference);
- the real case, written as the user's request, with any material the user gave;
- the question: "Following only these files, what do you do with this request, step by step? Where are the files unclear or contradictory?"

The test passes when its answer does what the plan said the skill should do in that case. When it goes another way, the text doesn't say what the plan decided: fix the text, not the reader. If the session can't start an agent, give the maintainer that prompt and the files, ready to run in a new conversation.

## New skill or description change: the trigger suite

Triggering is decided by the description, among all the descriptions in the session, and it varies from run to run. So it is tested with repeated runs in a clean process, using `claude plugin eval`.

**Where the suite lives:** in the target's `evals/triggers/<skill>-<case>/`, prefixed with the skill's name so suites of different skills don't mix. It is committed and kept, so the next description change reruns it.

**Each case** is a `prompt.md` plus one grader in `graders/`:

```markdown
---
description: fires deck on a report-to-slides request
tags: [trigger]
max_turns: 4
allowed_tools: [Skill]
---

<the request, as a user would write it>
```

```markdown
---
type: tool_used
tool: Skill
input_match: '"skill"\s*:\s*"(?:[\w-]+:)?deck"'
arm: both
---
```

For a case that must **not** fire the skill, the grader adds `min: 0` and `max: 0`.

**What to write:**
- **8–10 should-fire prompts:** the same intent in different phrasings, formal and casual, in more than one language if the plugin serves several. Include requests that don't name the skill or its output type but clearly need it, and requests where a sibling competes and this skill should win.
- **8–10 near-miss prompts that should not fire.** These are the valuable ones: they share words or subject with the skill but need something else, such as a sibling's request, the adjacent task the skill says it leaves out, or a request that is too simple for any skill. An obviously unrelated prompt tests nothing.
- **Realistic prompts:** concrete, with context, the way people actually write (a file name, a situation, an abbreviation, lowercase). A one-line abstract request ("make slides") is too simple: the model often answers those without any skill, whatever the description says.

Show the list to the maintainer before running it. They know which requests really arrive.

**Running it:**
- Run from an empty temporary folder, so the repository's CLAUDE.md doesn't take part.
- Point at the branch checkout: `claude plugin eval <path-to-branch-checkout> --tag trigger --case '<skill>-*' --ablation none --no-publish`. The checkout replaces an installed copy with the same name.
  - `--ablation none` skips the no-plugin baseline. That baseline would double the runs, and it means nothing for triggering.
  - `--no-publish` keeps the report on this machine.
- The default runs per case (3) absorb run-to-run variation.
- Read the report, then the transcripts of the failed cases: what the model did, not just whether it fired.
- Adjust the description by hand, toward the requests that failed, staying within the target's limit. Rerun once.
- If the second run still fails cases, show the maintainer which ones and why, and let them decide: change the description again, accept the miss, or change the scope.

**What it doesn't test:** the skill's whole flow. Skills that plan with the user in rounds can't be judged by a one-shot run, and a run without the skill writes a finished answer instead, so that comparison means nothing. For those, the cold reader is the nearest test before the first real use. Say so in the merge summary.

## Testing in a Claude app

When the target's skills stand alone (CLAUDE.md says so), offer a zip of the skill's folder from the branch, with the folder at the root of the zip. The maintainer can upload it as a personal skill and try it before the release.
