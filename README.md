# Sanning docs

The public documentation for [Sanning](https://sanning.io), served at docs.sanning.io and built on [Mintlify](https://mintlify.com). Pushes to `main` deploy.

## Working on it

Pages are MDX files with YAML frontmatter. Navigation, colours, logo, and fonts are set in `docs.json`.

```sh
npm i -g mint        # once
mint dev             # preview at http://localhost:3000
mint validate        # strict build check
mint broken-links    # link check
```

Work on a branch and open a pull request. Never commit to `main`.

## Brand

The brand is defined once, in [`sanning-design-system`](https://github.com/sanning-io/sanning-design-system). This site carries it through Mintlify's own configuration: colours from the semantic tokens, the Geist font, the lowercase wordmark, and the favicon. `logo/`, `favicon.svg`, and `fonts/` are copied verbatim from that repo's `assets/`. The design-system commit they came from is recorded in [`AGENTS.md`](AGENTS.md), which also holds the voice and terminology rules for anyone writing here.

## Agents

Read [`AGENTS.md`](AGENTS.md) first. For Mintlify's component and configuration reference, install their skill: `npx skills add https://mintlify.com/docs`.
