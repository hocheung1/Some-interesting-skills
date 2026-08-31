import unittest

from us_military_story_collector.models import Grade, Photo
from us_military_story_collector.photos import assess_photo


class PhotoValidationTests(unittest.TestCase):
    def test_complete_photo_is_eligible(self):
        photo = Photo("p1", "https://asset.example/p.jpg", "https://record.example/p", "Person", "Caption", "Photographer", "2021-02-03", "CC0", ("https://record.example/p",), "https://rights.example/p", ("c1",))
        result = assess_photo(photo, {"c1"})
        self.assertEqual(result.grade, Grade.A)
        self.assertTrue(result.eligible_for_final)

    def test_caption_does_not_substitute_for_identity_or_rights(self):
        photo = Photo("p1", "https://asset.example/p.jpg", caption="Person at event")
        result = assess_photo(photo, set())
        self.assertFalse(result.eligible_for_final)
        self.assertIn("missing separate evidence that the named person is pictured", result.reasons)
        self.assertIn("missing separate rights/copyright evidence", result.reasons)
