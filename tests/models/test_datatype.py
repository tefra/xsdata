from datetime import date
from datetime import datetime
from datetime import time
from datetime import timedelta
from datetime import timezone
from typing import Dict
from unittest import TestCase

from xsdata.models.datatype import XmlDate
from xsdata.models.datatype import XmlDateTime
from xsdata.models.datatype import XmlDuration
from xsdata.models.datatype import XmlPeriod
from xsdata.models.datatype import XmlTime
from xsdata.utils.collections import Immutable


def filter_none(mapping: Dict) -> Dict:
    return {k: v for k, v in mapping.items() if v is not None}


class XmlDateTests(TestCase):
    def test_from_string(self):
        examples = {
            "2002-01-01-00:00": XmlDate(2002, 1, 1, 0),
            "2002-01-01-02:15": XmlDate(2002, 1, 1, -135),
            "2002-01-01+02:15": XmlDate(2002, 1, 1, 135),
            "2002-01-01Z": XmlDate(2002, 1, 1, 0),
            "2002-01-01": XmlDate(2002, 1, 1),
        }

        for value, expected in examples.items():
            actual = XmlDate.from_string(value)
            self.assertIsInstance(actual, Immutable)
            self.assertEqual(-1, actual._hashcode)
            self.assertEqual(expected, actual, value)

    def test_from_string_invalid(self):
        examples = [
            "a",
            1,
            "2002/01-01",
            "2002/01/01",
            "2002-01-01U",
        ]
        for example in examples:
            with self.assertRaises(ValueError, msg=example):
                XmlDate.from_string(example)

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
            actual = XmlDate.from_string(value)
            self.assertEqual(expected, str(actual), value)

    def test_repr(self):
        examples = {
            "2002-01-01-00:00": "XmlDate(2002, 1, 1, 0)",
            "2002-01-01-02:15": "XmlDate(2002, 1, 1, -135)",
            "2002-01-01+02:15": "XmlDate(2002, 1, 1, 135)",
            "2002-01-01Z": "XmlDate(2002, 1, 1, 0)",
            "2002-01-01": "XmlDate(2002, 1, 1)",
            "-2002-01-01": "XmlDate(-2002, 1, 1)",
        }

        for value, expected in examples.items():
            actual = XmlDate.from_string(value)
            self.assertEqual(expected, repr(actual), value)

    def test_datetime_helpers(self):
        tz_plus_two = timezone(timedelta(minutes=120))

        obj = datetime(2021, 1, 1, 0, 0, tzinfo=tz_plus_two)
        actual = XmlDate(2021, 1, 1, 120)
        self.assertEqual(actual, XmlDate.from_datetime(obj))
        self.assertEqual(obj, actual.to_datetime())
        self.assertEqual(obj.date(), actual.to_date())

        actual = XmlDate(2021, 1, 1)
        self.assertEqual(actual, XmlDate.from_date(obj.date()))
        self.assertEqual(obj.date(), actual.to_date())

        obj = datetime(2021, 1, 1, 0, 0, tzinfo=timezone.utc)
        actual = XmlDate(2021, 1, 1, 0)
        self.assertEqual(actual, XmlDate.from_datetime(obj))

        actual = XmlDate(2021, 1, 1)
        self.assertEqual(actual, XmlDate.from_date(obj.date()))

        obj = datetime(2021, 1, 1, 0, 0)
        actual = XmlDate(2021, 1, 1, None)
        self.assertEqual(actual, XmlDate.from_datetime(obj))
        self.assertEqual(actual, XmlDate.from_date(obj.date()))

        self.assertEqual(XmlDate.from_date(date.today()), XmlDate.today())

        now = datetime.now()
        self.assertEqual(XmlDate.from_datetime(now), XmlDate.today())

    def test_replace(self):
        actual = XmlDate(2021, 1, 1, 120)
        self.assertIsNot(actual, actual.replace())
        self.assertEqual("2022-01-01+02:00", str(actual.replace(2022)))
        self.assertEqual("2021-01-01", str(actual.replace(offset=None)))
        self.assertEqual("2021-01-01Z", str(actual.replace(offset=False)))
        self.assertEqual("2022-12-25+02:00", str(actual.replace(2022, 12, 25)))
        self.assertEqual("2022-12-25+00:10", str(actual.replace(2022, 12, 25, 10)))

    def test_comparisons(self):
        a = XmlDate(2021, 1, 1)
        b = XmlDate(2021, 1, 2)

        self.assertLess(a, b)
        self.assertLessEqual(a, b)
        self.assertLessEqual(a, a.replace())
        self.assertGreater(b, a)
        self.assertGreaterEqual(b, a)
        self.assertGreaterEqual(a.replace(), a)
        self.assertEqual(a, a.replace())
        self.assertNotEqual(a, a.replace(offset=0))


class XmlDateTimeTests(TestCase):
    def test_from_string(self):
        examples = {
            "2002-01-01T12:01:01-00:00": XmlDateTime(2002, 1, 1, 12, 1, 1, 0, 0),
            "2002-01-01T12:01:01-02:15": XmlDateTime(2002, 1, 1, 12, 1, 1, 0, -135),
            "2002-01-01T12:01:01+02:15": XmlDateTime(2002, 1, 1, 12, 1, 1, 0, 135),
            "2002-01-01T12:01:01.010Z": XmlDateTime(2002, 1, 1, 12, 1, 1, 10000, 0),
            "2002-01-01T12:01:01.123456": XmlDateTime(2002, 1, 1, 12, 1, 1, 123456),
            "2002-01-01T12:01:01": XmlDateTime(2002, 1, 1, 12, 1, 1, 0),
            "2010-09-19T24:00:00Z": XmlDateTime(2010, 9, 19, 24, 0, 0, 0, 0),
        }

        for value, expected in examples.items():
            actual = XmlDateTime.from_string(value)
            self.assertIsInstance(actual, Immutable)
            self.assertEqual(-1, actual._hashcode)
            self.assertEqual(expected, actual, value)

    def test_from_string_invalid(self):
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
                XmlDateTime.from_string(example)

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
            actual = XmlDateTime.from_string(value)
            self.assertEqual(expected or value, str(actual), value)

    def test_repr(self):
        examples = {
            "2002-01-01T12:01:01-00:00": "XmlDateTime(2002, 1, 1, 12, 1, 1, 0, 0)",
            "2002-01-01T12:01:01-02:15": "XmlDateTime(2002, 1, 1, 12, 1, 1, 0, -135)",
            "2002-01-01T12:01:01+02:15": "XmlDateTime(2002, 1, 1, 12, 1, 1, 0, 135)",
            "2002-01-01T12:01:01.0100Z": "XmlDateTime(2002, 1, 1, 12, 1, 1, 10000, 0)",
            "2002-01-01T12:01:01.123456": "XmlDateTime(2002, 1, 1, 12, 1, 1, 123456)",
            "2002-01-01T12:01:01.123000": "XmlDateTime(2002, 1, 1, 12, 1, 1, 123000)",
            "2002-01-01T12:01:01.0": "XmlDateTime(2002, 1, 1, 12, 1, 1)",
            "2002-01-01T12:01:01": "XmlDateTime(2002, 1, 1, 12, 1, 1)",
            "2010-09-19T24:00:00Z": "XmlDateTime(2010, 9, 19, 24, 0, 0, 0, 0)",
            "-0001-09-19T24:00:00Z": "XmlDateTime(-1, 9, 19, 24, 0, 0, 0, 0)",
        }

        for value, expected in examples.items():
            actual = XmlDateTime.from_string(value)
            self.assertEqual(expected, repr(actual), value)

    def test_datetime_helpers(self):
        tz_plus_135 = timezone(timedelta(seconds=8100))

        obj = datetime(2002, 1, 1, 12, 1, 1, tzinfo=tz_plus_135)
        actual = XmlDateTime(2002, 1, 1, 12, 1, 1, 0, 135)
        self.assertEqual(actual, XmlDateTime.from_datetime(obj))
        self.assertEqual(obj, actual.to_datetime())

        obj = datetime(2002, 1, 1, 12, 1, 1, tzinfo=timezone.utc)
        actual = XmlDateTime(2002, 1, 1, 12, 1, 1, 0, 0)
        self.assertEqual(actual, XmlDateTime.from_datetime(obj))
        self.assertEqual(obj, actual.to_datetime())

        obj = datetime(2002, 1, 1, 12, 1, 1)
        actual = XmlDateTime(2002, 1, 1, 12, 1, 1, 0, None)
        self.assertEqual(actual, XmlDateTime.from_datetime(obj))
        self.assertEqual(obj, actual.to_datetime())

        now = datetime.now().replace(microsecond=0, second=0, minute=1)
        self.assertEqual(
            XmlDateTime.from_datetime(now),
            XmlDateTime.now().replace(microsecond=0, second=0, minute=1),
        )

        now = datetime.now(tz=timezone.utc).replace(microsecond=0, second=0, minute=1)
        self.assertEqual(
            XmlDateTime.from_datetime(now),
            XmlDateTime.utcnow().replace(microsecond=0, second=0, minute=1),
        )

        now = datetime.utcnow().replace(microsecond=0, second=0, minute=1)
        self.assertEqual(
            XmlDateTime.from_datetime(now),
            XmlDateTime.utcnow().replace(microsecond=0, second=0, minute=1),
        )

    def test_comparisons(self):
        a = XmlDateTime.from_string("2010-09-20T12:00:00Z")
        b = XmlDateTime.from_string("2010-09-20T13:00:00.000+01:00")
        c = a.replace(second=1)

        self.assertLess(a, c)
        self.assertLessEqual(a, c)
        self.assertLessEqual(a, a.replace())
        self.assertGreater(c, a)
        self.assertGreaterEqual(c, a)
        self.assertGreaterEqual(a.replace(), a)
        self.assertEqual(a, a.replace())
        self.assertNotEqual(a, c)
        self.assertEqual(a, b)

    def test_replace(self):
        actual = XmlDateTime(2002, 1, 1, 12, 1, 1, 0, -120)
        self.assertIsNot(actual, actual.replace())
        self.assertEqual("2022-01-01T12:01:01-02:00", str(actual.replace(2022)))
        self.assertEqual("2022-12-01T12:01:01-02:00", str(actual.replace(2022, 12)))
        self.assertEqual("2022-12-25T12:01:01-02:00", str(actual.replace(2022, 12, 25)))
        self.assertEqual(
            "2022-12-25T10:01:01-02:00", str(actual.replace(2022, 12, 25, 10))
        )
        self.assertEqual(
            "2022-12-25T10:15:01-02:00", str(actual.replace(2022, 12, 25, 10, 15))
        )
        self.assertEqual(
            "2022-12-25T10:15:30-02:00", str(actual.replace(2022, 12, 25, 10, 15, 30))
        )
        self.assertEqual(
            "2022-12-25T10:15:30.150-02:00",
            str(actual.replace(2022, 12, 25, 10, 15, 30, 150000)),
        )
        self.assertEqual(
            "2022-12-25T10:15:30.150+01:00",
            str(actual.replace(2022, 12, 25, 10, 15, 30, 150000, 60)),
        )
        self.assertEqual(
            "2022-12-25T10:15:30.150",
            str(actual.replace(2022, 12, 25, 10, 15, 30, 150000, None)),
        )
        self.assertEqual(
            "2022-12-25T10:15:30.150Z",
            str(actual.replace(2022, 12, 25, 10, 15, 30, 150000, False)),
        )


class XmlTimeTests(TestCase):
    def test_from_string(self):
        examples = {
            "12:01:01-00:00": XmlTime(12, 1, 1, 0, 0),
            "12:01:01-02:15": XmlTime(12, 1, 1, 0, -135),
            "12:01:01+02:15": XmlTime(12, 1, 1, 0, +135),
            "12:01:01.010Z": XmlTime(12, 1, 1, 10000, 0),
            "12:01:01.123456": XmlTime(12, 1, 1, 123456),
            "12:01:01": XmlTime(12, 1, 1, 0),
            "24:00:00Z": XmlTime(24, 0, 0, 0, 0),
        }

        for value, expected in examples.items():
            actual = XmlTime.from_string(value)
            self.assertIsInstance(actual, Immutable)
            self.assertEqual(-1, actual._hashcode)
            self.assertEqual(expected, actual, value)

    def test_from_string_invalid(self):
        examples = [
            "a",
            1,
            "12-01:01",
            "12:01-01",
            "12:01:01U",
        ]
        for example in examples:
            with self.assertRaises(ValueError, msg=example):
                XmlTime.from_string(example)

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
            actual = XmlTime.from_string(value)
            self.assertEqual(expected or value, str(actual), value)

    def test_repr(self):
        examples = {
            "12:01:01-00:00": "XmlTime(12, 1, 1, 0, 0)",
            "12:01:01-02:15": "XmlTime(12, 1, 1, 0, -135)",
            "12:01:01+02:15": "XmlTime(12, 1, 1, 0, 135)",
            "12:01:01.010Z": "XmlTime(12, 1, 1, 10000, 0)",
            "12:01:01.123456": "XmlTime(12, 1, 1, 123456)",
            "12:01:01.123000": "XmlTime(12, 1, 1, 123000)",
            "24:00:00Z": "XmlTime(24, 0, 0, 0, 0)",
        }

        for value, expected in examples.items():
            actual = XmlTime.from_string(value)
            self.assertEqual(expected, repr(actual), value)

    def test_datetime_helpers(self):
        tz_minus_120 = timezone(timedelta(minutes=-120))

        obj = time(12, 1, 1, 1, tzinfo=tz_minus_120)
        actual = XmlTime(12, 1, 1, 1, -120)
        self.assertEqual(actual, XmlTime.from_time(obj))
        self.assertEqual(obj, actual.to_time())

        obj = time(12, 1, 1, 1, tzinfo=timezone.utc)
        actual = XmlTime(12, 1, 1, 1, 0)
        self.assertEqual(actual, XmlTime.from_time(obj))
        self.assertEqual(obj, actual.to_time())

        obj = time(12, 1, 1, 1, tzinfo=timezone.utc)
        actual = XmlTime(12, 1, 1, 1, 0)
        self.assertEqual(actual, XmlTime.from_time(obj))
        self.assertEqual(obj, actual.to_time())

        now = datetime.now().replace(microsecond=0, second=0, minute=1)
        self.assertEqual(
            XmlTime.from_time(now.time()),
            XmlTime.now().replace(microsecond=0, second=0, minute=1),
        )

        now = datetime.now(tz=timezone.utc).replace(microsecond=0, second=0, minute=1)
        self.assertEqual(
            XmlTime.from_time(now.time()),
            XmlTime.utcnow().replace(microsecond=0, second=0, minute=1),
        )

        now = datetime.utcnow().replace(microsecond=0, second=0, minute=1)
        self.assertEqual(
            XmlTime.from_time(now.time()),
            XmlTime.utcnow().replace(microsecond=0, second=0, minute=1),
        )

    def test_comparisons(self):
        a = XmlTime.from_string("12:00:00Z")
        b = XmlTime.from_string("13:00:00.000+01:00")
        c = XmlTime.from_string("13:00:00.000")

        self.assertLess(a, c)
        self.assertLessEqual(a, c)
        self.assertLessEqual(a, a.replace())
        self.assertGreater(c, a)
        self.assertGreaterEqual(c, a)
        self.assertGreaterEqual(a.replace(), a)
        self.assertEqual(a, a.replace())
        self.assertNotEqual(a, c)
        self.assertEqual(a, b)

    def test_replace(self):
        actual = XmlTime(12, 1, 1, 1, 0)
        self.assertIsNot(actual, actual.replace())
        self.assertEqual("14:01:01.000001Z", str(actual.replace(14)))
        self.assertEqual("14:02:01.000001Z", str(actual.replace(14, 2)))
        self.assertEqual("14:02:03.000001Z", str(actual.replace(14, 2, 3)))
        self.assertEqual("14:02:03Z", str(actual.replace(14, 2, 3, 0)))
        self.assertEqual("14:02:03", str(actual.replace(14, 2, 3, 0, None)))
        self.assertEqual("14:02:03+00:55", str(actual.replace(14, 2, 3, 0, 55)))


class XmlDurationTests(TestCase):
    def test_properties(self):
        duration = XmlDuration("P2Y6M5DT12H35M30.5S")
        self.assertEqual(2, duration.years)
        self.assertEqual(6, duration.months)
        self.assertEqual(5, duration.days)
        self.assertEqual(12, duration.hours)
        self.assertEqual(35, duration.minutes)
        self.assertEqual(30.5, duration.seconds)
        self.assertFalse(duration.negative)

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


class XmlPeriodTests(TestCase):
    def test_properties(self):
        period = XmlPeriod("2001-10+02:00")
        self.assertEqual(2001, period.year)
        self.assertEqual(10, period.month)
        self.assertEqual(120, period.offset)
        self.assertIsNone(period.day)

        period = XmlPeriod("---20-02:44")
        self.assertIsNone(period.year)
        self.assertIsNone(period.month)
        self.assertEqual(20, period.day)
        self.assertEqual(-164, period.offset)

    def test_init_valid(self):

        fixtures = {
            "--05---05:00": {"month": 5, "offset": -300},
            "---01 ": {"day": 1},
            "---01Z": {"day": 1, "offset": 0},
            "---01+02:00": {"day": 1, "offset": 120},
            " ---01-04:00": {"day": 1, "offset": -240},
            "---15": {"day": 15},
            "---31": {"day": 31},
            "--05": {"month": 5},
            "--11Z": {"month": 11, "offset": 0},
            "--11+02:00": {"month": 11, "offset": 120},
            "--11-04:00": {"month": 11, "offset": -240},
            "--02": {"month": 2},
            "--05-01": {"day": 1, "month": 5},
            "--11-01Z": {"day": 1, "month": 11, "offset": 0},
            "--11-01+02:00": {"day": 1, "month": 11, "offset": 120},
            "--11-01-04:00": {"day": 1, "month": 11, "offset": -240},
            "--11-15": {"day": 15, "month": 11},
            "--02-29": {"day": 29, "month": 2},
            "2001": {"year": 2001},
            "2001+02:00": {"year": 2001, "offset": 120},
            "2001Z": {"year": 2001, "offset": 0},
            "2001+00:00": {"year": 2001, "offset": 0},
            "-2001": {"year": -2001},
            "-20000": {"year": -20000},
            "2001-10": {"month": 10, "year": 2001},
            "2001-10+02:00": {"month": 10, "year": 2001, "offset": 120},
            "2001-10Z": {"month": 10, "year": 2001, "offset": 0},
            "2001-10+00:00": {"month": 10, "year": 2001, "offset": 0},
            "-2001-10": {"month": 10, "year": -2001},
            "-20000-04": {"month": 4, "year": -20000},
        }

        for value, expected in fixtures.items():
            self.assertEqual(expected, filter_none(XmlPeriod(value).as_dict()))

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

    def test_equal(self):
        a = XmlPeriod("--02-29")
        b = XmlPeriod("--02-29")
        c = XmlPeriod("--03-30")

        self.assertEqual(a, b)
        self.assertNotEqual(a, c)
        self.assertNotEqual(1, c)
