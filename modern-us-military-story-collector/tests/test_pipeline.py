import json
import tempfile
import unittest
from pathlib import Path

from us_military_story_collector.io import load_story
from us_military_story_collector.pipeline import assess_story
from us_military_story_collector.reporting import markdown_report


class PipelineTests(unittest.TestCase):
    def test_excludes_unsupported_items_from_final_body(self):
        root = Path(__file__).parents[1]
        claims, photos, conflicts = load_story(root / "examples" / "story-candidate.json")
        assessment = assess_story(claims, photos, conflicts)
        report = markdown_report(claims, photos, assessment)
        self.assertTrue(assessment.claims["c-verified"].eligible_for_final)
        self.assertFalse(assessment.claims["c-unverified"].eligible_for_final)
        self.assertIn("Demonstration Person received", report)
        self.assertNotIn("rescued a colleague", report)
        self.assertIn("**Photo gap:** 1 verified photos", report)

    def test_validation_output_is_json_serializable(self):
        root = Path(__file__).parents[1]
        claims, photos, conflicts = load_story(root / "examples" / "story-candidate.json")
        json.dumps(assess_story(claims, photos, conflicts).to_dict())
