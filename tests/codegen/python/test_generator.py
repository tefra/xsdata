from dataclasses import asdict
from unittest import TestCase

from xsdata.codegen.python.generator import (
    PythonAbstractGenerator as generator,
)
from xsdata.models.codegen import Attr, Class, Object, Package


class AbstractPythonGeneratorTests(TestCase):
    def test_process_class(self):
        obj = Class(
            name="TypeFlexibleTimeSpec",
            help="",
            extensions=["TypeTimeSpec"],
            attrs=[
                Attr(
                    name="SearchExtraDays",
                    type="SearchExtraDays",
                    local_type="Element",
                    namespace=None,
                    help="",
                    forward_ref=True,
                    restrictions={},
                    default=None,
                )
            ],
            inner=[
                Class(
                    name="SearchExtraDays",
                    help=None,
                    extensions=[],
                    attrs=[
                        Attr(
                            name="DaysBefore",
                            type="xs:int",
                            local_type="Attribute",
                            namespace=None,
                            help="",
                            forward_ref=False,
                            restrictions={},
                            default=None,
                        ),
                        Attr(
                            name="DaysAfter",
                            type="xs:int",
                            local_type="Attribute",
                            namespace=None,
                            help="",
                            forward_ref=False,
                            restrictions={},
                            default=None,
                        ),
                    ],
                    inner=[],
                )
            ],
        )

        actual = generator.process_class(obj, {})
        self.maxDiff = None
        expected = {
            "attrs": [
                {
                    "default": None,
                    "forward_ref": True,
                    "help": "",
                    "local_name": "SearchExtraDays",
                    "local_type": "Element",
                    "name": "search_extra_days",
                    "namespace": None,
                    "restrictions": {},
                    "type": 'Optional["TypeFlexibleTimeSpec.SearchExtraDays"]',
                }
            ],
            "extensions": ["TypeTimeSpec"],
            "help": "",
            "inner": [
                {
                    "attrs": [
                        {
                            "default": None,
                            "forward_ref": False,
                            "help": "",
                            "local_name": "DaysBefore",
                            "local_type": "Attribute",
                            "name": "days_before",
                            "namespace": None,
                            "restrictions": {},
                            "type": "Optional[int]",
                        },
                        {
                            "default": None,
                            "forward_ref": False,
                            "help": "",
                            "local_name": "DaysAfter",
                            "local_type": "Attribute",
                            "name": "days_after",
                            "namespace": None,
                            "restrictions": {},
                            "type": "Optional[int]",
                        },
                    ],
                    "extensions": [],
                    "help": None,
                    "inner": [],
                    "name": "SearchExtraDays",
                }
            ],
            "name": "TypeFlexibleTimeSpec",
        }
        self.assertDictEqual(expected, asdict(actual))

    def test_process_import(self):
        package = Package(
            name="FoObAr",
            objects=[
                Object(name="foo", alias="foo:bar"),
                Object(name="foo_bar"),
            ],
        )

        actual = generator.process_import(package)
        self.assertIs(actual, package)
        self.assertEqual("FoObAr", package.name)
        self.assertEqual("Foo", package.objects[0].name)
        self.assertEqual("FooBar", package.objects[0].alias)
        self.assertEqual("FooBar", package.objects[1].name)
        self.assertIsNone(package.objects[1].alias)

    def test_class_name(self):
        self.assertEqual("XsString", generator.class_name("xs:string"))
        self.assertEqual("FooBarBam", generator.class_name("foo:bar_bam"))

    def test_type_name(self):
        self.assertEqual("str", generator.type_name("xs:string"))
        self.assertEqual("BarBam", generator.type_name("foo:bar_bam"))

    def test_attribute_name(self):
        self.assertEqual("foo", generator.attribute_name("foo"))
        self.assertEqual("bar", generator.attribute_name("foo:bar"))
        self.assertEqual("foo_bar", generator.attribute_name("FooBar"))
        self.assertEqual("none_value", generator.attribute_name("None"))
        self.assertEqual("break_value", generator.attribute_name("BrEak"))

    def test_attribute_type(self):
        overrides = {"thug:life"}
        parents = []
        attr = Attr(name="foo", type="foo_bar", default="foo", local_type="")

        actual = generator.attribute_type(attr, overrides, parents)
        self.assertEqual("FooBar", actual)

        attr.default = None
        actual = generator.attribute_type(attr, overrides, parents)
        self.assertEqual("Optional[FooBar]", actual)

        attr.forward_ref = True
        parents = ["Parent"]
        actual = generator.attribute_type(attr, overrides, parents)
        self.assertEqual('Optional["Parent.FooBar"]', actual)

        parents = ["A", "Parent"]
        attr.restrictions["max_occurs"] = "2"
        actual = generator.attribute_type(attr, overrides, parents)
        self.assertEqual('List["A.Parent.FooBar"]', actual)

        attr.type = "thug:life"
        actual = generator.attribute_type(attr, overrides, parents)
        self.assertEqual('List["A.Parent.ThugLife"]', actual)

    def test_attribute_default(self):
        attr = Attr(name="foo", type="str", local_type="")
        self.assertEqual(None, generator.attribute_default(attr))

        attr.default = "foo"
        self.assertEqual('"foo"', generator.attribute_default(attr))

        attr.default = "1.5"
        attr.type = "float"
        self.assertEqual(1.5, generator.attribute_default(attr))

        attr.default = "1"
        attr.type = "int"
        self.assertEqual(1, generator.attribute_default(attr))

        attr.default = "true"
        attr.type = "bool"
        self.assertTrue(generator.attribute_default(attr))

        attr.default = "not-true"
        self.assertFalse(generator.attribute_default(attr))

        attr.restrictions["max_occurs"] = "2"
        self.assertEqual("list", generator.attribute_default(attr))
