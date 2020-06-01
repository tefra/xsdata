from unittest import TestCase

from xsdata.models.xsd import Group


class GroupTests(TestCase):
    def test_property_is_attribute(self):
        obj = Group()
        self.assertTrue(obj.is_attribute)

    def test_property_real_type(self):
        obj = Group()
        self.assertIsNone(obj.real_type)

        obj.ref = "foo"
        self.assertEqual("foo", obj.real_type)
