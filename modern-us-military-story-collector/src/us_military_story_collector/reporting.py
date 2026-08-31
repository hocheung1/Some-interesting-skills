from __future__ import annotations

from .models import Claim, Photo, StoryAssessment


def markdown_report(claims: list[Claim], photos: list[Photo], assessment: StoryAssessment) -> str:
    lines = ["# Evidence-verified story report", "", "## Scope and audit rules", ""]
    lines.extend(f"- {note}" for note in assessment.scope_notes)
    lines += ["", "## Final fact body", ""]
    included_claims = [claim for claim in claims if assessment.claims[claim.id].eligible_for_final]
    if included_claims:
        for claim in included_claims:
            grade = assessment.claims[claim.id].grade.value
            citations = "; ".join(f"[{source.publisher}]({source.url})" for source in claim.sources)
            lines.append(f"- **{claim.text}** — grade {grade}. Sources: {citations}")
    else:
        lines.append("No claim met the final-publication evidence threshold.")
    lines += ["", "## Verified photographs", ""]
    included_photos = [photo for photo in photos if assessment.photos[photo.id].eligible_for_final]
    if included_photos:
        for photo in included_photos:
            lines += [
                f"### {photo.id} — {photo.depicted_person}",
                f"- Asset: {photo.asset_url}",
                f"- Original page: {photo.original_page_url}",
                f"- Caption: {photo.caption}",
                f"- Photographer: {photo.photographer}; captured: {photo.capture_date}",
                f"- Rights status: {photo.copyright_status} ([evidence]({photo.rights_evidence_url}))",
                f"- Identity evidence: {', '.join(photo.identity_evidence_urls)}",
                "",
            ]
    else:
        lines.append("No photograph met the complete identity-and-rights verification threshold.")
    lines += ["", "## Conflicts and excluded leads", ""]
    unresolved = [item for item in assessment.conflicts if not item.resolved]
    if unresolved:
        lines.extend(f"- **{item.claim_id}:** {item.description} (sources: {', '.join(item.source_urls)})" for item in unresolved)
    else:
        lines.append("No unresolved conflicts recorded.")
    rejected = [(key, result) for key, result in assessment.claims.items() if not result.eligible_for_final]
    rejected += [(key, result) for key, result in assessment.photos.items() if not result.eligible_for_final]
    if rejected:
        lines += ["", "### Exclusions (not final facts)", ""]
        lines.extend(f"- `{key}` ({result.grade.value}): {'; '.join(result.reasons)}" for key, result in rejected)
    photo_count = len(included_photos)
    if photo_count < 5:
        lines += ["", f"**Photo gap:** {photo_count} verified photos. Do not fill the 5–10 target with weaker material."]
    return "\n".join(lines) + "\n"
