from unittest import TestCase

from xsdata.models.elements import (
    Enumeration,
    FractionDigits,
    Length,
    MaxExclusive,
    MaxInclusive,
    MaxLength,
    MinExclusive,
    MinInclusive,
    MinLength,
    Pattern,
    Restriction,
    TotalDigits,
    WhiteSpace,
)


class RestrictionTests(TestCase):
    def test_property_raw_type(self):
        obj = Restriction.build(base="foo")
        self.assertEqual(obj.base, obj.raw_type)

    def test_property_raw_name(self):
        obj = Restriction.build()
        self.assertEqual("value", obj.raw_name)

    def test_get_restrictions(self):
        self.assertDictEqual({}, Restriction.build().get_restrictions())

        obj = Restriction.build(
            min_exclusive=MinExclusive.build(value=1),
            min_inclusive=MinInclusive.build(value=2),
            min_length=MinLength.build(value=3),
            max_exclusive=MaxExclusive.build(value=4),
            max_inclusive=MaxInclusive.build(value=5),
            max_length=MaxLength.build(value=6),
            total_digits=TotalDigits.build(value=7),
            fraction_digits=FractionDigits.build(value=8),
            length=Length.build(value=9),
            white_space=WhiteSpace.build(value="collapse"),
            pattern=Pattern.build(value=".*"),
            enumerations=Enumeration.build(value="str"),
        )
        expected = {
            "enumerations": "str",
            "fraction_digits": 8,
            "length": 9,
            "max_exclusive": 4,
            "max_inclusive": 5,
            "max_length": 6,
            "min_exclusive": 1,
            "min_inclusive": 2,
            "min_length": 3,
            "pattern": ".*",
            "total_digits": 7,
            "white_space": "collapse",
        }

        self.assertDictEqual(expected, obj.get_restrictions())
