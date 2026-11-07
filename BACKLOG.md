# Backlog

Ideas, bugs and debt for this plugin, managed with sensei's kanban skill. Each entry starts from a real case. Done work leaves this file: what changed goes to CHANGELOG.md.

## Plugin

### Try the cycle on a real plugin
- **Type:** Debt
- **Motivation:** no case recorded yet: sensei was designed, not used. Its first real runs (hajime on an existing plugin, a kata behavior change, a release) will show what the design missed.
- **Description:** Run hajime on an existing plugin, then one kata change and one shodan release, and record what went wrong here.
- **Open questions:**
  - Whether the permission pattern for the check script survives a sensei update.
  - Whether `attribution` with empty strings removes the commit trailer in practice.
  - Whether `claude plugin eval` with a branch checkout target behaves as `testing.md` assumes.
