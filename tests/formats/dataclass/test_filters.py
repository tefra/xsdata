from collections import namedtuple
from unittest import mock

from tests.fixtures.datatypes import Telephone
from xsdata.codegen.models import Restrictions
from xsdata.formats.dataclass.filters import Filters
from xsdata.models.config import DocstringStyle
from xsdata.models.config import ExtensionType
from xsdata.models.config import GeneratorConfig
from xsdata.models.config import GeneratorExtension
from xsdata.models.config import GeneratorSubstitution
from xsdata.models.config import NameCase
from xsdata.models.config import ObjectType
from xsdata.models.enums import DataType
from xsdata.models.enums import Namespace
from xsdata.models.enums import Tag
from xsdata.utils.testing import AttrFactory
from xsdata.utils.testing import AttrTypeFactory
from xsdata.utils.testing import ClassFactory
from xsdata.utils.testing import ExtensionFactory
from xsdata.utils.testing import FactoryTestCase

type_str = AttrTypeFactory.native(DataType.STRING)
type_int = AttrTypeFactory.native(DataType.INT)
type_float = AttrTypeFactory.native(DataType.FLOAT)
type_decimal = AttrTypeFactory.native(DataType.DECIMAL)
type_bool = AttrTypeFactory.native(DataType.BOOLEAN)
type_qname = AttrTypeFactory.native(DataType.QNAME)
type_tokens = AttrTypeFactory.native(DataType.NMTOKENS)
type_datetime = AttrTypeFactory.native(DataType.DATE_TIME)
type_duration = AttrTypeFactory.native(DataType.DURATION)


class FiltersTests(FactoryTestCase):
    def setUp(self) -> None:
        super().setUp()
        config = GeneratorConfig()
        self.filters = Filters(config)

    def test_class_name(self):
        self.filters.substitutions[ObjectType.CLASS]["Abc"] = "Cba"

        self.assertEqual("XsString", self.filters.class_name("xs:string"))
        self.assertEqual("FooBarBam", self.filters.class_name("foo:bar_bam"))
        self.assertEqual("ListType", self.filters.class_name("List"))
        self.assertEqual("TypeType", self.filters.class_name(".*"))
        self.assertEqual("Cbad", self.filters.class_name("abcd"))

    def test_class_bases(self):
        etp = ExtensionType.CLASS
        self.filters.extensions[etp] = [
            GeneratorExtension(
                type=etp,
                class_name=".*Bar",
                import_string="a.b",
                apply_if_derived=True,
                prepend=False,
            ),
            GeneratorExtension(
                type=etp,
                class_name="Foo.*",
                import_string="a.b",
                apply_if_derived=True,
                prepend=True,
            ),
            GeneratorExtension(
                type=etp,
                class_name="Foo.*",
                import_string="a.c",
                apply_if_derived=True,
                prepend=True,
            ),
            GeneratorExtension(
                type=etp,
                class_name="Foo.*",
                import_string="a.d",
                apply_if_derived=False,
                prepend=True,
            ),
            GeneratorExtension(
                type=etp,
                class_name="Nope.*",
                import_string="a.e",
                apply_if_derived=True,
                prepend=False,
            ),
        ]
        target = ClassFactory.create(extensions=ExtensionFactory.list(1))

        expected = self.filters.class_bases(target, "FooBar")
        self.assertEqual(["c", "b", "AttrB"], expected)

        target.extensions.clear()
        expected = self.filters.class_bases(target, "FooBar")
        self.assertEqual(["d", "c", "b"], expected)

    def test_class_annotations(self):
        etp = ExtensionType.DECORATOR
        self.filters.extensions[etp] = [
            GeneratorExtension(
                type=etp,
                class_name=".*Bar",
                import_string="a.b",
                apply_if_derived=True,
                prepend=False,
            ),
            GeneratorExtension(
                type=etp,
                class_name="Foo.*",
                import_string="a.b",
                apply_if_derived=True,
                prepend=True,
            ),
            GeneratorExtension(
                type=etp,
                class_name="Foo.*",
                import_string="a.c",
                apply_if_derived=True,
                prepend=True,
            ),
            GeneratorExtension(
                type=etp,
                class_name="Foo.*",
                import_string="a.d",
                apply_if_derived=False,
                prepend=False,
            ),
            GeneratorExtension(
                type=etp,
                class_name="Nope.*",
                import_string="a.e",
                apply_if_derived=True,
                prepend=False,
            ),
        ]
        target = ClassFactory.create(extensions=ExtensionFactory.list(1))

        expected = self.filters.class_annotations(target, "FooBar")
        self.assertEqual(["@c", "@b", "@dataclass"], expected)

        target.extensions.clear()
        expected = self.filters.class_annotations(target, "FooBar")
        self.assertEqual(["@c", "@b", "@dataclass", "@d"], expected)

    def test_field_name(self):
        self.filters.substitutions[ObjectType.FIELD]["abc"] = "cba"

        self.assertEqual("value", self.filters.field_name("", "cls"))
        self.assertEqual("foo", self.filters.field_name("foo", "cls"))
        self.assertEqual("foo_bar", self.filters.field_name("foo:bar", "cls"))
        self.assertEqual("foo_bar", self.filters.field_name("FooBar", "cls"))
        self.assertEqual("none", self.filters.field_name("None", "cls"))
        self.assertEqual("br_eak", self.filters.field_name("BrEak", "cls"))
        self.assertEqual("value_1", self.filters.field_name("1", "cls"))
        self.assertEqual("value_minus_1_1", self.filters.field_name("-1.1", "cls"))
        self.assertEqual("cbad", self.filters.field_name("abcd", "cls"))

    def test_constant_name(self):
        self.filters.substitutions[ObjectType.FIELD]["ABC"] = "CBA"

        self.assertEqual("VALUE", self.filters.constant_name("", "cls"))
        self.assertEqual("FOO", self.filters.constant_name("foo", "cls"))
        self.assertEqual("FOO_BAR", self.filters.constant_name("foo:bar", "cls"))
        self.assertEqual("FOO_BAR", self.filters.constant_name("FooBar", "cls"))
        self.assertEqual("NONE", self.filters.constant_name("None", "cls"))
        self.assertEqual("BR_EAK", self.filters.constant_name("BrEak", "cls"))
        self.assertEqual("VALUE_1", self.filters.constant_name("1", "cls"))
        self.assertEqual("VALUE_MINUS_1", self.filters.constant_name("-1", "cls"))
        self.assertEqual("CBAD", self.filters.constant_name("ABCD", "cls"))

    def test_module_name(self):
        self.filters.substitutions[ObjectType.MODULE].update(
            {"http://pypi.org/project/xsdata/": "xsdata"}
        )

        self.assertEqual("foo_bar", self.filters.module_name("fooBar"))
        self.assertEqual("foo_bar_wtf", self.filters.module_name("fooBar.wtf"))
        self.assertEqual("mod_1111", self.filters.module_name("1111"))
        self.assertEqual("xs_string", self.filters.module_name("xs:string"))
        self.assertEqual("foo_bar_bam", self.filters.module_name("foo:bar_bam"))
        self.assertEqual("bar_bam", self.filters.module_name("urn:bar_bam"))
        self.assertEqual(
            "xsdata", self.filters.module_name("http://pypi.org/project/xsdata/")
        )

    def test_package_name(self):
        self.filters.substitutions[ObjectType.PACKAGE]["bam"] = "boom"
        self.filters.substitutions[ObjectType.PACKAGE]["abc"] = "a.b.c"

        self.assertEqual(
            "foo.bar_bar.pkg_1", self.filters.package_name("Foo.BAR_bar.1")
        )
        self.assertEqual("foo.boom.pkg_1", self.filters.package_name("Foo.boom.1"))
        self.assertEqual("", self.filters.package_name(""))

    def test_type_name(self):
        self.assertEqual("str", self.filters.type_name(type_str))

        type_foo_bar_bam = AttrTypeFactory.create(qname="bar_bam")
        self.assertEqual("BarBam", self.filters.type_name(type_foo_bar_bam))

    def test_constant_value(self):
        attr = AttrFactory.create(
            types=[AttrTypeFactory.native(DataType.STRING)], default="foo"
        )
        self.assertEqual('"foo"', self.filters.constant_value(attr))

        attr = AttrFactory.create(types=[AttrTypeFactory.create(qname="foo")])
        self.assertEqual("Foo", self.filters.constant_value(attr))

        attr = AttrFactory.create(types=[AttrTypeFactory.create(alias="alias")])
        self.assertEqual("Alias", self.filters.constant_value(attr))

    def test_apply_substitutions_with_regexes(self):
        self.filters.substitutions[ObjectType.CLASS]["(.*)Class"] = "\\1Type"

        actual = self.filters.apply_substitutions("FooClass", ObjectType.CLASS)
        self.assertEqual("FooType", actual)

    @mock.patch.object(Filters, "field_default_value")
    def test_field_definition(self, mock_field_default_value):
        mock_field_default_value.side_effect = [1, False]
        attr = AttrFactory.native(DataType.INT)

        result = self.filters.field_definition(attr, {}, None, ["Root"])
        expected = (
            "field(\n"
            "        default=1,\n"
            "        metadata={\n"
            '            "name": "attr_B",\n'
            '            "type": "Element",\n'
            "        }\n"
            "    )"
        )
        self.assertEqual(expected, result)

        result = self.filters.field_definition(attr, {}, None, ["Root"])
        expected = (
            "field(\n"
            "        metadata={\n"
            '            "name": "attr_B",\n'
            '            "type": "Element",\n'
            "        }\n"
            "    )"
        )
        self.assertEqual(expected, result)

    def test_field_definition_with_prohibited_attr(self):
        attr = AttrFactory.native(DataType.INT)
        attr.restrictions.max_occurs = 0
        attr.default = "1"

        result = self.filters.field_definition(attr, {}, None, ["Root"])
        expected = (
            "field(\n"
            "        init=False,\n"
            "        metadata={\n"
            '            "type": "Ignore",\n'
            "        }\n"
            "    )"
        )
        self.assertEqual(expected, result)

    @mock.patch.object(Filters, "field_default_value")
    def test_field_definition_with_restriction_pattern(self, mock_field_default_value):
        mock_field_default_value.return_value = None
        str_attr = AttrFactory.create(types=[type_str], tag=Tag.RESTRICTION)
        # intentionally using a double-quote in the pattern to test for a regression in
        # https://github.com/tefra/xsdata/issues/592
        pattern = '([^\\ \\? > < \\* / " ": |]{1,256})'
        str_attr.restrictions.pattern = pattern

        result = self.filters.field_definition(str_attr, {}, None, ["Root"])
        expected = (
            "field(\n"
            "        default=None,\n"
            "        metadata={\n"
            '            "pattern": r"([^\\ \\? > < \\* / \\" \\": |]{1,256})",\n'
            "        }\n"
            "    )"
        )
        self.assertEqual(expected, result)

    def test_field_default_value_with_value_none(self):
        attr = AttrFactory.create(types=[type_str])
        self.assertEqual(None, self.filters.field_default_value(attr))

        self.filters.format.kw_only = True
        self.assertEqual(False, self.filters.field_default_value(attr))

        attr.restrictions.min_occurs = 0
        self.assertEqual(None, self.filters.field_default_value(attr))

    def test_field_default_value_with_type_str(self):
        attr = AttrFactory.create(types=[type_str], default="foo")
        self.assertEqual('"foo"', self.filters.field_default_value(attr))

    def test_field_default_value_with_type_tokens(self):
        attr = AttrFactory.create(types=[type_int, type_str], default="1  \n bar")
        attr.restrictions.tokens = True
        expected = """lambda: [
            1,
            "bar",
        ]"""

        self.assertEqual(expected, self.filters.field_default_value(attr))

        expected = """lambda: (
            1,
            "bar",
        )"""
        self.filters.format.frozen = True
        self.assertEqual(expected, self.filters.field_default_value(attr))

        attr.tag = Tag.ENUMERATION
        expected = """(
            1,
            "bar",
        )"""
        self.assertEqual(expected, self.filters.field_default_value(attr))

    def test_field_default_value_with_type_float(self):
        attr = AttrFactory.create(types=[type_float], default="1.5")
        self.assertEqual("1.5", self.filters.field_default_value(attr))

        attr.default = "inf"
        attr.types = [type_int, type_float]
        self.assertEqual('float("inf")', self.filters.field_default_value(attr))

        attr.default = "-inf"
        self.assertEqual('float("-inf")', self.filters.field_default_value(attr))

        attr.default = "NaN"
        self.assertEqual('float("nan")', self.filters.field_default_value(attr))

    def test_field_default_value_with_type_decimal(self):
        attr = AttrFactory.create(types=[type_decimal], default="1.5")
        self.assertEqual('Decimal("1.5")', self.filters.field_default_value(attr))

        attr.default = "-inf"
        self.assertEqual('Decimal("-Infinity")', self.filters.field_default_value(attr))

        attr.default = "inf"
        self.assertEqual('Decimal("Infinity")', self.filters.field_default_value(attr))

    def test_field_default_value_with_type_int(self):
        attr = AttrFactory.create(types=[type_int], default="1")
        self.assertEqual("1", self.filters.field_default_value(attr))

    def test_field_default_value_with_type_bool(self):
        attr = AttrFactory.create(types=[type_bool], default="true")
        self.assertTrue(self.filters.field_default_value(attr))

    def test_field_default_value_with_type_enum(self):
        attr = AttrFactory.create(
            types=AttrTypeFactory.list(1, qname="{a}foo"), default="@enum@{a}foo::bar"
        )
        self.assertEqual("Foo.BAR", self.filters.field_default_value(attr))

        attr.types[0].alias = "foo_bar"
        self.assertEqual("FooBar.BAR", self.filters.field_default_value(attr))

        attr.default = "@enum@{a}foo::bar@thug"
        self.assertEqual("FooBar.BAR_THUG", self.filters.field_default_value(attr))

        attr.restrictions.tokens = True
        expected = """lambda: [
            FooBar.BAR,
            FooBar.THUG,
        ]"""
        self.assertEqual(expected, self.filters.field_default_value(attr))

        attr.types[0].qname = "nomatch"  # impossible
        with self.assertRaises(Exception):
            self.filters.field_default_value(attr)

    def test_field_default_value_with_type_qname(self):
        attr = AttrFactory.create(types=[type_qname], default="xs:anyType")
        ns_map = {"xs": Namespace.XS.uri}
        self.assertEqual(
            'QName("{http://www.w3.org/2001/XMLSchema}anyType")',
            self.filters.field_default_value(attr, ns_map),
        )

    def test_field_default_value_with_xml_duration(self):
        attr = AttrFactory.create(types=[type_duration], default="P30M")

        self.assertEqual('XmlDuration("P30M")', self.filters.field_default_value(attr))

    def test_field_default_value_with_any_attribute(self):
        attr = AttrFactory.any_attribute()
        self.assertEqual("dict", self.filters.field_default_value(attr))

    def test_field_default_value_with_array_type(self):
        attr = AttrFactory.create(types=[type_bool])
        attr.restrictions.max_occurs = 2
        self.assertEqual("list", self.filters.field_default_value(attr))

        self.filters.format.frozen = True
        self.assertEqual("tuple", self.filters.field_default_value(attr))

    def test_field_default_value_with_multiple_types(self):
        attr = AttrFactory.create(types=[type_bool, type_int, type_float], default="2")
        self.assertEqual("2", self.filters.field_default_value(attr))

        attr.default = 1.0
        self.assertEqual("1.0", self.filters.field_default_value(attr))

        attr.default = "true"
        self.assertEqual("True", self.filters.field_default_value(attr))

    def test_field_metadata(self):
        attr = AttrFactory.element()
        expected = {"name": "attr_B", "type": "Element"}
        self.assertEqual(expected, self.filters.field_metadata(attr, None, ["cls"]))
        self.assertEqual(expected, self.filters.field_metadata(attr, "foo", ["cls"]))

    def test_field_metadata_namespace(self):
        attr = AttrFactory.element(namespace="foo")
        expected = {"name": "attr_B", "namespace": "foo", "type": "Element"}

        actual = self.filters.field_metadata(attr, None, ["cls"])
        self.assertEqual(expected, actual)

        actual = self.filters.field_metadata(attr, "foo", ["cls"])
        self.assertNotIn("namespace", actual)

        attr = AttrFactory.attribute(namespace="foo")
        expected = {"name": "attr_C", "namespace": "foo", "type": "Attribute"}
        actual = self.filters.field_metadata(attr, None, ["cls"])
        self.assertEqual(expected, actual)

        actual = self.filters.field_metadata(attr, "foo", ["cls"])
        self.assertIn("namespace", actual)

    def test_field_metadata_name(self):
        attr = AttrFactory.element(name="bar")
        attr.local_name = "foo"

        actual = self.filters.field_metadata(attr, None, ["cls"])
        self.assertEqual("foo", actual["name"])

        attr = AttrFactory.element(name="Foo")
        attr.local_name = "foo"
        actual = self.filters.field_metadata(attr, None, ["cls"])
        self.assertNotIn("name", actual)

        attr = AttrFactory.create(tag=Tag.ANY, name="bar")
        attr.local_name = "foo"
        actual = self.filters.field_metadata(attr, None, ["cls"])
        self.assertNotIn("name", actual)

    def test_field_metadata_restrictions(self):
        attr = AttrFactory.create(tag=Tag.RESTRICTION)
        attr.types.append(AttrTypeFactory.native(DataType.INT))
        attr.restrictions.min_occurs = 1
        attr.restrictions.max_occurs = 2
        attr.restrictions.max_inclusive = "2"

        expected = {"min_occurs": 1, "max_occurs": 2, "max_inclusive": 2}
        self.assertEqual(expected, self.filters.field_metadata(attr, None, []))

        attr.restrictions.min_occurs = 1
        attr.restrictions.max_occurs = 1
        expected = {"required": True, "max_inclusive": 2}
        self.assertEqual(expected, self.filters.field_metadata(attr, None, []))

        attr.restrictions.nillable = True
        expected = {"nillable": True, "max_inclusive": 2}
        self.assertEqual(expected, self.filters.field_metadata(attr, None, []))

        attr.default = None
        attr.restrictions.tokens = True
        expected = {"max_inclusive": 2, "nillable": True, "tokens": True}
        self.assertEqual(expected, self.filters.field_metadata(attr, None, []))

    def test_field_metadata_mixed(self):
        attr = AttrFactory.element(mixed=True)
        expected = {"mixed": True, "name": "attr_B", "type": "Element"}
        self.assertEqual(expected, self.filters.field_metadata(attr, "foo", ["cls"]))

    def test_field_metadata_choices(self):
        attr = AttrFactory.create(choices=AttrFactory.list(2, tag=Tag.ELEMENT))
        actual = self.filters.field_metadata(attr, "foo", ["cls"])
        expected = (
            {"name": "attr_B", "type": "Type[str]"},
            {"name": "attr_C", "type": "Type[str]"},
        )

        self.assertEqual(expected, actual["choices"])

    def test_field_choices(self):
        attr = AttrFactory.create(
            choices=[
                AttrFactory.element(
                    namespace="foo",
                    types=[type_float],
                    restrictions=Restrictions(max_exclusive="10"),
                ),
                AttrFactory.element(namespace="bar"),
                AttrFactory.any(namespace="##other"),
                AttrFactory.element(name="bar", default="aa"),
                AttrFactory.element(name="tok", restrictions=Restrictions(tokens=True)),
            ]
        )

        actual = self.filters.field_choices(attr, "foo", ["a", "b"])
        expected = (
            {"name": "attr_B", "type": "Type[float]", "max_exclusive": 10.0},
            {"name": "attr_C", "namespace": "bar", "type": "Type[str]"},
            {
                "namespace": "##other",
                "wildcard": True,
                "type": "Type[object]",
            },
            {"default": '"aa"', "name": "bar", "type": "Type[str]"},
            {
                "default_factory": "list",
                "name": "tok",
                "tokens": True,
                "type": "Type[List[str]]",
            },
        )

        self.assertEqual(expected, actual)

        self.filters.docstring_style = DocstringStyle.ACCESSIBLE
        attr.choices[0].help = "help"
        actual = self.filters.field_choices(attr, None, [])
        self.assertEqual(attr.choices[0].help, actual[0]["doc"])
        self.assertNotIn("doc", actual[1])

    def test_field_type_with_default_value(self):
        attr = AttrFactory.create(
            default="1", types=AttrTypeFactory.list(1, qname="foo_bar")
        )

        self.assertEqual("FooBar", self.filters.field_type(attr, []))

        attr.restrictions.nillable = True
        self.assertEqual("Optional[FooBar]", self.filters.field_type(attr, []))

        self.filters.union_type = True
        self.assertEqual("None | FooBar", self.filters.field_type(attr, []))

    def test_field_type_with_optional_value(self):
        attr = AttrFactory.create(types=AttrTypeFactory.list(1, qname="foo_bar"))

        self.assertEqual("Optional[FooBar]", self.filters.field_type(attr, []))

        self.filters.format.kw_only = True
        self.assertEqual("FooBar", self.filters.field_type(attr, []))

        attr.restrictions.min_occurs = 0
        self.assertEqual("Optional[FooBar]", self.filters.field_type(attr, []))

        self.filters.union_type = True
        self.assertEqual("None | FooBar", self.filters.field_type(attr, []))

    def test_field_type_with_circular_reference(self):
        attr = AttrFactory.create(
            types=AttrTypeFactory.list(1, qname="foo_bar", circular=True)
        )

        self.assertEqual(
            'Optional["FooBar"]', self.filters.field_type(attr, ["Parent"])
        )

    def test_field_type_with_forward_reference(self):
        attr = AttrFactory.create(
            types=AttrTypeFactory.list(1, qname="foo_bar", forward=True)
        )
        self.assertEqual(
            'Optional["Parent.Inner.FooBar"]',
            self.filters.field_type(attr, ["Parent", "Inner"]),
        )

        self.filters.postponed_annotations = True
        self.filters.union_type = True
        self.assertEqual(
            "None | Parent.Inner.FooBar",
            self.filters.field_type(attr, ["Parent", "Inner"]),
        )

    def test_field_type_with_forward_and_circular_reference(self):
        attr = AttrFactory.create(
            types=AttrTypeFactory.list(1, qname="foo_bar", forward=True, circular=True)
        )

        self.assertEqual(
            'Optional["Parent.Inner"]',
            self.filters.field_type(attr, ["Parent", "Inner"]),
        )

    def test_field_type_with_array_type(self):
        attr = AttrFactory.create(
            types=AttrTypeFactory.list(1, qname="foo_bar", forward=True)
        )
        attr.restrictions.max_occurs = 2
        self.assertEqual(
            'List["A.Parent.FooBar"]',
            self.filters.field_type(attr, ["A", "Parent"]),
        )

        self.filters.format.frozen = True
        self.assertEqual(
            'Tuple["A.Parent.FooBar", ...]',
            self.filters.field_type(attr, ["A", "Parent"]),
        )

        self.filters.subscriptable_types = True
        self.assertEqual(
            'tuple["A.Parent.FooBar", ...]',
            self.filters.field_type(attr, ["A", "Parent"]),
        )

        self.filters.format.frozen = False
        self.assertEqual(
            'list["A.Parent.FooBar"]',
            self.filters.field_type(attr, ["A", "Parent"]),
        )

    def test_field_type_with_token_attr(self):
        attr = AttrFactory.create(
            types=AttrTypeFactory.list(1, qname="foo_bar"),
            restrictions=Restrictions(tokens=True),
        )
        self.assertEqual("List[FooBar]", self.filters.field_type(attr, []))

        attr.restrictions.max_occurs = 2
        self.assertEqual("List[List[FooBar]]", self.filters.field_type(attr, []))

        attr.restrictions.max_occurs = 1
        self.filters.format.frozen = True
        self.assertEqual("Tuple[FooBar, ...]", self.filters.field_type(attr, []))

        attr.restrictions.max_occurs = 2
        self.assertEqual(
            "Tuple[Tuple[FooBar, ...], ...]", self.filters.field_type(attr, [])
        )

        self.filters.subscriptable_types = True
        self.assertEqual(
            "tuple[tuple[FooBar, ...], ...]", self.filters.field_type(attr, [])
        )

    def test_field_type_with_alias(self):
        attr = AttrFactory.create(
            types=AttrTypeFactory.list(
                1, qname="foo_bar", forward=True, alias="Boss:Life"
            )
        )
        attr.restrictions.max_occurs = 2
        self.assertEqual(
            'List["A.Parent.BossLife"]',
            self.filters.field_type(attr, ["A", "Parent"]),
        )

    def test_field_type_with_multiple_types(self):
        attr = AttrFactory.create(
            types=[
                AttrTypeFactory.create(qname="life", alias="Boss:Life", forward=True),
                AttrTypeFactory.native(DataType.INT),
            ]
        )
        attr.restrictions.max_occurs = 2

        self.assertEqual(
            'List[Union["A.Parent.BossLife", int]]',
            self.filters.field_type(attr, ["A", "Parent"]),
        )

        self.filters.union_type = True
        self.assertEqual(
            'List["A.Parent.BossLife" | int]',
            self.filters.field_type(attr, ["A", "Parent"]),
        )
        self.filters.subscriptable_types = True
        self.assertEqual(
            'list["A.Parent.BossLife" | int]',
            self.filters.field_type(attr, ["A", "Parent"]),
        )

    def test_field_type_with_any_attribute(self):
        attr = AttrFactory.any_attribute()

        self.assertEqual("Dict[str, str]", self.filters.field_type(attr, ["a", "b"]))

        self.filters.subscriptable_types = True
        self.assertEqual("dict[str, str]", self.filters.field_type(attr, ["a", "b"]))

    def test_field_type_with_native_type(self):
        attr = AttrFactory.create(
            types=[
                AttrTypeFactory.native(DataType.INT),
                AttrTypeFactory.native(DataType.POSITIVE_INTEGER),
                AttrTypeFactory.native(DataType.STRING),
            ]
        )
        self.assertEqual(
            "Optional[Union[int, str]]", self.filters.field_type(attr, ["a", "b"])
        )

        self.filters.union_type = True
        self.assertEqual("None | int | str", self.filters.field_type(attr, ["a", "b"]))

    def test_field_type_with_prohibited_attr(self):
        attr = AttrFactory.create(restrictions=Restrictions(max_occurs=0))

        self.assertEqual("Any", self.filters.field_type(attr, ["a", "b"]))

    def test_choice_type(self):
        choice = AttrFactory.create(types=[AttrTypeFactory.create("foobar")])
        actual = self.filters.choice_type(choice, ["a", "b"])
        self.assertEqual("Type[Foobar]", actual)

        self.filters.subscriptable_types = True
        actual = self.filters.choice_type(choice, ["a", "b"])
        self.assertEqual("type[Foobar]", actual)

    def test_choice_type_with_forward_reference(self):
        choice = AttrFactory.create(
            types=[AttrTypeFactory.create("foobar", forward=True)]
        )
        actual = self.filters.choice_type(choice, ["a", "b"])
        self.assertEqual('Type["A.B.Foobar"]', actual)

    def test_choice_type_with_circular_reference(self):
        choice = AttrFactory.create(
            types=[AttrTypeFactory.create("foobar", circular=True)]
        )
        actual = self.filters.choice_type(choice, ["a", "b"])
        self.assertEqual('Type["Foobar"]', actual)

        self.filters.postponed_annotations = True
        actual = self.filters.choice_type(choice, ["a", "b"])
        self.assertEqual("Type[Foobar]", actual)

    def test_choice_type_with_multiple_types(self):
        choice = AttrFactory.create(types=[type_str, type_bool])
        actual = self.filters.choice_type(choice, ["a", "b"])
        self.assertEqual("Type[Union[str, bool]]", actual)

        self.filters.subscriptable_types = True
        actual = self.filters.choice_type(choice, ["a", "b"])
        self.assertEqual("type[Union[str, bool]]", actual)

        self.filters.union_type = True
        actual = self.filters.choice_type(choice, ["a", "b"])
        self.assertEqual("type[str | bool]", actual)

    def test_choice_type_with_list_types_are_ignored(self):
        choice = AttrFactory.create(types=[type_str, type_bool])
        choice.restrictions.max_occurs = 200
        actual = self.filters.choice_type(choice, ["a", "b"])
        self.assertEqual("Type[Union[str, bool]]", actual)

    def test_choice_type_with_restrictions_tokens_true(self):
        choice = AttrFactory.create(types=[type_str, type_bool])
        choice.restrictions.tokens = True
        actual = self.filters.choice_type(choice, ["a", "b"])
        self.assertEqual("Type[List[Union[str, bool]]]", actual)

        self.filters.format.frozen = True
        actual = self.filters.choice_type(choice, ["a", "b"])
        self.assertEqual("Type[Tuple[Union[str, bool], ...]]", actual)

        self.filters.union_type = True
        self.filters.subscriptable_types = True
        actual = self.filters.choice_type(choice, ["a", "b"])
        self.assertEqual("type[tuple[str | bool, ...]]", actual)

    def test_default_imports_with_decimal(self):
        expected = "from decimal import Decimal"

        self.assertIn(expected, self.filters.default_imports("Optional[Decimal]"))
        self.assertIn(expected, self.filters.default_imports("Union[str, Decimal]"))
        self.assertIn(expected, self.filters.default_imports("Union[Decimal, "))
        self.assertIn(expected, self.filters.default_imports("Union[str, Decimal, int"))
        self.assertIn(expected, self.filters.default_imports("number: Decimal = "))
        self.assertIn(expected, self.filters.default_imports(" = Decimal("))
        self.assertNotIn(expected, self.filters.default_imports("class fooDecimal"))

    def test_default_imports_with_qname(self):
        expected = "from xml.etree.ElementTree import QName"

        self.assertIn(expected, self.filters.default_imports("Optional[QName]"))
        self.assertIn(expected, self.filters.default_imports("Union[str, QName]"))
        self.assertIn(expected, self.filters.default_imports("Union[QName, "))
        self.assertIn(expected, self.filters.default_imports("Union[str, QName, int"))
        self.assertIn(expected, self.filters.default_imports("number: QName = "))
        self.assertIn(expected, self.filters.default_imports(" = QName("))
        self.assertNotIn(expected, self.filters.default_imports("class fooQName"))

    def test_default_imports_with_enum(self):
        output = " (Enum) "

        expected = "from enum import Enum"
        self.assertIn(expected, self.filters.default_imports(output))

    def test_default_imports_with_dataclasses(self):
        output = " @dataclass "

        expected = "from dataclasses import dataclass"
        self.assertIn(expected, self.filters.default_imports(output))

        output = " = field( "
        expected = "from dataclasses import field"
        self.assertIn(expected, self.filters.default_imports(output))

        output = " = field( @dataclass "
        expected = "from dataclasses import dataclass, field"
        self.assertIn(expected, self.filters.default_imports(output))

    def test_default_imports_with_builtin_datatype(self):
        expected = "from xsdata.models.datatype import XmlDateTime"

        self.assertIn(expected, self.filters.default_imports("Optional[XmlDateTime]"))
        self.assertIn(expected, self.filters.default_imports("Union[str, XmlDateTime]"))
        self.assertIn(expected, self.filters.default_imports("Union[XmlDateTime, "))
        self.assertIn(expected, self.filters.default_imports("Union[a, XmlDateTime, a"))
        self.assertIn(expected, self.filters.default_imports("number: XmlDateTime = "))
        self.assertIn(expected, self.filters.default_imports(" = XmlDateTime("))
        self.assertNotIn(expected, self.filters.default_imports("class fooXmlDateTime"))

    def test_default_imports_with_typing(self):
        output = ": Dict["
        expected = "from typing import Dict"
        self.assertIn(expected, self.filters.default_imports(output))

        output = ": List["
        expected = "from typing import List"
        self.assertIn(expected, self.filters.default_imports(output))

        output = ": Tuple["
        expected = "from typing import Tuple"
        self.assertIn(expected, self.filters.default_imports(output))

        output = "Optional[ "
        expected = "from typing import Optional"
        self.assertIn(expected, self.filters.default_imports(output))

        output = " Union[ "
        expected = "from typing import Union"
        self.assertIn(expected, self.filters.default_imports(output))

        output = " Type["
        expected = "from typing import Type"
        self.assertIn(expected, self.filters.default_imports(output))

        output = ": Any = "
        expected = "from typing import Any"
        self.assertIn(expected, self.filters.default_imports(output))

    def test_default_imports_combo(self):
        output = (
            "@dataclass\n"
            "class Foo:\n"
            "    field: Optional[str] = field(default=None)"
        )

        expected = "\n".join(
            (
                "from dataclasses import dataclass, field",
                "from typing import Optional",
            )
        )

        self.assertEqual(expected, self.filters.default_imports(output))

    def test_default_imports_with_module(self):
        output = "@attrs.s\n"

        self.filters.import_patterns["attrs"] = {"__module__": ["@attrs.s"]}

        expected = "import attrs"
        self.assertEqual(expected, self.filters.default_imports(output))

    def test_default_imports_with_annotations(self):
        config = GeneratorConfig()
        config.output.postponed_annotations = True
        filters = Filters(config)

        expected = "from __future__ import annotations"
        self.assertEqual(expected, filters.default_imports(""))

    def test_format_metadata(self):
        data = dict(
            num=1,
            text="foo",
            text_two="fo'o",
            text_three='fo"o',
            pattern="foo",
            custom=Telephone(30, 123, 4567),
            level_two=dict(a=1),
            list=[
                dict(type="Type[object]"),
                dict(type="Type[object] mpla"),
            ],
            default="1",
            default_factory="list",
        )

        expected = (
            "{\n"
            '    "num": 1,\n'
            '    "text": "foo",\n'
            '    "text_two": "fo\'o",\n'
            '    "text_three": "fo\\"o",\n'
            '    "pattern": r"foo",\n'
            '    "custom": Telephone(country_code=30, area_code=123, number=4567),\n'
            '    "level_two": {\n'
            '        "a": 1,\n'
            "    },\n"
            '    "list": [\n'
            "        {\n"
            '            "type": object,\n'
            "        },\n"
            "        {\n"
            '            "type": "Type[object] mpla",\n'
            "        },\n"
            "    ],\n"
            '    "default": 1,\n'
            '    "default_factory": list,\n'
            "}"
        )
        self.assertEqual(expected, self.filters.format_metadata(data))
        self.assertEqual('""', self.filters.format_metadata(""))

    def test_import_module(self):
        case = namedtuple("Case", ["module", "from_module", "result"])
        cases = [
            case("foo.bar", "foo", ".bar"),
            case("bar.foo", "foo", "bar.foo"),
            case("a.b.e.f", "a.b.c.d", "..e.f"),
            case("a.b.c.f", "a.b.c.d", ".f"),
            case("a.b.c.f.e", "a.b", ".c.f.e"),
            case("a.b.c.f", "", "a.b.c.f"),
        ]

        transform = self.filters.import_module
        self.filters.relative_imports = False
        for case in cases:
            self.assertEqual(case.module, transform(case.module, case.from_module))

        self.filters.relative_imports = True
        for case in cases:
            self.assertEqual(case.result, transform(case.module, case.from_module))

    def test_build_class_annotation(self):
        config = GeneratorConfig()
        format = config.output.format

        actual = self.filters.build_class_annotation(format)
        self.assertEqual("@dataclass", actual)

        format.frozen = True
        actual = self.filters.build_class_annotation(format)
        self.assertEqual("@dataclass(frozen=True)", actual)

        format.repr = False
        format.eq = False
        format.order = True
        format.unsafe_hash = True
        format.slots = True
        format.kw_only = True
        actual = self.filters.build_class_annotation(format)
        expected = (
            "@dataclass(repr=False, eq=False, order=True,"
            " unsafe_hash=True, frozen=True, slots=True, kw_only=True)"
        )

        self.assertEqual(expected, actual)

    def test__init(self):
        config = GeneratorConfig()
        config.conventions.package_name.safe_prefix = "safe_package"
        config.conventions.package_name.case = NameCase.MIXED
        config.conventions.class_name.safe_prefix = "safe_class"
        config.conventions.class_name.case = NameCase.CAMEL
        config.conventions.field_name.safe_prefix = "safe_field"
        config.conventions.field_name.case = NameCase.PASCAL
        config.conventions.module_name.safe_prefix = "safe_module"
        config.conventions.module_name.case = NameCase.SNAKE
        config.substitutions.substitution.append(
            GeneratorSubstitution(ObjectType.FIELD, "k", "l")
        )
        config.substitutions.substitution.append(
            GeneratorSubstitution(ObjectType.PACKAGE, "m", "n")
        )
        config.extensions.extension.extend(
            [
                GeneratorExtension(ExtensionType.DECORATOR, "a", "a.b"),
                GeneratorExtension(ExtensionType.DECORATOR, "b", "a.c"),
                GeneratorExtension(ExtensionType.CLASS, "c", "a.d"),
                GeneratorExtension(ExtensionType.CLASS, "d", "a.e"),
            ]
        )

        filters = Filters(config)

        self.assertFalse(filters.relative_imports)

        self.assertEqual("safe_class", filters.class_safe_prefix)
        self.assertEqual("safe_field", filters.field_safe_prefix)
        self.assertEqual("safe_package", filters.package_safe_prefix)
        self.assertEqual("safe_module", filters.module_safe_prefix)

        self.assertEqual("cAb", filters.class_name("cAB"))
        self.assertEqual("CAb", filters.field_name("cAB", "cls"))
        self.assertEqual("cAB", filters.package_name("cAB"))
        self.assertEqual("c_ab", filters.module_name("cAB"))

        expected_substitutions = {
            ObjectType.CLASS: {},
            ObjectType.FIELD: {"k": "l"},
            ObjectType.MODULE: {},
            ObjectType.PACKAGE: {"m": "n"},
        }
        self.assertEqual(expected_substitutions, filters.substitutions)

        expected_extensions = {
            ExtensionType.DECORATOR: config.extensions.extension[0:2],
            ExtensionType.CLASS: config.extensions.extension[2:4],
        }
        self.assertEqual(expected_extensions, filters.extensions)

        expected_imports = {
            "b": {"@b"},
            "c": {"@c"},
            "d": {"(d", " d)"},
            "e": {"(e", " e)"},
        }
        self.assertEqual(expected_imports, filters.import_patterns["a"])
