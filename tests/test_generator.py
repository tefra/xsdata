from unittest import mock

from tests.factories import AttrFactory
from tests.factories import AttrTypeFactory
from tests.factories import ClassFactory
from tests.factories import ExtensionFactory
from tests.factories import FactoryTestCase
from tests.factories import PackageFactory
from xsdata.generators import PythonAbstractGenerator as generator
from xsdata.models.enums import DataType
from xsdata.models.enums import TagType


class PythonAbstractGeneratorTests(FactoryTestCase):
    @mock.patch.object(generator, "process_enumerations")
    @mock.patch.object(generator, "process_attributes")
    @mock.patch.object(generator, "process_extension")
    @mock.patch.object(generator, "class_name")
    def test_process_class(
        self,
        mock_class_name,
        mock_process_extension,
        mock_process_attributes,
        mock_process_enumerations,
    ):
        mock_class_name.side_effect = lambda x: f"@{x}"

        type_o = AttrTypeFactory.create(name="o")
        type_m = AttrTypeFactory.create(name="m")
        type_n = AttrTypeFactory.create(name="n")

        a = ClassFactory.create(
            name="a",
            extensions=[type_m, type_n],
            attrs=AttrFactory.list(2, local_type=TagType.EXTENSION),
        )
        e = ClassFactory.create(
            name="e", attrs=AttrFactory.list(2, local_type=TagType.ENUMERATION)
        )
        i = ClassFactory.create(
            name="i",
            extensions=[type_o],
            attrs=AttrFactory.list(2, local_type=TagType.EXTENSION),
        )
        a.inner = [e, i]

        generator.process_class(a)

        mock_class_name.assert_has_calls(
            [mock.call("a"), mock.call("e"), mock.call("i")]
        )

        mock_process_extension.assert_has_calls(
            [mock.call(type_o), mock.call(type_m), mock.call(type_n)]
        )

        mock_process_attributes.assert_has_calls(
            [mock.call(i, ["@a", "@i"]), mock.call(a, ["@a"])]
        )
        mock_process_enumerations.assert_called_once_with(e)

    @mock.patch.object(generator, "process_enumeration")
    def test_process_enumerations(self, mock_process_enumeration):
        obj = ClassFactory.create(
            attrs=[
                AttrFactory.create(default=3),
                AttrFactory.create(default=2),
                AttrFactory.create(default=1),
                AttrFactory.create(default=1),
            ]
        )
        calls = reversed([mock.call(attr, obj) for attr in obj.attrs])

        generator.process_enumerations(obj)
        mock_process_enumeration.assert_has_calls(calls)
        self.assertEqual(1, obj.attrs[0].default)
        self.assertEqual(2, obj.attrs[1].default)
        self.assertEqual(3, obj.attrs[2].default)
        self.assertEqual(3, len(obj.attrs))

    @mock.patch.object(generator, "process_attribute")
    def test_process_attributes(self, mock_process_attribute):
        obj = ClassFactory.create(attrs=AttrFactory.list(3))
        generator.process_attributes(obj, ["a", "b"])
        mock_process_attribute.assert_has_calls(
            [mock.call(attr, ["a", "b"]) for attr in obj.attrs]
        )

    @mock.patch.object(generator, "type_name", return_value="oof")
    def test_process_extension(self, mock_type_name):
        extension = ExtensionFactory.create(type=AttrTypeFactory.create(name="foobar"))
        generator.process_extension(extension)

        mock_type_name.assert_called_once_with(extension.type)

        self.assertEqual("oof", extension.type.name)

    @mock.patch("xsdata.utils.text.split", return_value=[None, "nope"])
    @mock.patch.object(generator, "attribute_default", return_value="life")
    @mock.patch.object(generator, "attribute_display_type", return_value="rab")
    @mock.patch.object(generator, "attribute_name", return_value="oof")
    def test_process_attribute(
        self, mock_name, mock_display_type, mock_default, mock_split
    ):
        type_bar = AttrTypeFactory.create(name="bar")
        attr = AttrFactory.create(name="foo", types=[type_bar], default="thug")

        self.assertIsNone(attr.display_type)

        generator.process_attribute(attr, ["a", "b"])

        self.assertEqual("oof", attr.name)
        self.assertEqual("rab", attr.display_type)
        self.assertEqual("nope", attr.local_name)
        self.assertEqual("life", attr.default)

        mock_name.assert_called_once_with("foo")
        mock_display_type.assert_called_once_with(attr, ["a", "b"])
        mock_default.assert_called_once_with(attr)
        mock_split.assert_called_once_with("foo")

    @mock.patch.object(generator, "attribute_default", return_value="2")
    @mock.patch.object(generator, "enumeration_name", return_value="OOF")
    def test_process_enumeration(self, mock_name, mock_default):
        type_bar = AttrTypeFactory.create(name="bar")
        attr = AttrFactory.create(name="foo", types=[type_bar], default="thug")
        extensions = ExtensionFactory.list(
            1, type=AttrTypeFactory.create(name="xs:int")
        )
        parent = ClassFactory.create(extensions=extensions)
        generator.process_enumeration(attr, parent)

        self.assertEqual("OOF", attr.name)
        self.assertEqual("foo", attr.local_name)
        self.assertEqual("2", attr.default)

        mock_name.assert_called_once_with("foo")
        mock_default.assert_called_once_with(attr)

    def test_process_enumeration_with_non_xsd_type_extensions(self):
        type_bar = AttrTypeFactory.create(name="bar")
        attr = AttrFactory.create(name="foo", types=[type_bar], default="thug")

        parent = ClassFactory.create()
        generator.process_enumeration(attr, parent)
        self.assertEqual([type_bar], attr.types)

        attr.types = []
        extensions = ExtensionFactory.list(
            2, type=AttrTypeFactory.create(name="xs:string")
        )
        parent = ClassFactory.create(extensions=extensions)
        generator.process_enumeration(attr, parent)
        self.assertEqual([], attr.types)

        attr.types = []
        extensions = ExtensionFactory.list(1, type=AttrTypeFactory.create(name="foo"))
        parent = ClassFactory.create(extensions=extensions)
        generator.process_enumeration(attr, parent)
        self.assertEqual([], attr.types)

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

        type_str = AttrTypeFactory.create(name="string", native=True)
        self.assertEqual("str", generator.type_name(type_str))

        type_foo_bar_bam = AttrTypeFactory.create(name="foo:bar_bam")
        self.assertEqual("BarBam", generator.type_name(type_foo_bar_bam))

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

    def test_attribute_display_type(self):
        parents = []
        type_foo_bar = AttrTypeFactory.create(name="foo_bar")

        attr = AttrFactory.create(name="foo", default="foo", types=[type_foo_bar])

        actual = generator.attribute_display_type(attr, parents)
        self.assertEqual("FooBar", actual)

        attr.default = None
        actual = generator.attribute_display_type(attr, parents)
        self.assertEqual("Optional[FooBar]", actual)

        parents = ["Parent"]
        attr.types[0].forward_ref = True
        actual = generator.attribute_display_type(attr, parents)
        self.assertEqual('Optional["Parent.FooBar"]', actual)

        parents = ["A", "Parent"]
        attr.restrictions.max_occurs = 2
        actual = generator.attribute_display_type(attr, parents)
        self.assertEqual('List["A.Parent.FooBar"]', actual)

        attr.types[0].alias = "Boss:Life"
        actual = generator.attribute_display_type(attr, parents)
        self.assertEqual('List["A.Parent.BossLife"]', actual)

        attr.types = [
            AttrTypeFactory.create(
                name="thug:life", alias="Boss:Life", forward_ref=True
            ),
            AttrTypeFactory.create(name="int", native=True),
        ]
        actual = generator.attribute_display_type(attr, parents)
        self.assertEqual('List[Union["A.Parent.BossLife", int]]', actual)

    def test_attribute_default(self):
        type_str = AttrTypeFactory.create(name=DataType.STRING.code, native=True)
        type_int = AttrTypeFactory.create(name=DataType.INTEGER.code, native=True)
        type_float = AttrTypeFactory.create(name=DataType.FLOAT.code, native=True)
        type_bool = AttrTypeFactory.create(name=DataType.BOOLEAN.code, native=True)

        attr = AttrFactory.create(name="foo", types=[type_str])
        self.assertEqual(None, generator.attribute_default(attr))

        attr.default = "foo"
        self.assertEqual('"foo"', generator.attribute_default(attr))

        attr.default = "1.5"
        attr.types[0] = type_float
        self.assertEqual(1.5, generator.attribute_default(attr))

        attr.default = "1"
        attr.types[0] = type_int
        self.assertEqual(1, generator.attribute_default(attr))

        attr.default = "true"
        attr.types[0] = type_bool
        self.assertTrue(generator.attribute_default(attr))

        attr.restrictions.max_occurs = 2
        self.assertEqual("list", generator.attribute_default(attr))

        attr.default = "1"
        attr.restrictions.max_occurs = 1
        attr.types = [type_bool, type_int, type_float]
        self.assertEqual(1, generator.attribute_default(attr))

        attr.default = "1.0"
        self.assertEqual(1.0, generator.attribute_default(attr))

        attr.default = "true"
        self.assertTrue(generator.attribute_default(attr))
