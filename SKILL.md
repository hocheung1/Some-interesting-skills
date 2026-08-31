# Modern U.S. Military Story Collector

Use this skill when researching a real modern U.S. military person, their story, and related images.

## Operating sequence

1. Set the story window to **1990–present**. Do not search or include World War II or Vietnam unless the requester explicitly opts in.
2. Discover leads from DVIDS, service/DoD sites, and first-party records. Treat discovery text as a lead only.
3. Convert each proposed statement into an atomic `Claim` with citations.
4. For each core claim, require one official/primary record **and** a second source from a different, genuinely independent publisher. Exclude syndicated wire copies, mirrors, and reuse of the first source's reporting.
5. Record disagreement as a conflict. Do not reconcile it by inference.
6. For every photo, independently verify: original asset page, subject identity, photographer/creator, capture date, full caption, and rights statement. Identity evidence and rights evidence must be separate fields.
7. Grade every claim and photo S/A/B/C/D. Only S/A/B claims and fully verified photos are allowed into the final narrative report.
8. Aim for 5–10 photographs only if that many meet the bar. Return fewer with an explicit gap note instead of padding the set.

## Guardrails

- Do not turn an allegation, inference, social post, reprint, or unverified caption into a final fact.
- Do not assume a U.S. government page means every image is public domain; record its actual statement.
- Do not use a photo of a unit or event as proof that a named person is pictured.
- Keep machine validation JSON alongside the human report so an editor can audit exclusions.
