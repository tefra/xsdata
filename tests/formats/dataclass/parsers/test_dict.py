import json
from dataclasses import asdict, dataclass, field
from decimal import Decimal
from typing import List, Optional, Union
from xml.etree.ElementTree import QName

from tests import fixtures_dir
from tests.fixtures.books import BookForm, Books
from tests.fixtures.models import (
    AttrsType,
    BaseC,
    BaseType,
    ChoiceType,
    ExtendedType,
    FixedType,
    OptionalChoiceType,
    TypeA,
    TypeB,
    TypeC,
    TypeD,
    UnionType,
)
from tests.fixtures.wrapper import Charlie, Wrapper
from xsdata.exceptions import ParserError
from xsdata.formats.dataclass.models.generics import AnyElement, DerivedElement
from xsdata.formats.dataclass.parsers import DictDecoder
from xsdata.models.datatype import XmlDate
from xsdata.utils.testing import FactoryTestCase


class DictDecoderTests(FactoryTestCase):
    def setUp(self) -> None:
        super().setUp()

        self.decoder = DictDecoder()

    def test_decode(self):
        path = fixtures_dir.joinpath("books/books.json")
        source = json.loads(path.read_text())
        books = self.decoder.decode(source, Books)

        self.assertIsInstance(books, Books)

        self.assertEqual(
            BookForm(
                author="Hightower, Kim",
                title="The First Book",
                genre="Fiction",
                price=44.95,
                pub_date=XmlDate.from_string("2000-10-01"),
                review="An amazing story of nothing.",
                id="bk001",
            ),
            books.book[0],
        )

        self.assertEqual(
            BookForm(
                author="Nagata, Suanne",
                title="Becoming Somebody",
                genre="Biography",
                price=None,
                pub_date=None,
                review="A masterpiece of the fine art of gossiping.",
                id="bk002",
            ),
            books.book[1],
        )

    def test_decode_empty_document(self):
        self.assertEqual(BookForm(), self.decoder.decode({}, BookForm))
        self.assertEqual([], self.decoder.decode([], List[BookForm]))

    def test_decode_list_of_objects(self):
        path = fixtures_dir.joinpath("books/books.json")
        data = json.loads(path.read_text())
        book_list = data["book"]

        books = self.decoder.decode(book_list, List[BookForm])
        self.assertIsInstance(books, list)
        self.assertEqual(2, len(books))
        self.assertIsInstance(books[0], BookForm)
        self.assertIsInstance(books[1], BookForm)

    def test_decode_with_unknown_class(self):
        path = fixtures_dir.joinpath("books/books.json")
        source = json.loads(path.read_text())
        books = self.decoder.decode(source)
        self.assertIsInstance(books, Books)
        self.assertEqual(2, len(books.book))

        book_list = self.decoder.decode(source["book"])
        self.assertIsInstance(book_list, list)
        self.assertEqual(2, len(book_list))
        self.assertIsInstance(book_list[0], BookForm)
        self.assertIsInstance(book_list[1], BookForm)

    def test_decode_with_fail_on_converter_warnings(self):
        json_str = {"x": "foo"}
        self.decoder.config.fail_on_converter_warnings = True
        with self.assertRaises(ParserError) as cm:
            self.decoder.decode(json_str, TypeA)

        self.assertEqual(
            "Failed to convert value `foo` to one of (<class 'int'>,)",
            str(cm.exception),
        )

    def test_decode_wrapper(self):
        data = {
            "alphas": {"alpha": "value"},
            "bravos": {"bravo": [1, 2]},
            "charlies": {
                "charlie": [
                    {"value": "first", "lang": "en"},
                    {"value": "second", "lang": "en"},
                ]
            },
        }

        actual = self.decoder.decode(data, Wrapper)
        expected = Wrapper(
            alpha="value",
            bravo=[1, 2],
            charlie=[
                Charlie(value="first", lang="en"),
                Charlie(value="second", lang="en"),
            ],
        )
        self.assertEqual(expected, actual)

    def test_verify_type(self):
        invalid_cases = [
            (
                {"not": 1, "found": 1},
                None,
                "Unable to locate model with properties(['not', 'found'])",
            ),
            ({}, None, "Document is empty, can not detect type"),
            ([], BookForm, "Document is array, expected object"),
            ({}, List[BookForm], "Document is object, expected array"),
            (
                {},
                Optional[ChoiceType],
                f"Invalid clazz argument: {Optional[ChoiceType]}",
            ),
            ([], List[int], f"Invalid clazz argument: {List[int]}"),
            ([], List, f"Invalid clazz argument: {List}"),
        ]

        for source, clazz, exc_msg in invalid_cases:
            with self.assertRaises(ParserError) as cm:
                self.decoder.decode(source, clazz=clazz)

            self.assertEqual(exc_msg, str(cm.exception))

    def test_bind_dataclass_with_unknown_property(self):
        data = {"unknown": True}
        with self.assertRaises(ParserError) as cm:
            self.decoder.bind_dataclass(data, Books)

        self.assertEqual("Unknown property Books.unknown", str(cm.exception))

        self.decoder.config.fail_on_unknown_properties = False
        self.assertEqual(Books(), self.decoder.bind_dataclass(data, Books))

    def test_bind_dataclass_with_required_fields(self):
        obj = self.decoder.bind_dataclass({"x": 1, "y": "a", "z": None}, TypeD)

        self.assertEqual(1, obj.x)
        self.assertEqual("a", obj.y)
        self.assertIsNone(obj.z)

        with self.assertRaises(ParserError):
            self.decoder.bind_dataclass({"x": 1, "y": "a"}, TypeD)

    def test_bind_dataclass_with_fixed_field(self):
        obj = self.decoder.bind_dataclass({"value": "abc"}, FixedType)
        self.assertEqual("abc", obj.value)

        with self.assertRaises(ParserError):
            self.decoder.bind_dataclass({"value": "abcd"}, FixedType)

    def test_bind_derived_dataclass(self):
        data = {
            "qname": "{urn:books}BookForm",
            "type": None,
            "value": {
                "author": "Nagata, Suanne",
                "title": "Becoming Somebody",
            },
        }

        actual = self.decoder.bind_dataclass(data, BookForm)
        expected = DerivedElement(
            qname="{urn:books}BookForm",
            value=BookForm(author="Nagata, Suanne", title="Becoming Somebody"),
            type=None,
        )
        self.assertEqual(expected, actual)

    def test_bind_derived_dataclass_with_xsi_type(self):
        data = {
            "qname": "foobar",
            "type": "{urn:books}BookForm",
            "value": {
                "author": "Nagata, Suanne",
                "title": "Becoming Somebody",
            },
        }

        actual = self.decoder.bind_dataclass(data, DerivedElement)
        expected = DerivedElement(
            qname="foobar",
            value=BookForm(author="Nagata, Suanne", title="Becoming Somebody"),
            type="{urn:books}BookForm",
        )
        self.assertEqual(expected, actual)

        with self.assertRaises(ParserError) as cm:
            data["type"] = "notExists"
            self.decoder.bind_dataclass(data, DerivedElement)

        self.assertEqual(
            "Unable to locate derived model with" " properties(['author', 'title'])",
            str(cm.exception),
        )

        with self.assertRaises(ParserError) as cm:
            data["type"] = None
            self.decoder.bind_dataclass(data, DerivedElement)

    def test_bind_dataclass_union(self):
        data = {"element": {"x": 1, "y": "foo", "z": "1.0"}}
        actual = self.decoder.bind_dataclass(data, UnionType)

        self.assertIsInstance(actual.element, TypeC)

        with self.assertRaises(ParserError) as cm:
            self.decoder.bind_dataclass({"element": {"a": 1}}, UnionType)

        self.assertEqual(
            "Failed to bind object with properties(['a']) "
            "to any of the ['TypeA', 'TypeB', 'TypeC', 'TypeD']",
            str(cm.exception),
        )

    def test_bind_dataclass_subclasses(self):
        data = {"element": {"x": "1", "y": "foo", "z": "1.0"}}
        actual = self.decoder.bind_dataclass(data, BaseType)

        self.assertIsInstance(actual.element, BaseC)

    def test_bind_attributes(self):
        data = {"attrs": {"a": 1, "b": 2}, "index": 1}

        actual = self.decoder.bind_dataclass(data, AttrsType)
        self.assertEqual(data["attrs"], actual.attrs)
        self.assertIsNot(data["attrs"], actual.attrs)

    def test_bind_simple_type_with_wildcard_var(self):
        data = {"any": 1, "wildcard": 2}
        actual = self.decoder.bind_dataclass(data, ExtendedType)
        self.assertEqual(1, actual.any)
        self.assertEqual(2, actual.wildcard)

    def test_bind_simple_type_with_elements_var(self):
        data = {"choice": ["1.0", 1, ["1.2"], "{a}b"]}

        actual = self.decoder.bind_dataclass(data, ChoiceType)

        self.assertEqual(1.0, actual.choice[0])
        self.assertEqual(1, actual.choice[1])
        self.assertEqual([Decimal("1.2")], actual.choice[2])
        self.assertEqual(QName("{a}b"), actual.choice[3])
        self.assertIsInstance(actual.choice[3], QName)

        data = {"choice": ["!NotAQname"]}
        with self.assertRaises(ParserError) as cm:
            self.decoder.bind_dataclass(data, ChoiceType)

        self.assertEqual(
            "Failed to bind '!NotAQname' to ChoiceType.choice field",
            str(cm.exception),
        )

    def test_bind_simple_type_with_optional_elements_var(self):
        data = {"a_or_b": None}
        actual = self.decoder.bind_dataclass(data, OptionalChoiceType)
        self.assertIsNone(None, actual.a_or_b)

    def test_bind_any_element(self):
        data = {
            "wildcard": {
                "qname": "a",
                "text": 1,
                "tail": None,
                "children": [],
                "attributes": {},
            }
        }
        self.assertEqual(
            ExtendedType(wildcard=AnyElement(qname="a", text="1")),
            self.decoder.bind_dataclass(data, ExtendedType),
        )

    def test_bind_choice_dataclass(self):
        data = {"choice": [{"x": 1}, {"x": 1, "y": "a"}]}
        expected = ChoiceType(choice=[TypeA(x=1), TypeB(x=1, y="a")])
        self.assertEqual(expected, self.decoder.bind_dataclass(data, ChoiceType))

    def test_bind_derived_value_with_choice_var(self):
        data = {
            "choice": [
                {
                    "qname": "b",
                    "type": None,
                    "value": {
                        "x": "1",
                        "y": "a",
                    },
                }
            ]
        }
        expected = ChoiceType(
            choice=[
                DerivedElement(
                    qname="b",
                    value=TypeB(x=1, y="a"),
                )
            ]
        )
        self.assertEqual(expected, self.decoder.bind_dataclass(data, ChoiceType))

        with self.assertRaises(ParserError) as cm:
            data["choice"][0]["qname"] = "nope"
            self.decoder.bind_dataclass(data, ChoiceType)

        self.assertEqual(
            "Unable to locate compound element ChoiceType.choice[nope]",
            str(cm.exception),
        )

    def test_bind_derived_value_with_simple_type(self):
        data = {"choice": [{"qname": "float", "value": 1, "type": None}]}

        actual = self.decoder.bind_dataclass(data, ChoiceType)
        expected = ChoiceType(choice=[DerivedElement(qname="float", value=1)])
        self.assertEqual(expected, actual)

    def test_bind_wildcard_dataclass(self):
        data = {"a": None, "wildcard": {"x": 1}}
        expected = ExtendedType(wildcard=TypeA(x=1))
        self.assertEqual(expected, self.decoder.bind_dataclass(data, ExtendedType))

    def test_bind_wildcard_with_derived_dataclass(self):
        data = {
            "wildcard": {
                "qname": "b",
                "type": "{xsdata}TypeB",
                "value": {
                    "x": "1",
                    "y": "a",
                },
            }
        }
        expected = ExtendedType(
            wildcard=DerivedElement(
                qname="b", value=TypeB(x=1, y="a"), type="{xsdata}TypeB"
            )
        )
        self.assertEqual(expected, self.decoder.bind_dataclass(data, ExtendedType))

    def test_bind_any_type_with_derived_dataclass(self):
        data = {
            "any": {
                "qname": "any",
                "type": None,
                "value": {"x": "1"},
            }
        }
        expected = ExtendedType(any=DerivedElement(qname="any", value=TypeA(x=1)))
        self.assertEqual(expected, self.decoder.bind_dataclass(data, ExtendedType))

        with self.assertRaises(ParserError) as cm:
            data["any"]["type"] = "notexists"
            self.decoder.bind_dataclass(data, ExtendedType)

        self.assertEqual("Unable to locate xsi:type `notexists`", str(cm.exception))

    def test_bind_text_with_unions(self):
        @dataclass
        class Fixture:
            x: List[Union[int, float, str, bool]] = field(metadata={"tokens": True})

        values = ["foo", 12.2, "12.2", 12, "12", True, "false"]

        result = self.decoder.decode({"x": values}, Fixture)
        expected = ["foo", 12.2, 12.2, 12, 12, True, False]
        self.assertEqual({"x": expected}, asdict(result))

    def test_find_var(self):
        meta = self.decoder.context.build(TypeB)
        xml_vars = meta.get_all_vars()

        self.assertEqual(xml_vars[0], self.decoder.find_var(xml_vars, "x", 1))
        self.assertIsNone(self.decoder.find_var(xml_vars, "x", [1, 2]))

        meta = self.decoder.context.build(ExtendedType)
        xml_vars = meta.get_all_vars()
        self.assertIsNone(self.decoder.find_var(xml_vars, "a", [1, 2]))
        self.assertEqual(xml_vars[0], self.decoder.find_var(xml_vars, "a", {"x": 1}))

        meta = self.decoder.context.build(Wrapper)
        xml_vars = meta.get_all_vars()
        self.assertIsNone(self.decoder.find_var(xml_vars, "charlies", {}))
        self.assertIsNone(self.decoder.find_var(xml_vars, "bravos", {"bravo": 1}))
        self.assertEqual(
            xml_vars[0], self.decoder.find_var(xml_vars, "alphas", {"alpha": "foo"})
        )
