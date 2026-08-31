# Modern U.S. Military Story Collector

An evidence-first research pipeline for modern U.S. military human-interest stories and reusable photo leads. It is designed to make unsupported narrative details hard to publish.

## Non-negotiable research rules

- **Scope:** 1990 to the present by default. World War II and Vietnam material is rejected unless explicitly enabled.
- **Facts:** A core claim needs a primary/official source and a genuinely independent second publisher. Syndication, mirrors, and reposts are not independent corroboration.
- **Photos:** A photograph's subject identity, original page, caption, date, photographer, and rights are separately recorded and verified. A caption alone is not a licence.
- **No quota pressure:** The desired range is 5–10 verified photos; fewer is correct when evidence is scarce. Unverified photos never enter the report's final photo set.
- **Conflicts:** Competing claims are retained, attributed, and marked unresolved rather than guessed away.
- **Confidence:** S/A/B/C/D grades are calculated from evidence; only S/A/B claims can enter the final fact body.

See [docs/research-protocol.md](docs/research-protocol.md) for the full decision rules.

## Quick start

```bash
cd modern-us-military-story-collector
python -m pip install -e .[dev]
us-story-collector validate examples/story-candidate.json
us-story-collector report examples/story-candidate.json --output report.md
python -m unittest discover -s tests -v
```

`validate` produces machine-readable verification results; `report` writes only eligible facts and fully verified photo records. The example intentionally includes findings that are excluded, so reviewers can see the safeguards working.

## Live discovery

Configure endpoints in `config/sources.toml`, then run:

```bash
us-story-collector discover --query "medic humanitarian rescue" --config config/sources.toml
```

The DVIDS adapter expects JSON search results and can be pointed at an approved DVIDS API/search proxy. The official-sites adapter searches configured official JSON endpoints. Network collection is deliberately separate from validation: discovery returns leads, never publishable facts.

## Layout

- `SKILL.md` — agent-facing operating procedure.
- `src/` — discovery, provenance modelling, verification, photo checks, reports, and CLI.
- `schemas/` — portable JSON schemas.
- `config/` — endpoint configuration.
- `examples/` — safe demonstration input.
- `tests/` — offline unit and pipeline tests.
- `docs/` — editorial protocol and data model.

## Legal and editorial note

This tool records rights statements; it does not grant permission to reuse a photo. Follow the source's actual licence/terms and any privacy, operational-security, and editorial-review requirements.
