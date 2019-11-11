from unittest import TestCase

from xsdata.models.elements import Extension, SimpleContent


class SimpleContentTests(TestCase):
    def test_property_extension(self):
        obj = SimpleContent.build()
        self.assertEqual([], obj.extensions)

        obj.extension = Extension.build(base="foo")
        self.assertEqual(["foo"], obj.extensions)
