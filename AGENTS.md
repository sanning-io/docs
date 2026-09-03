# Sanning docs — agent instructions

## About this project

- The public documentation for Sanning (sanning.io), built on [Mintlify](https://mintlify.com). Repo: `sanning-io/docs`. Pushes to `main` deploy.
- Pages are MDX files with YAML frontmatter. Configuration lives in `docs.json`.
- Work on a branch and open a PR; never commit to `main`. Preview locally with `mint dev`; run `mint validate` and `mint broken-links` before opening the PR.
- For Mintlify product knowledge (components, configuration, writing standards), install the Mintlify skill: `npx skills add https://mintlify.com/docs`. The Mintlify MCP server is `https://mcp.mintlify.com`; the Mintlify docs MCP server is `https://www.mintlify.com/docs/mcp`.

## Brand

The brand is defined once, in [`sanning-io/sanning-design-system`](https://github.com/sanning-io/sanning-design-system). Its [`AGENTS.md`](https://github.com/sanning-io/sanning-design-system/blob/main/AGENTS.md) is the contract; never re-derive brand values from memory.

- `docs.json` carries the brand through Mintlify's own configuration only: colours from the semantic tokens (`link` for `colors.primary` and `colors.light`, `primary` for `colors.dark`, `background` for the page background), the Geist font, the lowercase wordmark, and the favicon. No custom CSS or JS on top of the framework.
- `logo/`, `favicon.svg`, and `fonts/` are copied verbatim from the design system's `assets/`. **Copied from design-system commit `82e7e45`.** When tokens or assets change upstream, re-copy them here in the same PR that bumps this line.
- Voice follows the design system's [`brand/voice.md`](https://github.com/sanning-io/sanning-design-system/blob/main/brand/voice.md): short true sentences, sentence case everywhere, buttons say exactly what happens. Never claim "safe", "compliant", "approved", "certified", or "audit-proof" — Sanning records integrity, authenticity, and provenance; the conclusion belongs to the customer's auditors. No hype words, no blockchain vocabulary ("anchored", "permanent", "independent" — never "on-chain", "web3", "trustless").
- Technical values (code, hashes, timestamps, IDs) are always real-looking, never placeholders like `abc123`.

## Terminology

- The lifecycle is **anchor → read → verify**. The write path is "the anchor front" at `/anchor`; never "Turbo" on a customer-facing surface.
- The agent daemon is `sanningd`. Packages publish under the Sanning npm org (`@sanning/*`) and as `sanning-*` on PyPI. Nothing is `@ar.io/*` or `ario.*` on a Sanning-authored surface.
- The control plane is **not in the trust path**. Say so wherever issuance, roster, metering, or billing are described.
- Company: Sanning Inc. GitHub org: `sanning-io`. Production console: `console.sanning.io`.

## Style preferences

- Use active voice and second person ("you").
- Keep sentences concise — one idea per sentence.
- Use sentence case for headings.
- Bold for UI elements: Click **Settings**.
- Code formatting for file names, commands, paths, and code references.

## Content boundaries

- Claims about versions, packages, and shipped behaviour are verified against the `sanning-io` org repos on GitHub and against npm / PyPI, never against a local working tree.
- Product and strategy truth lives in [`sanning-io/knowledge-base`](https://github.com/sanning-io/knowledge-base); these docs describe what ships, not what is planned.
