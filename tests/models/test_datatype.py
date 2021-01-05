from typing import Dict
from unittest import TestCase

from xsdata.models.datatype import XmlDate
from xsdata.models.datatype import XmlDateTime
from xsdata.models.datatype import XmlDuration
from xsdata.models.datatype import XmlPeriod
from xsdata.models.datatype import XmlTime


def filter_none(mapping: Dict) -> Dict:
    return {k: v for k, v in mapping.items() if v is not None}


class XmlDateTests(TestCase):
    def test_parse_valid(self):
        examples = {
            "2002-01-01-00:00": XmlDate(2002, 1, 1, 0),
            "2002-01-01-02:15": XmlDate(2002, 1, 1, -8100),
            "2002-01-01+02:15": XmlDate(2002, 1, 1, 8100),
            "2002-01-01Z": XmlDate(2002, 1, 1, 0),
            "2002-01-01": XmlDate(2002, 1, 1),
        }

        for value, expected in examples.items():
            actual = XmlDate.parse(value)
            self.assertEqual(expected, actual, value)

    def test_parse_invalid(self):
        examples = [
            "a",
            1,
            "2002/01-01",
            "2002/01/01",
            "2002-01-01U",
        ]
        for example in examples:
            with self.assertRaises(ValueError, msg=example):
                XmlDate.parse(example)

    def test_str(self):
        examples = {
            "2002-01-01-00:00": "2002-01-01Z",
            "2002-01-01-02:15": "2002-01-01-02:15",
            "2002-01-01+02:15": "2002-01-01+02:15",
            "2002-01-01Z": "2002-01-01Z",
            "2002-01-01": "2002-01-01",
            "-2002-01-01": "-2002-01-01",
        }

        for value, expected in examples.items():
            actual = XmlDate.parse(value)
            self.assertEqual(expected, str(actual), value)

    def test_repr(self):
        examples = {
            "2002-01-01-00:00": "XmlDate(2002, 1, 1, 0)",
            "2002-01-01-02:15": "XmlDate(2002, 1, 1, -8100)",
            "2002-01-01+02:15": "XmlDate(2002, 1, 1, 8100)",
            "2002-01-01Z": "XmlDate(2002, 1, 1, 0)",
            "2002-01-01": "XmlDate(2002, 1, 1)",
            "-2002-01-01": "XmlDate(-2002, 1, 1)",
        }

        for value, expected in examples.items():
            actual = XmlDate.parse(value)
            self.assertEqual(expected, repr(actual), value)

    def test_eq(self):
        self.assertNotEqual(1, XmlDate(1, 0, 0))
        self.assertNotEqual(XmlDate(1, 1, 0), XmlDate(1, 0, 0))


class XmlDateTimeTests(TestCase):
    def test_parse_valid(self):
        examples = {
            "2002-01-01T12:01:01-00:00": XmlDateTime(2002, 1, 1, 12, 1, 1, 0, 0),
            "2002-01-01T12:01:01-02:15": XmlDateTime(2002, 1, 1, 12, 1, 1, 0, -8100),
            "2002-01-01T12:01:01+02:15": XmlDateTime(2002, 1, 1, 12, 1, 1, 0, 8100),
            "2002-01-01T12:01:01.010Z": XmlDateTime(2002, 1, 1, 12, 1, 1, 10000, 0),
            "2002-01-01T12:01:01.123456": XmlDateTime(2002, 1, 1, 12, 1, 1, 123456),
            "2002-01-01T12:01:01": XmlDateTime(2002, 1, 1, 12, 1, 1, 0),
            "2010-09-19T24:00:00Z": XmlDateTime(2010, 9, 19, 24, 0, 0, 0, 0),
        }

        for value, expected in examples.items():
            actual = XmlDateTime.parse(value)
            self.assertEqual(expected, actual, value)

    def test_parse_invalid(self):
        examples = [
            "a",
            1,
            "2002/01-01T12:01:01",
            "2002/01/01T12:01:01",
            "2002-01-01 12:01:01",
            "2002-01-01T12-01:01",
            "2002-01-01T12:01-01",
            "2002-01-01T12:01:01U",
        ]
        for example in examples:
            with self.assertRaises(ValueError, msg=example):
                XmlDateTime.parse(example)

    def test_str(self):
        examples = {
            "2002-01-01T12:01:01-00:00": "2002-01-01T12:01:01Z",
            "2002-01-01T12:01:01-02:15": None,
            "2002-01-01T12:01:01+02:15": None,
            "2002-01-01T12:01:01.0100Z": "2002-01-01T12:01:01.010Z",
            "2002-01-01T12:01:01.123456": None,
            "2002-01-01T12:01:01.123000": "2002-01-01T12:01:01.123",
            "2002-01-01T12:01:01.0": "2002-01-01T12:01:01",
            "2002-01-01T12:01:01": None,
            "2010-09-19T24:00:00Z": None,
            "-0001-09-19T24:00:00Z": None,
        }

        for value, expected in examples.items():
            actual = XmlDateTime.parse(value)
            self.assertEqual(expected or value, str(actual), value)

    def test_repr(self):
        examples = {
            "2002-01-01T12:01:01-00:00": "XmlDateTime(2002, 1, 1, 12, 1, 1, 0, 0)",
            "2002-01-01T12:01:01-02:15": "XmlDateTime(2002, 1, 1, 12, 1, 1, 0, -8100)",
            "2002-01-01T12:01:01+02:15": "XmlDateTime(2002, 1, 1, 12, 1, 1, 0, 8100)",
            "2002-01-01T12:01:01.0100Z": "XmlDateTime(2002, 1, 1, 12, 1, 1, 10000, 0)",
            "2002-01-01T12:01:01.123456": "XmlDateTime(2002, 1, 1, 12, 1, 1, 123456)",
            "2002-01-01T12:01:01.123000": "XmlDateTime(2002, 1, 1, 12, 1, 1, 123000)",
            "2002-01-01T12:01:01.0": "XmlDateTime(2002, 1, 1, 12, 1, 1, 0)",
            "2002-01-01T12:01:01": "XmlDateTime(2002, 1, 1, 12, 1, 1, 0)",
            "2010-09-19T24:00:00Z": "XmlDateTime(2010, 9, 19, 24, 0, 0, 0, 0)",
            "-0001-09-19T24:00:00Z": "XmlDateTime(-1, 9, 19, 24, 0, 0, 0, 0)",
        }

        for value, expected in examples.items():
            actual = XmlDateTime.parse(value)
            self.assertEqual(expected, repr(actual), value)

    def test_eq(self):
        self.assertNotEqual(1, XmlDateTime(2002, 1, 1, 12, 1, 1, 0, 8100))
        self.assertNotEqual(
            XmlDateTime(2002, 1, 1, 12, 1, 1, 1), XmlDateTime(2002, 1, 1, 12, 1, 1, 0)
        )


class XmlTimeTests(TestCase):
    def test_parse_valid(self):
        examples = {
            "12:01:01-00:00": XmlTime(12, 1, 1, 0, 0),
            "12:01:01-02:15": XmlTime(12, 1, 1, 0, -8100),
            "12:01:01+02:15": XmlTime(12, 1, 1, 0, +8100),
            "12:01:01.010Z": XmlTime(12, 1, 1, 10000, 0),
            "12:01:01.123456": XmlTime(12, 1, 1, 123456),
            "12:01:01": XmlTime(12, 1, 1, 0),
            "24:00:00Z": XmlTime(24, 0, 0, 0, 0),
        }

        for value, expected in examples.items():
            actual = XmlTime.parse(value)
            self.assertEqual(expected, actual, value)

    def test_parse_invalid(self):
        examples = [
            "a",
            1,
            "12-01:01",
            "12:01-01",
            "12:01:01U",
        ]
        for example in examples:
            with self.assertRaises(ValueError, msg=example):
                XmlTime.parse(example)

    def test_str(self):
        examples = {
            "12:01:01-00:00": "12:01:01Z",
            "12:01:01-02:15": "12:01:01-02:15",
            "12:01:01+02:15": "12:01:01+02:15",
            "12:01:01.010Z": "12:01:01.010Z",
            "12:01:01.123456": "12:01:01.123456",
            "12:01:01.123000": "12:01:01.123",
            "24:00:00Z": "24:00:00Z",
        }

        for value, expected in examples.items():
            actual = XmlTime.parse(value)
            self.assertEqual(expected or value, str(actual), value)

    def test_repr(self):
        examples = {
            "12:01:01-00:00": "XmlTime(12, 1, 1, 0, 0)",
            "12:01:01-02:15": "XmlTime(12, 1, 1, 0, -8100)",
            "12:01:01+02:15": "XmlTime(12, 1, 1, 0, 8100)",
            "12:01:01.010Z": "XmlTime(12, 1, 1, 10000, 0)",
            "12:01:01.123456": "XmlTime(12, 1, 1, 123456)",
            "12:01:01.123000": "XmlTime(12, 1, 1, 123000)",
            "24:00:00Z": "XmlTime(24, 0, 0, 0, 0)",
        }

        for value, expected in examples.items():
            actual = XmlTime.parse(value)
            self.assertEqual(expected, repr(actual), value)

    def test_eq(self):
        self.assertNotEqual(1, XmlTime(12, 1, 1, 0))
        self.assertNotEqual(XmlTime(12, 1, 1, 0), XmlTime(12, 1, 1, 1))


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
            obj = XmlDuration(value)
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
                XmlDuration(fixture)

    def test_repr(self):
        obj = XmlDuration("PT20M")
        self.assertEqual('XmlDuration("PT20M")', repr(obj))

    def test_user_string(self):
        obj = XmlDuration("PT20M")
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

        fixtures = {
            "---01": {"day": 1},
            "---01Z": {"day": 1, "offset": 0},
            "---01+02:00": {"day": 1, "offset": 7200},
            "---01-04:00": {"day": 1, "offset": -14400},
            "---15": {"day": 15},
            "---31": {"day": 31},
            "--05": {"month": 5},
            "--11Z": {"month": 11, "offset": 0},
            "--11+02:00": {"month": 11, "offset": 7200},
            "--11-04:00": {"month": 11, "offset": -14400},
            "--02": {"month": 2},
            "--05-01": {"day": 1, "month": 5},
            "--11-01Z": {"day": 1, "month": 11, "offset": 0},
            "--11-01+02:00": {"day": 1, "month": 11, "offset": 7200},
            "--11-01-04:00": {"day": 1, "month": 11, "offset": -14400},
            "--11-15": {"day": 15, "month": 11},
            "--02-29": {"day": 29, "month": 2},
            "2001": {"year": 2001},
            "2001+02:00": {"year": 2001, "offset": 7200},
            "2001Z": {"year": 2001, "offset": 0},
            "2001+00:00": {"year": 2001, "offset": 0},
            "-2001": {"year": -2001},
            "-20000": {"year": -20000},
            "2001-10": {"month": 10, "year": 2001},
            "2001-10+02:00": {"month": 10, "year": 2001, "offset": 7200},
            "2001-10Z": {"month": 10, "year": 2001, "offset": 0},
            "2001-10+00:00": {"month": 10, "year": 2001, "offset": 0},
            "-2001-10": {"month": 10, "year": -2001},
            "-20000-04": {"month": 4, "year": -20000},
        }

        for value, expected in fixtures.items():
            self.assertEqual(expected, filter_none(XmlPeriod(value).asdict()))

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
            "--1",
            # gYear
            "01",
            "210",
            # gMonthDay
            "-01-30-",
            "--01-35",
            "--1-5",
            "01-15",
            # gYearMonth
            "2001-13",
            "2001-13-26+02:00",
            "01-10",
        ]

        for value in fixtures:
            with self.assertRaises(ValueError, msg=value):
                XmlPeriod(value)

    def test_repr(self):
        obj = XmlPeriod("--02-29")
        self.assertEqual('XmlPeriod("--02-29")', repr(obj))
