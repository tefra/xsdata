from unittest import TestCase

from xsdata.models.elements import Group


class GroupTests(TestCase):
    def test_property_extends(self):
        obj = Group.create()
        self.assertIsNone(obj.extends)
