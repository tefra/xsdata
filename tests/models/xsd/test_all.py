from unittest import TestCase

from xsdata.models.xsd import All


class AllTests(TestCase):
    def test_get_restrictions(self):
        obj = All(min_occurs=1, max_occurs=2)
        self.assertEqual({"path": [("a", id(obj), 1, 2)]}, obj.get_restrictions())
