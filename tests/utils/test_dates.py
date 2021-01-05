from unittest import TestCase

from xsdata.utils.dates import parse_date_args


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
        self.assertEqual(134500, next(args))
        self.assertIsNone(next(args, None))

    def test_parse_date_args_negative_year(self):
        args = parse_date_args("-1970-05", "%Y-%m")

        self.assertEqual(-1970, next(args))
        self.assertEqual(5, next(args))
        self.assertIsNone(next(args, None))

    def test_parse_date_args_utc_timezone(self):
        args = parse_date_args("Z", "%z")

        self.assertEqual(0, next(args))
        self.assertIsNone(next(args, None))

    def test_parse_date_args_optional_timezone(self):
        args = parse_date_args("2020", "%Y%z")

        self.assertEqual(2020, next(args))
        self.assertIsNone(None, next(args))
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
