from unittest import TestCase

from xsdata.models.xsd import AttributeGroup


class AttributeGroupTests(TestCase):
    def test_property_is_attribute(self):
        obj = AttributeGroup()
        self.assertTrue(obj.is_attribute)

    def test_property_real_type(self):
        obj = AttributeGroup()
        self.assertEqual("", obj.real_type)

        obj.ref = "foo"
        self.assertEqual("foo", obj.real_type)
