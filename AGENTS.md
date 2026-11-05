# Sanning docs — agent instructions

## About this project

- The public documentation for Sanning (sanning.io), built on [Mintlify](https://mintlify.com). Repo: `sanning-io/docs`. Pushes to `main` deploy.
- Pages are MDX files with YAML frontmatter. Configuration lives in `docs.json`.
- Work on a branch and open a PR; never commit to `main`. Preview locally with `mint dev`; run `mint validate` and `mint broken-links` before opening the PR.
- Mintlify's own skill (components, configuration, writing standards) is installed in this repo under `.claude/skills/`; refresh it with `npx skills update`. `.mcp.json` connects Mintlify's documentation search (read-only). The admin MCP server, `https://mcp.mintlify.com`, reaches the dashboard and stays a per-founder, user-level connection — never committed here.

## Brand

The brand is defined once, in [`sanning-io/sanning-design-system`](https://github.com/sanning-io/sanning-design-system). Its [`AGENTS.md`](https://github.com/sanning-io/sanning-design-system/blob/main/AGENTS.md) is the contract; never re-derive brand values from memory.

- `docs.json` carries the brand through Mintlify's own configuration only: the colours, the page background, the Geist font, the wordmark, the favicons, and the share image. No custom CSS or JS on top of the framework.
- The design system's README section [Using it for the docs (Mintlify)](https://github.com/sanning-io/sanning-design-system#using-it-for-the-docs-mintlify) says which semantic token feeds each colour in `docs.json`, and which files to copy. Follow it, and keep no second map here.
- `logo/`, `favicon.svg`, `favicon-midnight.svg`, `og/`, and `fonts/` are copied verbatim from the design system's `assets/`. **Copied from design-system commit `b861b16`.** When tokens or assets change upstream, re-copy them here in the same PR that bumps this line.
- Voice follows the design system's [`brand/voice.md`](https://github.com/sanning-io/sanning-design-system/blob/main/brand/voice.md): short true sentences, sentence case everywhere, buttons say exactly what happens. Never claim "safe", "compliant", "approved", "certified", or "audit-proof" — Sanning records integrity, authenticity, and provenance; the conclusion belongs to the customer's auditors. No hype words. Use the approved words "anchored", "permanent" and "independent". Never use the banned blockchain words "on-chain", "web3", "trustless" or "crypto".
- Technical values (code, hashes, timestamps, IDs) are always real-looking, never placeholders like `abc123`.

## Terminology

- The product's steps are **Capture, Sign, Anchor, Verify**, the same words as the website. They explain the product on the Introduction; they do not name sidebar groups. The write path is "the anchor front" at `/anchor`; never "Turbo" on a customer-facing surface.
- The signing party is the **agent**, not the producer. Packages publish under the Sanning npm org (`@sanning/*`) and as `sanning-*` on PyPI.
- The control plane is **not in the trust path**. Say so wherever issuance, roster, metering, or billing are described.
- The two modes are **Sandbox** and **Live** in prose, and an **API key**, never a bare "key". The wire values (`sanning_test_`, `sanning_prod_`, `environment: "dev"` and `"production"`) appear in tables and reference. In a sentence, use one only where the reader must recognise it: a key prefix, or `environment: "production"` in an error they might meet. Every page is written for Live, with a Live API key. The [Quickstart](quickstart.mdx) and every guide carry one short callout near the top that says to use a Sandbox API key to test and links to [Test in the Sandbox](sandbox.mdx), the one page that explains the two modes. Never name a chain: say "the public record".
- Say **evidence pack** for the file a reviewer gets, and "evidence" in titles, as the website and the console do. Say **verdict** for Verified, Failed or Incomplete, and **reviewer** for the person who checks evidence.
- The docs are one path in four groups: Get started (Introduction, Quickstart, Test in the Sandbox), Record your agents (adapters), Evidence (build, verify), then Reference. A concept is a section on the page where a reader needs it, not a page of its own. Samples record through an adapter, never with `anchor()` calls placed through an agent's code.
- A guide holds all the code and commands that its example needs to work in Live. It links to other pages only for explanations.
- Company: Sanning Inc. GitHub org: `sanning-io`. Production console: `console.sanning.io`.

## Style preferences

- Use active voice and second person ("you").
- Keep sentences concise — one idea per sentence.
- A page does not open with "This page…". The description says what the page is for, and the first sentence of the body states the point.
- Use sentence case for headings.
- Bold for UI elements: Click **Settings**.
- Code formatting for file names, commands, paths, and code references.

## Content boundaries

- Claims about versions, packages, and shipped behaviour are verified against the `sanning-io` org repos on GitHub and against npm / PyPI, never against a local working tree.
- These docs describe what ships, not what is planned.
