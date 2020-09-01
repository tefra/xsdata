from typing import Iterator
from unittest import TestCase

from xsdata.models.xsd import MaxExclusive
from xsdata.models.xsd import MinExclusive
from xsdata.models.xsd import MinInclusive
from xsdata.models.xsd import MinLength
from xsdata.models.xsd import Restriction
from xsdata.models.xsd import SimpleType
from xsdata.models.xsd import Union


class UnionTests(TestCase):
    def test_property_extensions(self):
        obj = Union()
        self.assertIsInstance(obj.extensions, Iterator)
        self.assertEqual([], list(obj.extensions))

        obj.member_types = "foo bar   "
        self.assertEqual(["foo", "bar"], list(obj.extensions))

    def test_property_is_attribute(self):
        obj = Union()
        self.assertTrue(obj.is_attribute)

    def test_property_real_name(self):
        obj = Union()
        self.assertEqual("value", obj.real_name)

    def test_property_real_type(self):
        obj = Union()
        obj.member_types = "thug life"
        self.assertEqual(obj.member_types, obj.real_type)

        obj = Union(
            simple_types=[
                SimpleType(restriction=Restriction(base="foo")),
                SimpleType(restriction=Restriction(base="bar")),
            ]
        )

        self.assertEqual("foo bar", obj.real_type)

    def test_get_restrictions(self):
        first = Restriction(
            min_exclusive=MinExclusive(value=1), min_inclusive=MinInclusive(value=2)
        )
        second = Restriction(
            min_length=MinLength(value=3), max_exclusive=MaxExclusive(value=4)
        )
        obj = Union(
            simple_types=[
                SimpleType(restriction=first),
                SimpleType(restriction=second),
            ]
        )

        expected = {
            "max_exclusive": 4,
            "min_exclusive": 1,
            "min_inclusive": 2,
            "min_length": 3,
        }
        self.assertEqual(expected, obj.get_restrictions())
