from unittest import TestCase

from xsdata.models.elements import Any
from xsdata.models.enums import NamespaceType


class AnyTests(TestCase):
    def test_property_is_attribute(self):
        obj = Any.create()
        self.assertTrue(obj.is_attribute)

    def test_property_is_wildcard(self):
        obj = Any.create()
        self.assertTrue(obj.is_wildcard)

    def test_property_real_type(self):
        obj = Any.create()
        self.assertEqual("xml:object", obj.real_type)

    def test_property_raw_namespace(self):
        obj = Any.create()
        self.assertEqual(NamespaceType.ANY.value, obj.raw_namespace)

        obj.namespace = "foo"
        self.assertEqual("foo", obj.raw_namespace)

        obj = Any.create(namespace="    foo  \n    \t  \r  bar")
        self.assertEqual("foo bar", obj.raw_namespace)

    def test_property_real_name(self):
        obj = Any.create()
        self.assertEqual("##any_element", obj.real_name)

        obj.namespace = "foo"
        self.assertEqual("foo_element", obj.real_name)

    def test_get_restrictions(self):
        obj = Any.create(min_occurs=1, max_occurs=2)
        self.assertEqual({"max_occurs": 2, "min_occurs": 1}, obj.get_restrictions())
