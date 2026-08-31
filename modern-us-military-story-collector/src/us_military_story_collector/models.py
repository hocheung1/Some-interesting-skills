from __future__ import annotations

from dataclasses import asdict, dataclass, field
from enum import Enum
from typing import Any


class Grade(str, Enum):
    S = "S"  # multiple authoritative, independently corroborated records
    A = "A"  # primary + independent corroboration
    B = "B"  # clear, attributable, but not ideal corroboration
    C = "C"  # plausible lead; never final body text
    D = "D"  # unsupported, contradictory, or out of scope


@dataclass(frozen=True)
class Source:
    url: str
    publisher: str
    title: str = ""
    published_date: str | None = None
    source_type: str = "official"  # official, primary, independent, repost, social, unknown
    original_reporting: bool = True
    is_primary: bool = False
    is_official: bool = False
    notes: str = ""

    @property
    def is_independent_reporting(self) -> bool:
        return self.source_type == "independent" and self.original_reporting


@dataclass(frozen=True)
class Claim:
    id: str
    text: str
    event_year: int | None
    core: bool = True
    sources: tuple[Source, ...] = ()


@dataclass(frozen=True)
class Conflict:
    claim_id: str
    description: str
    source_urls: tuple[str, ...]
    resolved: bool = False


@dataclass(frozen=True)
class Photo:
    id: str
    asset_url: str
    original_page_url: str | None = None
    depicted_person: str | None = None
    caption: str | None = None
    photographer: str | None = None
    capture_date: str | None = None
    copyright_status: str | None = None
    identity_evidence_urls: tuple[str, ...] = ()
    rights_evidence_url: str | None = None
    related_claim_ids: tuple[str, ...] = ()


@dataclass
class Assessment:
    grade: Grade
    eligible_for_final: bool
    reasons: list[str] = field(default_factory=list)


@dataclass
class StoryAssessment:
    claims: dict[str, Assessment]
    photos: dict[str, Assessment]
    conflicts: list[Conflict]
    scope_notes: list[str]

    def to_dict(self) -> dict[str, Any]:
        return {
            "claims": {key: {"grade": value.grade.value, "eligible_for_final": value.eligible_for_final, "reasons": value.reasons} for key, value in self.claims.items()},
            "photos": {key: {"grade": value.grade.value, "eligible_for_final": value.eligible_for_final, "reasons": value.reasons} for key, value in self.photos.items()},
            "conflicts": [asdict(item) for item in self.conflicts],
            "scope_notes": self.scope_notes,
        }
