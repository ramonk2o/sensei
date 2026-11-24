# Glossary

What each term of the process means, for a user who has never used git, GitHub or skills. Use it the first time a term comes up in a conversation: say it in the user's language, in plain words, with the term in bold beside it, and add why it matters at that moment. Each entry gives the meaning, then why it matters; adapt the wording to what is happening, and say it once per conversation.

Tone: "Before setting up, I need to agree with you on the plugin's **principles**: the rules all your skills follow, such as 'always write in Portuguese'. I check every change against them, so it's worth settling them now."

## Sensei's concepts

- **Principles:** the rules every skill in the plugin follows, written down once in the project. Every change is checked against them, so a principle is named by what it says, not by its number.
- **Backlog:** the list of what is left to do: ideas, problems to fix and loose ends. Nothing is lost between sessions, and you choose what comes next from it.
- **Issue:** one task in the backlog, with a title and a description: on GitHub, a numbered page you see in the browser, where others can read and comment; otherwise, a file in the project's `backlog/` folder. Big work is split into several issues so each piece is small, built one at a time and easy to review or undo.
- **Ready / needs clarification:** an issue is ready when it can be built without asking you anything more and is small enough for one pull request; otherwise it needs clarification, and the open decisions are settled with you first. Building something unsettled means guessing, and a wrong guess is redone later.
- **Blocked by:** an issue that can't start until another one is done, because it builds on it. The blocked one waits; the one blocking it goes first.
- **Model tier:** how capable an AI model (the engine behind the assistant) a task needs: light for a wording fix, medium for a change to an existing skill, strong for a new skill, a rewrite or a change several skills share. A stronger model costs more, so each task gets the lightest one that does it well.
- **Cold reader:** a fresh assistant that sees only the skill's files, not this conversation, and is asked what it would do with a request. A skill runs without the conversation that wrote it, so this shows whether the text alone works.
- **Changelog:** a file that lists, version by version, what changed for the people who use the plugin. It's how they learn what an update brings.
- **Version:** the plugin's number, such as 1.4.0, raised at each release. People who installed the plugin receive changes only when it goes up.

## Git and GitHub

- **Git and GitHub:** git keeps the full history of the project's files on your computer; GitHub is a website that keeps a copy online, where others can see it and work on it. Together they let every change be reviewed and undone.
- **Branch:** a separate copy of the project where a change is made, so the main version isn't touched until you approve it. If the change goes wrong, the branch is dropped and nothing else is affected.
- **Commit:** a saved step in the project's history, with a short note on what changed. Any step can be looked at again or undone.
- **Pull request:** a request, on GitHub, to bring a branch into the main version; it shows exactly what changed, line by line. It's where a change is reviewed before it's accepted.
- **Merge:** bringing a branch's changes into the main version. After it, the change is part of the plugin.
- **Tag:** a fixed label on one point of the history, such as v1.4.0, marking a release. It lets anyone get that exact version back.

## A plugin and its skills

- **Plugin:** a package of skills (and sometimes helpers) that people install into Claude Code together. It's what gets a version and a release.
- **Skill:** a set of written instructions the assistant follows for one kind of request, such as writing a post or reviewing one. The assistant reads it only when a request calls for it.
- **SKILL.md:** the skill's main file. Its top lines (the description) tell the assistant when to use the skill and are always in view; the rest, the steps, is read in full each time the skill runs, so it holds only what every run needs.
- **references/:** a folder of texts that only one step or one kind of request needs, such as a format or a checklist. Each is read only at the step that names it, which keeps the skill fast and focused.
- **assets/:** a folder of files used as they are, such as a template to copy or a text to show. They're shown or copied rather than followed as instructions, so they come out the same every time.
- **scripts/:** a folder of small programs for mechanical work, such as counting or checking files. They run without being read, so they cost nothing to load and don't make mistakes a model would.
- **Agents:** helpers, kept in the plugin's `agents/` folder, that the assistant starts for one job with only what they're given, such as reviewing a change. Since they don't see the conversation, they judge the work without being swayed by it.
