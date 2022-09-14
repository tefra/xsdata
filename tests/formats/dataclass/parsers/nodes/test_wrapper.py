from dataclasses import dataclass
from dataclasses import field
from typing import List
from unittest import TestCase

from xsdata.formats.dataclass.parsers import XmlParser


class WrapperTests(TestCase):
    def setUp(self) -> None:
        self.parser = XmlParser()

    def test_namespace(self):
        @dataclass
        class NamespaceWrapper:
            items: List[str] = field(
                metadata={
                    "wrapper": "Items",
                    "type": "Element",
                    "name": "item",
                    "namespace": "ns",
                }
            )

        xml = '<NamespaceWrapper xmlns:foo="ns"><foo:Items><foo:item>a</foo:item><foo:item>b</foo:item></foo:Items></NamespaceWrapper>'
        obj = self.parser.from_string(xml, clazz=NamespaceWrapper)
        self.assertIsInstance(obj, NamespaceWrapper)
        self.assertTrue(hasattr(obj, "items"))
        self.assertEqual(len(obj.items), 2)
        self.assertEqual(obj.items[0], "a")
        self.assertEqual(obj.items[1], "b")

    def test_primitive(self):
        @dataclass
        class PrimitiveWrapper:
            primitive_list: List[str] = field(
                metadata={
                    "wrapper": "PrimitiveList",
                    "type": "Element",
                    "name": "Value",
                }
            )

        xml = r"<PrimitiveWrapper><PrimitiveList><Value>Value 1</Value><Value>Value 2</Value></PrimitiveList></PrimitiveWrapper>"
        obj = self.parser.from_string(xml, clazz=PrimitiveWrapper)
        self.assertTrue(hasattr(obj, "primitive_list"))
        self.assertIsInstance(obj.primitive_list, list)
        self.assertEqual(len(obj.primitive_list), 2)
        self.assertEqual(obj.primitive_list[0], "Value 1")
        self.assertEqual(obj.primitive_list[1], "Value 2")

    def test_element(self):
        @dataclass
        class ElementObject:
            content: str = field(metadata={"type": "Element"})

        @dataclass
        class ElementWrapper:
            elements: List[ElementObject] = field(
                metadata={"wrapper": "Elements", "type": "Element", "name": "Object"}
            )

        xml = "<ElementWrapper><Elements><Object><content>Hello</content></Object><Object><content>World</content></Object></Elements></ElementWrapper>"
        obj = self.parser.from_string(xml, clazz=ElementWrapper)
        self.assertTrue(hasattr(obj, "elements"))
        self.assertIsInstance(obj.elements, list)
        self.assertEqual(len(obj.elements), 2)
        self.assertIsInstance(obj.elements[0], ElementObject)
        self.assertIsInstance(obj.elements[1], ElementObject)
        self.assertEqual(obj.elements[0].content, "Hello")
        self.assertEqual(obj.elements[1].content, "World")
