# Triage Labels

Matt Pocock's skills speak in five triage roles. Sanning uses them literally: each role is a Linear label (team SAN) with the same name, and there is no translation layer.

## State roles (labels)

- `needs-triage`: a founder has not yet looked at it.
- `needs-info`: waiting on the person who filed it.
- `ready-for-agent`: fully specified, an agent can take it. Only a founder applies it.
- `ready-for-human`: needs a person to do it. Only a founder applies it.
- `wontfix`: will not be done.

Add or remove a label with `addLabels` and `removeLabels` in `save_issue`.

## Category (labels)

`bug` and `enhancement`, Matt's two. Linear's Bug, Feature and Improvement labels are not used.

## Statuses

Linear's defaults only: Triage, Backlog, Todo, In Progress, In Review, Done, Canceled and Duplicate. A status says where an issue is in the workflow; a label carries its triage role. They combine like this:

- An issue in Triage carries `needs-triage`.
- `wontfix` goes with Canceled, and a comment says why.
- `ready-for-agent` and `ready-for-human` go on an issue a founder has moved to Todo.

Only a founder applies `ready-for-agent` or `ready-for-human`: see "Rules for agents" in `issue-tracker.md`.

## The other labels

Ours, each for a job Matt's set has no equivalent for:

- **Decision**: a call a named founder must make. Assigned to that founder, and linked as a blocker of the work that waits on it. Only its owner closes it.
- **Design**: user-facing design work, or a design question that work waits on.
- **`soc`** and **`smoke`**: kept as they are.
- **Wayfinder group** (`map`, `research`, `prototype`, `grilling`, `task`): the ticket types `/wayfinder` uses, only in a project being shaped.

A workstream or a topic is a project, never a label.
