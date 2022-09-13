import re
from dataclasses import dataclass, field
from typing import List, Union
from unittest import TestCase

from xsdata.formats.dataclass.parsers import XmlParser
from xsdata.formats.dataclass.serializers import XmlSerializer

serializer = XmlSerializer()
parser = XmlParser()


@dataclass
class PrimitiveWrapper:
    primitive_list: List[Union[str,int]] = field(
        metadata={
            "wrapper": "PrimitiveList",
            "type": "Element",
            "name": "Value"
        }
    )


@dataclass
class ElementObject:
    content: str = field(
        metadata={
            "type": "Element"
        }
    )


@dataclass
class ElementWrapper:
    elements: List[ElementObject] = field(
        metadata={
            "wrapper": "Elements",
            "type": "Element",
            "name": "Object"
        }
    )


@dataclass
class NamespaceWrapper:
    items: List[str] = field(
        metadata={
            "wrapper": "Items",
            "type": "Element",
            "name": "item",
            "namespace": "ns"
        }
    )


class NamespaceTests(TestCase):
    def test_render(self):
        ns_map   = {"foo": "ns"}
        obj      = NamespaceWrapper(items=["a", "b"])
        xml      = serializer.render(obj, ns_map=ns_map)
        expected = '<NamespaceWrapper xmlns:foo="ns"><foo:Items><foo:item>a</foo:item><foo:item>b</foo:item></foo:Items></NamespaceWrapper>'
        self.assertIsNotNone(re.search(expected, xml))

    def test_parse(self):
        xml = '<NamespaceWrapper xmlns:foo="ns"><foo:Items><foo:item>a</foo:item><foo:item>b</foo:item></foo:Items></NamespaceWrapper>'
        obj = parser.from_string(xml, clazz=NamespaceWrapper)
        self.assertIsInstance(obj, NamespaceWrapper)
        self.assertTrue(hasattr(obj, "items"))
        self.assertEqual(len(obj.items), 2)
        self.assertEqual(obj.items[0], "a")
        self.assertEqual(obj.items[1], "b")


class PrimitiveWrapperTests(TestCase):
    def test_render(self):
        obj      = PrimitiveWrapper(primitive_list=["Value 1", "Value 2"])
        xml      = serializer.render(obj)
        expected = r"<PrimitiveWrapper><PrimitiveList><Value>Value 1</Value><Value>Value 2</Value></PrimitiveList></PrimitiveWrapper>"
        self.assertIsNotNone(re.search(expected, xml))

    def test_parse(self):
        xml = r"<PrimitiveWrapper><PrimitiveList><Value>Value 1</Value><Value>Value 2</Value></PrimitiveList></PrimitiveWrapper>"
        obj = parser.from_string(xml, clazz=PrimitiveWrapper)
        self.assertTrue(hasattr(obj, "primitive_list"))
        self.assertIsInstance(obj.primitive_list, list)
        self.assertEqual(len(obj.primitive_list), 2)
        self.assertEqual(obj.primitive_list[0], "Value 1")
        self.assertEqual(obj.primitive_list[1], "Value 2")


class ElementWrapperTests(TestCase):
    def test_render(self):
        obj      = ElementWrapper(elements=[ElementObject(content="Hello"), ElementObject(content="World")])
        xml      = serializer.render(obj)
        expected = "<ElementWrapper><Elements><Object><content>Hello</content></Object><Object><content>World</content></Object></Elements></ElementWrapper>"
        self.assertIsNotNone(re.search(expected, xml))

    def test_parse(self):
        xml = "<ElementWrapper><Elements><Object><content>Hello</content></Object><Object><content>World</content></Object></Elements></ElementWrapper>"
        obj = parser.from_string(xml, clazz=ElementWrapper)
        self.assertTrue(hasattr(obj, "elements"))
        self.assertIsInstance(obj.elements, list)
        self.assertEqual(len(obj.elements), 2)
        self.assertIsInstance(obj.elements[0], ElementObject)
        self.assertIsInstance(obj.elements[1], ElementObject)
        self.assertEqual(obj.elements[0].content, "Hello")
        self.assertEqual(obj.elements[1].content, "World")
