from unittest import mock

from tests.factories import (
    AttrFactory,
    ClassFactory,
    ExtensionFactory,
    FactoryTestCase,
)
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
        all = classes + common

        result = ClassReducer().process(self.schema, all)

        self.assertEqual(enums + classes, result)

        mock_add_common_types.assert_called_once_with(
            common, self.target_namespace
        )
        mock_flatten_classes.assert_has_calls(
            [mock.call(common, self.nsmap), mock.call(classes, self.nsmap)]
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

        self.assertEqual(obj, reducer.find_common_type("foo", self.nsmap))
        self.assertEqual(
            obj, reducer.find_common_type("common:foo", self.nsmap)
        )
        self.assertIsNone(reducer.find_common_type("bar", self.nsmap))

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
    def test_flatten_extension(self, mock_find_common_type):
        common_b = ClassFactory.create(
            name="b",
            attrs=[
                AttrFactory.create(name="i", type="i"),
                AttrFactory.create(name="j", type="other:j"),
            ],
        )
        common_c = ClassFactory.create(
            name="c",
            attrs=[
                AttrFactory.create(name="x", type="x"),
                AttrFactory.create(name="y", type="other:y"),
            ],
        )
        ext_a = ExtensionFactory.create(name="a", index=1)
        ext_b = ExtensionFactory.create(name="b", index=2)
        ext_c = ExtensionFactory.create(name="common:c", index=66)

        obj = ClassFactory.create(
            name="foo",
            extensions=[ext_a, ext_b, ext_c],
            attrs=[AttrFactory.create(name=x, index=ord(x)) for x in "ab"],
        )

        mock_find_common_type.side_effect = [None, common_b, common_c]

        reducer = ClassReducer()
        for extension in list(obj.extensions):
            reducer.flatten_extension(obj, extension, self.nsmap)

        attrs = [
            ("i", "i"),
            ("j", "other:j"),
            ("x", "common:x"),
            ("y", "other:y"),
            ("a", "xs:string"),
            ("b", "xs:string"),
        ]

        self.assertEqual([ext_a], obj.extensions)
        self.assertEqual(attrs, [(attr.name, attr.type) for attr in obj.attrs])

        mock_find_common_type.assert_has_calls(
            [
                mock.call("a", self.nsmap),
                mock.call("b", self.nsmap),
                mock.call("common:c", self.nsmap),
            ]
        )

    @mock.patch.object(ClassReducer, "find_common_type")
    def test_flatten_attribute_with_no_common_type(
        self, mock_find_common_type
    ):
        mock_find_common_type.return_value = None

        obj = AttrFactory.create(name="a", type="a", min_occurs=1)
        reducer = ClassReducer()
        reducer.flatten_attribute(obj, self.nsmap)

        self.assertEqual("a", obj.type)
        mock_find_common_type.assert_called_once_with("a", self.nsmap)

    @mock.patch.object(ClassReducer, "find_common_type")
    def test_flatten_attribute_with_enumeration_common_type(
        self, mock_find_common_type
    ):
        mock_find_common_type.return_value = ClassFactory.create(
            attrs=AttrFactory.list(1, local_type=TagType.ENUMERATION.cname)
        )

        obj = AttrFactory.create(name="a", type="a", min_occurs=1)
        reducer = ClassReducer()
        reducer.flatten_attribute(obj, self.nsmap)

        self.assertEqual("a", obj.type)
        mock_find_common_type.assert_called_once_with("a", self.nsmap)

    @mock.patch.object(ClassReducer, "find_common_type")
    def test_flatten_attribute(self, mock_find_common_type):
        mock_find_common_type.return_value = ClassFactory.create(
            name="bar",
            attrs=AttrFactory.list(1, name="b", type="b", required=True),
        )

        obj = AttrFactory.create(name="a", type="a", min_occurs=1)

        reducer = ClassReducer()
        reducer.flatten_attribute(obj, self.nsmap)

        self.assertEqual("b", obj.type)
        self.assertEqual({"required": True, "min_occurs": 1}, obj.restrictions)
        mock_find_common_type.assert_called_once_with("a", self.nsmap)

    @mock.patch("xsdata.reducer.logger.warning")
    @mock.patch.object(ClassReducer, "find_common_type")
    def test_flatten_attribute_with_common_multiple_attributes(
        self, mock_find_common_type, mock_logger_debug
    ):
        common = ClassFactory.create(name="bar", attrs=AttrFactory.list(2))
        mock_find_common_type.return_value = common

        obj = AttrFactory.create(name="a", type="a")

        reducer = ClassReducer()
        reducer.flatten_attribute(obj, self.nsmap)

        self.assertEqual(XSDType.STRING.code, obj.type)
        mock_logger_debug.assert_called_once_with(
            f"Missing type implementation: {common.type.__name__}"
        )
