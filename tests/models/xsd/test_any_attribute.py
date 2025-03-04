from unittest import TestCase

from xsdata.models.enums import Namespace, NamespaceType
from xsdata.models.xsd import AnyAttribute


class AnyAttributeTests(TestCase):
    def test_is_attribute(self) -> None:
        obj = AnyAttribute()
        self.assertTrue(obj.is_property)

    def test_property_raw_namespace(self) -> None:
        obj = AnyAttribute()
        self.assertEqual(NamespaceType.ANY_NS, obj.raw_namespace)

        obj.namespace = "foo"
        self.assertEqual("foo", obj.raw_namespace)

        obj = AnyAttribute(namespace="    foo  \n    \t  \r  bar foo ")
        self.assertEqual("foo bar", obj.raw_namespace)

    def test_property_real_name(self) -> None:
        obj = AnyAttribute()
        self.assertEqual("@any_attributes", obj.real_name)

        obj.namespace = "foo"
        self.assertEqual("@foo_attributes", obj.real_name)

        obj.namespace = "http://www.xsdata.com/somewhere.xsd"
        self.assertEqual("@xsdata_com/somewhere_attributes", obj.real_name)

        obj.namespace = "http://foo http://bar"
        self.assertEqual("@foo_bar_attributes", obj.real_name)

    def test_property_real_type(self) -> None:
        obj = AnyAttribute()
        obj.ns_map["xs"] = Namespace.XS.uri
        self.assertEqual(["xs:anyType"], list(obj.attr_types))

    def get_restrictions(self) -> None:
        obj = AnyAttribute()
        self.assertEqual({}, obj.get_restrictions())
