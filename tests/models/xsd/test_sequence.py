import sys
from unittest import TestCase

from xsdata.models.xsd import Sequence


class SequenceTests(TestCase):
    def test_get_restrictions(self):
        obj = Sequence(min_occurs=1, max_occurs=2)
        self.assertEqual({"path": [("s", id(obj), 1, 2)]}, obj.get_restrictions())

        obj = Sequence(min_occurs=1, max_occurs="unbounded")
        self.assertEqual(
            {"path": [("s", id(obj), 1, sys.maxsize)]}, obj.get_restrictions()
        )
