from unittest import mock

from tests.factories import (
    AttrFactory,
    ClassFactory,
    ExtensionFactory,
    FactoryTestCase,
    PackageFactory,
)
from xsdata.generators import PythonAbstractGenerator as generator
from xsdata.models.enums import TagType


class PythonAbstractGeneratorTests(FactoryTestCase):
    @mock.patch.object(generator, "process_attribute")
    @mock.patch.object(generator, "type_name")
    @mock.patch.object(generator, "class_name")
    def test_process_class(
        self, mock_class_name, mock_type_name, mock_process_attribute
    ):
        mock_class_name.side_effect = lambda x: f"@{x}"
        mock_type_name.side_effect = lambda x: f"!{x}"

        a = ClassFactory.create(
            name="a",
            extensions=[
                ExtensionFactory.create(name="m"),
                ExtensionFactory.create(name="n"),
            ],
        )
        a.attrs = [AttrFactory.create(name=x) for x in "bcd"]
        e = ClassFactory.create(name="e")
        e.attrs = [AttrFactory.create(name=x) for x in "fgh"]

        i = ClassFactory.create(
            name="i", extensions=ExtensionFactory.list(1, name="o")
        )
        i.attrs = [AttrFactory.create(name=x) for x in "jkl"]
        a.inner = [e, i]

        generator.process_class(a)

        self.assertEqual("!m", a.extensions[0].name)
        self.assertEqual("!n", a.extensions[1].name)
        self.assertEqual("!o", i.extensions[0].name)

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

    @mock.patch.object(generator, "process_enumeration")
    def test_process_enum_class(self, mock_process_enumeration):
        a = ClassFactory.create(
            name="a",
            attrs=AttrFactory.list(2, local_type=TagType.ENUMERATION.cname),
        )
        generator.process_class(a)

        mock_process_enumeration.assert_has_calls(
            [mock.call(a.attrs[0], a), mock.call(a.attrs[1], a)]
        )
        self.assertEqual(2, mock_process_enumeration.call_count)

    @mock.patch("xsdata.utils.text.split", return_value=[None, "nope"])
    @mock.patch.object(generator, "attribute_default", return_value="life")
    @mock.patch.object(generator, "attribute_type", return_value="rab")
    @mock.patch.object(generator, "attribute_name", return_value="oof")
    def test_process_attribute(
        self, mock_name, mock_type, mock_default, mock_split
    ):
        attr = AttrFactory.create(name="foo", type="bar", default="thug")
        generator.process_attribute(attr, ["a", "b"])

        self.assertEqual("oof", attr.name)
        self.assertEqual("rab", attr.type)
        self.assertEqual("nope", attr.local_name)
        self.assertEqual("life", attr.default)

        mock_name.assert_called_once_with("foo")
        mock_type.assert_called_once_with(attr, ["a", "b"])
        mock_default.assert_called_once_with(attr)
        mock_split.assert_called_once_with("foo")

    @mock.patch.object(generator, "attribute_default", return_value="2")
    @mock.patch.object(generator, "enumeration_name", return_value="OOF")
    def test_process_enumeration(self, mock_name, mock_default):
        attr = AttrFactory.create(name="foo", type="bar", default="thug")
        extensions = ExtensionFactory.list(1, name="int")
        parent = ClassFactory.create(extensions=extensions)
        generator.process_enumeration(attr, parent)

        self.assertEqual("OOF", attr.name)
        self.assertEqual("int", attr.type)
        self.assertEqual("foo", attr.local_name)
        self.assertEqual("2", attr.default)

        mock_name.assert_called_once_with("foo")
        mock_default.assert_called_once_with(attr)

    def test_process_enumeration_with_invalid_parent_extensions(self):
        attr = AttrFactory.create(name="foo", type="bar", default="thug")

        parent = ClassFactory.create()
        generator.process_enumeration(attr, parent)
        self.assertEqual("str", attr.type)

        attr.type = None
        extensions = ExtensionFactory.list(2, name="str")
        parent = ClassFactory.create(extensions=extensions)
        generator.process_enumeration(attr, parent)
        self.assertEqual("str", attr.type)

        attr.type = None
        extensions = ExtensionFactory.list(1, name="foo")
        parent = ClassFactory.create(extensions=extensions)
        generator.process_enumeration(attr, parent)
        self.assertEqual("str", attr.type)

    def test_process_import(self):
        package = PackageFactory.create(
            name="bar", alias="foo:bar", source="some.foo.bar"
        )

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
        self.assertEqual("br_eak_value", generator.attribute_name("BrEak"))
        self.assertEqual("value_1", generator.attribute_name("1"))

    def test_enumeration_name(self):
        self.assertEqual("FOO", generator.enumeration_name("foo"))
        self.assertEqual("BAR", generator.enumeration_name("foo:bar"))
        self.assertEqual("FOO_BAR", generator.enumeration_name("FooBar"))
        self.assertEqual("NONE_VALUE", generator.enumeration_name("None"))
        self.assertEqual("BR_EAK_VALUE", generator.enumeration_name("BrEak"))

    def test_attribute_type(self):
        parents = []
        attr = AttrFactory.create(name="foo", type="foo_bar", default="foo")

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
        attr.max_occurs = 2
        actual = generator.attribute_type(attr, parents)
        self.assertEqual('List["A.Parent.FooBar"]', actual)

        attr.type = "thug:life"
        attr.type_aliases = {"thug:life": "Boss:Life"}
        actual = generator.attribute_type(attr, parents)
        self.assertEqual('List["A.Parent.BossLife"]', actual)

        attr.type = "thug:life xs:int"
        attr.forward_ref = False
        attr.type_aliases = {"thug:life": "Boss:Life"}
        actual = generator.attribute_type(attr, parents)
        self.assertEqual("List[Union[BossLife, int]]", actual)

    def test_attribute_default(self):
        attr = AttrFactory.create(name="foo", type="str")
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

        attr.max_occurs = 2
        self.assertEqual("list", generator.attribute_default(attr))
