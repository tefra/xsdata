import sys
from unittest import TestCase

from xsdata.models.xsd import Choice


class ChoiceTests(TestCase):
    def test_get_restrictions(self):
        obj = Choice(min_occurs=1, max_occurs=2)

        expected = {
            "choice": str(id(obj)),
            "min_occurs": 0,
            "max_occurs": 2,
        }
        self.assertEqual(expected, obj.get_restrictions())

        obj = Choice(max_occurs="unbounded")
        expected = {
            "choice": str(id(obj)),
            "min_occurs": 0,
            "max_occurs": sys.maxsize,
        }
        self.assertEqual(expected, obj.get_restrictions())
