# Backlog

Ideas, bugs and debt for this plugin, managed with sensei's `log` skill. Each entry starts from a real case. Done work leaves this file: what changed goes to CHANGELOG.md.

## prepare

### Git permissions allow destructive variants
- **Type:** Bug
- **Motivation:** a cold reader of `prepare` (2026-11-07) found that allowing whole commands lets their destructive forms through without a prompt: `git tag*` allows `git tag -d`, `git switch*` allows `--discard-changes`, `git commit*` allows `--amend`, `git archive*` writes files with `-o`. Step 4 says deleting branches or files keeps asking.
- **Description:** Narrow the allowed patterns or add `permissions.deny` rules for the destructive forms, keeping what the cycle uses (`train` amends a wording fix; `graduate` runs `git tag -a`).
- **Open questions:**
  - Narrower allow rules or deny rules.

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

## Plugin

### Try the cycle on a real plugin
- **Type:** Debt
- **Motivation:** sensei was designed before it was used. Its first runs on itself (a `train` change to `prepare` and the 0.1.0 release, 2026-11-07) worked. It hasn't set up an existing plugin yet.
- **Description:** Run `prepare` on an existing plugin and record here what went wrong.
- **Open questions:**
  - Whether `Bash(python3 */plugins/cache/*/sensei/*/scripts/check.py*)` matches the command a real session runs, and whether Claude Code warns about it at startup.
  - Whether `claude plugin eval` with a branch checkout target behaves as `testing.md` assumes.

### Plan a new plugin from an idea
- **Type:** Idea
- **Motivation:** the maintainer asked (2026-11-09) whether sensei has something like minidev's `brainstorm`, which takes a new project from an idea to a working skeleton: a product interview, the architecture decided with the user, the first feature picked and the rest in the backlog. Sensei has no such step. For a folder with no plugin, `prepare` proposes only a name, the first skill's purpose in one sentence and the skeleton, and its rounds settle the principles, not the product. `train` designs one skill at a time and starts from a real case, which a plugin that is still an idea doesn't have.
- **Description:** When a plugin is still an idea, interview the maintainer before the skeleton:
  - who it's for and what problem it solves;
  - what the first version does and what it leaves out;
  - which skills it has and where each one's scope ends;
  - whether the skills stand alone, and whether it needs agents, hooks or scripts;
  - which skill comes first.

  The rest go to BACKLOG.md.
- **Open questions:**
  - Whether this extends `prepare`'s new-plugin path or becomes a skill of its own.
  - What counts as the real case for a skill that has never been used: the request it must serve, stated in the interview.
