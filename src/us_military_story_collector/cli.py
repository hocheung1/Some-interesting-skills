from __future__ import annotations

import argparse
import json
from pathlib import Path

from .discovery import discover
from .io import load_story
from .pipeline import assess_story
from .reporting import markdown_report


def main() -> None:
    parser = argparse.ArgumentParser(description="Evidence-first modern U.S. military story collector")
    sub = parser.add_subparsers(dest="command", required=True)
    for command in ("validate", "report"):
        cmd = sub.add_parser(command)
        cmd.add_argument("input", help="story candidate JSON")
        if command == "report":
            cmd.add_argument("--output", required=True)
    discover_parser = sub.add_parser("discover", help="collect unverified official-source leads")
    discover_parser.add_argument("--query", required=True)
    discover_parser.add_argument("--config", required=True)
    args = parser.parse_args()
    if args.command == "discover":
        print(json.dumps([lead.__dict__ for lead in discover(args.query, args.config)], ensure_ascii=False, indent=2))
        return
    claims, photos, conflicts = load_story(args.input)
    assessment = assess_story(claims, photos, conflicts)
    if args.command == "validate":
        print(json.dumps(assessment.to_dict(), ensure_ascii=False, indent=2))
    else:
        Path(args.output).write_text(markdown_report(claims, photos, assessment), encoding="utf-8")


if __name__ == "__main__":
    main()
