from dataclasses import dataclass, field, make_dataclass
from io import StringIO
from typing import Generator, List
from unittest import TestCase
from xml.etree.ElementTree import QName
from xml.sax import ContentHandler
from xml.sax.saxutils import XMLGenerator

from tests.fixtures.books import BookForm
from tests.fixtures.datatypes import Telephone
from tests.fixtures.models import Paragraph, SequentialType, Span, TypeA
from xsdata.exceptions import SerializerError, XmlContextError, XmlWriterError
from xsdata.formats.dataclass.models.elements import XmlType
from xsdata.formats.dataclass.models.generics import AnyElement, DerivedElement
from xsdata.formats.dataclass.serializers import XmlSerializer
from xsdata.formats.dataclass.serializers.config import SerializerConfig
from xsdata.formats.dataclass.serializers.mixins import (
    EventGenerator,
    XmlWriter,
)
from xsdata.models.enums import DataType, QNames
from xsdata.utils.testing import XmlVarFactory


class XmlWriterImpl(XmlWriter):
    def build_handler(self) -> ContentHandler:
        return XMLGenerator(
            self.output,
            encoding="UTF-8",
            short_empty_elements=True,
        )


class XmlWriterTests(TestCase):
    def setUp(self) -> None:
        super().setUp()

        output = StringIO()
        config = SerializerConfig()
        self.writer = XmlWriterImpl(output=output, config=config, ns_map={})

    def test_write(self):
        events = iter(
            [
                ("start", "{http://www.w3.org/1999/xhtml}p"),
                ("attr", "class", "section"),
                ("data", "total:"),
                ("data", 105.22),
                ("start", "{http://www.w3.org/1999/xhtml}br"),
                ("end", "{http://www.w3.org/1999/xhtml}br"),
                ("end", "{http://www.w3.org/1999/xhtml}p"),
            ]
        )

        self.writer.write(events)

        lines = self.writer.output.getvalue().splitlines()

        self.assertEqual(2, len(lines))
        self.assertEqual('<?xml version="1.0" encoding="UTF-8"?>', lines[0])
        self.assertEqual(
            (
                '<xhtml:p xmlns:xhtml="http://www.w3.org/1999/xhtml" class="section">'
                "total:<xhtml:br/>105.22</xhtml:p>"
            ),
            lines[1],
        )

    def test_convert_with_schema_location(self):
        self.writer.config.schema_location = "foo bar"
        events = iter(
            [
                ("start", "root"),
                ("end", "root"),
            ]
        )

        self.writer.write(events)

        lines = self.writer.output.getvalue().splitlines()
        self.assertEqual(
            (
                '<root xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" '
                'xsi:schemaLocation="foo bar"/>'
            ),
            lines[1],
        )

    def test_convert_with_no_namespace_schema_location(self):
        self.writer.config.no_namespace_schema_location = "foo.xsd"
        events = iter(
            [
                ("start", "root"),
                ("end", "root"),
            ]
        )

        self.writer.write(events)

        lines = self.writer.output.getvalue().splitlines()
        self.assertEqual(
            (
                '<root xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" '
                'xsi:noNamespaceSchemaLocation="foo.xsd"/>'
            ),
            lines[1],
        )

    def test_convert_with_unhandled_event_raises_exception(self):
        events = iter([("reverse", "p")])

        with self.assertRaises(XmlWriterError) as cm:
            self.writer.write(events)

        self.assertEqual("Unhandled event: `reverse`", str(cm.exception))

    def test_convert_removes_xsi_nil_if_necessary(self):
        events = iter(
            [
                ("start", "root"),
                ("start", "a"),
                ("attr", QNames.XSI_NIL, "true"),
                ("end", "a"),
                ("start", "a"),
                ("attr", QNames.XSI_NIL, "true"),
                ("data", "0"),
                ("end", "a"),
                ("start", "a"),
                ("attr", QNames.XSI_NIL, "true"),
                ("data", ""),
                ("end", "a"),
                ("start", "a"),
                ("attr", QNames.XSI_NIL, "true"),
                ("data", None),
                ("end", "a"),
                ("start", "a"),
                ("attr", QNames.XSI_NIL, "true"),
                ("data", [""]),
                ("end", "a"),
                ("start", "a"),
                ("attr", QNames.XSI_NIL, "true"),
                ("data", []),
                ("end", "a"),
                ("end", "root"),
            ]
        )
        self.writer.write(events)

        lines = self.writer.output.getvalue().splitlines()
        expected = (
            "<root>"
            '<a xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:nil="true"/>'
            "<a>0</a>"
            "<a/>"
            '<a xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:nil="true"/>'
            "<a/>"
            '<a xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:nil="true"/>'
            "</root>"
        )

        self.assertEqual(expected, lines[1])

    def test_convert_resets_default_namespace_for_unqualified_elements(self):
        events = iter(
            [
                ("start", "{a}a"),
                ("start", "b"),
                ("data", "foo"),
                ("start", "b"),
                ("end", "{a}a"),
            ]
        )

        self.writer.ns_map = {None: "a"}
        self.writer.write(events)
        lines = self.writer.output.getvalue().splitlines()
        self.assertEqual('<a xmlns="a"><b xmlns="">foo<b/>', lines[1])

    def test_add_attribute(self):
        with self.assertRaises(XmlWriterError) as cm:
            self.writer.add_attribute("foo", "bar")

        self.assertEqual("Empty pending tag.", str(cm.exception))

        self.writer.start_tag("a")
        self.writer.add_attribute("a", "bar")
        self.writer.add_attribute("b", True)
        self.writer.add_attribute("c", "{")
        self.writer.add_attribute("d", "{a}b")
        self.writer.add_attribute(QNames.XSI_TYPE, str(DataType.STRING))

        expected = {
            (None, "a"): "bar",
            (None, "b"): "true",
            (None, "c"): "{",
            (None, "d"): "{a}b",
            ("http://www.w3.org/2001/XMLSchema-instance", "type"): "xs:string",
        }

        self.assertEqual(expected, self.writer.attrs)

    def test_is_xsi_type(self):
        self.assertFalse(self.writer.is_xsi_type("key", 1))
        self.assertFalse(self.writer.is_xsi_type(QNames.XSI_TYPE, 1))
        self.assertFalse(self.writer.is_xsi_type(QNames.XSI_TYPE, "a"))
        self.assertTrue(self.writer.is_xsi_type(QNames.XSI_TYPE, "{b}a"))
        self.assertFalse(self.writer.is_xsi_type("type", "{b}a"))
        self.assertTrue(self.writer.is_xsi_type("type", str(DataType.STRING)))


class EventGeneratorTests(TestCase):
    def setUp(self) -> None:
        self.generator = EventGenerator()

    def test_with_primitive_wrapper(self):
        @dataclass
        class PrimitiveWrapper:
            primitive_list: List[str] = field(
                metadata={
                    "wrapper": "PrimitiveList",
                    "type": "Element",
                    "name": "Value",
                }
            )

        obj = PrimitiveWrapper(primitive_list=["Value 1", "Value 2"])
        events = self.generator.generate(obj)
        expected = [
            ("start", "PrimitiveWrapper"),
            ("start", "PrimitiveList"),
            ("start", "Value"),
            ("data", "Value 1"),
            ("end", "Value"),
            ("start", "Value"),
            ("data", "Value 2"),
            ("end", "Value"),
            ("end", "PrimitiveList"),
            ("end", "PrimitiveWrapper"),
        ]
        self.assertEqual(expected, list(events))

    def test_with_wrapper_element(self):
        @dataclass
        class ElementObject:
            content: str = field(metadata={"type": "Element"})

        @dataclass
        class ElementWrapper:
            elements: List[ElementObject] = field(
                metadata={"wrapper": "Elements", "type": "Element", "name": "Object"}
            )

        obj = ElementWrapper(
            elements=[ElementObject(content="Hello"), ElementObject(content="World")]
        )
        events = self.generator.generate(obj)
        expected = [
            ("start", "ElementWrapper"),
            ("start", "Elements"),
            ("start", "Object"),
            ("start", "content"),
            ("data", "Hello"),
            ("end", "content"),
            ("end", "Object"),
            ("start", "Object"),
            ("start", "content"),
            ("data", "World"),
            ("end", "content"),
            ("end", "Object"),
            ("end", "Elements"),
            ("end", "ElementWrapper"),
        ]
        self.assertEqual(expected, list(events))

    def test_with_wrapper_namespace(self):
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

        obj = NamespaceWrapper(items=["a", "b"])
        events = self.generator.generate(obj)
        expected = [
            ("start", "NamespaceWrapper"),
            ("start", "{ns}Items"),
            ("start", "{ns}item"),
            ("data", "a"),
            ("end", "{ns}item"),
            ("start", "{ns}item"),
            ("data", "b"),
            ("end", "{ns}item"),
            ("end", "{ns}Items"),
            ("end", "NamespaceWrapper"),
        ]

        self.assertEqual(expected, list(events))

    def test_with_derived_element(self):
        book = BookForm(id="123")
        obj = DerivedElement(qname="item", value=book)

        result = self.generator.generate(obj)
        expected = [
            ("start", "item"),
            ("attr", "id", "123"),
            ("attr", "lang", "en"),
            ("attr", QNames.XSI_TYPE, "{urn:books}BookForm"),
            ("end", "item"),
        ]
        self.assertIsInstance(result, Generator)
        self.assertEqual(expected, list(result))

        obj = DerivedElement(qname="{urn:books}BookForm", value=book)
        result = self.generator.generate(obj)
        expected = [
            ("start", "{urn:books}BookForm"),
            ("attr", "id", "123"),
            ("attr", "lang", "en"),
            ("end", "{urn:books}BookForm"),
        ]
        self.assertIsInstance(result, Generator)
        self.assertEqual(expected, list(result))

    def test_with_dataclass(self):
        book = BookForm(id="123", title="Misterioso: A Crime Novel", price=19.5)
        result = self.generator.generate(book)
        expected = [
            ("start", "BookForm"),
            ("attr", "id", "123"),
            ("attr", "lang", "en"),
            ("start", "title"),
            ("data", "Misterioso: A Crime Novel"),
            ("end", "title"),
            ("start", "price"),
            ("data", "19.5"),
            ("end", "price"),
            ("end", "BookForm"),
        ]
        self.assertIsInstance(result, Generator)
        self.assertEqual(expected, list(result))

    def test_convert_dataclass_can_overwrite_params(self):
        book = BookForm(id="123", title="Misterioso: A Crime Novel", price=19.5)
        result = self.generator.convert_dataclass(
            book, "xsdata", "book", True, "foo:book"
        )
        expected = [
            ("start", "book"),
            ("attr", "id", "123"),
            ("attr", "lang", "en"),
            ("attr", QNames.XSI_TYPE, "foo:book"),
            ("attr", QNames.XSI_NIL, "true"),
            ("start", "title"),
            ("data", "Misterioso: A Crime Novel"),
            ("end", "title"),
            ("start", "price"),
            ("data", "19.5"),
            ("end", "price"),
            ("end", "book"),
        ]
        self.assertIsInstance(result, Generator)
        self.assertEqual(expected, list(result))

    def test_convert_dataclass_with_no_dataclass(self):
        with self.assertRaises(XmlContextError) as cm:
            next(self.generator.convert_dataclass(1))
        self.assertEqual("Type '<class 'int'>' is not a dataclass.", str(cm.exception))

    def test_convert_mixed_content(self):
        var = XmlVarFactory.create(xml_type=XmlType.WILDCARD, qname="a", mixed=True)
        book = BookForm(id="123")
        ebook = DerivedElement("ebook", BookForm(id="123"))
        value = ["text", AnyElement(qname="br"), book, ebook, "tail"]
        result = self.generator.convert_value(value, var, "xsdata")
        expected = [
            ("data", "text"),
            ("start", "br"),
            ("data", None),
            ("end", "br"),
            ("start", "{xsdata}BookForm"),
            ("attr", "id", "123"),
            ("attr", "lang", "en"),
            ("end", "{xsdata}BookForm"),
            ("start", "ebook"),
            ("attr", "id", "123"),
            ("attr", "lang", "en"),
            ("attr", QNames.XSI_TYPE, "{urn:books}BookForm"),
            ("end", "ebook"),
            ("data", "tail"),
        ]

        self.assertIsInstance(result, Generator)
        self.assertEqual(expected, list(result))

    def test_convert_data(self):
        var = XmlVarFactory.create(xml_type=XmlType.TEXT, qname="a")
        expected = [("data", "123")]

        result = self.generator.convert_value("123", var, "xsdata")
        self.assertIsInstance(result, Generator)
        self.assertEqual(expected, list(result))

    def test_convert_tokens(self):
        var = XmlVarFactory.create(
            xml_type=XmlType.ELEMENT, qname="a", tokens_factory=list
        )

        result = self.generator.convert_value(None, var, "xsdata")
        self.assertIsInstance(result, Generator)
        self.assertListEqual([], list(result))

        result = self.generator.convert_value([], var, "xsdata")
        self.assertIsInstance(result, Generator)
        self.assertListEqual([], list(result))

        expected = [
            ("start", "a"),
            ("data", []),
            ("end", "a"),
        ]
        var.required = True
        result = self.generator.convert_value([], var, "xsdata")
        self.assertIsInstance(result, Generator)
        self.assertListEqual(expected, list(result))

        expected = [
            ("start", "a"),
            ("data", ["1", QName("{a}b"), "3"]),
            ("end", "a"),
        ]
        result = self.generator.convert_value([1, QName("{a}b"), 3], var, "xsdata")
        self.assertEqual(expected, list(result))

        expected = [
            ("start", "a"),
            ("data", ["1", "2", "3"]),
            ("end", "a"),
            ("start", "a"),
            ("data", ["4", "5", "6"]),
            ("end", "a"),
        ]

        result = self.generator.convert_value([[1, 2, 3], [4, 5, 6]], var, "xsdata")
        self.assertEqual(expected, list(result))

        var = XmlVarFactory.create(
            xml_type=XmlType.ELEMENT, qname="a", tokens=True, nillable=True
        )
        expected = [
            ("start", "a"),
            ("attr", QNames.XSI_NIL, "true"),
            ("data", []),
            ("end", "a"),
        ]

        result = self.generator.convert_value([], var, "xsdata")
        self.assertEqual(expected, list(result))

    def test_convert_any_type_with_primitive(self):
        var = XmlVarFactory.create(xml_type=XmlType.WILDCARD, qname="a")
        expected = [("data", "str")]

        result = self.generator.convert_value("str", var, "xsdata")
        self.assertIsInstance(result, Generator)
        self.assertEqual(expected, list(result))

    def test_convert_any_type_with_primitive_element(self):
        var = XmlVarFactory.create(xml_type=XmlType.ELEMENT, qname="a", types=(object,))
        expected = [
            ("start", "a"),
            ("data", "str"),
            ("end", "a"),
        ]

        result = self.generator.convert_value("str", var, "xsdata")
        self.assertIsInstance(result, Generator)
        self.assertEqual(expected, list(result))

    def test_convert_any_type_with_any_element(self):
        var = XmlVarFactory.create(xml_type=XmlType.WILDCARD, qname="a")
        value = AnyElement(
            qname="a",
            text="b",
            tail="c",
            attributes={"d": 1, "e": 2},
            children=[AnyElement(text="g"), "h"],
        )
        expected = [
            ("start", "a"),
            ("attr", "d", 1),
            ("attr", "e", 2),
            ("data", "b"),
            ("data", "g"),
            ("data", "h"),
            ("end", "a"),
            ("data", "c"),
        ]

        result = self.generator.convert_value(value, var, "xsdata")
        self.assertIsInstance(result, Generator)
        self.assertEqual(expected, list(result))

    def test_convert_any_type_with_derived_element_primitive(self):
        var = XmlVarFactory.create(xml_type=XmlType.WILDCARD, qname="a")
        value = DerivedElement(qname="a", value=1)
        expected = [
            ("start", "a"),
            ("attr", QNames.XSI_TYPE, QName(str(DataType.SHORT))),
            ("data", 1),
            ("end", "a"),
        ]

        result = self.generator.convert_value(value, var, "xsdata")
        self.assertIsInstance(result, Generator)
        self.assertEqual(expected, list(result))

    def test_convert_any_type_with_derived_element_dataclass(self):
        var = XmlVarFactory.create(xml_type=XmlType.WILDCARD, qname="a")
        value = DerivedElement(
            qname="a", value=BookForm(title="def"), type="{urn:books}BookForm"
        )
        expected = [
            ("start", "a"),
            ("attr", "lang", "en"),
            ("attr", QNames.XSI_TYPE, QName("{urn:books}BookForm")),
            ("start", "title"),
            ("data", "def"),
            ("end", "title"),
            ("end", "a"),
        ]

        result = self.generator.convert_value(value, var, "xsdata")
        self.assertIsInstance(result, Generator)
        self.assertEqual(expected, list(result))

    def test_convert_xsi_type(self):
        var = XmlVarFactory.create(
            xml_type=XmlType.ELEMENT,
            qname="a",
            name="a",
            types=(BookForm,),
        )
        value = BookForm(id="123")
        expected = [
            ("start", "a"),
            ("attr", "id", "123"),
            ("attr", "lang", "en"),
            ("end", "a"),
        ]

        result = self.generator.convert_value(value, var, "xsdata")
        self.assertIsInstance(result, Generator)
        self.assertEqual(expected, list(result))

    def test_convert_xsi_type_with_derived_class(self):
        var = XmlVarFactory.create(
            xml_type=XmlType.ELEMENT,
            qname="a",
            name="a",
            types=(BookForm,),
        )
        ebook = make_dataclass("eBook", [], bases=(BookForm,))
        expected = [
            ("start", "a"),
            ("attr", "id", "123"),
            ("attr", "lang", "en"),
            ("attr", QNames.XSI_TYPE, QName("eBook")),
            ("end", "a"),
        ]

        result = self.generator.convert_value(ebook(id="123"), var, "xsdata")
        self.assertIsInstance(result, Generator)
        self.assertEqual(expected, list(result))

    def test_convert_xsi_type_with_illegal_derived_class(self):
        var = XmlVarFactory.create(
            xml_type=XmlType.ELEMENT,
            qname="a",
            name="a",
            types=(BookForm,),
        )
        value = TypeA(1)

        result = self.generator.convert_value(value, var, "xsdata")
        with self.assertRaises(SerializerError) as cm:
            list(result)

        self.assertEqual("TypeA is not derived from BookForm", str(cm.exception))

    def test_convert_element(self):
        var = XmlVarFactory.create(xml_type=XmlType.ELEMENT, qname="a")
        expected = [
            ("start", "a"),
            ("data", "123"),
            ("end", "a"),
        ]

        result = self.generator.convert_value("123", var, "xsdata")
        self.assertIsInstance(result, Generator)
        self.assertEqual(expected, list(result))

    def test_convert_element_with_nillable_true(self):
        var = XmlVarFactory.create(xml_type=XmlType.ELEMENT, qname="a", nillable=True)
        expected = [
            ("start", "a"),
            ("attr", QNames.XSI_NIL, "true"),
            ("data", "123"),
            ("end", "a"),
        ]

        result = self.generator.convert_value("123", var, "xsdata")
        self.assertIsInstance(result, Generator)
        self.assertEqual(expected, list(result))

    def test_convert_element_with_any_type_var(self):
        var = XmlVarFactory.create(
            xml_type=XmlType.ELEMENT,
            qname="a",
            name="a",
            types=(object,),
            any_type=True,
        )
        expected = [
            ("start", "a"),
            ("attr", QNames.XSI_TYPE, QName(str(DataType.SHORT))),
            ("data", "123"),
            ("end", "a"),
        ]

        result = self.generator.convert_value(123, var, "xsdata")
        self.assertIsInstance(result, Generator)
        self.assertEqual(expected, list(result))

    def test_convert_element_with_any_type_var_ignore_xs_string(self):
        var = XmlVarFactory.create(
            xml_type=XmlType.ELEMENT,
            qname="a",
            name="a",
            types=(object,),
            any_type=True,
        )
        expected = [
            ("start", "a"),
            ("data", ""),
            ("end", "a"),
        ]
        result = self.generator.convert_value("", var, "xsdata")
        self.assertIsInstance(result, Generator)
        self.assertEqual(expected, list(result))

        expected = [
            ("start", "a"),
            ("data", "123"),
            ("end", "a"),
        ]
        result = self.generator.convert_value("123", var, "xsdata")
        self.assertIsInstance(result, Generator)
        self.assertEqual(expected, list(result))

    def test_convert_choice_with_derived_primitive_value(self):
        var = XmlVarFactory.create(
            xml_type=XmlType.ELEMENTS,
            name="compound",
            qname="compound",
            elements={
                "a": XmlVarFactory.create(
                    xml_type=XmlType.ELEMENT, qname="a", types=(int,)
                )
            },
        )
        value = DerivedElement(qname="a", value=1)
        expected = [
            ("start", "a"),
            ("data", "1"),
            ("end", "a"),
        ]

        result = self.generator.convert_value(value, var, "xsdata")
        self.assertIsInstance(result, Generator)
        self.assertEqual(expected, list(result))

    def test_convert_choice_with_derived_dataclass(self):
        var = XmlVarFactory.create(
            xml_type=XmlType.ELEMENTS,
            name="compound",
            elements={
                "a": XmlVarFactory.create(
                    xml_type=XmlType.ELEMENT, qname="a", types=(SequentialType,)
                )
            },
        )
        value = DerivedElement(qname="a", value=SequentialType("foo"))
        expected = [
            ("start", "a"),
            ("attr", "a0", "foo"),
            ("end", "a"),
        ]

        result = self.generator.convert_value(value, var, "xsdata")
        self.assertIsInstance(result, Generator)
        self.assertEqual(expected, list(result))

    def test_convert_choice_with_generic_object(self):
        var = XmlVarFactory.create(
            xml_type=XmlType.ELEMENTS,
            name="compound",
            qname="compound",
            elements={
                "a": XmlVarFactory.create(
                    xml_type=XmlType.ELEMENT, qname="a", types=(int,)
                )
            },
        )
        value = AnyElement(qname="a", text="1")
        expected = [
            ("start", "a"),
            ("data", "1"),
            ("end", "a"),
        ]

        result = self.generator.convert_value(value, var, "xsdata")
        self.assertIsInstance(result, Generator)
        self.assertEqual(expected, list(result))

    def test_convert_choice_with_raw_value(self):
        var = XmlVarFactory.create(
            xml_type=XmlType.ELEMENTS,
            name="compound",
            qname="compound",
            elements={
                "a": XmlVarFactory.create(
                    xml_type=XmlType.ELEMENT, qname="a", types=(int,)
                ),
                "b": XmlVarFactory.create(
                    xml_type=XmlType.ELEMENT,
                    qname="b",
                    name="b",
                    types=(int,),
                    tokens_factory=list,
                ),
            },
        )
        expected = [
            ("start", "a"),
            ("data", "1"),
            ("end", "a"),
            ("start", "b"),
            ("data", ["1", "2"]),
            ("end", "b"),
        ]

        result = self.generator.convert_value([1, [1, 2]], var, "xsdata")
        self.assertIsInstance(result, Generator)
        self.assertEqual(expected, list(result))

    def test_convert_choice_when_no_matching_choice_exists_but_value_is_model(self):
        var = XmlVarFactory.create(
            xml_type=XmlType.ELEMENTS,
            name="compound",
            qname="compound",
            elements={
                "a": XmlVarFactory.create(
                    xml_type=XmlType.WILDCARD, qname="a", types=(object,)
                )
            },
        )

        ebook = make_dataclass("eBook", [], bases=(BookForm,))
        expected = [
            ("start", "eBook"),
            ("attr", "lang", "en"),
            ("end", "eBook"),
        ]

        result = self.generator.convert_value(ebook(), var, None)
        self.assertIsInstance(result, Generator)
        self.assertEqual(expected, list(result))

    def test_convert_choice_when_no_matching_choice_exists(self):
        var = XmlVarFactory.create(
            xml_type=XmlType.ELEMENTS,
            name="compound",
            qname="compound",
            elements={
                "a": XmlVarFactory.create(
                    xml_type=XmlType.ELEMENT, qname="a", types=(float,)
                )
            },
        )

        with self.assertRaises(SerializerError) as cm:
            result = self.generator.convert_value(1, var, "xsdata")
            next(result)

        msg = "XmlElements undefined choice: `compound` for `<class 'int'>`"
        self.assertEqual(msg, str(cm.exception))

    def test_convert_value_with_list_value(self):
        var = XmlVarFactory.create(xml_type=XmlType.ELEMENT, qname="a", factory=list)
        value = [True, False]
        expected = [
            ("start", "a"),
            ("data", "true"),
            ("end", "a"),
            ("start", "a"),
            ("data", "false"),
            ("end", "a"),
        ]

        result = self.generator.convert_value(value, var, "xsdata")
        self.assertIsInstance(result, Generator)
        self.assertEqual(expected, list(result))

    def test_next_value(self):
        obj = SequentialType(x0=1, x1=[2, 3, 4, None], x2=[6, 7], x3=[9], x4=10)
        meta = self.generator.context.build(SequentialType)
        x0 = meta.text
        x1 = next(meta.find_children("x1"))
        x2 = next(meta.find_children("x2"))
        x3 = next(meta.find_children("x3"))
        x4 = next(meta.find_children("x4"))

        actual = self.generator.next_value(obj, meta)
        expected = [
            (x0, 1),
            (x1, 2),
            (x2, 6),
            (x1, 3),
            (x2, 7),
            (x1, 4),
            (x3, 9),
            (x4, 10),
        ]

        self.assertIsInstance(actual, Generator)
        self.assertEqual(expected, list(actual))

    def test_next_attribute(self):
        obj = SequentialType(a0="foo", a1={"b": "c", "d": "e"})
        meta = self.generator.context.build(SequentialType)

        actual = self.generator.next_attribute(obj, meta, False, None, False)
        expected = [
            ("a0", "foo"),
            ("b", "c"),
            ("d", "e"),
        ]

        self.assertIsInstance(actual, Generator)
        self.assertEqual(expected, list(actual))

        actual = self.generator.next_attribute(obj, meta, True, "xs:bool", False)
        expected.extend(
            [
                (QNames.XSI_TYPE, "xs:bool"),
                (QNames.XSI_NIL, "true"),
            ]
        )
        self.assertEqual(expected, list(actual))

        meta.attributes["a0"].required = False
        meta.attributes["a0"].default = "foo"
        actual = self.generator.next_attribute(obj, meta, False, None, True)
        expected = [
            ("b", "c"),
            ("d", "e"),
        ]

        self.assertIsInstance(actual, Generator)
        self.assertEqual(expected, list(actual))

    def test_with_mixed_content(self):
        obj = Paragraph()
        obj.content.append(AnyElement(qname="b", text="Mr."))
        obj.content.append(Span("chris"))
        obj.content.append("!")

        result = self.generator.generate(obj)
        expected = [
            ("start", "p"),
            ("start", "b"),
            ("data", "Mr."),
            ("end", "b"),
            ("start", "span"),
            ("data", "chris"),
            ("end", "span"),
            ("data", "!"),
            ("end", "p"),
        ]
        self.assertEqual(expected, list(result))

        obj = Paragraph()
        obj.content.append("Hi ")
        obj.content.append(AnyElement(qname="b", text="Mr."))
        obj.content.append(Span("chris"))
        obj.content.append("!")
        result = self.generator.generate(obj)
        expected = [
            ("start", "p"),
            ("data", "Hi "),
            ("start", "b"),
            ("data", "Mr."),
            ("end", "b"),
            ("start", "span"),
            ("data", "chris"),
            ("end", "span"),
            ("data", "!"),
            ("end", "p"),
        ]
        self.assertEqual(expected, list(result))

    def test_encode_primitive_with_namedtuple(self):
        var = XmlVarFactory.create(types=(Telephone,))
        actual = XmlSerializer.encode_primitive(Telephone(30, 234, 56783), var)
        self.assertEqual("30-234-56783", actual)
