---
name: introduce
description: Presents sensei to someone new to it: the cycle, each skill and how to call it, where to start in this folder, and what a term means, e.g. 'how does sensei work?', 'what is a pull request?', 'what goes in references?'. Not for the user's own plugin, or for setting a repo up (/sensei:prepare).
---

# Introduce

Shows someone new to sensei how it works and where to start, in one message, or answers what one term means. It writes and changes nothing, and asks nothing: the work belongs to the skills it presents.

Talk to the user in their language, in plain words: explain a term of the process the first time it comes up (`references/glossary.md`) and name a principle by what it says, not by its number.

A question about a term of the process or a skill's parts ("what is an issue?", "what goes in assets?") gets only its answer: the glossary's entry, meaning and why it matters, in the user's language, with no tour and no next-step line. Otherwise:

1. Read `assets/tour.md` and show everything after its marker line in the user's language: translate the text and the sample requests, and keep the skill names, the commands and the layout as they are.
2. Look at the current folder and add one line with the next step:
   - no plugin here (no `.claude-plugin/plugin.json`): `/sensei:meditate` to plan one, in an empty folder when this one holds something else;
   - a plugin whose CLAUDE.md doesn't name sensei: `/sensei:prepare` to set it up;
   - a plugin whose CLAUDE.md names sensei: ask "what's next?", which `log` answers from the backlog.
3. Before sending, check that the message has the cycle line, one row per skill in the tour and one next-step line that matches the folder. End there, with no question or offer.
