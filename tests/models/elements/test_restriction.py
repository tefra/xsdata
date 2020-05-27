from unittest import TestCase

from xsdata.models.xsd import Enumeration
from xsdata.models.xsd import FractionDigits
from xsdata.models.xsd import Length
from xsdata.models.xsd import MaxExclusive
from xsdata.models.xsd import MaxInclusive
from xsdata.models.xsd import MaxLength
from xsdata.models.xsd import MinExclusive
from xsdata.models.xsd import MinInclusive
from xsdata.models.xsd import MinLength
from xsdata.models.xsd import Pattern
from xsdata.models.xsd import Restriction
from xsdata.models.xsd import SimpleType
from xsdata.models.xsd import TotalDigits
from xsdata.models.xsd import WhiteSpace


class RestrictionTests(TestCase):
    def test_property_real_type(self):
        obj = Restriction.create(base="foo")
        self.assertEqual(obj.base, obj.real_type)

        obj.enumerations.append(Enumeration.create())
        self.assertIsNone(obj.real_type)

        obj = Restriction.create(
            simple_type=SimpleType.create(restriction=Restriction.create(base="bar"))
        )

        self.assertEqual("bar", obj.real_type)

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

    def test_get_restrictions_with_nested_simple_type(self):
        obj = Restriction.create(
            min_length=MinLength.create(value=2),
            simple_type=SimpleType.create(
                restriction=Restriction.create(
                    max_length=MaxLength.create(value=10),
                    min_length=MinLength.create(value=5),
                )
            ),
        )

        expected = {"max_length": 10, "min_length": 2}
        self.assertEqual(expected, obj.get_restrictions())
