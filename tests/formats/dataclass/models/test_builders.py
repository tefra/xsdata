import sys
from collections.abc import Iterator
from dataclasses import dataclass, field, fields, make_dataclass
from decimal import Decimal
from typing import get_type_hints
from unittest import TestCase, mock
from xml.etree.ElementTree import QName

from tests.fixtures.artists import Artist
from tests.fixtures.books import BookForm
from tests.fixtures.models import (
    AmbiguousChoiceType,
    ChoiceType,
    Parent,
    TypeA,
    TypeB,
    TypeNS1,
    UnionType,
)
from tests.fixtures.series import Country
from tests.fixtures.submodels import ChoiceTypeChild
from xsdata.exceptions import XmlContextError
from xsdata.formats.dataclass.compat import class_types
from xsdata.formats.dataclass.models.builders import XmlMetaBuilder, XmlVarBuilder
from xsdata.formats.dataclass.models.elements import XmlType
from xsdata.models.datatype import XmlDate
from xsdata.utils import text
from xsdata.utils.constants import return_input
from xsdata.utils.namespaces import build_qname
from xsdata.utils.testing import FactoryTestCase, XmlMetaFactory, XmlVarFactory


class XmlMetaBuilderTests(FactoryTestCase):
    def setUp(self) -> None:
        super().setUp()
        self.builder = XmlMetaBuilder(
            class_type=class_types.get_type("dataclasses"),
            element_name_generator=return_input,
            attribute_name_generator=return_input,
        )

    @mock.patch.object(XmlMetaBuilder, "build_vars")
    def test_build(self, mock_build_vars) -> None:
        var = XmlVarFactory.create(
            xml_type=XmlType.ELEMENT, name="foo", namespaces=("foo",), types=(int,)
        )
        mock_build_vars.return_value = [var]

        result = self.builder.build(Artist, None)
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
    def test_build_with_parent_namespace(self, mock_build_vars) -> None:
        result = self.builder.build(Country, "http://xsdata")

        self.assertEqual(build_qname("http://xsdata", "country"), result.qname)
        mock_build_vars.assert_called_once_with(
            Country, "http://xsdata", return_input, return_input
        )

    @mock.patch.object(XmlMetaBuilder, "build_vars", return_value=[])
    def test_build_with_no_meta_name_and_name_generator(self, *args) -> None:
        self.builder.element_name_generator = text.snake_case
        result = self.builder.build(BookForm, None)

        self.assertEqual("book_form", result.qname)

    def test_build_block_meta_inheritance(self) -> None:
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

        result = self.builder.build(Foo, None)
        self.assertEqual("Foo", result.qname)

        result = self.builder.build(Thug, None)
        self.assertEqual("thug", result.qname)

    def test_build_with_no_dataclass_raises_exception(self, *args) -> None:
        with self.assertRaises(XmlContextError) as cm:
            self.builder.build(int, None)

        self.assertEqual(f"Type '{int}' is not a dataclass.", str(cm.exception))

    def test_build_locates_globalns_per_field(self) -> None:
        actual = self.builder.build(ChoiceTypeChild, None)
        self.assertEqual(1, len(actual.choices))
        self.assertEqual(7, len(actual.choices[0].elements))

        with self.assertRaises(XmlContextError):
            self.builder.find_declared_class(object, "foo")

    def test_build_locates_parent_namespace_per_field(self) -> None:
        actual = self.builder.build(TypeNS1, None)
        self.assertEqual(["{ns2}x1", "{ns1}x2"], list(actual.elements.keys()))

    def test_build_inner_type_has_no_target_qname(self) -> None:
        actual = self.builder.build(Parent.Inner, None)
        self.assertIsNone(actual.target_qname)

    def test_build_local_type_has_no_target_qname(self) -> None:
        actual = self.builder.build(Parent, None)
        self.assertIsNone(actual.target_qname)

    def test_target_namespace(self) -> None:
        class Meta:
            namespace = "bar"
            target_namespace = "foo"

        self.assertEqual("foo", self.builder.target_namespace(None, Meta))

        del Meta.target_namespace
        self.assertEqual("bar", self.builder.target_namespace(None, Meta))

        class Module:
            __NAMESPACE__ = "gl"

        self.assertEqual("gl", self.builder.target_namespace(Module, Meta))

    def test_build_vars(self) -> None:
        result = self.builder.build_vars(BookForm, None, text.pascal_case, str.upper)
        self.assertIsInstance(result, Iterator)

        expected = [
            XmlVarFactory.create(
                xml_type=XmlType.ELEMENT,
                index=1,
                name="author",
                local_name="Author",
                types=(str,),
                required=True,
            ),
            XmlVarFactory.create(
                xml_type=XmlType.ELEMENT,
                index=2,
                name="title",
                local_name="Title",
                types=(str,),
                required=True,
            ),
            XmlVarFactory.create(
                xml_type=XmlType.ELEMENT,
                index=3,
                name="genre",
                local_name="Genre",
                types=(str,),
                required=True,
            ),
            XmlVarFactory.create(
                xml_type=XmlType.ELEMENT,
                index=4,
                name="price",
                local_name="Price",
                types=(float,),
                required=True,
            ),
            XmlVarFactory.create(
                xml_type=XmlType.ELEMENT,
                index=5,
                name="pub_date",
                local_name="PubDate",
                types=(XmlDate,),
                required=True,
            ),
            XmlVarFactory.create(
                xml_type=XmlType.ELEMENT,
                index=6,
                name="review",
                local_name="Review",
                types=(str,),
                required=True,
            ),
            XmlVarFactory.create(
                xml_type=XmlType.ATTRIBUTE,
                index=7,
                name="id",
                local_name="ID",
                types=(str,),
            ),
            XmlVarFactory.create(
                xml_type=XmlType.ATTRIBUTE,
                index=8,
                name="lang",
                local_name="LANG",
                types=(str,),
                init=False,
                default="en",
            ),
        ]

        result = list(result)
        self.assertEqual(expected, result)
        for var in result:
            self.assertIsNone(var.clazz)

    def test_build_vars_with_ignore_types(self) -> None:
        result = self.builder.build_vars(TypeB, None, return_input, return_input)
        self.assertIsInstance(result, Iterator)

        actual = list(result)
        self.assertEqual(2, len(actual))

    def test_default_xml_type(self) -> None:
        cls = make_dataclass("a", [("x", int)])
        self.assertEqual(XmlType.TEXT, self.builder.default_xml_type(cls))

        cls = make_dataclass("b", [("x", int), ("y", int)])
        self.assertEqual(XmlType.ELEMENT, self.builder.default_xml_type(cls))

        cls = make_dataclass(
            "c", [("x", int), ("y", int, field(metadata={"type": "Text"}))]
        )
        self.assertEqual(XmlType.ELEMENT, self.builder.default_xml_type(cls))

        cls = make_dataclass(
            "d", [("x", int), ("y", int, field(metadata={"type": "Element"}))]
        )
        self.assertEqual(XmlType.TEXT, self.builder.default_xml_type(cls))

        with self.assertRaises(XmlContextError) as cm:
            cls = make_dataclass(
                "e",
                [
                    ("x", int, field(metadata={"type": "Text"})),
                    ("y", int, field(metadata={"type": "Text"})),
                ],
            )
            self.builder.default_xml_type(cls)

        self.assertEqual(
            "Dataclass `e` includes more than one text node!", str(cm.exception)
        )


class XmlVarBuilderTests(TestCase):
    maxDiff = None

    def setUp(self) -> None:
        self.builder = XmlVarBuilder(
            class_type=class_types.get_type("dataclasses"),
            default_xml_type=XmlType.ELEMENT,
            element_name_generator=return_input,
            attribute_name_generator=return_input,
        )

        super().setUp()

    def test_build_with_choice_field(self) -> None:
        globalns = sys.modules[ChoiceType.__module__].__dict__
        type_hints = get_type_hints(ChoiceType)
        class_field = fields(ChoiceType)[0]

        actual = self.builder.build(
            ChoiceType,
            "choice",
            type_hints["choice"],
            class_field.metadata,
            True,
            "bar",
            list,
            globalns,
        )
        expected = XmlVarFactory.create(
            index=1,
            name="choice",
            types=(object,),
            factory=list,
            any_type=True,
            default=list,
            xml_type=XmlType.ELEMENTS,
            elements={
                "{bar}a": XmlVarFactory.create(
                    index=2,
                    name="choice",
                    local_name="a",
                    types=(TypeA,),
                    clazz=TypeA,
                    factory=list,
                    namespaces=("bar",),
                ),
                "{bar}b": XmlVarFactory.create(
                    index=3,
                    name="choice",
                    local_name="b",
                    types=(TypeB,),
                    clazz=TypeB,
                    factory=list,
                    namespaces=("bar",),
                ),
                "{bar}int": XmlVarFactory.create(
                    index=4,
                    name="choice",
                    local_name="int",
                    types=(int,),
                    factory=list,
                    namespaces=("bar",),
                ),
                "{bar}float": XmlVarFactory.create(
                    index=5,
                    name="choice",
                    local_name="float",
                    types=(float,),
                    factory=list,
                    namespaces=("bar",),
                ),
                "{bar}qname": XmlVarFactory.create(
                    index=6,
                    name="choice",
                    local_name="qname",
                    types=(QName,),
                    factory=list,
                    namespaces=("bar",),
                ),
                "{foo}union": XmlVarFactory.create(
                    index=7,
                    name="choice",
                    local_name="union",
                    types=(UnionType,),
                    clazz=UnionType,
                    factory=list,
                    namespaces=("foo",),
                ),
                "{bar}tokens": XmlVarFactory.create(
                    index=8,
                    name="choice",
                    local_name="tokens",
                    types=(Decimal,),
                    tokens_factory=list,
                    derived=True,
                    default=list,
                    factory=list,
                    namespaces=("bar",),
                ),
            },
            wildcards=[
                XmlVarFactory.create(
                    index=9,
                    name="choice",
                    xml_type=XmlType.WILDCARD,
                    local_name="any",
                    types=(object,),
                    factory=list,
                    default=None,
                    namespaces=("http://www.w3.org/1999/xhtml",),
                ),
            ],
        )

        self.assertEqual(expected, actual)

    def test_build_with_ambiguous_choices(self) -> None:
        type_hints = get_type_hints(AmbiguousChoiceType)
        class_field = fields(AmbiguousChoiceType)[0]

        with self.assertRaises(XmlContextError) as cm:
            self.builder.build(
                AmbiguousChoiceType,
                "choice",
                type_hints["choice"],
                class_field.metadata,
                True,
                None,
                None,
                {},
            )

        self.assertEqual(
            "Error on AmbiguousChoiceType::choice: Compound field contains ambiguous types",
            str(cm.exception),
        )

    def test_build_validates_result(self) -> None:
        with self.assertRaises(XmlContextError) as cm:
            self.builder.build(
                BookForm,
                "foo",
                list[int],
                {"type": "Attributes"},
                True,
                None,
                None,
                None,
            )

        self.assertEqual(
            "Error on BookForm::foo: Xml Attributes does not support typing `list[int]`",
            str(cm.exception),
        )

    def test_resolve_namespaces(self) -> None:
        func = self.builder.resolve_namespaces

        actual = func(XmlType.ELEMENT, "foo", "bar")
        self.assertEqual(("foo",), actual)

        actual = func(XmlType.ELEMENT, "", "bar")
        self.assertEqual((), actual)

        actual = func(XmlType.ELEMENT, None, "bar")
        self.assertEqual(("bar",), actual)

        actual = func(XmlType.ATTRIBUTE, None, "bar")
        self.assertEqual((), actual)

        actual = func(XmlType.WILDCARD, None, "bar")
        self.assertEqual(("bar",), actual)

        actual = func(XmlType.WILDCARD, "##any", "bar")
        self.assertEqual(("##any",), actual)

        actual = func(XmlType.WILDCARD, "##targetNamespace", "")
        self.assertEqual(("##any",), actual)

        actual = func(XmlType.WILDCARD, "##targetNamespace", None)
        self.assertEqual(("##any",), actual)

        actual = func(XmlType.WILDCARD, "##targetNamespace", "p")
        self.assertEqual(("p",), actual)

        actual = func(XmlType.WILDCARD, "##local", "p")
        self.assertEqual(("",), actual)

        actual = func(XmlType.WILDCARD, "##other", "p")
        self.assertEqual(("!p",), actual)

        actual = func(XmlType.WILDCARD, "##other   ##local", "p")
        self.assertEqual(("", "!p"), tuple(sorted(actual)))

        actual = func(XmlType.WILDCARD, "##targetNamespace   foo", "p")
        self.assertEqual(("foo", "p"), tuple(sorted(actual)))
