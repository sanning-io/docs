# Triage Labels

Matt Pocock's skills speak in five triage roles. This file says what each role is in Linear (team SAN). Linear's default statuses are Triage, Backlog, Todo, In Progress, In Review, Done, Canceled and Duplicate.

| Role in the skills | In Linear |
| ------------------ | --------- |
| `needs-triage` | Triage status |
| `needs-info` | Needs info label |
| `ready-for-agent` | Todo, plus the Agent label (a founder sets it) |
| `ready-for-human` | Todo, assigned to a person (a founder sets it) |
| `wontfix` | Canceled, with a comment |

A role that maps to a status is set with `state`; a role that maps to a label is added with `addLabels`. Only a founder applies `ready-for-agent` or `ready-for-human`, because both move an issue to Todo: see "Rules for agents" in `issue-tracker.md`.

## The other labels

Use only these. Linear's own: **Bug**, **Feature**, **Improvement**. Ours, each for a job Linear has no default for:

- **Agent**: ready for an agent to pick up. A founder sets it.
- **Decision**: a call a named founder must make. Assigned to that founder, and linked as a blocker of the work that waits on it. Only its owner closes it.
- **Design**: user-facing design work, or a design question that work waits on.
- **Needs info**: waiting on the person who filed it.
- **Wayfinder group** (`map`, `research`, `prototype`, `grilling`, `task`): the ticket types `/wayfinder` uses, only in a project being shaped.

A workstream or a topic is a project, never a label.
