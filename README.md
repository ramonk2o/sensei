# Sensei

A lean maintenance cycle for Claude Code skill plugins. Sensei sets up a plugin repository, keeps its backlog and changelog, carries each change to a skill from a real case to a merge, and releases versions. A script handles the checks that are certain, and readers who never saw the conversation handle the ones that need judgment.

The skills are written in English and talk to you in your own language. Everything they write to your repository is in English unless you ask for another language.

## Skills

The names come from the dojo.

- **hajime** ("begin") sets up a plugin repository, new or existing:
  - what's missing of the skeleton, and the principles your skills follow;
  - a CLAUDE.md with the project's facts;
  - settings that turn off conflicting plugins and skills, and the installed copy of the plugin itself, in its own repository (except for sensei itself, whose installed copy does the maintenance);
  - the rules of an old process document moved into place.

  Run it with `/sensei:hajime`.
- **kanban** ("board") keeps `BACKLOG.md` (ideas, bugs and debt, each from a real case) and `CHANGELOG.md` (what changed in each version).
- **kata** ("form") creates or changes a skill:
  - the real case, rounds of questions with recommended answers, and a change plan you approve;
  - the edit on a branch, reaching every sibling skill that states the same rule;
  - then checks, independent reviews, a test scaled to the change, the changelog entry and the merge.

  It also judges issues and pull requests, audits consistency and recreates skills from old ones.
- **shodan** ("first degree") releases a version: number, checks, changelog, `plugin.json`, tag, push, and one zip per skill when your skills stand alone. Run it with `/sensei:shodan`.

Two read-only agents review changes for kata:
- **shihan** ("master instructor") judges a new skill's architecture;
- **soji** ("the cleaning after practice") finds leftovers, contradictions, redundancy, drift between skills, broken references, inconsistent terms, vague instructions and scope overlap.

`scripts/check.py` checks:
- sizes and description lengths against your principles;
- names across folders, README and manifests;
- the files each skill points to;
- the changelog's structure, and that each branch changing the plugin has a changelog entry;
- `claude plugin validate`, on an archive of the last commit.

It also prints a scope map of your skills.

## How a change goes

| Kind | Plan | Branch | Reviews | Test |
|---|---|---|---|---|
| Wording fix | no | no | none | none |
| Behavior change | yes | yes | soji | a cold reader |
| Description change | yes | yes | soji | trigger suite (`claude plugin eval`) |
| New skill or rewrite | yes | yes | shihan and soji | a cold reader and the trigger suite |

Nothing is edited before you approve the plan, nothing is merged before you approve the change, and nothing is released before you approve the version.

## Status

Early and experimental (before 1.0). See [CHANGELOG.md](CHANGELOG.md).

## Install

```
/plugin marketplace add ramonk2o/sensei
/plugin install sensei@sensei
```

Then open your plugin's repository and run `/sensei:hajime`. Sensei needs Claude Code with `claude plugin validate` and `claude plugin eval`, `git`, and Python 3.

## How it is built

The principles sensei follows, and the questions used to judge a proposed change, are in [docs/principles.md](docs/principles.md).

kata's guidance on writing and testing skills is adapted from Anthropic's [skill-creator](https://github.com/anthropics/claude-plugins-official/tree/main/plugins/skill-creator) (Apache 2.0). Its ideas are rewritten in our own words, not copied.

## Contributing

Issues and pull requests are welcome. The most useful report is a real case: what you asked a skill, what it did and what it should have done.

## License

[MIT](LICENSE)
