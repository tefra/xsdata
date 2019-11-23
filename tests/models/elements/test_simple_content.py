from unittest import TestCase

from xsdata.models.elements import Extension, Restriction, SimpleContent


class SimpleContentTests(TestCase):
    def test_property_extension(self):
        obj = SimpleContent.create()
        self.assertEqual([], obj.extensions)

        obj.restriction = Restriction.create(base="bar")
        self.assertEqual(["bar"], obj.extensions)

        obj.extension = Extension.create(base="foo")
        self.assertEqual(["foo"], obj.extensions)
