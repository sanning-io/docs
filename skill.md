---
name: sanning
description: Use Sanning when an AI agent must produce evidence of what it did that a third party can verify without trusting you or Sanning. Use it to anchor agent steps with the Sanning SDKs, build an evidence pack, or verify a pack someone handed you. Start in the sandbox with a sandbox API key.
metadata:
  docs: https://docs.sanning.io
---

# Sanning

Sanning records what an AI agent does so a third party can check it later without trusting you or Sanning. The agent hashes each step locally and signs a commitment. Sanning stores the signed envelope, never the content, and seals the envelopes into a stamp on the public record. Verification runs offline, on the checker's machine, with an open-source kernel.

The lifecycle is anchor, read, verify.

## Event types

Read the event types page before you write any record: https://docs.sanning.io/reference/event-types. It is the single place for names. Every agent record has one of 19 `agent.*` types, for example `agent.run_opened`, `agent.model_call.started`, `agent.tool_call.ended`, `agent.decision` and `agent.file`. A name outside the set makes the pack `failed` with the reason kind `nonconforming`, shown as "Failed: a record does not follow the rules." (exit 1). Plain `anchor()` builds an `event` record and refuses an `agent.*` type. An adapter writes the right `agent.*` type for each moment, or you build one with the agent record builder in https://docs.sanning.io/guides/anchor; the table of moments, events and what Sanning receives is at https://docs.sanning.io/guides/what-to-record.

Sanning receives ids, times, outcomes and each record's type, with no content, no content hash, no names and no model details. Sanning receives the case id, run ids, chain key, conversation id and agent id in clear; use an opaque id when a case id would be personal data. The SDK refuses to sign a record that breaks the schema, and `recordingStatus().refused` (`recording_status().refused` in Python) lists each refused record by event id, type, reason and pointer. Every record carries a random salt that the SDK writes and Sanning does not receive. To check an integration, run the conformance suite in `sanning-io/specs`: https://docs.sanning.io/reference/specs-and-conformance.

## Start in the sandbox

Every new integration starts in the sandbox. One host serves both modes, and the API key decides which one a request reaches.

| | Sandbox | Live |
|---|---|---|
| API key prefix | `sanning_test_` | `sanning_prod_` |
| Signed `environment` | `"dev"`, set by the SDK from the key | `"production"` |
| Stamp | Simulated, never reaches the public record | Reaches the public record and stays there |
| Records | Deleted after 30 days; Reset clears them | Permanent |
| Offline verify | Sandbox line, exit code 3 | `Verified`, exit code 0 |

A person creates the API key in the console: sign in at `https://console.sanning.io`, open the account menu, choose **Switch to sandbox**, then **Settings, API keys, Create key**. Every key carries the three anchor scopes (`agent:enroll`, `anchor:write`, `anchor:read`); scopes are not chosen one at a time. You cannot create an organization or an API key through the API on your own; access starts with the Sanning team.

Requests go to `https://api.sanning.io`. A live plane refuses a sandbox API key (`SANDBOX_KEY_ON_LIVE`), and a sandbox refuses a live one (`LIVE_KEY_ON_SANDBOX`). Every sandbox response carries the header `Sanning-Mode: sandbox`.

## Set up

1. Install the SDK: `npm install @sanning/anchor` (Node.js 22 or later) or `pip install sanning-anchor` (Python 3.11 or later).
2. Make the agent's signing seed once and keep it: `openssl rand -hex 32`. Store it as `SANNING_SIGNING_SEED` in a secret store and load the same value on every start. A new seed on each start makes a new agent identity, and a second key for the same agent is refused as an unauthorized rotation.
3. Set `SANNING_API_KEY` to the sandbox API key.

Never commit the API key or the seed, and never send either to Sanning in content. Sanning never receives the seed.

## Anchor a step

```ts
import { createAnchorer, FsLogStore, LocalEd25519Signer } from "@sanning/anchor";

const anchorer = createAnchorer({
  apiKey: process.env.SANNING_API_KEY!,
  subject: { type: "agent", agent_id: "claims-triage" },
  signer: LocalEd25519Signer.fromSeedHex(process.env.SANNING_SIGNING_SEED!),
  logStore: new FsLogStore("./logstore"),
});
await anchorer.anchor({ content: JSON.stringify({ claim: "CLM-4417", action: "referred" }) });
await anchorer.close(); // throws if any signed event was not delivered
```

```python
import json
import os
from sanning_anchor import Anchorer, FsLogStore, LocalEd25519Signer

anchorer = Anchorer(
    api_key=os.environ["SANNING_API_KEY"],
    subject={"type": "agent", "agent_id": "claims-triage"},
    signer=LocalEd25519Signer.from_seed_hex(os.environ["SANNING_SIGNING_SEED"]),
    log_store=FsLogStore("./logstore"),
)
anchorer.anchor(content=json.dumps({"claim": "CLM-4417", "action": "referred"}).encode())
anchorer.close()
```

- Pass no `environment`: the SDK signs it from the API key.
- The SDK enrolls the signing key on the first anchor; the agent then appears on the console's **Agents** page.
- The log store keeps the content on your side. The pack step reads it, so keep the directory.
- For LangChain, use `AnchorCallbackHandler(anchorer, raise_on_gaps=True)` as a context manager; for the Vercel AI SDK, see the Vercel guide in Pages.

## Build a pack and verify it

A record can go into a pack once its stamp has sealed. In the sandbox that takes about a minute. Until then, `bundle` exits 3 and says the records are not yet stamped: wait and run it again.

```bash
npx @sanning/anchor bundle --agent claims-triage --from 2026-10-27 --to 2026-10-27 --logs ./logstore --out pack.zip
unzip pack.zip -d pack && cd pack
npx @sanning/proof verify bundle.json --logs logs/
```

The Python commands take the same flags: `sanning-anchor bundle ...` and `sanning-proof verify ...`. `bundle` reads `SANNING_API_KEY` from the environment.

Verify exit codes: 0 verified, 1 failed (a claim is disproven; the output names the record), 2 incomplete (nothing is disproven and something could not be checked), 3 sandbox (verified, and the records are sandbox evidence), 4 could not run (a bad flag, a missing file, or an input that is not a pack or case). The verdict words are `verified`, `failed` and `incomplete`. A person can also drop the pack on `https://verify.sanning.io`.

## Go live

Switch to a `sanning_prod_` API key. A live agent enrolls fresh: sandbox and live identities are separate. Live records are permanent once their stamp reaches the public record, so try everything in the sandbox first. Use durable storage for the log store, such as an S3-compatible bucket.

## Rules

- Content never leaves your side; only the signed record does. Ids are never hashed and reach Sanning in clear, so keep secrets and personal data out of `agent_id` and every id.
- Keep one signing seed per agent, for the agent's life.
- Treat exit code 3 as "sandbox", never as production evidence.
- Sanning is not in the trust path: a pack verifies offline without Sanning.

## Pages

- Event types: https://docs.sanning.io/reference/event-types
- What to record: https://docs.sanning.io/guides/what-to-record
- Hide, reveal and scrub fields: https://docs.sanning.io/concepts/hide-and-reveal-fields
- What a pack proves: https://docs.sanning.io/concepts/what-a-pack-proves
- Specs and conformance: https://docs.sanning.io/reference/specs-and-conformance
- Glossary: https://docs.sanning.io/reference/glossary
- Quickstart: https://docs.sanning.io/quickstart
- Sandbox and live: https://docs.sanning.io/concepts/sandbox-and-live
- Go live: https://docs.sanning.io/guides/go-live
- LangChain: https://docs.sanning.io/guides/langchain
- Vercel AI SDK: https://docs.sanning.io/guides/vercel
- Errors: https://docs.sanning.io/reference/errors
- CLI: https://docs.sanning.io/reference/cli
- Every page as Markdown: https://docs.sanning.io/llms.txt
