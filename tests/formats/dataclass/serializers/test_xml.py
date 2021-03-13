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
from xsdata.formats.dataclass.models.elements import XmlVar
from xsdata.formats.dataclass.models.generics import AnyElement
from xsdata.formats.dataclass.models.generics import DerivedElement
from xsdata.formats.dataclass.serializers import XmlSerializer
from xsdata.formats.dataclass.serializers.mixins import XmlWriterEvent
from xsdata.models.enums import DataType
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

    def test_write_object_with_derived_element(self):
        book = BookForm(id="123")
        obj = DerivedElement(qname="item", value=book)

        result = self.serializer.write_object(obj)
        expected = [
            (XmlWriterEvent.START, "item"),
            (XmlWriterEvent.ATTR, "id", "123"),
            (XmlWriterEvent.ATTR, "lang", "en"),
            (XmlWriterEvent.ATTR, QNames.XSI_TYPE, "{urn:books}BookForm"),
            (XmlWriterEvent.END, "item"),
        ]
        self.assertIsInstance(result, Generator)
        self.assertEqual(expected, list(result))

    def test_write_dataclass(self):
        book = BookForm(id="123", title="Misterioso: A Crime Novel", price=19.5)
        result = self.serializer.write_object(book)
        expected = [
            (XmlWriterEvent.START, "BookForm"),
            (XmlWriterEvent.ATTR, "id", "123"),
            (XmlWriterEvent.ATTR, "lang", "en"),
            (XmlWriterEvent.START, "title"),
            (XmlWriterEvent.DATA, "Misterioso: A Crime Novel"),
            (XmlWriterEvent.END, "title"),
            (XmlWriterEvent.START, "price"),
            (XmlWriterEvent.DATA, "19.5"),
            (XmlWriterEvent.END, "price"),
            (XmlWriterEvent.END, "BookForm"),
        ]
        self.assertIsInstance(result, Generator)
        self.assertEqual(expected, list(result))

    def test_write_dataclass_can_overwrite_params(self):
        book = BookForm(id="123", title="Misterioso: A Crime Novel", price=19.5)
        result = self.serializer.write_dataclass(
            book, "xsdata", "book", True, "foo:book"
        )
        expected = [
            (XmlWriterEvent.START, "book"),
            (XmlWriterEvent.ATTR, "id", "123"),
            (XmlWriterEvent.ATTR, "lang", "en"),
            (XmlWriterEvent.ATTR, QNames.XSI_TYPE, "foo:book"),
            (XmlWriterEvent.ATTR, QNames.XSI_NIL, "true"),
            (XmlWriterEvent.START, "title"),
            (XmlWriterEvent.DATA, "Misterioso: A Crime Novel"),
            (XmlWriterEvent.END, "title"),
            (XmlWriterEvent.START, "price"),
            (XmlWriterEvent.DATA, "19.5"),
            (XmlWriterEvent.END, "price"),
            (XmlWriterEvent.END, "book"),
        ]
        self.assertIsInstance(result, Generator)
        self.assertEqual(expected, list(result))

    def test_write_dataclass_with_no_dataclass(self):
        with self.assertRaises(XmlContextError) as cm:
            next(self.serializer.write_dataclass(1))
        self.assertEqual("Object <class 'int'> is not a dataclass.", str(cm.exception))

    def test_write_mixed_content(self):
        var = XmlVar(wildcard=True, qname="a", name="a", mixed=True)
        book = BookForm(id="123")
        ebook = DerivedElement("ebook", BookForm(id="123"))
        value = ["text", AnyElement(qname="br"), book, ebook, "tail"]
        result = self.serializer.write_value(value, var, "xsdata")
        expected = [
            (XmlWriterEvent.DATA, "text"),
            (XmlWriterEvent.START, "br"),
            (XmlWriterEvent.DATA, None),
            (XmlWriterEvent.END, "br"),
            (XmlWriterEvent.START, "{xsdata}BookForm"),
            (XmlWriterEvent.ATTR, "id", "123"),
            (XmlWriterEvent.ATTR, "lang", "en"),
            (XmlWriterEvent.END, "{xsdata}BookForm"),
            (XmlWriterEvent.START, "ebook"),
            (XmlWriterEvent.ATTR, "id", "123"),
            (XmlWriterEvent.ATTR, "lang", "en"),
            (XmlWriterEvent.END, "ebook"),
            (XmlWriterEvent.DATA, "tail"),
        ]

        self.assertIsInstance(result, Generator)
        self.assertEqual(expected, list(result))

    def test_write_data(self):
        var = XmlVar(text=True, qname="a", name="a")
        expected = [(XmlWriterEvent.DATA, "123")]

        result = self.serializer.write_value("123", var, "xsdata")
        self.assertIsInstance(result, Generator)
        self.assertEqual(expected, list(result))

    def test_write_tokens(self):
        var = XmlVar(element=True, qname="a", name="a", tokens=True)

        result = self.serializer.write_value([], var, "xsdata")
        self.assertIsInstance(result, Generator)
        self.assertEqual(0, len(list(result)))

        expected = [
            (XmlWriterEvent.START, "a"),
            (XmlWriterEvent.DATA, ["1", QName("{a}b"), "3"]),
            (XmlWriterEvent.END, "a"),
        ]
        result = self.serializer.write_value([1, QName("{a}b"), 3], var, "xsdata")
        self.assertEqual(expected, list(result))

        expected = [
            (XmlWriterEvent.START, "a"),
            (XmlWriterEvent.DATA, ["1", "2", "3"]),
            (XmlWriterEvent.END, "a"),
            (XmlWriterEvent.START, "a"),
            (XmlWriterEvent.DATA, ["4", "5", "6"]),
            (XmlWriterEvent.END, "a"),
        ]

        result = self.serializer.write_value([[1, 2, 3], [4, 5, 6]], var, "xsdata")
        self.assertEqual(expected, list(result))

        var = XmlVar(element=True, qname="a", name="a", tokens=True, nillable=True)
        expected = [
            (XmlWriterEvent.START, "a"),
            (XmlWriterEvent.ATTR, QNames.XSI_NIL, "true"),
            (XmlWriterEvent.DATA, []),
            (XmlWriterEvent.END, "a"),
        ]

        result = self.serializer.write_value([], var, "xsdata")
        self.assertEqual(expected, list(result))

    def test_write_any_type_with_primitive(self):
        var = XmlVar(wildcard=True, qname="a", name="a")
        expected = [(XmlWriterEvent.DATA, "str")]

        result = self.serializer.write_value("str", var, "xsdata")
        self.assertIsInstance(result, Generator)
        self.assertEqual(expected, list(result))

    def test_write_any_type_with_primitive_element(self):
        var = XmlVar(element=True, qname="a", name="a", types=[object])
        expected = [
            (XmlWriterEvent.START, "a"),
            (XmlWriterEvent.DATA, "str"),
            (XmlWriterEvent.END, "a"),
        ]

        result = self.serializer.write_value("str", var, "xsdata")
        self.assertIsInstance(result, Generator)
        self.assertEqual(expected, list(result))

    def test_write_any_type_with_any_element(self):
        var = XmlVar(wildcard=True, qname="a", name="a")
        value = AnyElement(
            qname="a",
            text="b",
            tail="c",
            attributes={"d": 1, "e": 2},
            children=[AnyElement(text="g"), "h"],
        )
        expected = [
            (XmlWriterEvent.START, "a"),
            (XmlWriterEvent.ATTR, "d", 1),
            (XmlWriterEvent.ATTR, "e", 2),
            (XmlWriterEvent.DATA, "b"),
            (XmlWriterEvent.DATA, "g"),
            (XmlWriterEvent.DATA, "h"),
            (XmlWriterEvent.END, "a"),
            (XmlWriterEvent.DATA, "c"),
        ]

        result = self.serializer.write_value(value, var, "xsdata")
        self.assertIsInstance(result, Generator)
        self.assertEqual(expected, list(result))

    def test_write_any_type_with_derived_element_primitive(self):
        var = XmlVar(wildcard=True, qname="a", name="a")
        value = DerivedElement(qname="a", value=1)
        expected = [
            (XmlWriterEvent.START, "a"),
            (XmlWriterEvent.ATTR, QNames.XSI_TYPE, QName(str(DataType.SHORT))),
            (XmlWriterEvent.DATA, 1),
            (XmlWriterEvent.END, "a"),
        ]

        result = self.serializer.write_value(value, var, "xsdata")
        self.assertIsInstance(result, Generator)
        self.assertEqual(expected, list(result))

    def test_write_any_type_with_derived_element_dataclass(self):
        var = XmlVar(wildcard=True, qname="a", name="a")
        value = DerivedElement(qname="a", value=BookForm(title="def"), substituted=True)
        expected = [
            (XmlWriterEvent.START, "a"),
            (XmlWriterEvent.ATTR, "lang", "en"),
            (XmlWriterEvent.ATTR, QNames.XSI_TYPE, QName("{urn:books}BookForm")),
            (XmlWriterEvent.START, "title"),
            (XmlWriterEvent.DATA, "def"),
            (XmlWriterEvent.END, "title"),
            (XmlWriterEvent.END, "a"),
        ]

        result = self.serializer.write_value(value, var, "xsdata")
        self.assertIsInstance(result, Generator)
        self.assertEqual(expected, list(result))

    def test_write_xsi_type(self):
        var = XmlVar(
            element=True, qname="a", name="a", dataclass=True, types=[BookForm]
        )
        value = BookForm(id="123")
        expected = [
            (XmlWriterEvent.START, "a"),
            (XmlWriterEvent.ATTR, "id", "123"),
            (XmlWriterEvent.ATTR, "lang", "en"),
            (XmlWriterEvent.END, "a"),
        ]

        result = self.serializer.write_value(value, var, "xsdata")
        self.assertIsInstance(result, Generator)
        self.assertEqual(expected, list(result))

    def test_write_xsi_type_with_derived_class(self):
        var = XmlVar(
            element=True, qname="a", name="a", dataclass=True, types=[BookForm]
        )
        ebook = make_dataclass("eBook", [], bases=(BookForm,))

        value = ebook(id="123")
        expected = [
            (XmlWriterEvent.START, "a"),
            (XmlWriterEvent.ATTR, "id", "123"),
            (XmlWriterEvent.ATTR, "lang", "en"),
            (XmlWriterEvent.ATTR, QNames.XSI_TYPE, QName("eBook")),
            (XmlWriterEvent.END, "a"),
        ]

        result = self.serializer.write_value(value, var, "xsdata")
        self.assertIsInstance(result, Generator)
        self.assertEqual(expected, list(result))

    def test_write_xsi_type_with_illegal_derived_class(self):
        var = XmlVar(
            element=True, qname="a", name="a", dataclass=True, types=[BookForm]
        )
        ebook = make_dataclass("eBook", [])
        value = ebook()

        result = self.serializer.write_value(value, var, "xsdata")
        with self.assertRaises(SerializerError) as cm:
            list(result)

        self.assertEqual("eBook is not derived from BookForm", str(cm.exception))

    def test_write_element(self):
        var = XmlVar(element=True, qname="a", name="a")
        expected = [
            (XmlWriterEvent.START, "a"),
            (XmlWriterEvent.DATA, "123"),
            (XmlWriterEvent.END, "a"),
        ]

        result = self.serializer.write_value("123", var, "xsdata")
        self.assertIsInstance(result, Generator)
        self.assertEqual(expected, list(result))

    def test_write_element_with_nillable_true(self):
        var = XmlVar(element=True, qname="a", name="a", nillable=True)
        expected = [
            (XmlWriterEvent.START, "a"),
            (XmlWriterEvent.ATTR, QNames.XSI_NIL, "true"),
            (XmlWriterEvent.DATA, "123"),
            (XmlWriterEvent.END, "a"),
        ]

        result = self.serializer.write_value("123", var, "xsdata")
        self.assertIsInstance(result, Generator)
        self.assertEqual(expected, list(result))

    def test_write_element_with_any_type_var(self):
        var = XmlVar(element=True, qname="a", name="a", types=[object], any_type=True)
        expected = [
            (XmlWriterEvent.START, "a"),
            (XmlWriterEvent.ATTR, QNames.XSI_TYPE, QName(str(DataType.SHORT))),
            (XmlWriterEvent.DATA, "123"),
            (XmlWriterEvent.END, "a"),
        ]

        result = self.serializer.write_value(123, var, "xsdata")
        self.assertIsInstance(result, Generator)
        self.assertEqual(expected, list(result))

    def test_write_element_with_any_type_var_ignore_xs_string(self):
        var = XmlVar(element=True, qname="a", name="a", types=[object], any_type=True)
        expected = [
            (XmlWriterEvent.START, "a"),
            (XmlWriterEvent.DATA, ""),
            (XmlWriterEvent.END, "a"),
        ]
        result = self.serializer.write_value("", var, "xsdata")
        self.assertIsInstance(result, Generator)
        self.assertEqual(expected, list(result))

        expected = [
            (XmlWriterEvent.START, "a"),
            (XmlWriterEvent.DATA, "123"),
            (XmlWriterEvent.END, "a"),
        ]
        result = self.serializer.write_value("123", var, "xsdata")
        self.assertIsInstance(result, Generator)
        self.assertEqual(expected, list(result))

    def test_write_choice_with_derived_primitive_value(self):
        var = XmlVar(
            elements=True,
            name="compound",
            qname="compound",
            choices=[XmlVar(element=True, qname="a", name="a", types=[int])],
        )
        value = DerivedElement(qname="a", value=1)
        expected = [
            (XmlWriterEvent.START, "a"),
            (XmlWriterEvent.DATA, "1"),
            (XmlWriterEvent.END, "a"),
        ]

        result = self.serializer.write_value(value, var, "xsdata")
        self.assertIsInstance(result, Generator)
        self.assertEqual(expected, list(result))

    def test_write_choice_with_derived_dataclass(self):
        var = XmlVar(
            elements=True,
            name="compound",
            qname="compound",
            choices=[XmlVar(element=True, qname="a", name="a", types=[A])],
        )
        value = DerivedElement(qname="a", value=A("foo"))
        expected = [
            (XmlWriterEvent.START, "a"),
            (XmlWriterEvent.ATTR, "a0", "foo"),
            (XmlWriterEvent.END, "a"),
        ]

        result = self.serializer.write_value(value, var, "xsdata")
        self.assertIsInstance(result, Generator)
        self.assertEqual(expected, list(result))

    def test_write_choice_with_generic_object(self):
        var = XmlVar(
            elements=True,
            name="compound",
            qname="compound",
            choices=[XmlVar(element=True, qname="a", name="a", types=[int])],
        )
        value = AnyElement(qname="a", text="1")
        expected = [
            (XmlWriterEvent.START, "a"),
            (XmlWriterEvent.DATA, "1"),
            (XmlWriterEvent.END, "a"),
        ]

        result = self.serializer.write_value(value, var, "xsdata")
        self.assertIsInstance(result, Generator)
        self.assertEqual(expected, list(result))

    def test_write_choice_with_raw_value(self):
        var = XmlVar(
            elements=True,
            name="compound",
            qname="compound",
            choices=[
                XmlVar(element=True, qname="a", name="a", types=[int]),
                XmlVar(element=True, qname="b", name="b", types=[int], tokens=True),
            ],
        )
        expected = [
            (XmlWriterEvent.START, "a"),
            (XmlWriterEvent.DATA, "1"),
            (XmlWriterEvent.END, "a"),
            (XmlWriterEvent.START, "b"),
            (XmlWriterEvent.DATA, ["1", "2"]),
            (XmlWriterEvent.END, "b"),
        ]

        result = self.serializer.write_value([1, [1, 2]], var, "xsdata")
        self.assertIsInstance(result, Generator)
        self.assertEqual(expected, list(result))

    def test_write_choice_when_no_matching_choice_exists(self):
        var = XmlVar(
            elements=True,
            name="compound",
            qname="compound",
            choices=[XmlVar(element=True, qname="a", name="a", types=[float])],
        )

        with self.assertRaises(SerializerError) as cm:
            result = self.serializer.write_value(1, var, "xsdata")
            next(result)

        msg = "XmlElements undefined choice: `compound` for `<class 'int'>`"
        self.assertEqual(msg, str(cm.exception))

    def test_write_value_with_list_value(self):
        var = XmlVar(element=True, qname="a", name="a", list_element=True)
        value = [True, False]
        expected = [
            (XmlWriterEvent.START, "a"),
            (XmlWriterEvent.DATA, "true"),
            (XmlWriterEvent.END, "a"),
            (XmlWriterEvent.START, "a"),
            (XmlWriterEvent.DATA, "false"),
            (XmlWriterEvent.END, "a"),
        ]

        result = self.serializer.write_value(value, var, "xsdata")
        self.assertIsInstance(result, Generator)
        self.assertEqual(expected, list(result))

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

        self.serializer.pretty_print = False
        result = self.serializer.render(obj).splitlines()
        self.assertEqual("<p><b>Mr.</b><span>chris</span>!</p>", result[1])

        obj = Example()
        obj.content.append("Hi ")
        obj.content.append(AnyElement(qname="b", text="Mr."))
        obj.content.append(Span("chris"))
        obj.content.append("!")
        result = self.serializer.render(obj).splitlines()
        self.assertEqual("<p>Hi <b>Mr.</b><span>chris</span>!</p>", result[1])
