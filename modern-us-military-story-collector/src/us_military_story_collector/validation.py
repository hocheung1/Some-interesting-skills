from __future__ import annotations

from .models import Assessment, Claim, Conflict, Grade

MODERN_START_YEAR = 1990


def assess_claim(claim: Claim, conflicts: list[Conflict], modern_start_year: int = MODERN_START_YEAR) -> Assessment:
    reasons: list[str] = []
    if claim.event_year is None:
        reasons.append("event year is missing; modern-war scope cannot be checked")
    elif claim.event_year < modern_start_year:
        reasons.append(f"event year {claim.event_year} predates default modern scope ({modern_start_year}–present)")
    active_conflicts = [c for c in conflicts if c.claim_id == claim.id and not c.resolved]
    if active_conflicts:
        reasons.append("unresolved source conflict: " + "; ".join(c.description for c in active_conflicts))

    authoritative = [s for s in claim.sources if s.is_primary or s.is_official]
    independent = [s for s in claim.sources if s.is_independent_reporting]
    distinct_independent_publishers = {s.publisher.strip().lower() for s in independent}
    primary_publishers = {s.publisher.strip().lower() for s in authoritative}
    genuinely_second = [s for s in independent if s.publisher.strip().lower() not in primary_publishers]
    if not authoritative:
        reasons.append("no official or primary source")
    if not genuinely_second:
        reasons.append("no genuinely independent second source; reposts and syndication do not count")
    if len(claim.sources) != len({s.url for s in claim.sources}):
        reasons.append("duplicate source URL supplied")

    scope_ok = claim.event_year is not None and claim.event_year >= modern_start_year
    corroborated = bool(authoritative and genuinely_second)
    if not scope_ok or active_conflicts:
        return Assessment(Grade.D, False, reasons)
    if claim.core and corroborated:
        grade = Grade.S if len(distinct_independent_publishers) >= 2 and len(authoritative) >= 2 else Grade.A
        return Assessment(grade, True, reasons or ["primary/official and independent corroboration verified"])
    if not claim.core and authoritative:
        return Assessment(Grade.B, True, reasons or ["non-core claim has authoritative attribution"])
    return Assessment(Grade.C, False, reasons)
