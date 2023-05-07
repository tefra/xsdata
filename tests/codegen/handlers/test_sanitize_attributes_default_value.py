from unittest import mock

from xsdata.codegen.container import ClassContainer
from xsdata.codegen.handlers import SanitizeAttributesDefaultValue
from xsdata.codegen.models import Restrictions
from xsdata.models.config import GeneratorConfig
from xsdata.models.enums import DataType
from xsdata.models.enums import Namespace
from xsdata.models.enums import Tag
from xsdata.utils.testing import AttrFactory
from xsdata.utils.testing import AttrTypeFactory
from xsdata.utils.testing import ClassFactory
from xsdata.utils.testing import FactoryTestCase


class SanitizeAttributesDefaultValueTests(FactoryTestCase):
    def setUp(self):
        super().setUp()

        container = ClassContainer(config=GeneratorConfig())
        self.processor = SanitizeAttributesDefaultValue(container=container)

    def test_process_attribute_with_enumeration(self):
        target = ClassFactory.create()
        attr = AttrFactory.enumeration()
        attr.restrictions.max_occurs = 2
        attr.fixed = True

        self.processor.process_attribute(target, attr)
        self.assertTrue(attr.fixed)

    @mock.patch.object(SanitizeAttributesDefaultValue, "process_attribute")
    def test_process_with_attr_choices(self, mock_process_attribute):
        choice = AttrFactory.create(
            name="attr_B_Or_attr_C",
            tag="Choice",
            index=0,
            types=[AttrTypeFactory.native(DataType.ANY_TYPE)],
            choices=[
                AttrFactory.reference("one"),
                AttrFactory.reference("two"),
                AttrFactory.reference("three"),
            ],
        )
        target = ClassFactory.create()
        target.attrs.append(choice)

        self.processor.process(target)

        self.assertEqual(4, mock_process_attribute.call_count)
        mock_process_attribute.assert_has_calls(
            [
                mock.call(target, target.attrs[0]),
                mock.call(target, target.attrs[0].choices[0]),
                mock.call(target, target.attrs[0].choices[1]),
                mock.call(target, target.attrs[0].choices[2]),
            ]
        )

    @mock.patch.object(SanitizeAttributesDefaultValue, "process_types")
    @mock.patch.object(SanitizeAttributesDefaultValue, "should_reset_default")
    @mock.patch.object(SanitizeAttributesDefaultValue, "should_reset_required")
    def test_process_attribute(
        self, mock_should_reset_required, mock_should_reset_default, mock_process_types
    ):
        target = ClassFactory.create()
        mock_should_reset_required.side_effect = [
            True,
            False,
            False,
            False,
            False,
            False,
        ]
        mock_should_reset_default.side_effect = [
            False,
            True,
            False,
            False,
            False,
            False,
        ]

        attr = AttrFactory.element(restrictions=Restrictions(min_occurs=2))
        self.processor.process_attribute(target, attr)
        self.assertEqual(0, attr.restrictions.min_occurs)

        attr = AttrFactory.element(fixed=True, default="abc")
        self.processor.process_attribute(target, attr)
        self.assertIsNone(attr.default)
        self.assertFalse(attr.fixed)

        attr = AttrFactory.element(default="abc")
        self.processor.process_attribute(target, attr)
        mock_process_types.assert_called_once_with(target, attr)

        attr = AttrFactory.extension()
        self.processor.process_attribute(target, attr)
        self.assertEqual("", attr.default)

        attr = AttrFactory.extension(default="abc")
        self.processor.process_attribute(target, attr)
        self.assertEqual("abc", attr.default)

        attr = AttrFactory.extension(types=[AttrTypeFactory.native(DataType.INTEGER)])
        self.processor.process_attribute(target, attr)
        self.assertIsNone(attr.default)

    def test_should_reset_required(self):
        attr = AttrFactory.create()
        self.assertFalse(self.processor.should_reset_required(attr))

        attr = AttrFactory.any(restrictions=Restrictions(max_occurs=2))
        self.assertFalse(self.processor.should_reset_required(attr))

        attr = AttrFactory.any(default="abc")
        self.assertFalse(self.processor.should_reset_required(attr))

        attr = AttrFactory.any()
        self.assertTrue(self.processor.should_reset_required(attr))

    def test_should_reset_default(self):
        attr = AttrFactory.create()
        self.assertFalse(self.processor.should_reset_default(attr))

        attr = AttrFactory.create(name="type", namespace=Namespace.XSI.uri)
        self.assertFalse(self.processor.should_reset_default(attr))

        attr.default = "abc"
        self.assertTrue(self.processor.should_reset_default(attr))

        attr = AttrFactory.element(
            default="abc", restrictions=Restrictions(min_occurs=1)
        )
        self.assertFalse(self.processor.should_reset_default(attr))
        attr.restrictions.max_occurs = 2
        self.assertTrue(self.processor.should_reset_default(attr))

        attr = AttrFactory.attribute(
            default="abc", restrictions=Restrictions(min_occurs=0)
        )
        self.assertFalse(self.processor.should_reset_default(attr))

        attr.tag = Tag.ELEMENT
        self.assertTrue(self.processor.should_reset_default(attr))

    @mock.patch(
        "xsdata.codegen.handlers.sanitize_attributes_default_value.logger.warning"
    )
    @mock.patch.object(SanitizeAttributesDefaultValue, "reset_attribute_types")
    @mock.patch.object(SanitizeAttributesDefaultValue, "is_valid_native_value")
    @mock.patch.object(SanitizeAttributesDefaultValue, "is_valid_external_value")
    def test_process_types(
        self,
        mock_is_valid_external_value,
        mock_is_valid_native_value,
        mock_reset_attribute_types,
        mock_warning,
    ):
        mock_is_valid_external_value.side_effect = [True, False, False]
        mock_is_valid_native_value.side_effect = [True, False]

        target = ClassFactory.create()
        attr = AttrFactory.native(DataType.INT)
        attr.restrictions.format = "foo"

        self.processor.process_types(target, attr)
        self.assertEqual(0, mock_is_valid_native_value.call_count)

        self.processor.process_types(target, attr)
        self.assertEqual(0, mock_reset_attribute_types.call_count)

        self.processor.process_types(target, attr)
        self.assertEqual(1, mock_reset_attribute_types.call_count)
        mock_warning.assert_called_once_with(
            "Failed to match %s.%s default value `%s` to one of %s",
            target.name,
            attr.local_name,
            attr.default,
            [str(DataType.INT)],
        )

    def test_is_valid_native_value(self):
        target = ClassFactory.create()

        # Not native types
        attr = AttrFactory.create(types=[AttrTypeFactory.create("foo")], default="abc")
        self.assertFalse(self.processor.is_valid_native_value(target, attr))

        # Successful
        attr = AttrFactory.native(DataType.INT, default="2")
        self.assertTrue(self.processor.is_valid_native_value(target, attr))

        # Failed: mixed types
        attr = AttrFactory.native(
            DataType.INT, default="2 a 3", restrictions=Restrictions(tokens=True)
        )
        self.assertFalse(self.processor.is_valid_native_value(target, attr))

        # Successful: mixed types
        attr.types.append(AttrTypeFactory.native(DataType.STRING))
        self.assertTrue(self.processor.is_valid_native_value(target, attr))

        # Successful: not strict
        attr = AttrFactory.native(DataType.FLOAT, default="2.00")
        self.assertTrue(self.processor.is_valid_native_value(target, attr))

        # Failed: strict
        attr.fixed = True
        self.assertFalse(self.processor.is_valid_native_value(target, attr))

        # Successful qname
        attr = AttrFactory.enumeration()
        attr.types = [AttrTypeFactory.native(DataType.QNAME)]
        attr.restrictions.tokens = True
        attr.fixed = True
        attr.default = "a:b b:a"
        target.ns_map["a"] = "b"
        target.ns_map["b"] = "a"
        self.assertTrue(self.processor.is_valid_native_value(target, attr))

        # Filed qname: missing prefix / Bonus tokens downgrade
        attr.default = "nope:a"
        self.assertFalse(self.processor.is_valid_native_value(target, attr))
        self.assertFalse(attr.restrictions.tokens)

    @mock.patch.object(SanitizeAttributesDefaultValue, "is_valid_enum_type")
    @mock.patch.object(SanitizeAttributesDefaultValue, "is_valid_inner_type")
    def test_is_valid_external_value(
        self, mock_is_valid_inner_type, mock_is_valid_enum_type
    ):
        mock_is_valid_inner_type.side_effect = [False, False, False, True]
        mock_is_valid_enum_type.side_effect = [False, False, True]

        attr = AttrFactory.create()
        attr.types = [
            AttrTypeFactory.create("foo"),
            AttrTypeFactory.create("bar"),
        ]
        target = ClassFactory.create()
        foo = ClassFactory.create(qname="foo")
        bar = ClassFactory.create(qname="bar")
        self.processor.container.add(foo)
        self.processor.container.add(bar)

        self.assertFalse(self.processor.is_valid_external_value(target, attr))
        self.assertTrue(self.processor.is_valid_external_value(target, attr))
        self.assertTrue(self.processor.is_valid_external_value(target, attr))

    def test_is_valid_inner_type(self):
        source = ClassFactory.elements(2)

        attr_type = AttrTypeFactory.create()
        attr = AttrFactory.create()

        self.assertFalse(self.processor.is_valid_inner_type(source, attr, attr_type))

        attr_type.forward = True
        self.assertFalse(self.processor.is_valid_inner_type(source, attr, attr_type))

        source.attrs.append(AttrFactory.extension())
        attr.default = "abc"
        attr.fixed = True
        self.assertTrue(self.processor.is_valid_inner_type(source, attr, attr_type))

        self.assertFalse(attr.fixed)
        self.assertIsNone(attr.default)
        self.assertTrue(source.attrs[2].fixed)
        self.assertEqual("abc", source.attrs[2].default)

    def test_is_valid_enum_type(self):
        enumeration = ClassFactory.enumeration(2, qname="{a}root")
        enumeration.attrs[0].default = "1"
        enumeration.attrs[0].name = "one"
        enumeration.attrs[1].default = "2"
        enumeration.attrs[1].name = "two"

        attr = AttrFactory.create(default="1")
        self.assertTrue(self.processor.is_valid_enum_type(enumeration, attr))
        self.assertEqual("@enum@{a}root::one", attr.default)

        attr = AttrFactory.create(default="  1  2")
        self.assertTrue(self.processor.is_valid_enum_type(enumeration, attr))
        self.assertEqual("@enum@{a}root::one@two", attr.default)

        attr = AttrFactory.create(default="3")
        self.assertFalse(self.processor.is_valid_enum_type(enumeration, attr))
        self.assertEqual("3", attr.default)

    def test_find_type(self):
        target = ClassFactory.create()
        attr_type = AttrTypeFactory.create("foo")
        foo = ClassFactory.create(qname="foo")
        self.processor.container.add(foo)

        self.assertIs(foo, self.processor.find_type(target, attr_type))

        attr_type = AttrTypeFactory.create("bar", forward=True)
        bar = ClassFactory.create(qname="bar")
        target.inner.append(bar)
        self.assertIs(bar, self.processor.find_type(target, attr_type))

    def test_reset_attribute_types(self):
        attr = AttrFactory.create(
            types=[
                AttrTypeFactory.native(DataType.INT),
                AttrTypeFactory.native(DataType.FLOAT),
            ]
        )
        attr.restrictions.format = "foo"

        self.processor.reset_attribute_types(attr)
        self.assertIsNone(attr.restrictions.format)
        self.assertEqual(1, len(attr.types))
        self.assertEqual(str(DataType.STRING), attr.types[0].qname)
        self.assertTrue(attr.types[0].native)
