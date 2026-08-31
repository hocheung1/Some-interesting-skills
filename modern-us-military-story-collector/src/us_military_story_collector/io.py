from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from .models import Claim, Conflict, Photo, Source


def load_story(path: str | Path) -> tuple[list[Claim], list[Photo], list[Conflict]]:
    data: dict[str, Any] = json.loads(Path(path).read_text(encoding="utf-8"))
    claims = []
    for raw in data.get("claims", []):
        sources = tuple(Source(**source) for source in raw.pop("sources", []))
        claims.append(Claim(sources=sources, **raw))
    photos = []
    for raw in data.get("photos", []):
        for key in ("identity_evidence_urls", "related_claim_ids"):
            raw[key] = tuple(raw.get(key, []))
        photos.append(Photo(**raw))
    conflicts = [Conflict(source_urls=tuple(raw.get("source_urls", [])), **{k: v for k, v in raw.items() if k != "source_urls"}) for raw in data.get("conflicts", [])]
    return claims, photos, conflicts
