import unittest

from us_military_story_collector.models import Claim, Conflict, Grade, Source
from us_military_story_collector.validation import assess_claim


OFFICIAL = Source("https://service.mil/record", "Service", source_type="official", is_official=True)
INDEPENDENT = Source("https://news.example/story", "Independent News", source_type="independent")
REPOST = Source("https://copy.example/story", "Copy Site", source_type="independent", original_reporting=False)


class ClaimValidationTests(unittest.TestCase):
    def test_core_claim_needs_official_and_independent_second_source(self):
        result = assess_claim(Claim("c1", "A 2020 event", 2020, True, (OFFICIAL, INDEPENDENT)), [])
        self.assertEqual(result.grade, Grade.A)
        self.assertTrue(result.eligible_for_final)

    def test_repost_does_not_count_as_independent(self):
        result = assess_claim(Claim("c1", "A 2020 event", 2020, True, (OFFICIAL, REPOST)), [])
        self.assertEqual(result.grade, Grade.C)
        self.assertFalse(result.eligible_for_final)

    def test_pre_1990_is_rejected_by_default(self):
        result = assess_claim(Claim("c1", "Old event", 1989, True, (OFFICIAL, INDEPENDENT)), [])
        self.assertEqual(result.grade, Grade.D)
        self.assertFalse(result.eligible_for_final)

    def test_unresolved_conflict_blocks_final_fact(self):
        claim = Claim("c1", "A 2020 event", 2020, True, (OFFICIAL, INDEPENDENT))
        conflict = Conflict("c1", "Sources disagree on the date", (OFFICIAL.url, INDEPENDENT.url))
        result = assess_claim(claim, [conflict])
        self.assertEqual(result.grade, Grade.D)
