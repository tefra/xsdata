from typing import Iterator
from unittest import TestCase

from xsdata.models.xsd import Extension


class ExtensionTests(TestCase):
    def test_property_extensions(self):
        obj = Extension(base="xs:string")
        self.assertIsInstance(obj.extensions, Iterator)
        self.assertEqual(["xs:string"], list(obj.extensions))
