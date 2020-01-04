from unittest import TestCase

from xsdata.models.elements import Union


class UnionTests(TestCase):
    def test_property_real_name(self):
        obj = Union.create()
        self.assertIsNone(obj.extends)

        obj.member_types = "foo"
        self.assertEqual("foo", obj.extends)
