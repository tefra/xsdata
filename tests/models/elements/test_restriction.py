from unittest import TestCase

from xsdata.models.elements import Enumeration
from xsdata.models.elements import FractionDigits
from xsdata.models.elements import Length
from xsdata.models.elements import MaxExclusive
from xsdata.models.elements import MaxInclusive
from xsdata.models.elements import MaxLength
from xsdata.models.elements import MinExclusive
from xsdata.models.elements import MinInclusive
from xsdata.models.elements import MinLength
from xsdata.models.elements import Pattern
from xsdata.models.elements import Restriction
from xsdata.models.elements import TotalDigits
from xsdata.models.elements import WhiteSpace


class RestrictionTests(TestCase):
    def test_property_real_type(self):
        obj = Restriction.create(base="foo")
        self.assertEqual(obj.base, obj.real_type)

    def test_property_real_name(self):
        obj = Restriction.create()
        self.assertEqual("value", obj.real_name)

    def test_property_extends(self):
        obj = Restriction.create(base="foo")
        self.assertEqual("foo", obj.extends)

    def test_get_restrictions(self):
        self.assertEqual({}, Restriction.create().get_restrictions())

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
            patterns=[Pattern.create(value="[0-9]"), Pattern.create(value="[A-Z]")],
            enumerations=[Enumeration.create(value="str")],
        )
        expected = {
            "fraction_digits": 8,
            "length": 9,
            "max_exclusive": 4,
            "max_inclusive": 5,
            "max_length": 6,
            "min_exclusive": 1,
            "min_inclusive": 2,
            "min_length": 3,
            "pattern": "[0-9]|[A-Z]",
            "total_digits": 7,
            "white_space": "collapse",
        }

        self.assertEqual(expected, obj.get_restrictions())
