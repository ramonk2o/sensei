# Model tiers

A backlog entry's Model field names a tier, not a model, so the entry stays right when models change. This is the only file in sensei that names models: when a new family or generation changes which one fits a tier, update the table here.

| Tier | For | Model |
|---|---|---|
| `light` | a wording fix | Haiku (`haiku`) |
| `medium` | a behavior or description change to an existing skill | Sonnet (`sonnet`) |
| `strong` | a new skill, a full rewrite, or a change to what several skills share (a format, the borders between them) | Opus (`opus`) |

When the kind of change is in doubt, take the stronger tier. The names in parentheses are Claude Code's model aliases (for `/model`, `--model` and an agent's `model` field), which follow each family's latest version.
