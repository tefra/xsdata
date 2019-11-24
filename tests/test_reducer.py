from unittest import mock

from tests.factories import AttrFactory, ClassFactory, FactoryTestCase
from xsdata.models import elements
from xsdata.models.elements import (
    Attribute,
    ComplexType,
    Element,
    Schema,
    SimpleType,
)
from xsdata.models.enums import TagType, XSDType
from xsdata.reducer import ClassReducer
from xsdata.utils.text import capitalize


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

    @mock.patch.object(ClassReducer, "flatten_class")
    @mock.patch.object(ClassReducer, "add_common_type")
    def test_process(self, mock_add_common_type, mock_flatten_class):
        classes = ClassFactory.list(3, type=Element)
        classes.extend(ClassFactory.list(3, type=SimpleType))

        result = ClassReducer().process(self.schema, classes.copy())
        self.assertEqual(classes[:3], result)

        common_types = reversed(classes[3:])
        mock_add_common_type.assert_has_calls(
            [mock.call(obj, self.target_namespace) for obj in common_types]
        )
        mock_flatten_class.assert_has_calls(
            [mock.call(obj, self.nsmap) for obj in classes], any_order=True
        )

    def test_is_common(self):
        for tag in TagType:
            cl = getattr(elements, capitalize(tag.value))
            obj = ClassFactory.create(name="foo", type=cl)
            if obj.type in [Attribute, Element, ComplexType]:
                self.assertFalse(
                    ClassReducer.is_common(obj), f"Is common: {cl}"
                )
            else:
                self.assertTrue(
                    ClassReducer.is_common(obj), f"Is not common: {cl}"
                )

        obj = ClassFactory.create(
            type=SimpleType,
            attrs=AttrFactory.list(1, local_type=TagType.ENUMERATION.cname),
        )
        self.assertFalse(ClassReducer.is_common(obj))

    def test_add_common_type(self):
        reducer = ClassReducer()
        obj = ClassFactory.create(name="foo", type=SimpleType)
        reducer.add_common_type(obj, "common")
        reducer.add_common_type(obj, None)
        expected = {"{common}foo": obj, "foo": obj}
        self.assertEqual(expected, reducer.common_types)

    def test_find_common_type(self):
        reducer = ClassReducer()
        obj = ClassFactory.create(name="foo", type=SimpleType)
        reducer.add_common_type(obj, self.nsmap["common"])
        reducer.add_common_type(obj, self.nsmap[None])

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

        obj = ClassFactory.create(
            name="foo",
            extensions=["a", "b", "common:c"],
            attrs=[AttrFactory.create(name=x) for x in "ab"],
        )

        mock_find_common_type.side_effect = [None, common_b, common_c]

        reducer = ClassReducer()
        reducer.flatten_extension(obj, "a", self.nsmap)
        reducer.flatten_extension(obj, "b", self.nsmap)
        reducer.flatten_extension(obj, "common:c", self.nsmap)
        attrs = [
            ("x", "common:x"),
            ("y", "other:y"),
            ("i", "i"),
            ("j", "other:j"),
            ("a", "xs:string"),
            ("b", "xs:string"),
        ]

        self.assertEqual(["a"], obj.extensions)
        self.assertEqual(attrs, [(attr.name, attr.type) for attr in obj.attrs])

        mock_find_common_type.assert_has_calls(
            [
                mock.call("a", self.nsmap),
                mock.call("b", self.nsmap),
                mock.call("common:c", self.nsmap),
            ]
        )

    @mock.patch.object(ClassReducer, "find_common_type")
    def test_flatten_attribute(self, mock_find_common_type):
        common = ClassFactory.create(
            name="bar",
            attrs=[
                AttrFactory.create(
                    name="b", type="b", restrictions={"required": True},
                )
            ],
        )
        mock_find_common_type.side_effect = [None, common]

        obj = AttrFactory.create(
            name="a", type="a", restrictions={"min_occurs": 1}
        )

        reducer = ClassReducer()
        reducer.flatten_attribute(obj, self.nsmap)
        reducer.flatten_attribute(obj, self.nsmap)

        self.assertEqual("b", obj.type)
        self.assertEqual({"required": True, "min_occurs": 1}, obj.restrictions)
        mock_find_common_type.assert_has_calls(
            [mock.call("a", self.nsmap), mock.call("a", self.nsmap)]
        )

    @mock.patch("xsdata.reducer.logger.debug")
    @mock.patch.object(ClassReducer, "find_common_type")
    def test_flatten_attribute_with_common_attrs_not_equal_one(
        self, mock_find_common_type, mock_logger_debug
    ):
        common = ClassFactory.create(
            name="bar", attrs=[AttrFactory.create(name=x) for x in "xy"],
        )
        mock_find_common_type.return_value = common

        obj = AttrFactory.create(name="a", type="a")

        reducer = ClassReducer()
        reducer.flatten_attribute(obj, self.nsmap)

        self.assertEqual(XSDType.STRING.code, obj.type)
        mock_logger_debug.assert_called_once_with(
            f"Missing type implementation: {common.type.__name__}"
        )
