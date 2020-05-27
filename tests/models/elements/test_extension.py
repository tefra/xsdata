from unittest import TestCase

from xsdata.models.xsd import Extension


class ExtensionTests(TestCase):
    def test_property_extends(self):
        obj = Extension.create(base="xs:string")
        self.assertEqual("xs:string", obj.extends)
