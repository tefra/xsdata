from unittest import TestCase

from xsdata.models.xsd import AttributeGroup


class AttributeGroupTests(TestCase):
    def test_property_is_attribute(self):
        obj = AttributeGroup()
        self.assertTrue(obj.is_attribute)

    def test_property_attr_types(self):
        obj = AttributeGroup()
        self.assertEqual([], list(obj.attr_types))

        obj.ref = "foo"
        self.assertEqual(["foo"], list(obj.attr_types))
