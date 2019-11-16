from unittest import TestCase

from xsdata.models.elements import (
    AttributeGroup,
    ComplexContent,
    ComplexType,
    Extension,
    SimpleContent,
)


class ComplexTypeTests(TestCase):
    def test_property_extensions_with_no_content(self):
        obj = ComplexType.create()
        self.assertEqual([], obj.extensions)

    def test_property_extensions_with_complex_content(self):
        obj = ComplexType.create()
        obj.complex_content = ComplexContent.create()
        self.assertEqual([], obj.extensions)

        obj.complex_content.extension = Extension.create(base="foo_bar")
        self.assertEqual(["foo_bar"], obj.extensions)

    def test_property_extensions_with_attribute_groups(self):
        obj = ComplexType.create()
        obj.attribute_groups = [
            AttributeGroup.create(name="foo"),
            AttributeGroup.create(ref="bar"),
        ]
        self.assertEqual(["foo", "bar"], obj.extensions)

    def test_property_extensions_with_simple_content(self):
        obj = ComplexType.create()
        obj.simple_content = SimpleContent.create()
        self.assertEqual([], obj.extensions)

        obj.simple_content.extension = Extension.create(base="foo_bar")
        self.assertEqual(["foo_bar"], obj.extensions)
