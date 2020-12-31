from datetime import timedelta
from datetime import timezone
from unittest import TestCase

from xsdata.utils.dates import DateTimeParser


class DateParserTests(TestCase):
    def test_parse(self):
        fmt = "%Y-%M-%DT%h:%m:%s%z"
        value = "2002-01-01T12:01:01-01:00"
        parser = DateTimeParser(value, fmt)
        parser.parse()

        self.assertEqual(2002, parser.year)
        self.assertEqual(1, parser.month)
        self.assertEqual(1, parser.day)
        self.assertEqual(12, parser.hour)
        self.assertEqual(1, parser.minute)
        self.assertEqual(1, parser.second)
        self.assertIsNone(parser.microsecond)
        self.assertEqual(timezone(timedelta(seconds=-3600)), parser.tz_info)

    def test_parse_microsecond(self):
        fmt = "%s"
        value = "55.1345"
        parser = DateTimeParser(value, fmt)
        parser.parse()
        self.assertEqual(55, parser.second)
        self.assertEqual(134500, parser.microsecond)

    def test_parse_negative_year(self):
        fmt = "%Y-%M"
        value = "-1970-05"
        parser = DateTimeParser(value, fmt)
        parser.parse()
        self.assertEqual(-1970, parser.year)
        self.assertEqual(5, parser.month)

    def test_parse_utc_timezone(self):
        fmt = "%z"
        value = "Z"
        parser = DateTimeParser(value, fmt)
        parser.parse()
        self.assertEqual(timezone.utc, parser.tz_info)

    def test_parse_optional_timezone(self):
        fmt = "%Y%z"
        value = "2020"
        parser = DateTimeParser(value, fmt)
        parser.parse()
        self.assertIsNone(parser.tz_info)

    def test_parse_unknown_var(self):
        fmt = "%F"
        value = "2002-01-01"
        parser = DateTimeParser(value, fmt)

        with self.assertRaises(ValueError) as cm:
            parser.parse()

        self.assertEqual(
            "String '2002-01-01' does not match format '%F'", str(cm.exception)
        )

    def test_parse_raises_value_error(self):
        cases = {
            "2002-01-01": "%F",  # Unknown var
            "2002-01-01": "%Y",  # Mismatch format
            "2002-1-01": "%Y",  # Minimum required digits
            "2002": "%Y-%M",  # Run out of value
            "$": "%z",  # Unknown timezone
        }

        for value, fmt in cases.items():
            with self.assertRaises(ValueError) as cm:
                parser = DateTimeParser(value, fmt)
                parser.parse()

            self.assertEqual(
                f"String '{value}' does not match format '{fmt}'", str(cm.exception)
            )
