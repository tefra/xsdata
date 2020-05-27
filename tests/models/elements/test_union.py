from unittest import TestCase

from xsdata.models.xsd import MaxExclusive
from xsdata.models.xsd import MinExclusive
from xsdata.models.xsd import MinInclusive
from xsdata.models.xsd import MinLength
from xsdata.models.xsd import Restriction
from xsdata.models.xsd import SimpleType
from xsdata.models.xsd import Union


class UnionTests(TestCase):
    def test_property_extends(self):
        obj = Union.create()
        self.assertIsNone(obj.extends)

        obj.member_types = "foo"
        self.assertEqual("foo", obj.extends)

    def test_property_is_attribute(self):
        obj = Union.create()
        self.assertTrue(obj.is_attribute)

    def test_property_real_type(self):
        obj = Union.create()
        obj.member_types = "thug life"
        self.assertEqual(obj.member_types, obj.real_type)

        obj = Union.create(
            simple_types=[
                SimpleType.create(restriction=Restriction.create(base="foo")),
                SimpleType.create(restriction=Restriction.create(base="bar")),
            ]
        )

        self.assertEqual("foo bar", obj.real_type)

    def test_property_real_name(self):
        obj = Union.create()
        self.assertEqual("value", obj.real_name)

    def test_get_restrictions(self):
        first = Restriction.create(
            min_exclusive=MinExclusive.create(value=1),
            min_inclusive=MinInclusive.create(value=2),
        )
        second = Restriction.create(
            min_length=MinLength.create(value=3),
            max_exclusive=MaxExclusive.create(value=4),
        )
        obj = Union.create(
            simple_types=[
                SimpleType.create(restriction=first),
                SimpleType.create(restriction=second),
            ]
        )

        expected = {
            "max_exclusive": 4,
            "min_exclusive": 1,
            "min_inclusive": 2,
            "min_length": 3,
        }
        self.assertEqual(expected, obj.get_restrictions())
