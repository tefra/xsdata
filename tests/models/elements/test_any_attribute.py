from unittest import TestCase

from xsdata.exceptions import SchemaValueError
from xsdata.models.enums import NamespaceType
from xsdata.models.xsd import AnyAttribute


class AnyAttributeTests(TestCase):
    def test_is_attribute(self):
        obj = AnyAttribute.create()
        self.assertTrue(obj.is_attribute)

    def test_property_raw_namespace(self):
        obj = AnyAttribute.create()
        self.assertEqual(NamespaceType.ANY.value, obj.raw_namespace)

        obj.namespace = "foo"
        self.assertEqual("foo", obj.raw_namespace)

        obj = AnyAttribute.create(namespace="    foo  \n    \t  \r  bar foo ")
        self.assertEqual("foo bar", obj.raw_namespace)

    def test_property_real_name(self):
        obj = AnyAttribute.create()
        self.assertEqual("any_attributes", obj.real_name)

        obj.namespace = "foo"
        self.assertEqual("foo_attributes", obj.real_name)

        obj.namespace = None
        with self.assertRaises(SchemaValueError):
            obj.real_name

    def test_property_real_type(self):
        obj = AnyAttribute.create()
        self.assertEqual("xs:qmap", obj.real_type)

    def get_restrictions(self):
        obj = AnyAttribute.create()
        self.assertEqual({}, obj.get_restrictions())
