from typing import Dict
from typing import Hashable
from unittest import TestCase

from xsdata.models.datatype import Duration


def filter_none(mapping: Dict) -> Dict:
    return {k: v for k, v in mapping.items() if v is not None}


class DurationTests(TestCase):
    def test_init_valid(self):

        fixtures = {
            "P2Y6M5DT12H35M30.5S": {
                "days": 5,
                "hours": 12,
                "minutes": 35,
                "months": 6,
                "negative": False,
                "seconds": 30.5,
                "years": 2,
            },
            "P1DT2H": {"days": 1, "hours": 2, "negative": False},
            "P20M": {"months": 20, "negative": False},
            "PT20M": {"minutes": 20, "negative": False},
            "P0Y20M0D": {"days": 0, "months": 20, "negative": False, "years": 0},
            "P0Y": {"negative": False, "years": 0},
            "-P60D": {"days": 60, "negative": True},
            "-P60DT1M": {"days": 60, "minutes": 1, "negative": True},
            "PT1M30.5S": {"minutes": 1, "negative": False, "seconds": 30.5},
        }

        for value, expected in fixtures.items():
            obj = Duration(value)
            self.assertEqual(expected, filter_none(obj.asdict()), f"Failed in: {value}")
            self.assertEqual(value, str(obj), f"Failed out: {value}")

    def test_init_invalid(self):
        fixtures = [
            True,
            "P-20M",
            "P20MT",
            "P1YM5D",
            "P15.5Y",
            "P1D2H",
            "1Y2M",
            "P2M1Y",
            "P",
            "PT15.S",
        ]

        for fixture in fixtures:
            with self.assertRaises(ValueError, msg=fixture):
                Duration(fixture)

    def test_repr(self):
        obj = Duration("PT20M")
        self.assertEqual('Duration("PT20M")', repr(obj))

    def test_user_string(self):
        obj = Duration("PT20M")
        obj_b = obj + "5.0S"
        expected = {
            "days": None,
            "hours": None,
            "minutes": 20,
            "months": None,
            "negative": False,
            "seconds": 5.0,
            "years": None,
        }

        self.assertIsNot(obj, obj_b)
        self.assertEqual(expected, obj_b.asdict())
