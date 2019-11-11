from unittest import TestCase

from xsdata.models.elements import AttributeGroup


class AttributeGroupTests(TestCase):
    def test_property_real_name(self):
        with self.assertRaises(NotImplementedError):
            obj = AttributeGroup.build()
            obj.real_name

        obj.ref = "foo"
        self.assertEqual(obj.ref, obj.real_name)

        obj.name = "bar"
        self.assertEqual(obj.name, obj.real_name)

    def test_property_extensions(self):
        obj = AttributeGroup.build()
        self.assertEqual([], obj.extensions)
