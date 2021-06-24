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
from typing import Union
from unittest import mock
from unittest import TestCase
from xml.etree.ElementTree import QName

from tests.fixtures.artists import Artist
from tests.fixtures.books import BookForm
from tests.fixtures.models import ChoiceType
from tests.fixtures.models import TypeA
from tests.fixtures.models import TypeB
from tests.fixtures.models import UnionType
from tests.fixtures.series import Country
from tests.fixtures.submodels import ChoiceTypeChild
from xsdata.exceptions import XmlContextError
from xsdata.formats.dataclass.compat import class_types
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
    def setUp(self):
        super().setUp()
        self.builder = XmlMetaBuilder(
            class_type=class_types.get_type("dataclasses"),
            element_name_generator=return_input,
            attribute_name_generator=return_input,
        )

    @mock.patch.object(XmlMetaBuilder, "build_vars")
    def test_build(self, mock_build_vars):
        var = XmlVarFactory.create(
            xml_type=XmlType.ELEMENT, name="foo", qname="{foo}bar", types=(int,)
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
    def test_build_with_parent_namespace(self, mock_build_vars):
        result = self.builder.build(Country, "http://xsdata")

        self.assertEqual(build_qname("http://xsdata", "country"), result.qname)
        mock_build_vars.assert_called_once_with(
            Country, "http://xsdata", return_input, return_input
        )

    @mock.patch.object(XmlMetaBuilder, "build_vars", return_value=[])
    def test_build_with_no_meta_name_and_name_generator(self, *args):
        self.builder.element_name_generator = text.snake_case
        result = self.builder.build(BookForm, None)

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

        result = self.builder.build(Foo, None)
        self.assertEqual("Foo", result.qname)

        result = self.builder.build(Thug, None)
        self.assertEqual("thug", result.qname)

    def test_build_with_no_dataclass_raises_exception(self, *args):
        with self.assertRaises(XmlContextError) as cm:
            self.builder.build(int, None)

        self.assertEqual(f"Type '{int}' is not a dataclass.", str(cm.exception))

    def test_build_locates_globalns_per_field(self):
        actual = self.builder.build(ChoiceTypeChild, None)
        self.assertEqual(1, len(actual.choices))
        self.assertEqual(9, len(actual.choices[0].elements))
        self.assertIsNone(self.builder.find_globalns(object, "foo"))

    def test_target_namespace(self):
        class Meta:
            namespace = "bar"
            target_namespace = "foo"

        self.assertEqual("foo", self.builder.target_namespace(None, Meta))

        del Meta.target_namespace
        self.assertEqual("bar", self.builder.target_namespace(None, Meta))

        class Module:
            __NAMESPACE__ = "gl"

        self.assertEqual("gl", self.builder.target_namespace(Module, Meta))

    def test_build_vars(self):
        result = self.builder.build_vars(BookForm, None, text.pascal_case, str.upper)
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
        result = self.builder.build_vars(TypeB, None, return_input, return_input)
        self.assertIsInstance(result, Iterator)

        actual = list(result)
        self.assertEqual(2, len(actual))

    def test_default_xml_type(self):
        cls = make_dataclass("a", [("x", int)])
        self.assertEqual(XmlType.TEXT, self.builder.default_xml_type(cls))

        cls = make_dataclass("b", [("x", int), ("y", int)])
        self.assertEqual(XmlType.ELEMENT, self.builder.default_xml_type(cls))

        cls = make_dataclass(
            "c", [("x", int), ("y", int, field(metadata=dict(type="Text")))]
        )
        self.assertEqual(XmlType.ELEMENT, self.builder.default_xml_type(cls))

        cls = make_dataclass(
            "d", [("x", int), ("y", int, field(metadata=dict(type="Element")))]
        )
        self.assertEqual(XmlType.TEXT, self.builder.default_xml_type(cls))

        with self.assertRaises(XmlContextError) as cm:
            cls = make_dataclass(
                "e",
                [
                    ("x", int, field(metadata=dict(type="Text"))),
                    ("y", int, field(metadata=dict(type="Text"))),
                ],
            )
            self.builder.default_xml_type(cls)

        self.assertEqual(
            "Dataclass `e` includes more than one text node!", str(cm.exception)
        )


class XmlVarBuilderTests(TestCase):
    def setUp(self) -> None:
        self.builder = XmlVarBuilder(
            class_type=class_types.get_type("dataclasses"),
            parent_ns=None,
            default_xml_type=XmlType.ELEMENT,
            element_name_generator=return_input,
            attribute_name_generator=return_input,
        )

        super().setUp()
        self.maxDiff = None

    def test_build_with_choice_field(self):
        globalns = sys.modules[ChoiceType.__module__].__dict__
        type_hints = get_type_hints(ChoiceType)
        class_field = fields(ChoiceType)[0]
        self.builder.parent_ns = "bar"

        self.maxDiff = None
        actual = self.builder.build(
            66,
            "choice",
            type_hints["choice"],
            class_field.metadata,
            True,
            list,
            globalns,
        )
        expected = XmlVarFactory.create(
            index=67,
            name="choice",
            types=(object,),
            factory=list,
            any_type=True,
            default=list,
            xml_type=XmlType.ELEMENTS,
            elements={
                "{bar}a": XmlVarFactory.create(
                    index=1,
                    name="choice",
                    qname="{bar}a",
                    types=(TypeA,),
                    clazz=TypeA,
                    factory=list,
                    namespaces=("bar",),
                ),
                "{bar}b": XmlVarFactory.create(
                    index=2,
                    name="choice",
                    qname="{bar}b",
                    types=(TypeB,),
                    clazz=TypeB,
                    factory=list,
                    namespaces=("bar",),
                ),
                "{bar}int": XmlVarFactory.create(
                    index=3,
                    name="choice",
                    qname="{bar}int",
                    types=(int,),
                    factory=list,
                    namespaces=("bar",),
                ),
                "{bar}int2": XmlVarFactory.create(
                    index=4,
                    name="choice",
                    qname="{bar}int2",
                    types=(int,),
                    derived=True,
                    nillable=True,
                    factory=list,
                    namespaces=("bar",),
                ),
                "{bar}float": XmlVarFactory.create(
                    index=5,
                    name="choice",
                    qname="{bar}float",
                    types=(float,),
                    factory=list,
                    namespaces=("bar",),
                ),
                "{bar}qname": XmlVarFactory.create(
                    index=6,
                    name="choice",
                    qname="{bar}qname",
                    types=(QName,),
                    factory=list,
                    namespaces=("bar",),
                ),
                "{bar}tokens": XmlVarFactory.create(
                    index=7,
                    name="choice",
                    qname="{bar}tokens",
                    types=(int,),
                    tokens_factory=list,
                    derived=True,
                    factory=list,
                    default=return_true,
                    namespaces=("bar",),
                ),
                "{foo}union": XmlVarFactory.create(
                    index=8,
                    name="choice",
                    qname="{foo}union",
                    types=(UnionType,),
                    clazz=UnionType,
                    factory=list,
                    namespaces=("foo",),
                ),
                "{bar}p": XmlVarFactory.create(
                    index=9,
                    name="choice",
                    qname="{bar}p",
                    types=(float,),
                    derived=True,
                    factory=list,
                    default=1.1,
                    namespaces=("bar",),
                ),
            },
            wildcards=[
                XmlVarFactory.create(
                    index=10,
                    name="choice",
                    xml_type=XmlType.WILDCARD,
                    qname="{http://www.w3.org/1999/xhtml}any",
                    types=(object,),
                    factory=list,
                    default=None,
                    namespaces=("http://www.w3.org/1999/xhtml",),
                ),
            ],
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
