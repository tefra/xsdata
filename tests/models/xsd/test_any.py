from unittest import TestCase

from xsdata.models.enums import Namespace
from xsdata.models.enums import NamespaceType
from xsdata.models.xsd import Any


class AnyTests(TestCase):
    def test_property_is_attribute(self):
        self.assertTrue(Any().is_attribute)

    def test_property_attr_types(self):
        obj = Any()
        obj.ns_map["xs"] = Namespace.XS.uri
        self.assertEqual(["xs:anyType"], list(obj.attr_types))

    def test_property_raw_namespace(self):
        obj = Any()
        self.assertEqual(NamespaceType.ANY_NS, obj.raw_namespace)

        obj.namespace = "foo"
        self.assertEqual("foo", obj.raw_namespace)

        obj = Any(namespace="    foo  \n    \t  \r  bar foo ")
        self.assertEqual("foo bar", obj.raw_namespace)

    def test_property_real_name(self):
        obj = Any()
        self.assertEqual("@any_element", obj.real_name)

        obj.namespace = "foo"
        self.assertEqual("@foo_element", obj.real_name)

        obj.namespace = "http://www.xsdata.com/somewhere.xsd"
        self.assertEqual("@xsdata_com/somewhere_element", obj.real_name)

        obj.namespace = "http://foo http://bar"
        self.assertEqual("@foo_bar_element", obj.real_name)

    def test_get_restrictions(self):
        obj = Any(min_occurs=1, max_occurs=2)
        self.assertEqual({"max_occurs": 2, "min_occurs": 1}, obj.get_restrictions())
