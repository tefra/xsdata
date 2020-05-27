from unittest import TestCase

from xsdata.exceptions import SchemaValueError
from xsdata.models.enums import NamespaceType
from xsdata.models.xsd import Any


class AnyTests(TestCase):
    def test_property_is_attribute(self):
        self.assertTrue(Any.create().is_attribute)

    def test_property_real_type(self):
        self.assertEqual("xs:object", Any.create().real_type)

    def test_property_raw_namespace(self):
        obj = Any.create()
        self.assertEqual(NamespaceType.ANY.value, obj.raw_namespace)

        obj.namespace = "foo"
        self.assertEqual("foo", obj.raw_namespace)

        obj = Any.create(namespace="    foo  \n    \t  \r  bar foo ")
        self.assertEqual("foo bar", obj.raw_namespace)

    def test_property_real_name(self):
        obj = Any.create()
        self.assertEqual("any_element", obj.real_name)

        obj.namespace = "foo"
        self.assertEqual("foo_element", obj.real_name)

        obj.namespace = None
        with self.assertRaises(SchemaValueError):
            obj.real_name

    def test_get_restrictions(self):
        obj = Any.create(min_occurs=1, max_occurs=2)
        self.assertEqual({"max_occurs": 2, "min_occurs": 1}, obj.get_restrictions())
