from unittest import mock

from tests.factories import AttrFactory
from tests.factories import AttrTypeFactory
from tests.factories import ClassFactory
from tests.factories import FactoryTestCase
from xsdata.models.codegen import AttrType
from xsdata.models.elements import ComplexType
from xsdata.models.elements import Element
from xsdata.models.elements import Restriction
from xsdata.models.elements import Schema
from xsdata.models.elements import SimpleType
from xsdata.models.enums import DataType
from xsdata.models.enums import TagType
from xsdata.reducer import ClassReducer


class ClassReducerTests(FactoryTestCase):
    def setUp(self) -> None:
        super(ClassReducerTests, self).setUp()
        self.target_namespace = "http://namespace/target"
        self.nsmap = {
            None: "http://namespace/foobar",
            "common": "http://namespace/common",
        }
        self.schema = Schema.create(
            target_namespace=self.target_namespace, nsmap=self.nsmap
        )
        self.reducer = ClassReducer()

    @mock.patch.object(ClassReducer, "flatten_classes")
    @mock.patch.object(ClassReducer, "add_common_types")
    def test_process(self, mock_add_common_types, mock_flatten_classes):
        classes = ClassFactory.list(3, type=Element)
        simplies = ClassFactory.list(2, type=SimpleType)
        enums = ClassFactory.list(
            2,
            type=Restriction,
            attrs=AttrFactory.list(2, local_type=TagType.ENUMERATION),
        )
        abstracts = ClassFactory.list(2, is_abstract=True, type=ComplexType)

        common = simplies + abstracts + enums
        all_classes = classes + common

        self.reducer.redefined_types = {"a": ClassFactory.create()}
        result = self.reducer.process(self.schema, all_classes)

        self.assertEqual(enums + classes, result)
        self.assertEqual(0, len(self.reducer.redefined_types))

        mock_add_common_types.assert_called_once_with(common, self.schema)
        mock_flatten_classes.assert_has_calls(
            [mock.call(common, self.schema), mock.call(classes, self.schema)]
        )

    @mock.patch.object(ClassReducer, "flatten_class")
    def test_flatten_classes(self, mock_flatten_class):
        classes = ClassFactory.list(2)
        ClassReducer().flatten_classes(classes, self.target_namespace)

        mock_flatten_class.assert_has_calls(
            [mock.call(obj, self.target_namespace) for obj in classes]
        )

    def test_add_common_types(self):
        classes = ClassFactory.list(2)
        expected = {f"{{{self.target_namespace}}}{obj.name}": obj for obj in classes}

        self.reducer.add_common_types(classes, self.schema)
        self.assertEqual(expected, self.reducer.common_types)

    @mock.patch.object(ClassReducer, "flatten_class")
    def test_add_common_types_with_redefine(self, mock_flatten_class):
        classes = ClassFactory.list(2)
        self.reducer.add_common_types(classes, self.schema)

        expected = {f"{{{self.target_namespace}}}{obj.name}": obj for obj in classes}
        self.assertEqual(expected, self.reducer.common_types)
        self.assertEqual(dict(), self.reducer.redefined_types)

        self.reducer.add_common_types(classes, self.schema)
        self.assertEqual(expected, self.reducer.common_types)
        self.assertEqual(expected, self.reducer.redefined_types)

        mock_flatten_class.assert_has_calls(
            [mock.call(classes[0], self.schema), mock.call(classes[1], self.schema)]
        )

    def test_find_common_type(self):
        obj = ClassFactory.create(name="foo", type=SimpleType)
        self.reducer.common_types = {
            f"{{http://namespace/target}}{obj.name}": obj,
            f"{{http://namespace/common}}{obj.name}": obj,
        }

        self.assertEqual(obj, self.reducer.find_common_type("foo", self.schema))
        self.assertEqual(obj, self.reducer.find_common_type("common:foo", self.schema))
        self.assertIsNone(self.reducer.find_common_type("bar", self.schema))

    @mock.patch.object(ClassReducer, "flatten_enumeration_unions")
    @mock.patch.object(ClassReducer, "flatten_attribute")
    @mock.patch.object(ClassReducer, "flatten_extension")
    def test_flatten_class(
        self,
        mock_flatten_extension,
        mock_flatten_attribute,
        mock_flatten_enumeration_unions,
    ):
        obj = ClassFactory.create(
            name="a",
            type=SimpleType,
            extensions=["b", "c"],
            attrs=[AttrFactory.create(name=x) for x in "de"],
            inner=[
                ClassFactory.create(
                    name="f",
                    type="f",
                    extensions=["g", "h"],
                    attrs=[AttrFactory.create(name=x) for x in "ij"],
                )
            ],
        )

        self.reducer.flatten_class(obj, self.schema)

        mock_flatten_enumeration_unions.assert_has_calls(
            [mock.call(obj, self.schema), mock.call(obj.inner[0], self.schema)]
        )

        mock_flatten_extension.assert_has_calls(
            [
                mock.call(obj, "b", self.schema),
                mock.call(obj, "c", self.schema),
                mock.call(obj.inner[0], "g", self.schema),
                mock.call(obj.inner[0], "h", self.schema),
            ]
        )
        mock_flatten_attribute.assert_has_calls(
            [
                mock.call(obj, obj.attrs[0], self.schema),
                mock.call(obj, obj.attrs[1], self.schema),
                mock.call(obj.inner[0], obj.inner[0].attrs[0], self.schema),
                mock.call(obj.inner[0], obj.inner[0].attrs[1], self.schema),
            ]
        )

    @mock.patch.object(ClassReducer, "flatten_enumeration_unions")
    def test_flatten_class_skip_enumeration_unions_when_class_not_common(
        self, mock_flatten_enumeration_unions,
    ):
        obj = ClassFactory.create(type=Element)
        self.reducer.flatten_class(obj, self.schema)

        self.assertEqual(0, mock_flatten_enumeration_unions.call_count)

    @mock.patch.object(ClassReducer, "find_common_type")
    def test_flatten_extension_when_no_common(self, mock_find_common_type):
        mock_find_common_type.return_value = None

        extension = AttrTypeFactory.create()
        obj = ClassFactory.create(extensions=[extension])
        self.reducer.flatten_extension(obj, extension, self.nsmap)

        self.assertEqual(1, len(obj.extensions))
        mock_find_common_type.assert_called_once_with(extension.name, self.nsmap)

    @mock.patch.object(ClassReducer, "create_default_attribute")
    @mock.patch.object(ClassReducer, "find_common_type")
    def test_flatten_extension_when_common_is_enumeration(
        self, mock_find_common_type, mock_create_default_attribute
    ):
        mock_find_common_type.return_value = ClassFactory.create(
            attrs=AttrFactory.list(2, local_type=TagType.ENUMERATION)
        )

        extension = AttrTypeFactory.create()
        obj = ClassFactory.create(extensions=[extension])

        self.reducer.flatten_extension(obj, extension, self.nsmap)

        self.assertEqual(0, len(obj.extensions))
        mock_create_default_attribute.assert_called_once_with(obj, extension)

    @mock.patch.object(ClassReducer, "copy_attributes")
    @mock.patch.object(ClassReducer, "find_common_type")
    def test_flatten_extension_when_item_is_not_enumeration(
        self, mock_find_common_type, mock_copy_attributes
    ):
        common = ClassFactory.create(attrs=AttrFactory.list(2))
        mock_find_common_type.return_value = common

        extension = AttrTypeFactory.create()
        obj = ClassFactory.create(extensions=[extension], attrs=AttrFactory.list(2))

        self.reducer.flatten_extension(obj, extension, self.nsmap)

        mock_copy_attributes.assert_called_once_with(common, obj, extension)
        self.assertEqual(0, len(obj.extensions))

    @mock.patch.object(ClassReducer, "create_default_attribute")
    @mock.patch.object(ClassReducer, "copy_attributes")
    @mock.patch.object(ClassReducer, "find_common_type")
    def test_flatten_extension_when_item_is_common(
        self, mock_find_common_type, mock_copy_attributes, mock_create_default_attribute
    ):
        item = ClassFactory.create(attrs=AttrFactory.create(local_type=TagType.ELEMENT))
        mock_find_common_type.return_value = item

        extension = AttrTypeFactory.create()
        item.extensions.append(extension)

        self.reducer.flatten_extension(item, extension, self.nsmap)

        self.assertEqual(0, len(item.extensions))
        self.assertEqual(0, mock_copy_attributes.call_count)
        self.assertEqual(0, mock_create_default_attribute.call_count)

    def test_create_default_attribute(self):
        item = ClassFactory.create()
        extension = AttrTypeFactory.create()

        ClassReducer.create_default_attribute(item, extension)
        expected = AttrFactory.create(
            name="value",
            index=0,
            default=None,
            types=[extension],
            local_type=TagType.EXTENSION,
        )

        self.assertEqual(1, len(item.attrs))
        self.assertEqual(expected, item.attrs[0])

    def test_copy_attributes(self):
        common_b = ClassFactory.create(
            attrs=[
                AttrFactory.create(name="i", types=AttrTypeFactory.list(1, name="i")),
                AttrFactory.create(
                    name="j", types=AttrTypeFactory.list(1, name="other:j")
                ),
            ]
        )
        common_c = ClassFactory.create(
            attrs=[
                AttrFactory.create(name="x", types=AttrTypeFactory.list(1, name="x")),
                AttrFactory.create(
                    name="y", types=AttrTypeFactory.list(1, name="other:y")
                ),
            ]
        )
        ext_b = AttrTypeFactory.create(name="b", index=2)
        ext_c = AttrTypeFactory.create(name="common:c", index=66)

        obj = ClassFactory.create(
            name="foo",
            extensions=[ext_b, ext_c],
            attrs=[AttrFactory.create(name=x, index=ord(x)) for x in "ab"],
        )

        ClassReducer.copy_attributes(common_b, obj, ext_b)
        ClassReducer.copy_attributes(common_c, obj, ext_c)

        attrs = [
            ("i", "i"),
            ("j", "other:j"),
            ("x", "common:x"),
            ("y", "other:y"),
            ("a", "string"),
            ("b", "string"),
        ]
        self.assertEqual(
            attrs,
            [
                (attr.name, " ".join([attr_type.name for attr_type in attr.types]))
                for attr in obj.attrs
            ],
        )

    @mock.patch.object(ClassReducer, "find_common_type")
    def test_flatten_attribute_with_no_common_type(self, mock_find_common_type):
        mock_find_common_type.return_value = None

        parent = ClassFactory.create()
        type_a = AttrTypeFactory.create(name="a")
        attr = AttrFactory.create(name="a", types=[type_a], min_occurs=1)
        self.reducer.flatten_attribute(parent, attr, self.schema)

        self.assertEqual([type_a], attr.types)
        mock_find_common_type.assert_called_once_with("a", self.schema)

    @mock.patch.object(ClassReducer, "find_common_type")
    def test_flatten_attribute_with_enumeration_common_type(
        self, mock_find_common_type
    ):
        mock_find_common_type.return_value = ClassFactory.create(
            attrs=AttrFactory.list(1, local_type=TagType.ENUMERATION)
        )

        parent = ClassFactory.create()
        type_a = AttrTypeFactory.create(name="a")
        attr = AttrFactory.create(name="a", types=[type_a], min_occurs=1)
        self.reducer.flatten_attribute(parent, attr, self.schema)

        self.assertEqual([type_a], attr.types)
        mock_find_common_type.assert_called_once_with("a", self.schema)

    @mock.patch.object(ClassReducer, "copy_inner_classes")
    @mock.patch.object(ClassReducer, "find_common_type")
    def test_flatten_attribute(self, mock_find_common_type, mock_copy_inner_classes):
        type_a = AttrTypeFactory.create(name="a")
        type_b = AttrTypeFactory.create(name="b")
        common = ClassFactory.create(
            name="bar",
            attrs=AttrFactory.list(
                1, name="b", types=[type_b], required=True, min_occurs=2
            ),
        )

        mock_find_common_type.return_value = common

        parent = ClassFactory.create()
        attr = AttrFactory.create(name="a", types=[type_a], min_occurs=1)

        self.reducer.flatten_attribute(parent, attr, self.schema)

        self.assertEqual([type_b], attr.types)
        self.assertEqual({"required": True, "min_occurs": 1}, attr.restrictions)
        mock_find_common_type.assert_called_once_with(type_a.name, self.schema)
        mock_copy_inner_classes.assert_called_once_with(common, parent)

    @mock.patch("xsdata.reducer.logger.warning")
    @mock.patch.object(ClassReducer, "find_common_type")
    def test_flatten_attribute_with_common_multiple_attributes(
        self, mock_find_common_type, mock_logger_warning
    ):
        type_a = AttrTypeFactory.create(name="a")
        type_str = AttrType(name=DataType.STRING.code, native=True)
        common = ClassFactory.create(name="bar", attrs=AttrFactory.list(2))
        mock_find_common_type.return_value = common

        parent = ClassFactory.create()
        attr = AttrFactory.create(name="a", types=[type_a])

        self.reducer.flatten_attribute(parent, attr, self.schema)

        self.assertEqual([type_str], attr.types)
        mock_logger_warning.assert_called_once_with(
            "Missing type implementation: %s", common.type.__name__
        )

    @mock.patch.object(ClassReducer, "find_common_type")
    def test_flatten_enumeration_unions(self, mock_find_common_type):
        enum_a = ClassFactory.create(
            attrs=AttrFactory.list(2, local_type=TagType.ENUMERATION)
        )
        enum_b = ClassFactory.create(
            attrs=AttrFactory.list(3, local_type=TagType.ENUMERATION)
        )

        mock_find_common_type.return_value = enum_b

        obj = ClassFactory.create(
            attrs=[
                AttrFactory.create(
                    name="value",
                    types=[
                        AttrTypeFactory.create(name=enum_a.name, forward_ref=True),
                        AttrTypeFactory.create(name=enum_b.name),
                    ],
                )
            ],
            inner=[enum_a],
        )

        self.assertFalse(obj.is_enumeration)

        self.reducer.flatten_enumeration_unions(obj, self.schema)

        self.assertTrue(obj.is_enumeration)
        self.assertEqual(5, len(obj.attrs))
        self.assertEqual(
            ["attr_B", "attr_C", "attr_D", "attr_E", "attr_F"],
            [attr.name for attr in obj.attrs],
        )
