---
name: meditate
description: Plans a new skill plugin, or a change to one that needs clarification, in rounds of decisions, then splits it into ready backlog issues, e.g. 'help me plan a plugin for teachers', 'think this through and break it into issues'. Not for a ready change (train) or noting an idea (log).
---

# Meditate

Takes a new plugin, or a change to one that needs clarification (`../log/references/backlog.md`, Ready), to issues ready to build: it settles every decision in rounds, splits what it settled into issues `train` builds one at a time, and writes them to the backlog. `train` starts it on a request that needs clarification. It doesn't change skills (`train` does, from these issues), note a stray idea (`log`) or set up a repository (`/sensei:prepare`).

Talk to the user in their language. Write in English, unless the project's CLAUDE.md names another language or, for a new plugin, the user asks for one.

Nothing is written before the user's OK to the review (step 4).

## 1. Look

Read where you are before asking anything:
- **No plugin yet** (empty, or only notes such as a README or a sketch): a new plugin. Read `references/new-plugin.md`. Read the notes too: what they already decide isn't asked again.
- **A plugin** (`.claude-plugin/plugin.json` or a `skills/` folder): a change to it. Read `references/change.md`.
- **An unrelated folder** (the home folder, another project): ask where the plugin lives or will live, and work there.

## 2. Decisions

Settle every decision the issues need, in rounds. Your mode's reference says what there is to settle.
- **The tree:** keep the list of open decisions, each with the decisions it depends on. One is ready to ask once everything it depends on is settled. When an answer opens a new decision, add it.
- **A round:** the ready decisions, up to five, riskiest first, numbered. Each has a short title, the question with its options when it has any, and a line of its own that opens with the recommendation in bold, then its reason in one line:

  ```
  1. **Sending.** Should the plugin send the emails, or only write them?
     - **Recommended: only write them.** Sending needs access to the user's mail account.
  ```

  Ready decisions past five wait for the next round. End the round with one line: the user needs to answer only what they disagree with, and the case when the round asks for it.
- **The reply** accepts every recommendation it doesn't contest: "ok" accepts them all, "I disagree with 3" accepts the others. A question it mentions without deciding is asked again in the next round.
- **The case** is the exception: only the user has it, so ask for it without proposing one, since an invented request tests only what the model already expects. It stays open until the user gives it.
- **Facts aren't questions:** what the repository holds, what is installed, what Claude Code allows. Look them up, in an agent if the session can start one, so the reading stays out of the conversation, and give the answer with where it came from. While it runs, only the decisions that depend on the fact wait: ask the other ready ones in the current round, before the agent reports.
- **The end:** no decision left open. Approving a round's answers isn't the OK to write.

## 3. Split into issues

Cut the understanding into as few issues as `train` can build one at a time, each in one run and one pull request:
- **Vertical:** each issue gives something usable on its own once merged (a request the plugin now serves end to end, or what a later issue builds on), not one layer across many skills (every description, then every flow).
- **Preparatory work first:** when there are several, what the others build on (a shared reference, a format, a rename) is done in an earlier issue, and they're Blocked by it.
- **Old and new forms:** when several skills move from one form to another (a format, a path, a field) and can't all move in one pull request, expand, migrate, contract. One issue adds the new form beside the old, then one per skill, or per few skills, moves them to it, and a last one removes the old form, so the plugin works after every merge.
- **Each issue** is an entry in the format of `../log/references/backlog.md`: its case as the Motivation, the behavior wanted as the Description, its Acceptance criteria, the Decisions settled for it, Blocked by (only the issues it needs done first) and its Model tier (`../log/references/models.md`).
- **Ready:** check each one against `../log/references/backlog.md`, Ready. One that fails goes back to step 2 for what it lacks, unless the user decides to leave it for later as needing clarification.

## 4. Review

Show everything in one message:
- **The understanding:** what will be done and why, in a few sentences, with every decision settled, those accepted by default included.
- **The issues,** in build order, each as it will be written, with its type, area, readiness, tier and blockers.
- **The other files** your mode's reference writes; for a file that exists, the changes section by section.

One OK covers the understanding and the split. Wait for it. A correction reopens the decisions it touches (step 2), then the review is shown again.

## 5. Write

Write as your mode's reference says, the issues in build order, so each one's blockers already have their numbers. When a file exists, merge into it: keep every entry and section the review doesn't change.

## 6. Finish

Tell the user what was written, where, and the next step your mode's reference gives.
