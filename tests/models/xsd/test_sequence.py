import sys
from unittest import TestCase

from xsdata.models.xsd import Sequence


class SequenceTests(TestCase):
    def test_get_restrictions(self):
        obj = Sequence(min_occurs=1, max_occurs=2)
        self.assertEqual({"path": [("s", 0, 1, 2)]}, obj.get_restrictions())

        obj = Sequence(min_occurs=1, max_occurs="unbounded")
        obj.index = 2
        self.assertEqual({"path": [("s", 2, 1, sys.maxsize)]}, obj.get_restrictions())
