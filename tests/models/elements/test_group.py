from unittest import TestCase

from xsdata.models.elements import Group


class GroupTests(TestCase):
    def test_property_extensions(self):
        obj = Group.create()
        self.assertEqual([], obj.extensions)
