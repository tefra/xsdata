from typing import Iterator
from unittest import TestCase

from xsdata.models.xsd import Extension


class ExtensionTests(TestCase):
    def test_property_bases(self):
        obj = Extension()
        self.assertEqual([], list(obj.bases))
        obj.base = "a b c"
        self.assertEqual(["a b c"], list(obj.bases))
