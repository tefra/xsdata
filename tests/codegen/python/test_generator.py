from unittest import TestCase, mock

from xsdata.codegen.python.generator import (
    PythonAbstractGenerator as generator,
)
from xsdata.models.codegen import Attr, Class, Package


class PythonAbstractGeneratorTests(TestCase):
    @mock.patch.object(generator, "process_attribute")
    @mock.patch.object(generator, "type_name")
    @mock.patch.object(generator, "class_name")
    def test_process_class(
        self, mock_class_name, mock_type_name, mock_process_attribute
    ):
        mock_class_name.side_effect = lambda x: f"@{x}"
        mock_type_name.side_effect = lambda x: f"!{x}"

        a = Class(name="a", extensions=["m", "n"])
        a.attrs = [
            Attr(name=x, type=x, default=x, local_type=x) for x in "bcd"
        ]
        e = Class(name="e")
        e.attrs = [
            Attr(name=x, type=x, default=x, local_type=x) for x in "fgh"
        ]

        i = Class(name="i", extensions=["o"])
        i.attrs = [
            Attr(name=x, type=x, default=x, local_type=x) for x in "jkl"
        ]
        a.inner = [e, i]

        generator.process_class(a)

        mock_class_name.assert_has_calls(
            [mock.call("a"), mock.call("e"), mock.call("i")]
        )

        mock_type_name.assert_has_calls(
            [mock.call("m"), mock.call("n"), mock.call("o")]
        )

        mock_process_attribute.assert_has_calls(
            [
                mock.call(e.attrs[0], ["@a", "@e"]),
                mock.call(e.attrs[1], ["@a", "@e"]),
                mock.call(e.attrs[2], ["@a", "@e"]),
                mock.call(i.attrs[0], ["@a", "@i"]),
                mock.call(i.attrs[1], ["@a", "@i"]),
                mock.call(i.attrs[2], ["@a", "@i"]),
                mock.call(a.attrs[0], ["@a"]),
                mock.call(a.attrs[1], ["@a"]),
                mock.call(a.attrs[2], ["@a"]),
            ]
        )
        self.assertEqual(9, mock_process_attribute.call_count)

    @mock.patch("xsdata.utils.text.strip_prefix", return_value="nope")
    @mock.patch.object(generator, "attribute_default", return_value="life")
    @mock.patch.object(generator, "attribute_type", return_value="rab")
    @mock.patch.object(generator, "attribute_name", return_value="oof")
    def test_process_attribute(
        self, mock_name, mock_type, mock_default, mock_strip_prefix
    ):
        attr = Attr(name="foo", type="bar", default="thug", local_type="")
        generator.process_attribute(attr, ["a", "b"])

        self.assertEqual("oof", attr.name)
        self.assertEqual("rab", attr.type)
        self.assertEqual("nope", attr.local_name)
        self.assertEqual("life", attr.default)

        mock_name.assert_called_once_with("foo")
        mock_type.assert_called_once_with(attr, ["a", "b"])
        mock_default.assert_called_once_with(attr)
        mock_strip_prefix.assert_called_once_with("foo")

    def test_process_import(self):
        package = Package(name="bar", alias="foo:bar", source="some.foo.bar")

        actual = generator.process_import(package)
        self.assertIs(actual, package)
        self.assertEqual("Bar", package.name)
        self.assertEqual("FooBar", package.alias)
        self.assertEqual("some.foo.bar", package.source)

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
        parents = []
        attr = Attr(name="foo", type="foo_bar", default="foo", local_type="")

        actual = generator.attribute_type(attr, parents)
        self.assertEqual("FooBar", actual)

        attr.default = None
        actual = generator.attribute_type(attr, parents)
        self.assertEqual("Optional[FooBar]", actual)

        attr.forward_ref = True
        parents = ["Parent"]
        actual = generator.attribute_type(attr, parents)
        self.assertEqual('Optional["Parent.FooBar"]', actual)

        parents = ["A", "Parent"]
        attr.restrictions["max_occurs"] = "2"
        actual = generator.attribute_type(attr, parents)
        self.assertEqual('List["A.Parent.FooBar"]', actual)

        attr.type = "thug:life"
        attr.type_alias = "Boss:Life"
        actual = generator.attribute_type(attr, parents)
        self.assertEqual('List["A.Parent.BossLife"]', actual)

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
