# The CLAUDE.md `prepare` writes

The CLAUDE.md has three parts. The first two are fixed, copied as written below. The third is the project's facts, discovered in the repository or asked. The cycle's steps live in sensei's skills, not here, so an update to sensei reaches every project. Keep the file short: it loads in every session in the repository.

## Template

```markdown
# <Plugin name>

<One sentence: what the plugin is and who it's for.>

## Maintenance with sensei

This repository is maintained with the sensei plugin. If sensei is installed:
- creating or changing a skill, judging an issue or pull request, or auditing consistency: the `train` skill;
- BACKLOG.md and CHANGELOG.md: the `log` skill (`train` writes its own changelog entries);
- releasing a version: `/sensei:graduate`.

Other skills or plugins that write skills or manage these files don't apply in this repository. Without sensei, follow `docs/principles.md` and keep CHANGELOG.md in the Keep a Changelog format.

**The skills are the object of the work here, not tools.** When the conversation is about the plugin's subject (<the subject, e.g. "prompts, projects and knowledge files">), it's about improving the skills. Don't run a skill's flow unless explicitly asked to use it.

## Project facts

- **Documents:** English. <or the language the maintainer asked for>
- **Principles:** `docs/principles.md`. Every change is checked against them.
- **Skills stand alone:** <yes: each skill reads nothing outside its folder, so a shared rule is written in every skill that needs it, and each release ships one zip per skill | no: each release ships one zip of the whole plugin>
- **Validate:** sensei's check script on every change (it runs `claude plugin validate` on the last commit); `--release` at release, which adds `--profile directory`.
- **Commits:** <author, if fixed>; <trailers: none | the environment's default>.
- **Integration:** <local merge with `--no-ff`; push main when the maintainer says so or at release | pull requests: …>
- **Tags:** <`vX.Y.Z` | `{name}--v{version}` with `claude plugin tag`>
- <Each rule specific to this repository, one line each.>
```

## Filling the facts

- **Look before asking.**
  - Existing tags (`git tag`) give the tag format.
  - The git log gives the commit author and whether trailers appear.
  - The README's install section says whether there are per-skill zips.
  - The principles say whether skills stand alone.
- **Repo-specific rules** come from the old process document, if any: a reference repository to read but never change, a reminder owed to another project, a file that must stay in sync. Keep each one as one line, with its reason when the reason isn't obvious.
- **Leave out:**
  - the cycle's steps, because the skills own them;
  - personal preferences, such as the language to talk in or how the maintainer likes answers, which go to the user-level CLAUDE.md;
  - anything already in `docs/principles.md`, except whether skills stand alone, which `train` and `graduate` read here.

## An existing CLAUDE.md

Don't overwrite it. Show what changes, section by section: what's added, what the new text replaces, what stays. Keep everything project-specific that's still true. On a re-run of `prepare`, refresh only the "Maintenance with sensei" section from the template above, and propose fact changes only where the repository now says something different. When the plugin being maintained is sensei itself, keep its "Maintenance with sensei" section as it is: it is adapted to a plugin that maintains itself (its fallback points to the repository's own `skills/train/SKILL.md`).
