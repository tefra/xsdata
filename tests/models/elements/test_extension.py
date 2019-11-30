from unittest import TestCase

from xsdata.models.elements import AttributeGroup, Extension


class ExtensionTests(TestCase):
    def test_property_extensions(self):
        obj = Extension.create(base="xs:string")
        self.assertEqual(["xs:string"], obj.extensions)

        obj.attribute_groups = [
            AttributeGroup.create(ref=ref) for ref in "abc"
        ]
        self.assertEqual(["a", "b", "c", "xs:string"], obj.extensions)
