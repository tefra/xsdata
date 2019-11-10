import sys
from unittest import TestCase

from xsdata.models.elements import List


class ListTests(TestCase):
    def test_get_restrictions(self):
        obj = List.build()
        expected = dict(min_occurs=0, max_occurs=sys.maxsize)
        self.assertDictEqual(expected, obj.get_restrictions())
