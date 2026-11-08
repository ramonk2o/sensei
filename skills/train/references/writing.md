# Writing a skill

How to write or change a skill's text. The target plugin's `docs/principles.md` comes first. Where this file and the principles differ (size limits, description style, how skills share rules), the principles win. This guidance is adapted from Anthropic's skill-creator (Apache 2.0).

## The reader

A skill is read by a model that has only the text and the user's request. It never saw the conversation where the skill was designed, and it will run in thousands of situations nobody tested. Write for that reader:
- **Say why, not just what.** A model that understands the reason for a rule applies it to cases the rule didn't name. If you find yourself writing ALWAYS or NEVER in capitals, or a rigid structure, treat it as a warning sign: say what's at stake instead. Keep a hard rule for what truly has no exception, and give its reason.
- **Use the imperative** for instructions ("Ask for the case before proposing"), and plain statements for facts.
- **Don't name the tools of one surface.** Describe what the session can do ("if the session can start an agent"), unless the target's principles say otherwise.

## Fix the case, not the example

The change starts from one real case, but the skill must work for every case like it.
- **Find the root.** Ask what made the skill fail there: a missing step, an ambiguous rule, a wrong default. Write the fix at that level, not as a patch for the exact words of the example.
- **Change the approach when a problem persists.** If a rule was already tightened once and the failure came back, more emphasis rarely helps. Try another framing, an example of the reasoning, or moving the step earlier.
- **Keep examples general.** An example pulls the model toward its surface. Use examples for formats, tones and borderline cases, and make sure they don't become the only shape the skill produces.

## Lean

`SKILL.md` loads in full on every use. Every sentence costs on every run, so each one has to change the result.
- **Cut what doesn't pull its weight:** restated rules, explanations of what any capable model does anyway, history ("this used to…"), hedges.
- **Read what the model did, not just what it answered.** When a test or a real case shows the model spending turns on something unproductive, find the text that sends it there and remove or narrow it.
- **Bundle repeated work.** When every test run writes the same helper, or a step is mechanical (counting, formatting, checking files), put a script in the skill's `scripts/` and tell the skill when to run it. A script runs without being read into context.

## Layers

- **Description:** always in context. It says when to use the skill and when not to (which sibling takes those requests), within the target's limit. Triggering comes from it, so name real requests, in the user's words, not categories.
- **`SKILL.md`:** the flow, and what every step needs. It opens with what the skill is for and, when siblings exist, what it leaves to them.
- **`references/`:** what only one step, case or kind of input needs. SKILL.md names each reference at the step that uses it, and says when to read it ("read `references/<name>.md` before step 3"). A reference over about 300 lines gets a short table of contents at the top.
- **`scripts/`:** mechanical work, run rather than read.

## Draft, then reread

After writing, reread the whole changed text as the cold reader would: someone with only the text. Look for:
- a step that assumes something not written;
- a term used two ways;
- a rule that now contradicts another file;
- a sentence that would make sense only to someone who was in the conversation.

Fix those before the checks run.
