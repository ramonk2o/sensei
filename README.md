# Sensei

Sensei helps you make your own skills for Claude Code and keep them working as they grow. You say what you want in plain words; sensei plans it with you, writes the skill, checks it, tests it and releases it. You approve each step.

You don't need to know how skills are built. The skills talk to you in your own language, and everything they write to your files is in English unless you ask for another language.

## What you need to know first

- A **skill** is a set of instructions that teaches Claude how to do one task your way, such as writing a weekly report or reviewing an invoice.
- A **plugin** is a folder that packages one or more skills, so you can install them and share them.
- Sensei works on one plugin at a time: the folder where your skills live.

## Install

In Claude Code, run:

```
/plugin marketplace add ramonk2o/sensei
/plugin install sensei@sensei
```

Sensei also needs `git` and Python 3 on your computer.

## Where to start

Pick the line that describes you:

| You have… | Do this |
|---|---|
| Only an idea for some skills | Open an empty folder and run `/sensei:meditate` |
| A folder with skills already | Open it and run `/sensei:prepare` |
| One skill made elsewhere, and you want an opinion on it | Run `/sensei:spar` on it |
| No idea how any of this works | Run `/sensei:help` for a short tour |

## The cycle

**meditate → prepare → train ⇄ log → graduate**, then back to `log` or `meditate` for the next version.

1. **Plan** with `meditate`. Sensei asks you questions in rounds about who the skills are for, what requests they must handle and where one skill ends and the next begins. Each question comes with a recommended answer, and you reply only to the ones you disagree with. It ends with a list of small tasks, ready to build. Use it at the start, or later for a change that you haven't fully thought through.
2. **Set up** with `prepare`. Sensei gets the plugin folder ready: the basic files, a place for your list of tasks (on GitHub or in a folder), and a note that tells Claude this plugin is maintained with sensei. You run it once per plugin.
3. **Build and change** with `train`. Each task, and each time a skill did something wrong, goes through `train`: it shows you a plan, makes the change once you approve it, checks it, has it reviewed by readers who never saw your conversation, tests it, and records it in the changelog.
4. **Keep notes** with `log`. Ideas, bugs and loose ends go into your list of tasks, and `log` tells you what to take next.
5. **Release** with `graduate`. When you're happy with what you have, sensei gives it a version number, runs the checks one last time and packages it so others can install it.

## Day to day: just say what you want

After `prepare`, you rarely need to type a command. Say what you want, and the right skill starts:

| You say | What happens |
|---|---|
| "The deck skill made the title too long, it should keep it under ten words" | `train` plans and makes the fix |
| "I want a new skill that turns meeting notes into tasks" | `train` builds it, or sends it to `meditate` first if it needs more thought |
| "Note this idea: the deck skill could add speaker notes" | `log` adds it to your list of tasks |
| "What's next?" | `log` shows the tasks that are ready |

Only three you run by hand: `/sensei:prepare` to set up a plugin, `/sensei:spar` to evaluate a skill made elsewhere, and `/sensei:graduate` to release a version.

The best requests come from something that really happened: what you asked a skill, what it did, and what it should have done.

## You stay in charge

Nothing is edited before you approve the plan, nothing is merged before you approve the change, and nothing is released before you approve the version. If a request isn't clear yet, sensei asks before it builds.

## Under the hood

This part is for those who want to know how sensei works inside.

### The skills in detail

The names follow a dojo: you ask the sensei for **help**; you **spar** with a skill made elsewhere, **meditate** on a plugin or a change, **prepare** the repository, **train** each skill, **log** what is left and what was earned, **graduate** a version.

- **meditate** plans a new plugin from an idea, or a change to an existing one, before anything is built:
  - for a new plugin, who it serves, the concrete requests it must answer, its skills and their borders, and its principles, written to `docs/principles.md` for `prepare` to pick up;
  - for a change, its case and every decision it needs;
  - in both, rounds of questions with a recommended answer each, accepted unless you contest it, then the work split into ready backlog issues that `train` builds one at a time, each with its acceptance criteria, blockers and model tier.
- **prepare** sets up a plugin repository, new or existing:
  - what's missing of the skeleton, and the principles your skills follow;
  - a CLAUDE.md with the project's facts, recommending pull requests and a backlog in GitHub issues when `gh` is signed in, and offering to create the GitHub repository when there's none;
  - the backlog's home: the `ready` and `needs-clarification` labels in GitHub issues, or a `backlog/` folder, with an existing BACKLOG.md moved into it;
  - settings that turn off conflicting plugins and skills, and the installed copy of the plugin itself, in its own repository (except for sensei itself, whose installed copy does the maintenance);
  - the rules of an old process document moved into place.
- **log** keeps the backlog (ideas, bugs and debt, each from its case and marked ready or needing clarification, in GitHub issues or a `backlog/` folder), shows what to take next, and keeps `CHANGELOG.md` (what changed in each version).
- **train** creates or changes a skill:
  - the real case, a check that the request is ready to plan (one that needs clarification goes to `meditate`), and a change plan you approve;
  - the edit on a branch, reaching every sibling skill that states the same rule;
  - then checks, independent reviews, a test scaled to the change, the changelog entry and the merge.

  It also judges issues and pull requests, audits consistency and recreates skills from old ones.
- **help** presents sensei: the cycle, each skill and how to call it, and where to start in the current folder; it also answers what a term of the process means, and points to `/sensei:spar` when asked to judge a skill.
- **spar**, run by hand as `/sensei:spar`, evaluates one skill made outside sensei, loose or in a plugin, with no setup: the check script and an independent review, judged by the plugin's principles or `train`'s writing guide, then what recreating it with sensei would change and the next step. It writes nothing.
- **graduate** releases a version: number, checks, changelog, `plugin.json`, tag, push, and one zip per skill when your skills stand alone, or one zip of the whole plugin otherwise.

### Reviewers

Two read-only agents review changes for `train`, and a skill made elsewhere for `spar`:
- **examiner** judges a new skill's architecture, every skill's in an audit, or one made elsewhere, and lists the sentences that can be cut;
- **sweeper** finds leftovers, contradictions, redundancy, drift between skills, broken references, inconsistent terms, vague instructions and scope overlap.

### The check script

`scripts/check.py` checks:
- sizes and description lengths against your principles, and, on a branch, each changed SKILL.md's and description's size and growth against main (information only);
- names across folders, README, manifests and any file marked `<!-- sensei:listing -->`;
- the files each skill points to, each path resolving from the file that names it;
- the changelog's structure, and that each branch changing the plugin has a changelog entry;
- `claude plugin validate`, on an archive of the last commit.

It also prints a scope map of your skills. With `--skill <folder>`, it checks one skill on its own, loose or in a plugin: its frontmatter, sizes and the files it points to.

Sensei needs Claude Code with `claude plugin validate` and `claude plugin eval`.

### How a change goes

| Kind | Plan | Branch | Reviews | Test |
|---|---|---|---|---|
| Wording fix | no | with pull requests | none | none |
| Behavior change | yes | yes | sweeper | a cold reader |
| Description change | yes | yes | sweeper | trigger suite (`claude plugin eval`) |
| New skill or rewrite | yes | yes | examiner and sweeper | a cold reader and the trigger suite |

### How it is built

The principles sensei follows, and the questions used to judge a proposed change, are in [docs/principles.md](docs/principles.md).

`train`'s guidance on writing and testing skills is adapted from Anthropic's [skill-creator](https://github.com/anthropics/claude-plugins-official/tree/main/plugins/skill-creator) (Apache 2.0). Its ideas are rewritten in our own words, not copied.

## Status

Early and experimental (before 1.0). See [CHANGELOG.md](CHANGELOG.md).

## Contributing

Issues and pull requests are welcome. The most useful report is a real case: what you asked a skill, what it did and what it should have done.

## License

[MIT](LICENSE)
