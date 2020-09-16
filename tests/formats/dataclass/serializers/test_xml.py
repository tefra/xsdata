from dataclasses import dataclass
from dataclasses import field
from dataclasses import make_dataclass
from typing import Dict
from typing import Generator
from typing import List
from typing import Optional
from unittest import TestCase
from xml.etree.ElementTree import QName

from tests.fixtures.books import BookForm
from xsdata.exceptions import SerializerError
from xsdata.exceptions import XmlContextError
from xsdata.formats.dataclass.models.elements import XmlElement
from xsdata.formats.dataclass.models.elements import XmlText
from xsdata.formats.dataclass.models.elements import XmlVar
from xsdata.formats.dataclass.models.elements import XmlWildcard
from xsdata.formats.dataclass.models.generics import AnyElement
from xsdata.formats.dataclass.serializers import XmlSerializer
from xsdata.formats.dataclass.serializers.mixins import XmlEventWriter
from xsdata.models.enums import QNames


@dataclass
class A:
    a0: Optional[str] = field(default=None, metadata=dict(type="Attribute"))
    a1: Dict = field(default_factory=dict, metadata=dict(type="Attributes"))
    a2: List[str] = field(
        default_factory=list, metadata=dict(type="Attribute", tokens=True)
    )
    x0: Optional[int] = field(default=None)
    x1: List[int] = field(
        default_factory=list, metadata=dict(type="Element", sequential=True)
    )
    x2: List[int] = field(
        default_factory=list, metadata=dict(type="Element", sequential=True)
    )
    x3: List[int] = field(
        default_factory=list, metadata=dict(type="Element", sequential=True)
    )


class XmlSerializerTests(TestCase):
    def setUp(self) -> None:
        self.serializer = XmlSerializer()

    def test_write_dataclass(self):
        book = BookForm(id="123", title="Misterioso: A Crime Novel", price=19.5)
        result = self.serializer.write_dataclass(book)
        expected = [
            (XmlEventWriter.START_TAG, "BookForm"),
            (XmlEventWriter.ADD_ATTR, "id", "123"),
            (XmlEventWriter.ADD_ATTR, "lang", "en"),
            (XmlEventWriter.START_TAG, "title"),
            (XmlEventWriter.SET_DATA, "Misterioso: A Crime Novel"),
            (XmlEventWriter.END_TAG, "title"),
            (XmlEventWriter.START_TAG, "price"),
            (XmlEventWriter.SET_DATA, 19.5),
            (XmlEventWriter.END_TAG, "price"),
            (XmlEventWriter.END_TAG, "BookForm"),
        ]
        self.assertIsInstance(result, Generator)
        self.assertEqual(expected, list(result))

    def test_write_dataclass_can_overwrite_params(self):
        book = BookForm(id="123", title="Misterioso: A Crime Novel", price=19.5)
        result = self.serializer.write_dataclass(
            book, "xsdata", "book", True, "foo:book"
        )
        expected = [
            (XmlEventWriter.START_TAG, "book"),
            (XmlEventWriter.ADD_ATTR, "id", "123"),
            (XmlEventWriter.ADD_ATTR, "lang", "en"),
            (XmlEventWriter.ADD_ATTR, QNames.XSI_TYPE, "foo:book"),
            (XmlEventWriter.ADD_ATTR, QNames.XSI_NIL, "true"),
            (XmlEventWriter.START_TAG, "title"),
            (XmlEventWriter.SET_DATA, "Misterioso: A Crime Novel"),
            (XmlEventWriter.END_TAG, "title"),
            (XmlEventWriter.START_TAG, "price"),
            (XmlEventWriter.SET_DATA, 19.5),
            (XmlEventWriter.END_TAG, "price"),
            (XmlEventWriter.END_TAG, "book"),
        ]
        self.assertIsInstance(result, Generator)
        self.assertEqual(expected, list(result))

    def test_write_dataclass_with_no_dataclass(self):
        with self.assertRaises(XmlContextError) as cm:
            next(self.serializer.write_dataclass(1))
        self.assertEqual("Object <class 'int'> is not a dataclass.", str(cm.exception))

    def test_write_mixed_content(self):
        var = XmlWildcard(qname="a", name="a", mixed=True)
        book = BookForm(id="123")
        ebook = BookForm(id="123")
        ebook.qname = "ebook"
        value = ["text", AnyElement(qname="br"), book, ebook, "tail"]
        result = self.serializer.write_value(value, var, "xsdata")
        expected = [
            (XmlEventWriter.SET_DATA, "text"),
            (XmlEventWriter.START_TAG, "br"),
            (XmlEventWriter.SET_DATA, None),
            (XmlEventWriter.END_TAG, "br"),
            (XmlEventWriter.SET_DATA, None),
            (XmlEventWriter.START_TAG, "{xsdata}BookForm"),
            (XmlEventWriter.ADD_ATTR, "id", "123"),
            (XmlEventWriter.ADD_ATTR, "lang", "en"),
            (XmlEventWriter.END_TAG, "{xsdata}BookForm"),
            (XmlEventWriter.START_TAG, "ebook"),
            (XmlEventWriter.ADD_ATTR, "id", "123"),
            (XmlEventWriter.ADD_ATTR, "lang", "en"),
            (XmlEventWriter.END_TAG, "ebook"),
            (XmlEventWriter.SET_DATA, "tail"),
        ]

        self.assertIsInstance(result, Generator)
        self.assertEqual(expected, list(result))

    def test_write_data(self):
        var = XmlText(qname="a", name="a")
        expected = [(XmlEventWriter.SET_DATA, "123")]

        result = self.serializer.write_value("123", var, "xsdata")
        self.assertIsInstance(result, Generator)
        self.assertEqual(expected, list(result))

    def test_write_tokens(self):
        var = XmlElement(qname="a", name="a", tokens=True)

        result = self.serializer.write_value([], var, "xsdata")
        self.assertIsInstance(result, Generator)
        self.assertEqual(0, len(list(result)))

        expected = [
            (XmlEventWriter.START_TAG, "a"),
            (XmlEventWriter.SET_DATA, [1, 2, 3]),
            (XmlEventWriter.END_TAG, "a"),
        ]
        result = self.serializer.write_value([1, 2, 3], var, "xsdata")
        self.assertEqual(expected, list(result))

        expected = [
            (XmlEventWriter.START_TAG, "a"),
            (XmlEventWriter.SET_DATA, [1, 2, 3]),
            (XmlEventWriter.END_TAG, "a"),
            (XmlEventWriter.START_TAG, "a"),
            (XmlEventWriter.SET_DATA, [4, 5, 6]),
            (XmlEventWriter.END_TAG, "a"),
        ]

        result = self.serializer.write_value([[1, 2, 3], [4, 5, 6]], var, "xsdata")
        self.assertEqual(expected, list(result))

    def test_write_any_type_with_primitive(self):
        var = XmlWildcard(qname="a", name="a")
        expected = [(XmlEventWriter.SET_DATA, "str")]

        result = self.serializer.write_value("str", var, "xsdata")
        self.assertIsInstance(result, Generator)
        self.assertEqual(expected, list(result))

    def test_write_any_type_with_primitive_element(self):
        var = XmlElement(qname="a", name="a", types=[object])
        expected = [
            (XmlEventWriter.START_TAG, "a"),
            (XmlEventWriter.SET_DATA, "str"),
            (XmlEventWriter.END_TAG, "a"),
        ]

        result = self.serializer.write_value("str", var, "xsdata")
        self.assertIsInstance(result, Generator)
        self.assertEqual(expected, list(result))

    def test_write_any_type_with_generic_object(self):
        var = XmlWildcard(qname="a", name="a")
        value = AnyElement(
            qname="a",
            text="b",
            tail="c",
            attributes={"d": 1, "e": 2},
            children=[AnyElement(text="g"), "h"],
        )
        expected = [
            (XmlEventWriter.START_TAG, "a"),
            (XmlEventWriter.ADD_ATTR, "d", 1),
            (XmlEventWriter.ADD_ATTR, "e", 2),
            (XmlEventWriter.SET_DATA, "b"),
            (XmlEventWriter.SET_DATA, "g"),
            (XmlEventWriter.SET_DATA, None),
            (XmlEventWriter.SET_DATA, "h"),
            (XmlEventWriter.END_TAG, "a"),
            (XmlEventWriter.SET_DATA, "c"),
        ]

        result = self.serializer.write_value(value, var, "xsdata")
        self.assertIsInstance(result, Generator)
        self.assertEqual(expected, list(result))

    def test_write_xsi_type(self):
        var = XmlElement(qname="a", name="a", dataclass=True, types=[BookForm])
        value = BookForm(id="123")
        expected = [
            (XmlEventWriter.START_TAG, "a"),
            (XmlEventWriter.ADD_ATTR, "id", "123"),
            (XmlEventWriter.ADD_ATTR, "lang", "en"),
            (XmlEventWriter.END_TAG, "a"),
        ]

        result = self.serializer.write_value(value, var, "xsdata")
        self.assertIsInstance(result, Generator)
        self.assertEqual(expected, list(result))

    def test_write_xsi_type_with_derived_class(self):
        var = XmlElement(qname="a", name="a", dataclass=True, types=[BookForm])
        ebook = make_dataclass("eBook", [], bases=(BookForm,))

        value = ebook(id="123")
        expected = [
            (XmlEventWriter.START_TAG, "a"),
            (XmlEventWriter.ADD_ATTR, "id", "123"),
            (XmlEventWriter.ADD_ATTR, "lang", "en"),
            (XmlEventWriter.ADD_ATTR, QNames.XSI_TYPE, QName("eBook")),
            (XmlEventWriter.END_TAG, "a"),
        ]

        result = self.serializer.write_value(value, var, "xsdata")
        self.assertIsInstance(result, Generator)
        self.assertEqual(expected, list(result))

    def test_write_xsi_type_with_illegal_derived_class(self):
        var = XmlElement(qname="a", name="a", dataclass=True, types=[BookForm])
        ebook = make_dataclass("eBook", [])
        value = ebook()

        result = self.serializer.write_value(value, var, "xsdata")
        with self.assertRaises(SerializerError) as cm:
            list(result)

        self.assertEqual("eBook is not derived from BookForm", str(cm.exception))

    def test_write_element(self):
        var = XmlElement(qname="a", name="a")
        expected = [
            (XmlEventWriter.START_TAG, "a"),
            (XmlEventWriter.SET_DATA, "123"),
            (XmlEventWriter.END_TAG, "a"),
        ]

        result = self.serializer.write_value("123", var, "xsdata")
        self.assertIsInstance(result, Generator)
        self.assertEqual(expected, list(result))

    def test_write_element_with_nillable_true(self):
        var = XmlElement(qname="a", name="a", nillable=True)
        expected = [
            (XmlEventWriter.START_TAG, "a"),
            (XmlEventWriter.ADD_ATTR, QNames.XSI_NIL, "true"),
            (XmlEventWriter.SET_DATA, "123"),
            (XmlEventWriter.END_TAG, "a"),
        ]

        result = self.serializer.write_value("123", var, "xsdata")
        self.assertIsInstance(result, Generator)
        self.assertEqual(expected, list(result))

    def test_write_value_with_list_value(self):
        var = XmlElement(qname="a", name="a", list_element=True)
        value = [True, False]
        expected = [
            (XmlEventWriter.START_TAG, "a"),
            (XmlEventWriter.SET_DATA, True),
            (XmlEventWriter.END_TAG, "a"),
            (XmlEventWriter.START_TAG, "a"),
            (XmlEventWriter.SET_DATA, False),
            (XmlEventWriter.END_TAG, "a"),
        ]

        result = self.serializer.write_value(value, var, "xsdata")
        self.assertIsInstance(result, Generator)
        self.assertEqual(expected, list(result))

    def test_write_value_with_unhandled_xml_var(self):
        foo = make_dataclass("foo", [], bases=(XmlVar,), frozen=True)
        var = foo(qname="a", name="a", list_element=True)
        result = self.serializer.write_value("123", var, "xsdata")

        with self.assertRaises(SerializerError) as cm:
            list(result)

        self.assertEqual("Unhandled xml var: `foo`", str(cm.exception))

    def test_next_value(self):
        obj = A(x0=1, x1=[2, 3, 4], x2=[6, 7], x3=[9])
        meta = self.serializer.context.build(A)
        x0 = meta.find_var("x0")
        x1 = meta.find_var("x1")
        x2 = meta.find_var("x2")
        x3 = meta.find_var("x3")

        actual = self.serializer.next_value(obj, meta)
        expected = [
            (x0, 1),
            (x1, 2),
            (x2, 6),
            (x3, 9),
            (x1, 3),
            (x2, 7),
            (x1, 4),
        ]

        self.assertIsInstance(actual, Generator)
        self.assertEqual(expected, list(actual))

    def test_next_attribute(self):
        obj = A(a0="foo", a1={"b": "c", "d": "e"})
        meta = self.serializer.context.build(A)

        actual = self.serializer.next_attribute(obj, meta, False, None)
        expected = [
            ("a0", "foo"),
            ("b", "c"),
            ("d", "e"),
        ]

        self.assertIsInstance(actual, Generator)
        self.assertEqual(expected, list(actual))

        actual = self.serializer.next_attribute(obj, meta, True, "xs:bool")
        expected.extend(
            [
                (QNames.XSI_TYPE, "xs:bool"),
                (QNames.XSI_NIL, "true"),
            ]
        )
        self.assertEqual(expected, list(actual))

    def test_render_mixed_content(self):
        @dataclass
        class Span:
            class Meta:
                name = "span"

            content: str

        @dataclass
        class Example:
            class Meta:
                name = "p"

            content: List[object] = field(
                default_factory=list,
                metadata=dict(
                    type="Wildcard",
                    namespace="##any",
                    mixed=True,
                    min_occurs=0,
                    max_occurs=9223372036854775807,
                ),
            )

        obj = Example()
        obj.content.append(AnyElement(qname="b", text="Mr."))
        obj.content.append(Span("chris"))
        obj.content.append("!")

        self.serializer.xml_declaration = False
        self.serializer.pretty_print = False
        result = self.serializer.render(obj)
        self.assertEqual("<p><b>Mr.</b><span>chris</span>!</p>", result)

        obj = Example()
        obj.content.append("Hi ")
        obj.content.append(AnyElement(qname="b", text="Mr."))
        obj.content.append(Span("chris"))
        obj.content.append("!")
        result = self.serializer.render(obj)
        self.assertEqual("<p>Hi <b>Mr.</b><span>chris</span>!</p>", result)
