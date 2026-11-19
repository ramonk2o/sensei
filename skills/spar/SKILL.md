---
name: spar
description: Evaluates one skill made outside sensei, in any folder and with no setup, with sensei's checks and review, and says how to bring it in, e.g. 'can sensei tell me if my skill is good?', 'spar my invoice-summary skill'. Not for changing a skill (train).
---

# Spar

Evaluates one skill made elsewhere, so its author sees what sensei would say before adopting it: the check script and an independent review, with nothing at stake. It reads and reports, and writes nothing to the user's folders. Changing a skill belongs to `train`, in a repository set up with `/sensei:prepare`; a whole plugin goes to `/sensei:prepare`, then `train`'s audit.

Talk to the user in their language.

## 1. The skill

- **Named:** a skill folder (`SKILL.md` at its root) or a `.skill` file. A `.skill` file is a zip: unpack it into a new temporary folder, never one of the user's, and use the folder in it that holds `SKILL.md`.
- **A plugin** (a folder with `skills/*/SKILL.md`): list its skills and ask which one. One skill per run; for the whole plugin, point to `/sensei:prepare`, then `train`'s audit.
- **None named:** look in the current folder (a `SKILL.md` at its root, in a subfolder or in `skills/*/`), in `.claude/skills/*/` and in `~/.claude/skills/*/`. List what you found, by name and path, and ask which. When there's none, ask for the path.

## 2. The criteria

- **In a plugin** (the skill's folder is `<plugin>/skills/<name>/`, with a `.claude-plugin/` folder in `<plugin>`) whose folder or repository root has `docs/principles.md`: those principles and their limits.
- **Otherwise:** `train`'s writing guide, `${CLAUDE_PLUGIN_ROOT}/skills/train/references/writing.md`, with limits of 4000 tokens for SKILL.md and 300 characters for the description.

Never sensei's own `docs/principles.md`: they govern sensei's skills, not the user's.

## 3. Check

Run `python3 ${CLAUDE_PLUGIN_ROOT}/scripts/check.py --skill <folder>`, adding `--skill-tokens 4000 --description-chars 300` when step 2 found no principles. Then get the scope map: the same command with `--scope-map`, or, for a skill in a plugin, `check.py <plugin> --scope-map`, so the review sees its siblings.

## 4. Review

Start the agent `sensei:examiner` with a message that holds only:
- **Base:** none. Files to read in full: every file in the skill's folder.
- **Siblings:** the SKILL.md of every other skill in its plugin, or none.
- **Principles:** the path from step 2, or "none: judge by the writing guide, with limits of 4000 tokens for SKILL.md and 300 characters for the description".
- **Writing guide:** `${CLAUDE_PLUGIN_ROOT}/skills/train/references/writing.md`.
- **Scope map:** step 3's output.

When the skill has siblings, start `sensei:sweeper` at the same time, with the same message without the writing guide. Add nothing about what you think of the skill: the review is worth more for not knowing it. If the agents aren't available, start a general agent with the same message, prefixed by the body of `${CLAUDE_PLUGIN_ROOT}/agents/examiner.md` (or `sweeper.md`) without its frontmatter.

## 5. Report

One message:
- **Criteria:** which ones judged the skill (step 2).
- **Check:** the script's failures and warnings, and the sizes against the limits.
- **Findings:** the agents' findings that pass the bar ("What to leave out" in `${CLAUDE_PLUGIN_ROOT}/agents/examiner.md`), merged and ranked, each with where, what and the fix. Drop the rest without listing or counting it.
- **Cuts:** the examiner's cuts, as their own list.
- **With sensei:** what recreating it would change: rebuilt minimal from the requests it serves, each rule kept only where a test on one of them earns it, the description tested by a trigger suite. Name the findings and cuts that settles.
- **Next step:**
  - a loose skill: `/sensei:prepare` in a new folder for a plugin to hold it, then ask `train` to recreate the skill there;
  - a skill in a plugin: `/sensei:prepare` in the plugin's repository, then either fix the findings one at a time with `train`, as in an audit, or ask `train` to recreate it.

Before sending, check that every part is there and that the next step matches where the skill is. Then remove the temporary folder, if step 1 made one.
