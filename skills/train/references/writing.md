# Writing a skill

How to write or change a skill's text. The target plugin's `docs/principles.md` comes first. Where this file and the principles differ (size limits, description style, how skills share rules), the principles win. This guidance is adapted from Anthropic's skill-creator (Apache 2.0).

## The reader

A skill is read by a model that has only the text and the user's request. It never saw the conversation where the skill was designed, and it will run in thousands of situations nobody tested. Write for that reader:
- **Use the imperative** for instructions ("Ask for the case before proposing"), and plain statements for facts.
- **Don't name the tools of one surface.** Describe what the session can do ("if the session can start an agent"), unless the target's principles say otherwise.

## Fix the case, not the example

The change starts from one real case, but the skill must work for every case like it.
- **Find the root.** Ask what made the skill fail there: a missing step, an ambiguous rule, a wrong default. Write the fix at that level, not as a patch for the exact words of the example.
- **Change the approach when a problem persists.** If a rule was already tightened once and the failure came back, more emphasis rarely helps. Try another framing, an example of the reasoning, or moving the step earlier.
- **Keep examples general.** An example pulls the model toward its surface. Use examples for formats, tones and borderline cases, and make sure they don't become the only shape the skill produces.

## Lean

`SKILL.md` loads in full on every use, and a reference on every run that reaches it, so each sentence has to change what the model does. Run these tests on every sentence the change writes or alters, in `SKILL.md` and in references:
- **No-op:** would the model act differently without it? If not, delete the whole sentence, or the part of it that changes nothing. Typical no-ops: history ("this used to…"), hedges, what the model does anyway. Judge for a capable current model, unless the target's principles name a weaker one its users run. When in doubt, delete, except a gate before a costly or irreversible action: that failure can't be learned from.
- **Branch** (`SKILL.md` only): does every run need it? What one branch needs goes to a reference (Layers), unless it's as short as the pointer to it.
- **One source:** does a source the model running the skill will have read already say it? That is one the skill tells it to read (the principles, a config file, a command's output) or one always in its context (the project's CLAUDE.md). Then don't restate it.
- **Positive:** does it state the target behavior? Keep a prohibition, or ALWAYS and NEVER in capitals, only for a hard guardrail: a rule that truly has no exception.
- **One word:** name a recurring thing with one strong word and repeat it, instead of a phrase explained again at each use.
- **Why:** give the reason, as a clause, where the model must generalize a judgment: it then applies the rule to cases the rule didn't name. A mechanical step gets none.

Beyond the sentence:
- **Read what the model did, not just what it answered.** When a test or a real case shows the model spending turns on something unproductive, find the text that sends it there and remove or narrow it.
- **Bundle repeated work.** When every test run writes the same helper, or a step is mechanical (counting, formatting, checking files), put a script in the skill's `scripts/` and tell the skill when to run it. A script runs without being read into context.

## Layers

- **Description:** always in context, and triggering comes from it. It says what the skill does and gives one trigger per kind of request it takes: a request quoted in the user's words, or, when quotes for every kind won't fit the limit, a short phrase naming the kind. The flow belongs in `SKILL.md`. When a sibling has neighboring scope, one short clause names it ("Not for X (sibling)"). A skill only the user can invoke (`disable-model-invocation: true`) never reaches the model: its description is one short line saying what the skill does, for the person reading the menu.
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
