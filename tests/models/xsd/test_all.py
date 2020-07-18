from unittest import TestCase

from xsdata.models.xsd import All


class AllTests(TestCase):
    def test_get_restrictions(self):
        obj = All(min_occurs=1, max_occurs=2)
        self.assertEqual({"max_occurs": 2, "min_occurs": 1}, obj.get_restrictions())
