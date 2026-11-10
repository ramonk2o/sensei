# Backlog

Ideas, bugs and debt for this plugin, managed with sensei's `log` skill. Each entry starts from a real case. Done work leaves this file: what changed goes to CHANGELOG.md.

## prepare

### Re-run on an already set-up repository is underspecified
- **Type:** Debt
- **Motivation:** a cold reader of `prepare` (2026-11-08) was asked to re-run it on a repository set up with an earlier sensei, whose CLAUDE.md still routed to kata, kanban and shodan. It replaced the "Maintenance with sensei" section correctly. But it had to guess several things:
  - what counts as "already set up";
  - which of steps 1 to 8 still run on a re-run;
  - how to carry over the project's subject wording when the section is refreshed from the template's placeholder;
  - whether the sensei-owned wording in "Project facts" can be refreshed, such as the Validate line and the "Skills stand alone" note.
- **Description:** Make `prepare`'s "Re-running" section and `references/claude-md.md` say:
  - what signals a repository already set up;
  - which steps run again and which are skipped;
  - that the project's own subject wording is kept;
  - how sensei-owned wording in the facts is refreshed.

### A new plugin's facts have no source
- **Type:** Debt
- **Motivation:** a cold reader of `prepare` (2026-11-10), run on a new plugin set up from a `meditate` plan with no git history, had to guess several facts that an existing repository would answer:
  - the commit author, the LICENSE holder and the marketplace's `owner`;
  - the tag format, with no tags to read;
  - whether to ask these in a round before drafting or fold them into step 7's review with recommended defaults.

  A cold reader of `meditate` (same day) also found no basis for recommending the `sensei:limits` numbers, which the check script then enforces.
- **Description:** Give `prepare` (and `references/principles.md`, for the limits) a default for each fact a new plugin can't answer, and say when they're asked.
- **Open questions:**
  - Whether the limits default to sensei's own (4000 tokens, 600 characters) or come from Claude Code's documented limits.

### A conflicting skill inside a large plugin
- **Type:** Debt
- **Motivation:** a cold reader of `prepare` (2026-11-10) found that the main conflict in a typical session, a skill-writing skill shipped inside a large plugin of unrelated skills, can only be handled by turning off the whole plugin (losing the unrelated skills) or by relying on the routing. Step 5 allows `skillOverrides` only for skills with no plugin prefix, and two readers would recommend differently.
- **Description:** Say how to weigh turning off a whole plugin against relying on the routing, and use a per-skill override for a plugin's skill if Claude Code supports one.
- **Open questions:**
  - Whether `skillOverrides` accepts a `plugin:skill` name.

## Plugin

### Try the cycle on a real plugin
- **Type:** Debt
- **Motivation:** sensei was designed before it was used. Its first runs on itself (a `train` change to `prepare` and the 0.1.0 release, 2026-11-07) worked. It hasn't set up an existing plugin yet.
- **Description:** Run `prepare` on an existing plugin and record here what went wrong.
- **Open questions:**
  - Whether `Bash(python3 */plugins/cache/*/sensei/*/scripts/check.py*)` matches the command a real session runs, and whether Claude Code warns about it at startup.
  - Whether `claude plugin eval` with a branch checkout target behaves as `testing.md` assumes.
