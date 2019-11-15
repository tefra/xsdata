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
        obj = ComplexType.build()
        self.assertEqual([], obj.extensions)

    def test_property_extensions_with_complex_content(self):
        obj = ComplexType.build()
        obj.complex_content = ComplexContent.build()
        self.assertEqual([], obj.extensions)

        obj.complex_content.extension = Extension.build(base="foo_bar")
        self.assertEqual(["foo_bar"], obj.extensions)

    def test_property_extensions_with_attribute_groups(self):
        obj = ComplexType.build()
        obj.attribute_groups = [
            AttributeGroup.build(name="foo"),
            AttributeGroup.build(ref="bar"),
        ]
        self.assertEqual(["foo", "bar"], obj.extensions)

    def test_property_extensions_with_simple_content(self):
        obj = ComplexType.build()
        obj.simple_content = SimpleContent.build()
        self.assertEqual([], obj.extensions)

        obj.simple_content.extension = Extension.build(base="foo_bar")
        self.assertEqual(["foo_bar"], obj.extensions)
