from __future__ import annotations

import tomllib
from pathlib import Path

from .sources import DvidsSearchClient, DiscoveryLead, OfficialSiteSearchClient


def discover(query: str, config_path: str | Path) -> list[DiscoveryLead]:
    config = tomllib.loads(Path(config_path).read_text(encoding="utf-8"))
    leads: list[DiscoveryLead] = []
    dvids = config.get("dvids", {})
    if dvids.get("enabled"):
        leads.extend(DvidsSearchClient(dvids["search_url"], dvids.get("api_key_env", "DVIDS_API_KEY")).search(query))
    for site in config.get("official_sites", []):
        leads.extend(OfficialSiteSearchClient(site["name"], site["search_url"]).search(query))
    return leads
