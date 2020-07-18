from typing import Iterator
from unittest import TestCase

from xsdata.models.xsd import Extension


class ExtensionTests(TestCase):
    def test_property_extensions(self):
        obj = Extension()
        self.assertIsInstance(obj.extensions, Iterator)
        self.assertEqual([], list(obj.extensions))
        obj.base = "a b c"
        self.assertEqual(["a b c"], list(obj.extensions))
