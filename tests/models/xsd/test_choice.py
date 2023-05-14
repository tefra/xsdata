import sys
from unittest import TestCase

from xsdata.models.xsd import Choice


class ChoiceTests(TestCase):
    def test_get_restrictions(self):
        obj = Choice(min_occurs=1, max_occurs=2)
        self.assertEqual({"path": [("c", id(obj), 1, 2)]}, obj.get_restrictions())

        obj = Choice(max_occurs="unbounded")
        self.assertEqual(
            {"path": [("c", id(obj), 1, sys.maxsize)]}, obj.get_restrictions()
        )
