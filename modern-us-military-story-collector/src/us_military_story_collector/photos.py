from __future__ import annotations

from .models import Assessment, Grade, Photo

REQUIRED_FIELDS = ("asset_url", "original_page_url", "depicted_person", "caption", "photographer", "capture_date", "copyright_status")


def assess_photo(photo: Photo, verified_claim_ids: set[str]) -> Assessment:
    reasons: list[str] = []
    for field in REQUIRED_FIELDS:
        if not getattr(photo, field):
            reasons.append(f"missing required photo metadata: {field}")
    if not photo.identity_evidence_urls:
        reasons.append("missing separate evidence that the named person is pictured")
    if not photo.rights_evidence_url:
        reasons.append("missing separate rights/copyright evidence")
    if photo.related_claim_ids and not set(photo.related_claim_ids).issubset(verified_claim_ids):
        reasons.append("photo links to a claim that is not eligible for final narrative")
    if reasons:
        return Assessment(Grade.D if len(reasons) > 2 else Grade.C, False, reasons)
    return Assessment(Grade.A, True, ["identity and rights were independently recorded; required metadata complete"])
