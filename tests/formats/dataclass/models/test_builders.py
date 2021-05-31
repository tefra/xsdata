import sys
import uuid
from dataclasses import dataclass
from dataclasses import field
from dataclasses import fields
from dataclasses import make_dataclass
from typing import Dict
from typing import get_type_hints
from typing import Iterator
from typing import List
from typing import Type
from typing import Union
from unittest import mock
from unittest import TestCase

from tests.fixtures.artists import Artist
from tests.fixtures.books import BookForm
from tests.fixtures.models import TypeB
from tests.fixtures.series import Country
from xsdata.exceptions import XmlContextError
from xsdata.formats.dataclass.models.builders import XmlMetaBuilder
from xsdata.formats.dataclass.models.builders import XmlVarBuilder
from xsdata.formats.dataclass.models.elements import XmlType
from xsdata.models.datatype import XmlDate
from xsdata.utils import text
from xsdata.utils.constants import return_input
from xsdata.utils.constants import return_true
from xsdata.utils.namespaces import build_qname
from xsdata.utils.testing import FactoryTestCase
from xsdata.utils.testing import XmlMetaFactory
from xsdata.utils.testing import XmlVarFactory


class XmlMetaBuilderTests(FactoryTestCase):
    @mock.patch.object(XmlMetaBuilder, "build_vars")
    def test_build(self, mock_build_vars):
        var = XmlVarFactory.create(
            xml_type=XmlType.ELEMENT, name="foo", qname="{foo}bar", types=(int,)
        )
        mock_build_vars.return_value = [var]

        result = XmlMetaBuilder.build(Artist, None, return_input, return_input)
        expected = XmlMetaFactory.create(
            clazz=Artist,
            qname="{http://musicbrainz.org/ns/mmd-2.0#}artist",
            elements={var.qname: [var]},
        )

        self.assertEqual(expected, result)
        mock_build_vars.assert_called_once_with(
            Artist, "http://musicbrainz.org/ns/mmd-2.0#", return_input, return_input
        )

    @mock.patch.object(XmlMetaBuilder, "build_vars", return_value=[])
    def test_build_with_parent_namespace(self, mock_build_vars):
        result = XmlMetaBuilder.build(
            Country, "http://xsdata", return_input, return_input
        )

        self.assertEqual(build_qname("http://xsdata", "country"), result.qname)
        mock_build_vars.assert_called_once_with(
            Country, "http://xsdata", return_input, return_input
        )

    @mock.patch.object(XmlMetaBuilder, "build_vars", return_value=[])
    def test_build_with_no_meta_name_and_name_generator(self, *args):
        result = XmlMetaBuilder.build(BookForm, None, text.snake_case, return_input)

        self.assertEqual("book_form", result.qname)

    def test_build_block_meta_inheritance(self):
        @dataclass
        class Bar:
            class Meta:
                name = "bar"

        @dataclass
        class Foo(Bar):
            pass

        @dataclass
        class Thug(Bar):
            class Meta:
                name = "thug"

        result = XmlMetaBuilder.build(Foo, None, return_input, return_input)
        self.assertEqual("Foo", result.qname)

        result = XmlMetaBuilder.build(Thug, None, return_input, return_input)
        self.assertEqual("thug", result.qname)

    def test_build_with_no_dataclass_raises_exception(self, *args):
        with self.assertRaises(XmlContextError) as cm:
            XmlMetaBuilder.build(int, None, return_input, return_input)

        self.assertEqual(f"Type '{int}' is not a dataclass.", str(cm.exception))

    def test_build_vars(self):
        result = XmlMetaBuilder.build_vars(BookForm, None, text.pascal_case, str.upper)
        self.assertIsInstance(result, Iterator)

        expected = [
            XmlVarFactory.create(
                xml_type=XmlType.ELEMENT,
                index=1,
                name="author",
                qname="Author",
                types=(str,),
            ),
            XmlVarFactory.create(
                xml_type=XmlType.ELEMENT,
                index=2,
                name="title",
                qname="Title",
                types=(str,),
            ),
            XmlVarFactory.create(
                xml_type=XmlType.ELEMENT,
                index=3,
                name="genre",
                qname="Genre",
                types=(str,),
            ),
            XmlVarFactory.create(
                xml_type=XmlType.ELEMENT,
                index=4,
                name="price",
                qname="Price",
                types=(float,),
            ),
            XmlVarFactory.create(
                xml_type=XmlType.ELEMENT,
                index=5,
                name="pub_date",
                qname="PubDate",
                types=(XmlDate,),
            ),
            XmlVarFactory.create(
                xml_type=XmlType.ELEMENT,
                index=6,
                name="review",
                qname="Review",
                types=(str,),
            ),
            XmlVarFactory.create(
                xml_type=XmlType.ATTRIBUTE, index=7, name="id", qname="ID", types=(str,)
            ),
            XmlVarFactory.create(
                xml_type=XmlType.ATTRIBUTE,
                index=8,
                name="lang",
                qname="LANG",
                types=(str,),
                init=False,
                default="en",
            ),
        ]

        result = list(result)
        self.assertEqual(expected, result)
        for var in result:
            self.assertIsNone(var.clazz)

    def test_build_vars_with_ignore_types(self):
        result = XmlMetaBuilder.build_vars(TypeB, None, return_input, return_input)
        self.assertIsInstance(result, Iterator)

        actual = list(result)
        self.assertEqual(2, len(actual))

    def test_default_xml_type(self):
        cls = make_dataclass("a", [("x", int)])
        self.assertEqual(XmlType.TEXT, XmlMetaBuilder.default_xml_type(cls))

        cls = make_dataclass("b", [("x", int), ("y", int)])
        self.assertEqual(XmlType.ELEMENT, XmlMetaBuilder.default_xml_type(cls))

        cls = make_dataclass(
            "c", [("x", int), ("y", int, field(metadata=dict(type="Text")))]
        )
        self.assertEqual(XmlType.ELEMENT, XmlMetaBuilder.default_xml_type(cls))

        cls = make_dataclass(
            "d", [("x", int), ("y", int, field(metadata=dict(type="Element")))]
        )
        self.assertEqual(XmlType.TEXT, XmlMetaBuilder.default_xml_type(cls))

        with self.assertRaises(XmlContextError) as cm:
            cls = make_dataclass(
                "e",
                [
                    ("x", int, field(metadata=dict(type="Text"))),
                    ("y", int, field(metadata=dict(type="Text"))),
                ],
            )
            XmlMetaBuilder.default_xml_type(cls)

        self.assertEqual(
            "Dataclass `e` includes more than one text node!", str(cm.exception)
        )


class XmlVarBuilderTests(TestCase):
    def setUp(self) -> None:
        self.builder = XmlVarBuilder(
            default_xml_type=XmlType.ELEMENT,
            parent_ns=None,
            element_name_generator=return_input,
            attribute_name_generator=return_input,
        )

        super().setUp()

    def test_build_with_choice_field(self):
        globalns = sys.modules[CompoundFieldExample.__module__].__dict__
        type_hints = get_type_hints(CompoundFieldExample)
        class_field = fields(CompoundFieldExample)[0]

        builder = XmlVarBuilder(XmlType.ELEMENT, "bar", return_input, return_input)

        actual = builder.build(
            66,
            "compound",
            type_hints["compound"],
            class_field.metadata,
            True,
            list,
            globalns,
        )
        expected = XmlVarFactory.create(
            index=67,
            xml_type=XmlType.ELEMENTS,
            name="compound",
            qname="compound",
            list_element=True,
            any_type=True,
            default=list,
            elements={
                "{foo}node": XmlVarFactory.create(
                    index=1,
                    xml_type=XmlType.ELEMENT,
                    name="compound",
                    qname="{foo}node",
                    list_element=True,
                    types=(CompoundFieldExample,),
                    namespaces=("foo",),
                    derived=False,
                ),
                "{bar}x": XmlVarFactory.create(
                    index=2,
                    xml_type=XmlType.ELEMENT,
                    name="compound",
                    qname="{bar}x",
                    tokens=True,
                    list_element=True,
                    types=(str,),
                    namespaces=("bar",),
                    derived=False,
                    default=return_true,
                    format="Nope",
                ),
                "{bar}y": XmlVarFactory.create(
                    index=3,
                    xml_type=XmlType.ELEMENT,
                    name="compound",
                    qname="{bar}y",
                    nillable=True,
                    list_element=True,
                    types=(int,),
                    namespaces=("bar",),
                    derived=False,
                ),
                "{bar}z": XmlVarFactory.create(
                    index=4,
                    xml_type=XmlType.ELEMENT,
                    name="compound",
                    qname="{bar}z",
                    nillable=False,
                    list_element=True,
                    types=(int,),
                    namespaces=("bar",),
                    derived=True,
                ),
                "{bar}o": XmlVarFactory.create(
                    index=5,
                    xml_type=XmlType.ELEMENT,
                    name="compound",
                    qname="{bar}o",
                    nillable=False,
                    list_element=True,
                    types=(object,),
                    namespaces=("bar",),
                    derived=True,
                    any_type=True,
                ),
                "{bar}p": XmlVarFactory.create(
                    index=6,
                    xml_type=XmlType.ELEMENT,
                    name="compound",
                    qname="{bar}p",
                    types=(float,),
                    list_element=True,
                    namespaces=("bar",),
                    default=1.1,
                ),
            },
            wildcards=[
                XmlVarFactory.create(
                    index=7,
                    xml_type=XmlType.WILDCARD,
                    name="compound",
                    qname="{http://www.w3.org/1999/xhtml}any",
                    types=(object,),
                    namespaces=("http://www.w3.org/1999/xhtml",),
                    derived=True,
                    any_type=False,
                    list_element=True,
                )
            ],
            types=(object,),
        )
        self.assertEqual(expected, actual)

    def test_build_validates_result(self):
        with self.assertRaises(XmlContextError) as cm:
            self.builder.build(
                1, "foo", List[int], {"type": "Attributes"}, True, None, None
            )

        self.assertEqual(
            "Xml type 'Attributes' does not support typing: typing.List[int]",
            str(cm.exception),
        )

    def test_resolve_namespaces(self):
        func = self.builder.resolve_namespaces
        self.builder.parent_ns = "bar"

        self.assertEqual(("foo",), func(XmlType.ELEMENT, "foo"))
        self.assertEqual((), func(XmlType.ELEMENT, ""))
        self.assertEqual(("bar",), func(XmlType.ELEMENT, None))

        self.assertEqual((), func(XmlType.ATTRIBUTE, None))

        self.assertEqual(("bar",), func(XmlType.WILDCARD, None))
        self.assertEqual(("##any",), func(XmlType.WILDCARD, "##any"))

        self.builder.parent_ns = ""
        self.assertEqual(("##any",), func(XmlType.WILDCARD, "##targetNamespace"))

        self.builder.parent_ns = None
        self.assertEqual(("##any",), func(XmlType.WILDCARD, "##targetNamespace"))

        self.builder.parent_ns = "p"
        self.assertEqual(("p",), func(XmlType.WILDCARD, "##targetNamespace"))
        self.assertEqual(("",), func(XmlType.WILDCARD, "##local"))
        self.assertEqual(("!p",), func(XmlType.WILDCARD, "##other"))
        self.assertEqual(
            ("", "!p"), tuple(sorted(func(XmlType.WILDCARD, "##other   ##local")))
        )

        self.assertEqual(
            ("foo", "p"),
            tuple(sorted(func(XmlType.WILDCARD, "##targetNamespace   foo"))),
        )

    def test_analyze_types(self):
        actual = self.builder.analyze_types(List[List[Union[str, int]]], None)
        self.assertEqual((list, list, (int, str)), actual)

        actual = self.builder.analyze_types(Union[str, int], None)
        self.assertEqual((None, None, (int, str)), actual)

        actual = self.builder.analyze_types(Dict[str, int], None)
        self.assertEqual((dict, None, (int, str)), actual)

        with self.assertRaises(XmlContextError) as cm:
            self.builder.analyze_types(List[List[List[int]]], None)

        self.assertEqual(
            "Unsupported typing: typing.List[typing.List[typing.List[int]]]",
            str(cm.exception),
        )

    def test_is_valid(self):
        # Attributes need origin dict
        self.assertFalse(
            self.builder.is_valid(XmlType.ATTRIBUTES, None, None, (), False, True)
        )

        # Attributes don't support any origin
        self.assertFalse(
            self.builder.is_valid(XmlType.ATTRIBUTES, dict, list, (), False, True)
        )

        # Attributes don't support xs:NMTOKENS
        self.assertFalse(
            self.builder.is_valid(XmlType.ATTRIBUTES, dict, None, (), True, True)
        )

        self.assertTrue(
            self.builder.is_valid(
                XmlType.ATTRIBUTES, dict, None, (str, str), False, True
            )
        )

        # xs:NMTOKENS need origin list
        self.assertFalse(
            self.builder.is_valid(XmlType.TEXT, dict, None, (), True, True)
        )

        # xs:NMTOKENS need origin list
        self.assertFalse(self.builder.is_valid(XmlType.TEXT, set, None, (), True, True))

        # Any type object is a superset, it's only supported alone
        self.assertFalse(
            self.builder.is_valid(
                XmlType.ELEMENT, None, None, (object, int), False, True
            )
        )

        # Type is not registered in converter.
        self.assertFalse(
            self.builder.is_valid(
                XmlType.TEXT, None, None, (int, uuid.UUID), False, True
            )
        )

        # init false vars are ignored!
        self.assertTrue(
            self.builder.is_valid(
                XmlType.TEXT, None, None, (int, uuid.UUID), False, False
            )
        )


@dataclass
class CompoundFieldExample:

    compound: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "node",
                    "type": Type["CompoundFieldExample"],
                    "namespace": "foo",
                },
                {
                    "name": "x",
                    "type": List[str],
                    "tokens": True,
                    "default_factory": return_true,
                    "format": "Nope",
                },
                {"name": "y", "type": List[int], "nillable": True},
                {"name": "z", "type": List[int]},
                {"name": "o", "type": object},
                {"name": "p", "type": float, "fixed": True, "default": 1.1},
                {
                    "wildcard": True,
                    "type": object,
                    "namespace": "http://www.w3.org/1999/xhtml",
                },
            ),
        },
    )
