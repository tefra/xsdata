from unittest import TestCase

from xsdata.utils.dates import parse_date_args
from xsdata.utils.dates import validate_date
from xsdata.utils.dates import validate_time


class DatesUtilsTests(TestCase):
    def test_parse_date_args(self):
        args = parse_date_args("2002-01-02T12:14:30-01:22", "%Y-%m-%dT%H:%M:%S%z")

        self.assertEqual(2002, next(args))
        self.assertEqual(1, next(args))
        self.assertEqual(2, next(args))
        self.assertEqual(12, next(args))
        self.assertEqual(14, next(args))
        self.assertEqual(30, next(args))
        self.assertEqual(0, next(args))
        self.assertEqual(-82, next(args))
        self.assertIsNone(next(args, None))

    def test_parse_date_args_microsecond(self):
        args = parse_date_args("55.1345", "%S")

        self.assertEqual(55, next(args))
        self.assertEqual(134500000, next(args))
        self.assertIsNone(next(args, None))

    def test_parse_date_args_nanosecond(self):
        args = parse_date_args("55.1345678", "%S")

        self.assertEqual(55, next(args))
        self.assertEqual(134567800, next(args))
        self.assertIsNone(next(args, None))

    def test_parse_date_args_year(self):
        args = parse_date_args("-1970-05", "%Y-%m")

        self.assertEqual(-1970, next(args))
        self.assertEqual(5, next(args))
        self.assertIsNone(next(args, None))

        args = parse_date_args("0009", "%Y")
        self.assertEqual(9, next(args))

        args = parse_date_args("0099", "%Y")
        self.assertEqual(99, next(args))

        args = parse_date_args("0999", "%Y")
        self.assertEqual(999, next(args))

        args = parse_date_args("9999", "%Y")
        self.assertEqual(9999, next(args))

        with self.assertRaises(ValueError):
            next(parse_date_args("09999", "%Y"))

        with self.assertRaises(ValueError):
            next(parse_date_args("00999", "%Y"))

        with self.assertRaises(ValueError):
            next(parse_date_args("00099", "%Y"))

        with self.assertRaises(ValueError):
            next(parse_date_args("00009", "%Y"))

    def test_parse_date_args_utc_timezone(self):
        args = parse_date_args("Z", "%z")

        self.assertEqual(0, next(args))
        self.assertIsNone(next(args, None))

    def test_parse_date_args_optional_timezone(self):
        args = parse_date_args("2020", "%Y%z")

        self.assertEqual(2020, next(args))
        self.assertIsNone(None, next(args))
        self.assertIsNone(next(args, None))

    def test_parse_date_args_trim_input(self):
        args = parse_date_args("\n Z ", "%z")

        self.assertEqual(0, next(args))
        self.assertIsNone(next(args, None))

    def test_parse_date_args_raises_value_error(self):
        cases = {
            "2002-12-01": "%F",  # Unknown var
            "2002-01-01": "%Y",  # Mismatch format
            "2002-1-01": "%Y",  # Minimum required digits
            "2002": "%Y-%M",  # Run out of value
            "$": "%z",  # Unknown timezone
        }

        for value, fmt in cases.items():
            with self.assertRaises(ValueError, msg=f"{value} ({fmt})") as cm:
                list(parse_date_args(value, fmt))

            self.assertEqual(
                f"String '{value}' does not match format '{fmt}'", str(cm.exception)
            )

    def test_validate_date(self):
        invalid = {
            (0, 0, 0): "Month must be in 1..12",
            (0, 2, 0): "Day must be in 1..29",
            (2003, 2, 29): "Day must be in 1..28",
        }

        for args, msg in invalid.items():
            with self.assertRaises(ValueError) as cm:
                validate_date(*args)

            self.assertEqual(msg, str(cm.exception))

    def test_validate_time(self):
        invalid = {
            (-1, 0, 0, 0): "Hour must be in 0..24",
            (25, 0, 0, 0): "Hour must be in 0..24",
            (24, 1, 0, 0): "Day time exceeded",
            (24, 0, 1, 0): "Day time exceeded",
            (24, 0, 0, 1): "Day time exceeded",
            (23, -1, 0, 1): "Minute must be in 0..59",
            (23, 66, 0, 1): "Minute must be in 0..59",
            (23, 59, -1, 1): "Second must be in 0..59",
            (23, 59, 60, 1): "Second must be in 0..59",
            (23, 59, 59, -1): "Fractional second must be in 0..999999999",
            (23, 59, 59, 1000000000): "Fractional second must be in 0..999999999",
        }

        for args, msg in invalid.items():
            with self.assertRaises(ValueError) as cm:
                validate_time(*args)

            self.assertEqual(msg, str(cm.exception))
