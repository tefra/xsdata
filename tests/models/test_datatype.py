from datetime import timedelta
from datetime import timezone
from typing import Dict
from typing import Hashable
from unittest import TestCase

from xsdata.models.datatype import Duration
from xsdata.models.datatype import Period


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


class PeriodTests(TestCase):
    def test_init_valid(self):
        timezone_plus_two = timezone(timedelta(seconds=7200))
        timezone_minus_four = timezone(timedelta(seconds=-14400))

        fixtures = {
            "---01": {"day": 1},
            "---01Z": {"day": 1, "timezone": timezone.utc},
            "---01+02:00": {"day": 1, "timezone": timezone_plus_two},
            "---01-04:00": {"day": 1, "timezone": timezone_minus_four},
            "---15": {"day": 15},
            "---31": {"day": 31},
            "--05": {"month": 5},
            "--11Z": {"month": 11, "timezone": timezone.utc},
            "--11+02:00": {"month": 11, "timezone": timezone_plus_two},
            "--11-04:00": {"month": 11, "timezone": timezone_minus_four},
            "--02": {"month": 2},
            "--05-01": {"day": 1, "month": 5},
            "--11-01Z": {"day": 1, "month": 11, "timezone": timezone.utc},
            "--11-01+02:00": {"day": 1, "month": 11, "timezone": timezone_plus_two},
            "--11-01-04:00": {"day": 1, "month": 11, "timezone": timezone_minus_four},
            "--11-15": {"day": 15, "month": 11},
            "--02-29": {"day": 29, "month": 2},
            "2001": {"year": 2001},
            "2001+02:00": {"year": 2001, "timezone": timezone_plus_two},
            "2001Z": {"year": 2001, "timezone": timezone.utc},
            "2001+00:00": {"year": 2001, "timezone": timezone.utc},
            "-2001": {"year": -2001},
            "-20000": {"year": -20000},
            "2001-10": {"month": 10, "year": 2001},
            "2001-10+02:00": {"month": 10, "year": 2001, "timezone": timezone_plus_two},
            "2001-10Z": {"month": 10, "year": 2001, "timezone": timezone.utc},
            "2001-10+00:00": {"month": 10, "year": 2001, "timezone": timezone.utc},
            "-2001-10": {"month": 10, "year": -2001},
            "-20000-04": {"month": 4, "year": -20000},
        }

        for value, expected in fixtures.items():
            self.assertEqual(expected, filter_none(Period(value).asdict()))

    def test_init_invalid(self):
        fixtures = [
            # gDay
            "--30-",
            "---35",
            "---5",
            "15"
            # gMonth
            "-01-",
            "--13",
            "--1"
            # gYear
            "01",
            "210",
            # gMonthDay
            "-01-30-",
            "--01-35",
            "--1-5",
            "01-15"
            # gYearMonth
            "2001-13",
            "2001-13-26+02:00",
            "01-10",
        ]

        for value in fixtures:
            with self.assertRaises(ValueError, msg=value):
                Period(value)

    def test_repr(self):
        obj = Period("--02-29")
        self.assertEqual('Period("--02-29")', repr(obj))
