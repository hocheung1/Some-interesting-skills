from __future__ import annotations

from .models import Claim, Conflict, Photo, StoryAssessment
from .photos import assess_photo
from .validation import assess_claim


def assess_story(claims: list[Claim], photos: list[Photo], conflicts: list[Conflict]) -> StoryAssessment:
    claim_results = {claim.id: assess_claim(claim, conflicts) for claim in claims}
    verified_claim_ids = {claim_id for claim_id, result in claim_results.items() if result.eligible_for_final}
    photo_results = {photo.id: assess_photo(photo, verified_claim_ids) for photo in photos}
    scope_notes = [
        "Default chronology: 1990–present. Earlier conflicts require explicit requester approval.",
        "Final fact body contains only S/A/B claims; rejected leads remain available in the audit output.",
        "Photo target is 5–10, but the report will not pad the set with unverified assets.",
    ]
    return StoryAssessment(claim_results, photo_results, conflicts, scope_notes)
