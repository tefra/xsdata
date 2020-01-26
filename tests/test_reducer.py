from unittest import mock

from tests.factories import (
    AttrFactory,
    AttrTypeFactory,
    ClassFactory,
    ExtensionFactory,
    FactoryTestCase,
)
from xsdata.models.codegen import AttrType
from xsdata.models.elements import (
    ComplexType,
    Element,
    Restriction,
    Schema,
    SimpleType,
)
from xsdata.models.enums import TagType, XSDType
from xsdata.reducer import ClassReducer


class ClassReducerTests(FactoryTestCase):
    def setUp(self) -> None:
        super(ClassReducerTests, self).setUp()
        self.target_namespace = "http://namespace/target"
        self.nsmap = {
            None: "http://namespace/target",
            "common": "http://namespace/common",
        }
        self.schema = Schema.create(
            target_namespace=self.target_namespace, nsmap=self.nsmap
        )

    @mock.patch.object(ClassReducer, "flatten_classes")
    @mock.patch.object(ClassReducer, "add_common_types")
    def test_process(self, mock_add_common_types, mock_flatten_classes):
        classes = ClassFactory.list(3, type=Element)
        simplies = ClassFactory.list(2, type=SimpleType)
        enums = ClassFactory.list(
            2,
            type=Restriction,
            attrs=AttrFactory.list(2, local_type=TagType.ENUMERATION.cname),
        )
        abstracts = ClassFactory.list(2, is_abstract=True, type=ComplexType)

        common = simplies + abstracts + enums
        all_classes = classes + common

        result = ClassReducer().process(self.schema, all_classes)

        self.assertEqual(enums + classes, result)

        mock_add_common_types.assert_called_once_with(
            common, self.target_namespace
        )
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
        reducer = ClassReducer()
        classes = ClassFactory.list(2)
        reducer.add_common_types(classes, self.target_namespace)
        expected = {
            f"{{{self.target_namespace}}}{obj.name}": obj for obj in classes
        }

        self.assertEqual(expected, reducer.common_types)

    def test_find_common_type(self):
        reducer = ClassReducer()
        obj = ClassFactory.create(name="foo", type=SimpleType)
        reducer.common_types = {
            f"{{http://namespace/target}}{obj.name}": obj,
            f"{{http://namespace/common}}{obj.name}": obj,
        }

        self.assertEqual(obj, reducer.find_common_type("foo", self.schema))
        self.assertEqual(
            obj, reducer.find_common_type("common:foo", self.schema)
        )
        self.assertIsNone(reducer.find_common_type("bar", self.schema))

    @mock.patch.object(ClassReducer, "flatten_attribute")
    @mock.patch.object(ClassReducer, "flatten_extension")
    def test_flatten_class(
        self, mock_flatten_extension, mock_flatten_attribute
    ):
        reducer = ClassReducer()
        obj = ClassFactory.create(
            name="a",
            type="a",
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

        reducer.flatten_class(obj, self.nsmap)
        mock_flatten_extension.assert_has_calls(
            [
                mock.call(obj, "b", self.nsmap),
                mock.call(obj, "c", self.nsmap),
                mock.call(obj.inner[0], "g", self.nsmap),
                mock.call(obj.inner[0], "h", self.nsmap),
            ]
        )
        mock_flatten_attribute.assert_has_calls(
            [
                mock.call(obj.attrs[0], self.nsmap),
                mock.call(obj.attrs[1], self.nsmap),
                mock.call(obj.inner[0].attrs[0], self.nsmap),
                mock.call(obj.inner[0].attrs[1], self.nsmap),
            ]
        )

    @mock.patch.object(ClassReducer, "find_common_type")
    def test_flatten_extension_when_common_not_found(
        self, mock_find_common_type
    ):
        mock_find_common_type.return_value = None

        reducer = ClassReducer()
        extension = ExtensionFactory.create()
        obj = ClassFactory.create(extensions=[extension])
        reducer.flatten_extension(obj, extension, self.nsmap)

        self.assertEqual(1, len(obj.extensions))
        mock_find_common_type.assert_called_once_with(
            extension.name, self.nsmap
        )

    @mock.patch.object(ClassReducer, "find_common_type")
    def test_flatten_extension_with_enumeration_when_extension_is_restriction(
        self, mock_find_common_type
    ):
        mock_find_common_type.return_value = ClassFactory.create(
            attrs=AttrFactory.list(2, local_type=TagType.ENUMERATION.cname)
        )

        reducer = ClassReducer()
        extension = ExtensionFactory.create(type=TagType.EXTENSION.cname)
        obj = ClassFactory.create(
            extensions=[extension],
            attrs=AttrFactory.list(2, local_type=TagType.ENUMERATION.cname),
        )

        reducer.flatten_extension(obj, extension, self.nsmap)

        self.assertEqual(0, len(obj.extensions))

    @mock.patch.object(ClassReducer, "copy_attributes")
    @mock.patch.object(ClassReducer, "find_common_type")
    def test_flatten_extension_copy_attributes(
        self, mock_find_common_type, mock_copy_attributes
    ):
        common = ClassFactory.create(attrs=AttrFactory.list(2))
        mock_find_common_type.return_value = common

        reducer = ClassReducer()
        extension = ExtensionFactory.create(type=TagType.UNION.cname)
        obj = ClassFactory.create(
            extensions=[extension], attrs=AttrFactory.list(2)
        )

        reducer.flatten_extension(obj, extension, self.nsmap)

        mock_copy_attributes.assert_called_once_with(common, obj, extension)
        self.assertEqual(0, len(obj.extensions))

    def test_copy_attributes(self):
        common_b = ClassFactory.create(
            attrs=[
                AttrFactory.create(
                    name="i", types=AttrTypeFactory.list(1, name="i")
                ),
                AttrFactory.create(
                    name="j", types=AttrTypeFactory.list(1, name="other:j")
                ),
            ],
        )
        common_c = ClassFactory.create(
            attrs=[
                AttrFactory.create(
                    name="x", types=AttrTypeFactory.list(1, name="x")
                ),
                AttrFactory.create(
                    name="y", types=AttrTypeFactory.list(1, name="other:y")
                ),
            ],
        )
        ext_b = ExtensionFactory.create(name="b", index=2)
        ext_c = ExtensionFactory.create(name="common:c", index=66)

        obj = ClassFactory.create(
            name="foo",
            extensions=[ext_b, ext_c],
            attrs=[AttrFactory.create(name=x, index=ord(x)) for x in "ab"],
        )

        reducer = ClassReducer()
        reducer.copy_attributes(common_b, obj, ext_b)
        reducer.copy_attributes(common_c, obj, ext_c)

        attrs = [
            ("i", "i"),
            ("j", "other:j"),
            ("x", "common:x"),
            ("y", "other:y"),
            ("a", "xs:string"),
            ("b", "xs:string"),
        ]
        self.assertEqual(
            attrs,
            [
                (
                    attr.name,
                    " ".join([attr_type.name for attr_type in attr.types]),
                )
                for attr in obj.attrs
            ],
        )

    @mock.patch.object(ClassReducer, "find_common_type")
    def test_flatten_attribute_with_no_common_type(
        self, mock_find_common_type
    ):
        mock_find_common_type.return_value = None

        type_a = AttrTypeFactory.create(name="a")
        obj = AttrFactory.create(name="a", types=[type_a], min_occurs=1)
        reducer = ClassReducer()
        reducer.flatten_attribute(obj, self.nsmap)

        self.assertEqual([type_a], obj.types)
        mock_find_common_type.assert_called_once_with("a", self.nsmap)

    @mock.patch.object(ClassReducer, "find_common_type")
    def test_flatten_attribute_with_enumeration_common_type(
        self, mock_find_common_type
    ):
        mock_find_common_type.return_value = ClassFactory.create(
            attrs=AttrFactory.list(1, local_type=TagType.ENUMERATION.cname)
        )

        type_a = AttrTypeFactory.create(name="a")
        obj = AttrFactory.create(name="a", types=[type_a], min_occurs=1)
        reducer = ClassReducer()
        reducer.flatten_attribute(obj, self.nsmap)

        self.assertEqual([type_a], obj.types)
        mock_find_common_type.assert_called_once_with("a", self.nsmap)

    @mock.patch.object(ClassReducer, "find_common_type")
    def test_flatten_attribute(self, mock_find_common_type):
        type_a = AttrTypeFactory.create(name="a")
        type_b = AttrTypeFactory.create(name="b")

        mock_find_common_type.return_value = ClassFactory.create(
            name="bar",
            attrs=AttrFactory.list(
                1, name="b", types=[type_b], required=True, min_occurs=2
            ),
        )

        obj = AttrFactory.create(name="a", types=[type_a], min_occurs=1)

        reducer = ClassReducer()
        reducer.flatten_attribute(obj, self.nsmap)

        self.assertEqual([type_b], obj.types)
        self.assertEqual({"required": True, "min_occurs": 1}, obj.restrictions)
        mock_find_common_type.assert_called_once_with(type_a.name, self.nsmap)

    @mock.patch("xsdata.reducer.logger.warning")
    @mock.patch.object(ClassReducer, "find_common_type")
    def test_flatten_attribute_with_common_multiple_attributes(
        self, mock_find_common_type, mock_logger_debug
    ):
        type_a = AttrTypeFactory.create(name="a")
        type_str = AttrType(name=XSDType.STRING.code)
        common = ClassFactory.create(name="bar", attrs=AttrFactory.list(2))
        mock_find_common_type.return_value = common

        obj = AttrFactory.create(name="a", types=[type_a])

        reducer = ClassReducer()
        reducer.flatten_attribute(obj, self.nsmap)

        self.assertEqual([type_str], obj.types)
        mock_logger_debug.assert_called_once_with(
            "Missing type implementation: %s", common.type.__name__
        )
