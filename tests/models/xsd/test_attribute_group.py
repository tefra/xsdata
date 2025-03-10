from unittest import TestCase

from xsdata.models.xsd import AttributeGroup


class AttributeGroupTests(TestCase):
    def test_property_is_property(self) -> None:
        obj = AttributeGroup()
        self.assertTrue(obj.is_property)

    def test_property_attr_types(self) -> None:
        obj = AttributeGroup()
        self.assertEqual([], list(obj.attr_types))

        obj.ref = "foo"
        self.assertEqual(["foo"], list(obj.attr_types))
