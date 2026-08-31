"""Lead discovery adapters. They never confer factual verification."""
from __future__ import annotations

import json
import os
from dataclasses import dataclass
from typing import Any
from urllib.parse import urlencode
from urllib.request import Request, urlopen


@dataclass(frozen=True)
class DiscoveryLead:
    title: str
    url: str
    publisher: str
    published_date: str | None = None
    summary: str = ""
    source_kind: str = "official"


def _read_json(url: str, headers: dict[str, str] | None = None, timeout: int = 20) -> Any:
    request = Request(url, headers={"Accept": "application/json", "User-Agent": "us-story-collector/0.1", **(headers or {})})
    with urlopen(request, timeout=timeout) as response:  # nosec B310: URL comes from trusted configuration
        return json.load(response)


def _items(payload: Any) -> list[dict[str, Any]]:
    if isinstance(payload, list):
        return payload
    if isinstance(payload, dict):
        for key in ("results", "items", "data"):
            if isinstance(payload.get(key), list):
                return payload[key]
    return []


class DvidsSearchClient:
    def __init__(self, search_url: str, api_key_env: str = "DVIDS_API_KEY") -> None:
        self.search_url, self.api_key_env = search_url, api_key_env

    def search(self, query: str, limit: int = 20) -> list[DiscoveryLead]:
        query_url = f"{self.search_url}?{urlencode({'q': query, 'limit': limit})}"
        key = os.environ.get(self.api_key_env)
        payload = _read_json(query_url, {"X-Api-Key": key} if key else None)
        return [DiscoveryLead(item.get("title", "Untitled"), item.get("url") or item.get("link", ""), "DVIDS", item.get("date") or item.get("published_date"), item.get("description", ""), "official") for item in _items(payload) if item.get("url") or item.get("link")]


class OfficialSiteSearchClient:
    def __init__(self, name: str, search_url: str) -> None:
        self.name, self.search_url = name, search_url

    def search(self, query: str, limit: int = 20) -> list[DiscoveryLead]:
        separator = "&" if "?" in self.search_url else "?"
        payload = _read_json(f"{self.search_url}{separator}{urlencode({'q': query, 'limit': limit})}")
        return [DiscoveryLead(item.get("title", "Untitled"), item.get("url") or item.get("link", ""), self.name, item.get("date") or item.get("published_date"), item.get("description", ""), "official") for item in _items(payload) if item.get("url") or item.get("link")]
