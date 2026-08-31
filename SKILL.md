---
name: modern-us-military-story-collector
description: Research and verify real modern U.S. military human-interest stories and photos when factual provenance and image rights must be audit-ready.
metadata:
  short-description: Verify modern U.S. military stories and photo leads
---

# Modern U.S. Military Story Collector

Use this skill for real-person stories and associated images involving the U.S. military. It produces an evidence ledger, a validation result, and a report that excludes unsupported material.

## Essential constraints

- Default scope is **1990–present**. Do not include World War II or Vietnam unless the requester explicitly opts in.
- A core fact needs an official/primary source and a genuinely independent second publisher. Reposts, syndication, mirrors, and reused reporting are not independent corroboration.
- Record conflicts with their sources; do not resolve them by inference.
- A photo requires its original page, caption, photographer, capture date, rights status, and separately documented evidence identifying the depicted person. A caption is not a licence, and an asset page is not automatically public domain.
- Apply S/A/B/C/D grades. Only S/A/B claims and fully verified photos enter the final narrative. Aim for 5–10 verified photos, but report fewer rather than pad the result.

## Workflow

1. Use DVIDS, service/DoD sites, and first-party records to discover leads; discovery material is never final evidence on its own.
2. Turn proposed facts into atomic claims with source records and log conflicts.
3. Collect photo metadata and record separate identity and rights evidence.
4. Validate the ledger with `us-story-collector validate <candidate.json>`, then generate the report with `us-story-collector report <candidate.json> --output <report.md>`.

## References

- Read [docs/research-protocol.md](docs/research-protocol.md) for the full grading and conflict rules.
- Use [schemas/story-candidate.schema.json](schemas/story-candidate.schema.json) for the evidence-ledger format.
- Start from [examples/story-candidate.json](examples/story-candidate.json) when creating a new ledger.
