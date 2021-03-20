from xsdata.codegen.models import Restrictions
from xsdata.formats.dataclass.filters import Filters
from xsdata.models.config import DocstringStyle
from xsdata.models.config import GeneratorAlias
from xsdata.models.config import GeneratorConfig
from xsdata.models.config import NameCase
from xsdata.models.enums import DataType
from xsdata.models.enums import Namespace
from xsdata.models.enums import Tag
from xsdata.utils.testing import AttrFactory
from xsdata.utils.testing import AttrTypeFactory
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
        self.filters = Filters()

    def test_class_name(self):
        self.filters.class_aliases["boom"] = "Bang"

        self.assertEqual("XsString", self.filters.class_name("xs:string"))
        self.assertEqual("FooBarBam", self.filters.class_name("foo:bar_bam"))
        self.assertEqual("ListType", self.filters.class_name("List"))
        self.assertEqual("Type", self.filters.class_name(".*"))
        self.assertEqual("Bang", self.filters.class_name("boom"))

    def test_field_name(self):
        self.filters.field_aliases["boom"] = "Bang"

        self.assertEqual("foo", self.filters.field_name("foo", "cls"))
        self.assertEqual("foo_bar", self.filters.field_name("foo:bar", "cls"))
        self.assertEqual("foo_bar", self.filters.field_name("FooBar", "cls"))
        self.assertEqual("none_value", self.filters.field_name("None", "cls"))
        self.assertEqual("br_eak_value", self.filters.field_name("BrEak", "cls"))
        self.assertEqual("value_1", self.filters.field_name("1", "cls"))
        self.assertEqual("Bang", self.filters.field_name("boom", "cls"))

    def test_constant_name(self):
        self.filters.field_aliases["boom"] = "Bang"

        self.assertEqual("FOO", self.filters.constant_name("foo", "cls"))
        self.assertEqual("FOO_BAR", self.filters.constant_name("foo:bar", "cls"))
        self.assertEqual("FOO_BAR", self.filters.constant_name("FooBar", "cls"))
        self.assertEqual("NONE_VALUE", self.filters.constant_name("None", "cls"))
        self.assertEqual("BR_EAK_VALUE", self.filters.constant_name("BrEak", "cls"))
        self.assertEqual("VALUE_1", self.filters.constant_name("1", "cls"))
        self.assertEqual("Bang", self.filters.constant_name("boom", "cls"))

    def test_module_name(self):
        self.filters.module_aliases["http://github.com/tefra/xsdata"] = "xsdata"

        self.assertEqual("foo_bar", self.filters.module_name("fooBar"))
        self.assertEqual("foo_bar_wtf", self.filters.module_name("fooBar.wtf"))
        self.assertEqual("mod_1111", self.filters.module_name("1111"))
        self.assertEqual("xs_string", self.filters.module_name("xs:string"))
        self.assertEqual("foo_bar_bam", self.filters.module_name("foo:bar_bam"))
        self.assertEqual("bar_bam", self.filters.module_name("urn:bar_bam"))
        self.assertEqual(
            "pypi_org_project_xsdata",
            self.filters.module_name("http://pypi.org/project/xsdata/"),
        )
        self.assertEqual(
            "xsdata", self.filters.module_name("http://github.com/tefra/xsdata")
        )

    def test_package_name(self):
        self.filters.package_aliases["boom"] = "bang"
        self.filters.package_aliases["boom.boom"] = "booom"

        self.assertEqual(
            "foo.bar_bar.pkg_1", self.filters.package_name("Foo.BAR_bar.1")
        )
        self.assertEqual("foo.bang.pkg_1", self.filters.package_name("Foo.boom.1"))
        self.assertEqual("booom", self.filters.package_name("boom.boom"))

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

    def test_field_default_value_with_value_none(self):
        attr = AttrFactory.create(types=[type_str])
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

    def test_field_default_value_with_type_list(self):
        attr = AttrFactory.create(types=[type_bool])
        attr.restrictions.max_occurs = 2
        self.assertEqual("list", self.filters.field_default_value(attr))

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
        attr.restrictions.required = False

        expected = {"min_occurs": 1, "max_occurs": 2, "max_inclusive": 2}
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
            default="foo", types=AttrTypeFactory.list(1, qname="foo_bar")
        )

        self.assertEqual("FooBar", self.filters.field_type(attr, []))

    def test_field_type_with_optional_value(self):
        attr = AttrFactory.create(types=AttrTypeFactory.list(1, qname="foo_bar"))

        self.assertEqual("Optional[FooBar]", self.filters.field_type(attr, []))

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

    def test_field_type_with_forward_and_circular_reference(self):
        attr = AttrFactory.create(
            types=AttrTypeFactory.list(1, qname="foo_bar", forward=True, circular=True)
        )

        self.assertEqual(
            'Optional["Parent.Inner"]',
            self.filters.field_type(attr, ["Parent", "Inner"]),
        )

    def test_field_type_with_list_type(self):
        attr = AttrFactory.create(
            types=AttrTypeFactory.list(1, qname="foo_bar", forward=True)
        )
        attr.restrictions.max_occurs = 2
        self.assertEqual(
            'List["A.Parent.FooBar"]',
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

    def test_field_type_with_any_attribute(self):
        attr = AttrFactory.any_attribute()

        self.assertEqual("Dict", self.filters.field_type(attr, ["a", "b"]))

    def test_field_type_with_native_type(self):
        attr = AttrFactory.create(
            types=[
                AttrTypeFactory.native(DataType.INT),
                AttrTypeFactory.native(DataType.POSITIVE_INTEGER),
            ]
        )
        self.assertEqual("Optional[int]", self.filters.field_type(attr, ["a", "b"]))

    def test_choice_type(self):
        choice = AttrFactory.create(types=[AttrTypeFactory.create("foobar")])
        actual = self.filters.choice_type(choice, ["a", "b"])
        self.assertEqual("Type[Foobar]", actual)

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

    def test_choice_type_with_multiple_types(self):
        choice = AttrFactory.create(types=[type_str, type_bool])
        actual = self.filters.choice_type(choice, ["a", "b"])
        self.assertEqual("Type[Union[str, bool]]", actual)

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

        output = "Optional[ "
        expected = "from typing import Optional"
        self.assertIn(expected, self.filters.default_imports(output))

        output = " Union[ "
        expected = "from typing import Union"
        self.assertIn(expected, self.filters.default_imports(output))

        output = " Type["
        expected = "from typing import Type"
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

    def test_format_metadata(self):
        data = dict(
            num=1,
            text="foo",
            text_two="fo'o",
            text_three='fo"o',
            pattern="foo",
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

    def test_from_config(self):
        config = GeneratorConfig()
        config.conventions.package_name.safe_prefix = "safe_package"
        config.conventions.package_name.case = NameCase.MIXED
        config.conventions.class_name.safe_prefix = "safe_class"
        config.conventions.class_name.case = NameCase.CAMEL
        config.conventions.field_name.safe_prefix = "safe_field"
        config.conventions.field_name.case = NameCase.PASCAL
        config.conventions.module_name.safe_prefix = "safe_module"
        config.conventions.module_name.case = NameCase.SNAKE
        config.aliases.class_name.append(GeneratorAlias("a", "b"))
        config.aliases.class_name.append(GeneratorAlias("c", "d"))
        config.aliases.field_name.append(GeneratorAlias("e", "f"))
        config.aliases.package_name.append(GeneratorAlias("g", "h"))
        config.aliases.module_name.append(GeneratorAlias("i", "j"))

        filters = Filters.from_config(config)

        self.assertEqual("safe_class", filters.class_safe_prefix)
        self.assertEqual("safe_field", filters.field_safe_prefix)
        self.assertEqual("safe_package", filters.package_safe_prefix)
        self.assertEqual("safe_module", filters.module_safe_prefix)

        self.assertEqual("cAb", filters.class_name("cAB"))
        self.assertEqual("CAb", filters.field_name("cAB", "cls"))
        self.assertEqual("cAB", filters.package_name("cAB"))
        self.assertEqual("c_ab", filters.module_name("cAB"))

        self.assertEqual({"a": "b", "c": "d"}, filters.class_aliases)
        self.assertEqual({"e": "f"}, filters.field_aliases)
        self.assertEqual({"g": "h"}, filters.package_aliases)
        self.assertEqual({"i": "j"}, filters.module_aliases)
