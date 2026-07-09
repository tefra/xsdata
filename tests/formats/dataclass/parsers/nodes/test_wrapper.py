from dataclasses import dataclass, field
from unittest import TestCase

from xsdata.formats.dataclass.parsers import XmlParser


class WrapperTests(TestCase):
    def setUp(self) -> None:
        self.parser = XmlParser()

    def test_namespace(self) -> None:
        @dataclass
        class NamespaceWrapper:
            items: list[str] = field(
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

    def test_primitive(self) -> None:
        @dataclass
        class PrimitiveWrapper:
            primitive_list: list[str] = field(
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

    def test_element(self) -> None:
        @dataclass
        class ElementObject:
            content: str = field(metadata={"type": "Element"})

        @dataclass
        class ElementWrapper:
            elements: list[ElementObject] = field(
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

    def test_reused_item_name(self) -> None:
        @dataclass
        class Foo:
            class Meta:
                name = "Property"

            foo_id: int = field(metadata={"name": "Foo-Id", "type": "Attribute"})

        @dataclass
        class Bar:
            class Meta:
                name = "Property"

            bar_id: str = field(metadata={"name": "Bar-Id", "type": "Attribute"})

        @dataclass
        class Response:
            foos: list[Foo] = field(
                metadata={"wrapper": "Foos", "name": "Property", "type": "Element"}
            )
            bars: list[Bar] = field(
                metadata={"wrapper": "Bars", "name": "Property", "type": "Element"}
            )

        xml = (
            "<Response>"
            '<Foos><Property Foo-Id="1"/><Property Foo-Id="2"/></Foos>'
            '<Bars><Property Bar-Id="3"/><Property Bar-Id="4"/></Bars>'
            "</Response>"
        )
        obj = self.parser.from_string(xml, clazz=Response)
        self.assertEqual([Foo(foo_id=1), Foo(foo_id=2)], obj.foos)
        self.assertEqual([Bar(bar_id="3"), Bar(bar_id="4")], obj.bars)
