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
    def test_property_real_type(self):
        obj = Restriction.create(base="foo")
        self.assertEqual(obj.base, obj.real_type)

    def test_property_real_name(self):
        obj = Restriction.create()
        self.assertEqual("value", obj.real_name)

    def test_get_restrictions(self):
        self.assertDictEqual({}, Restriction.create().get_restrictions())

        obj = Restriction.create(
            min_exclusive=MinExclusive.create(value=1),
            min_inclusive=MinInclusive.create(value=2),
            min_length=MinLength.create(value=3),
            max_exclusive=MaxExclusive.create(value=4),
            max_inclusive=MaxInclusive.create(value=5),
            max_length=MaxLength.create(value=6),
            total_digits=TotalDigits.create(value=7),
            fraction_digits=FractionDigits.create(value=8),
            length=Length.create(value=9),
            white_space=WhiteSpace.create(value="collapse"),
            pattern=Pattern.create(value=".*"),
            enumerations=Enumeration.create(value="str"),
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
