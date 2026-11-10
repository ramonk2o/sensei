# The principles file

`docs/principles.md` holds the rules every skill of the plugin follows and the questions for judging a change to it. `train` checks every change against it, and the check script reads its limits. `prepare` settles it for a plugin that has none; `meditate` settles it while planning a new plugin.

## Settling it

Settle the principles with the user in rounds of up to five numbered questions, each with a recommended answer and a one-line reason. Cover:
- what every skill does before writing;
- how results are checked;
- whether each skill stands alone (reads nothing outside its folder);
- the size limits;
- the language rule.

When the repository or the plan already answers one, use that answer and say where it came from.

## The file

- **Title:** `# <plugin-name> principles`, with the name exactly as `plugin.json` will hold it, so `prepare` can read it from there.
- **Opening:** one paragraph on what the plugin's skills do, for whom, and what they leave out.
- **Principles:** numbered, each a checkable statement with its reason, so a reviewer can say whether a skill follows it.
- **Limits:** the limits agreed in the rounds, in a machine-readable block that the check script reads:

  ```
  <!-- sensei:limits
  skill_tokens: <agreed limit for a SKILL.md, in tokens>
  description_chars: <agreed limit for a description, in characters>
  -->
  ```

  Recommend `skill_tokens: 4000` and `description_chars: 600` unless the plugin needs otherwise. Claude Code's own limits are looser (SKILL.md under 500 lines; a description up to 1,024 characters in the Agent Skills format), but every skill's description shares one listing budget, about 1% of the context window, so a shorter one is cut less often.

- **Judging a proposal:** the file ends with the questions for judging a proposed change, such as which real case it comes from, whether it conflicts with a principle, and whether it fits an existing skill or needs a new one.
