from typing import Iterator
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
    def test_property_attr_types(self):
        obj = Restriction()
        self.assertEqual([], list(obj.attr_types))

        obj = Restriction(base="foo")
        self.assertEqual([obj.base], list(obj.attr_types))

        obj.enumerations.append(Enumeration())
        self.assertEqual([], list(obj.attr_types))

        obj = Restriction(simple_type=SimpleType(restriction=Restriction(base="bar")))

        self.assertEqual(["bar"], list(obj.attr_types))

    def test_property_real_name(self):
        obj = Restriction()
        self.assertEqual("@value", obj.real_name)

    def test_property_bases(self):
        obj = Restriction()
        self.assertEqual([], list(obj.bases))

        obj.base = "foo"
        self.assertIsInstance(obj.bases, Iterator)
        self.assertEqual(["foo"], list(obj.bases))

    def test_get_restrictions(self):
        self.assertEqual({}, Restriction().get_restrictions())

        obj = Restriction(
            min_exclusive=MinExclusive(value=1),
            min_inclusive=MinInclusive(value=2),
            min_length=MinLength(value=3),
            max_exclusive=MaxExclusive(value=4),
            max_inclusive=MaxInclusive(value=5),
            max_length=MaxLength(value=6),
            total_digits=TotalDigits(value=7),
            fraction_digits=FractionDigits(value=8),
            length=Length(value=9),
            white_space=WhiteSpace(value="collapse"),
            patterns=[Pattern(value="[0-9]"), Pattern(value="[A-Z]")],
            enumerations=[Enumeration(value="str")],
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
        obj = Restriction(
            min_length=MinLength(value=2),
            simple_type=SimpleType(
                restriction=Restriction(
                    max_length=MaxLength(value=10), min_length=MinLength(value=5)
                )
            ),
        )

        expected = {"max_length": 10, "min_length": 2}
        self.assertEqual(expected, obj.get_restrictions())
