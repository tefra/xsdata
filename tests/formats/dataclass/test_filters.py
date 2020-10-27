from tests.factories import AttrChoiceFactory
from tests.factories import AttrFactory
from tests.factories import AttrTypeFactory
from tests.factories import ClassFactory
from tests.factories import FactoryTestCase
from xsdata.codegen.models import Restrictions
from xsdata.formats.dataclass.filters import CLASS
from xsdata.formats.dataclass.filters import FIELD
from xsdata.formats.dataclass.filters import Filters
from xsdata.formats.dataclass.filters import MODULE
from xsdata.formats.dataclass.filters import PACKAGE
from xsdata.models.config import GeneratorAlias
from xsdata.models.config import GeneratorConfig
from xsdata.models.config import NameCase
from xsdata.models.enums import Namespace
from xsdata.models.enums import Tag

type_str = AttrTypeFactory.xs_string()
type_int = AttrTypeFactory.xs_int()
type_float = AttrTypeFactory.xs_float()
type_decimal = AttrTypeFactory.xs_decimal()
type_bool = AttrTypeFactory.xs_bool()
type_qname = AttrTypeFactory.xs_qname()
type_tokens = AttrTypeFactory.xs_tokens()


class FiltersTests(FactoryTestCase):
    def setUp(self) -> None:
        super().setUp()
        self.filters = Filters()

    def test_class_name(self):
        self.filters.class_aliases["boom"] = "Bang"
        self.filters.cache[CLASS]["pow"] = "Zap"

        self.assertEqual("XsString", self.filters.class_name("xs:string"))
        self.assertEqual("FooBarBam", self.filters.class_name("foo:bar_bam"))
        self.assertEqual("ListType", self.filters.class_name("List"))
        self.assertEqual("Type", self.filters.class_name(".*"))
        self.assertEqual("Bang", self.filters.class_name("boom"))
        self.assertEqual("Zap", self.filters.class_name("pow"))

    def test_field_name(self):
        self.filters.field_aliases["boom"] = "Bang"
        self.filters.cache[FIELD]["pow"] = "Zap"

        self.assertEqual("foo", self.filters.field_name("foo"))
        self.assertEqual("foo_bar", self.filters.field_name("foo:bar"))
        self.assertEqual("foo_bar", self.filters.field_name("FooBar"))
        self.assertEqual("none_value", self.filters.field_name("None"))
        self.assertEqual("br_eak_value", self.filters.field_name("BrEak"))
        self.assertEqual("value_1", self.filters.field_name("1"))
        self.assertEqual("Bang", self.filters.field_name("boom"))
        self.assertEqual("Zap", self.filters.field_name("pow"))

    def test_constant_name(self):
        self.filters.field_aliases["boom"] = "Bang"
        self.filters.cache[FIELD]["pow"] = "Zap"

        self.assertEqual("FOO", self.filters.constant_name("foo"))
        self.assertEqual("FOO_BAR", self.filters.constant_name("foo:bar"))
        self.assertEqual("FOO_BAR", self.filters.constant_name("FooBar"))
        self.assertEqual("NONE_VALUE", self.filters.constant_name("None"))
        self.assertEqual("BR_EAK_VALUE", self.filters.constant_name("BrEak"))
        self.assertEqual("VALUE_1", self.filters.constant_name("1"))
        self.assertEqual("BANG", self.filters.constant_name("boom"))
        self.assertEqual("ZAP", self.filters.constant_name("pow"))

    def test_module_name(self):
        self.filters.module_aliases["http://github.com/tefra/xsdata"] = "xsdata"
        self.filters.cache[MODULE]["pow"] = "Zap"

        self.assertEqual("foo_bar", self.filters.module_name("fooBar"))
        self.assertEqual("foo_bar_wtf", self.filters.module_name("fooBar.wtf"))
        self.assertEqual("mod_1111", self.filters.module_name("1111"))
        self.assertEqual("xs_string", self.filters.module_name("xs:string"))
        self.assertEqual("foo_bar_bam", self.filters.module_name("foo:bar_bam"))
        self.assertEqual("bar_bam", self.filters.module_name("urn:bar_bam"))
        self.assertEqual("Zap", self.filters.module_name("pow"))
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
        self.filters.cache[PACKAGE]["pow"] = "Zap"

        self.assertEqual(
            "foo.bar_bar.pkg_1", self.filters.package_name("Foo.BAR_bar.1")
        )
        self.assertEqual("foo.bang.pkg_1", self.filters.package_name("Foo.boom.1"))
        self.assertEqual("booom", self.filters.package_name("boom.boom"))
        self.assertEqual("Zap", self.filters.package_name("pow"))

    def test_type_name(self):
        self.assertEqual("str", self.filters.type_name(type_str))

        type_foo_bar_bam = AttrTypeFactory.create(qname="bar_bam")
        self.assertEqual("BarBam", self.filters.type_name(type_foo_bar_bam))

    def test_constant_value(self):
        attr = AttrFactory.create(types=[AttrTypeFactory.xs_string()], default="foo")
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
        self.assertEqual('lambda: [1, "bar"]', self.filters.field_default_value(attr))

    def test_field_default_value_with_type_float(self):
        attr = AttrFactory.create(types=[type_float], default="1.5")
        self.assertEqual(1.5, self.filters.field_default_value(attr))

        attr.default = "inf"
        attr.types = [type_int, type_float]
        self.assertEqual("float('inf')", self.filters.field_default_value(attr))

        attr.default = "-inf"
        self.assertEqual("float('-inf')", self.filters.field_default_value(attr))

    def test_field_default_value_with_type_decimal(self):
        attr = AttrFactory.create(types=[type_decimal], default="1.5")
        self.assertEqual("Decimal('1.5')", self.filters.field_default_value(attr))

        attr.default = "-inf"
        self.assertEqual("Decimal('-Infinity')", self.filters.field_default_value(attr))

        attr.default = "inf"
        self.assertEqual("Decimal('Infinity')", self.filters.field_default_value(attr))

    def test_field_default_value_with_type_int(self):
        attr = AttrFactory.create(types=[type_int], default="1")
        self.assertEqual(1, self.filters.field_default_value(attr))

    def test_field_default_value_with_type_bool(self):
        attr = AttrFactory.create(types=[type_bool], default="true")
        self.assertTrue(self.filters.field_default_value(attr))

    def test_field_default_value_with_type_enum(self):
        attr = AttrFactory.create(
            types=AttrTypeFactory.list(1, qname="foo"), default="@enum@foo::bar"
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

    def test_field_default_value_with_any_attribute(self):
        attr = AttrFactory.any_attribute()
        self.assertEqual("dict", self.filters.field_default_value(attr))

    def test_field_default_value_with_type_list(self):
        attr = AttrFactory.create(types=[type_bool])
        attr.restrictions.max_occurs = 2
        self.assertEqual("list", self.filters.field_default_value(attr))

    def test_field_default_value_with_multiple_types(self):
        attr = AttrFactory.create(types=[type_bool, type_int, type_float], default="1")
        self.assertEqual(1, self.filters.field_default_value(attr))

        attr.default = "1.0"
        self.assertEqual(1.0, self.filters.field_default_value(attr))

        attr.default = "true"
        self.assertTrue(self.filters.field_default_value(attr))

    def test_field_metadata(self):
        attr = AttrFactory.element()
        expected = {"name": "attr_B", "type": "Element"}
        self.assertEqual(expected, self.filters.field_metadata(attr, None, []))
        self.assertEqual(expected, self.filters.field_metadata(attr, "foo", []))

    def test_field_metadata_namespace(self):
        attr = AttrFactory.element(namespace="foo")
        expected = {"name": "attr_B", "namespace": "foo", "type": "Element"}

        self.assertEqual(expected, self.filters.field_metadata(attr, None, []))
        self.assertNotIn("namespace", self.filters.field_metadata(attr, "foo", []))

        attr = AttrFactory.attribute(namespace="foo")
        expected = {"name": "attr_C", "namespace": "foo", "type": "Attribute"}

        self.assertEqual(expected, self.filters.field_metadata(attr, None, []))
        self.assertIn("namespace", self.filters.field_metadata(attr, "foo", []))

    def test_field_metadata_name(self):
        attr = AttrFactory.element(local_name="foo", name="bar")
        self.assertEqual("foo", self.filters.field_metadata(attr, None, [])["name"])

        attr = AttrFactory.element(local_name="foo", name="Foo")
        self.assertNotIn("name", self.filters.field_metadata(attr, None, []))

        attr = AttrFactory.create(tag=Tag.ANY, local_name="foo", name="bar")
        self.assertNotIn("name", self.filters.field_metadata(attr, None, []))

    def test_field_metadata_restrictions(self):
        attr = AttrFactory.create(tag=Tag.RESTRICTION)
        attr.types.append(AttrTypeFactory.xs_int())
        attr.restrictions.min_occurs = 1
        attr.restrictions.max_occurs = 2
        attr.restrictions.max_inclusive = "2"
        attr.restrictions.required = False

        expected = {"min_occurs": 1, "max_occurs": 2, "max_inclusive": 2}
        self.assertEqual(expected, self.filters.field_metadata(attr, None, []))

    def test_field_metadata_mixed(self):
        attr = AttrFactory.element(mixed=True)
        expected = {"mixed": True, "name": "attr_B", "type": "Element"}
        self.assertEqual(expected, self.filters.field_metadata(attr, "foo", []))

    def test_field_metadata_choices(self):
        attr = AttrFactory.create(choices=AttrChoiceFactory.list(2, tag=Tag.ELEMENT))
        actual = self.filters.field_metadata(attr, "foo", [])
        expected = [
            {"name": "choice_B", "type": "Type[str]"},
            {"name": "choice_C", "type": "Type[str]"},
        ]

        self.assertEqual(expected, actual["choices"])

    def test_field_choices(self):
        attr = AttrFactory.create(
            choices=[
                AttrChoiceFactory.element(
                    namespace="foo",
                    types=[type_float],
                    restrictions=Restrictions(max_exclusive="10"),
                ),
                AttrChoiceFactory.element(namespace="bar"),
                AttrChoiceFactory.any(namespace="##other"),
            ]
        )

        actual = self.filters.field_choices(attr, "foo", ["a", "b"])
        expected = [
            {"name": "choice_B", "type": "Type[float]", "max_exclusive": 10.0},
            {"name": "choice_C", "namespace": "bar", "type": "Type[str]"},
            {
                "name": "choice_D",
                "namespace": "##other",
                "wildcard": True,
                "type": "Type[object]",
            },
        ]

        self.assertEqual(expected, actual)

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
                AttrTypeFactory.xs_int(),
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
            types=[AttrTypeFactory.xs_int(), AttrTypeFactory.xs_positive_int()]
        )
        self.assertEqual("Optional[int]", self.filters.field_type(attr, ["a", "b"]))

    def test_choice_type(self):
        choice = AttrChoiceFactory.create(types=[AttrTypeFactory.create("foobar")])
        actual = self.filters.choice_type(choice, ["a", "b"])
        self.assertEqual("Type[Foobar]", actual)

    def test_choice_type_with_forward_reference(self):
        choice = AttrChoiceFactory.create(
            types=[AttrTypeFactory.create("foobar", forward=True)]
        )
        actual = self.filters.choice_type(choice, ["a", "b"])
        self.assertEqual('Type["A.B.Foobar"]', actual)

    def test_choice_type_with_circular_reference(self):
        choice = AttrChoiceFactory.create(
            types=[AttrTypeFactory.create("foobar", circular=True)]
        )
        actual = self.filters.choice_type(choice, ["a", "b"])
        self.assertEqual('Type["Foobar"]', actual)

    def test_choice_type_with_multiple_types(self):
        choice = AttrChoiceFactory.create(types=[type_str, type_bool])
        actual = self.filters.choice_type(choice, ["a", "b"])
        self.assertEqual("Type[Union[str, bool]]", actual)

    def test_choice_type_with_list_types_are_ignored(self):
        choice = AttrChoiceFactory.create(types=[type_str, type_bool])
        choice.restrictions.max_occurs = 200
        actual = self.filters.choice_type(choice, ["a", "b"])
        self.assertEqual("Type[Union[str, bool]]", actual)

    def test_choice_type_with_restrictions_tokens_true(self):
        choice = AttrChoiceFactory.create(types=[type_str, type_bool])
        choice.restrictions.tokens = True
        actual = self.filters.choice_type(choice, ["a", "b"])
        self.assertEqual("Type[List[Union[str, bool]]]", actual)

    def test_default_imports_with_decimal(self):
        expected = "from decimal import Decimal"

        self.assertIn(expected, self.filters.default_imports("Optional[Decimal]"))
        self.assertIn(expected, self.filters.default_imports("Union[str, Decimal]"))
        self.assertIn(expected, self.filters.default_imports("number: Decimal"))
        self.assertIn(expected, self.filters.default_imports(" = Decimal"))
        self.assertNotIn(expected, self.filters.default_imports("class fooDecimal"))

    def test_default_imports_with_qname(self):
        expected = "from xml.etree.ElementTree import QName"

        self.assertIn(expected, self.filters.default_imports("Optional[QName]"))
        self.assertIn(expected, self.filters.default_imports("Union[str, QName]"))
        self.assertIn(expected, self.filters.default_imports("qname: QName"))
        self.assertIn(expected, self.filters.default_imports(" = QName"))
        self.assertNotIn(expected, self.filters.default_imports("class fooQName"))

    def test_default_imports_with_enum(self):
        output = " (Enum) "

        expected = "from enum import Enum"
        self.assertIn(expected, self.filters.default_imports(output))

    def test_default_imports_with_dataclasses(self):
        output = " @dataclass "

        expected = "from dataclasses import dataclass"
        self.assertIn(expected, self.filters.default_imports(output))

        output = " field( "
        expected = "from dataclasses import field"
        self.assertIn(expected, self.filters.default_imports(output))

        output = " field( @dataclass "
        expected = "from dataclasses import dataclass, field"
        self.assertIn(expected, self.filters.default_imports(output))

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

        expected = (
            "from dataclasses import dataclass, field\n" "from typing import Optional"
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
        )

        expected = (
            "{\n"
            '    "num": 1,\n'
            '    "text": "foo",\n'
            '    "text_two": "fo\'o",\n'
            '    "text_three": "fo\'o",\n'
            '    "pattern": r"foo",\n'
            '    "level_two": {\n'
            '        "a": 1,\n'
            "    },\n"
            '    "list": (\n'
            "        {\n"
            '            "type": object,\n'
            "        },\n"
            "        {\n"
            '            "type": "Type[object] mpla",\n'
            "        },\n"
            "    ),\n"
            "}"
        )
        self.assertEqual(expected, self.filters.format_metadata(data))

    def test_class_docstring(self):
        target = ClassFactory.create(
            attrs=[
                AttrFactory.element(help="help"),
                AttrFactory.element(help="Foo\nBar"),
                AttrFactory.element(),
            ]
        )

        expected = (
            '"""\n'
            ":ivar attr_b: help\n"
            ":ivar attr_c: Foo\n"
            "Bar\n"
            ":ivar attr_d:\n"
            '"""'
        )
        self.assertEqual(expected, self.filters.class_docstring(target))

    def test_class_docstring_with_class_help(self):
        target = ClassFactory.elements(2, help="Help Me!")

        expected = '"""Help Me!\n' "\n" ":ivar attr_b:\n" ":ivar attr_c:\n" '"""'
        self.assertEqual(expected, self.filters.class_docstring(target))

    def test_class_docstring_with_enumeration(self):
        target = ClassFactory.enumeration(2, help="Help Me!")

        expected = '"""Help Me!\n' "\n" ":cvar ATTR_B:\n" ":cvar ATTR_C:\n" '"""'
        self.assertEqual(expected, self.filters.class_docstring(target, enum=True))

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
        self.assertEqual("CAb", filters.field_name("cAB"))
        self.assertEqual("cAB", filters.package_name("cAB"))
        self.assertEqual("c_ab", filters.module_name("cAB"))

        self.assertEqual({"a": "b", "c": "d"}, filters.class_aliases)
        self.assertEqual({"e": "f"}, filters.field_aliases)
        self.assertEqual({"g": "h"}, filters.package_aliases)
        self.assertEqual({"i": "j"}, filters.module_aliases)
