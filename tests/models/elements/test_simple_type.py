import sys
from unittest import TestCase

import pytest

from tests.testcases import ModelTestCase
from xsdata.models.elements import (
    AnnotationBase,
    BaseModel,
    Enumeration,
    Length,
    List,
    Restriction,
    Schema,
    SimpleType,
)
from xsdata.parser import SchemaParser


class SimpleTypeTests(TestCase):
    def test_property_raw_name(self):
        obj = SimpleType.build(name="foo")
        self.assertEqual("foo", obj.raw_name)

        with self.assertRaises(NotImplementedError):
            obj = SimpleType.build()
            self.assertFalse(hasattr(obj, "ref"))
            obj.raw_name

    def test_property_raw_base(self):
        self.assertIsNone(SimpleType.build().raw_base)

    def test_property_raw_type(self):
        obj = SimpleType.build()
        self.assertIsNone(obj.raw_type)

        obj.list = List.build(item_type="foo")
        self.assertEquals("foo", obj.raw_type)

        obj.restriction = Restriction.build(base="bar")
        self.assertEquals("bar", obj.raw_type)

    def test_get_restrictions(self):
        obj = SimpleType.build()
        self.assertDictEqual({}, obj.get_restrictions())

        expected = dict(min_occurs=0, max_occurs=sys.maxsize)
        obj.list = List.build()
        self.assertDictEqual(expected, obj.get_restrictions())

        expected = dict(length=2)
        obj.restriction = Restriction.build(length=Length.build(value=2))
        self.assertDictEqual(expected, obj.get_restrictions())


class SimpleTypeDeserializeTests(ModelTestCase):
    result: BaseModel

    @classmethod
    def setUpClass(cls) -> None:
        xsd = cls.fixture_path("simple_types")
        reader = SchemaParser(xsd)
        cls.result = reader.parse()

    def setUp(self) -> None:
        self.assertIsInstance(self.result, Schema)

    def test_with_restriction(self):
        actual: SimpleType = self.result.simple_types[0]

        expected = SimpleType.build(
            name="DeviceType",
            restriction=Restriction.build(
                base="xs:string",
                enumerations=[
                    Enumeration.build(value="mobile"),
                    Enumeration.build(value="tablet"),
                    Enumeration.build(value="desktop"),
                ],
            ),
        )
        self.assertEqual(expected, actual)
        self.assertIsInstance(actual, AnnotationBase)

    @pytest.mark.skip(reason="Missing sample")
    def test_with_list(self):
        pass

    @pytest.mark.skip(reason="Missing sample")
    def test_with_union(self):
        pass
