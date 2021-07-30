from unittest import mock

from xsdata.codegen.container import ClassContainer
from xsdata.codegen.handlers import AttributeDefaultValueHandler
from xsdata.codegen.models import Restrictions
from xsdata.models.config import GeneratorConfig
from xsdata.models.enums import DataType
from xsdata.models.enums import Namespace
from xsdata.models.enums import Tag
from xsdata.utils.testing import AttrFactory
from xsdata.utils.testing import AttrTypeFactory
from xsdata.utils.testing import ClassFactory
from xsdata.utils.testing import FactoryTestCase


class AttributeDefaultValueHandlerTests(FactoryTestCase):
    def setUp(self):
        super().setUp()

        container = ClassContainer(config=GeneratorConfig())
        self.processor = AttributeDefaultValueHandler(container=container)

    def test_process_attribute_with_enumeration(self):
        target = ClassFactory.create()
        attr = AttrFactory.enumeration()
        attr.restrictions.max_occurs = 2
        attr.fixed = True

        self.processor.process_attribute(target, attr)
        self.assertTrue(attr.fixed)

    @mock.patch.object(AttributeDefaultValueHandler, "process_attribute")
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

    def test_process_attribute_with_choice_field(self):
        target = ClassFactory.create()
        attr = AttrFactory.element(fixed=True, default=2)
        attr.restrictions.min_occurs = 1
        attr.restrictions.choice = "a"
        self.processor.process_attribute(target, attr)

        self.assertEqual(2, attr.default)
        self.assertTrue(attr.fixed)

        attr.restrictions.min_occurs = 0
        self.processor.process_attribute(target, attr)
        self.assertFalse(attr.fixed)
        self.assertIsNone(attr.default)

    def test_process_attribute_with_sequential_field(self):
        target = ClassFactory.create()
        attr = AttrFactory.element(fixed=True, default=2)
        attr.restrictions.min_occurs = 1
        attr.restrictions.sequential = True
        self.processor.process_attribute(target, attr)

        self.assertEqual(2, attr.default)
        self.assertTrue(attr.fixed)

        attr.restrictions.min_occurs = 0
        self.processor.process_attribute(target, attr)
        self.assertFalse(attr.fixed)
        self.assertIsNone(attr.default)

    def test_process_attribute_with_list_field(self):
        target = ClassFactory.create()
        attr = AttrFactory.element(fixed=True, default=2)
        attr.restrictions.max_occurs = 5
        self.processor.process_attribute(target, attr)
        self.assertFalse(attr.fixed)
        self.assertIsNone(attr.default)

    def test_process_attribute_with_xsi_type(self):
        target = ClassFactory.create()
        attr = AttrFactory.attribute(
            fixed=True,
            default="xs:int",
            name="type",
            namespace=Namespace.XSI.uri,
            restrictions=Restrictions(min_occurs=1, max_occurs=1),
        )
        self.processor.process_attribute(target, attr)
        self.assertFalse(attr.fixed)
        self.assertIsNone(attr.default)
        self.assertEqual(0, attr.restrictions.min_occurs)

    def test_process_attribute_with_valid_case(self):
        target = ClassFactory.create()
        attr = AttrFactory.create(fixed=True, default=2)
        self.processor.process_attribute(target, attr)
        self.assertTrue(attr.fixed)
        self.assertEqual(2, attr.default)

    def test_process_attribute_with_text_attr(self):
        target = ClassFactory.create()

        attr = AttrFactory.native(DataType.INT, tag=Tag.EXTENSION)
        self.processor.process_attribute(target, attr)
        self.assertIsNone(attr.default)

        attr = AttrFactory.native(DataType.STRING, tag=Tag.EXTENSION)
        self.processor.process_attribute(target, attr)
        self.assertEqual("", attr.default)

    @mock.patch("xsdata.codegen.handlers.attribute_default_value.logger.warning")
    @mock.patch.object(AttributeDefaultValueHandler, "find_enum")
    def test_process_attribute_enum(self, mock_find_enum, mock_logger_warning):
        enum_one = ClassFactory.enumeration(1, qname="{a}root")
        enum_one.attrs[0].default = "1"
        enum_one.attrs[0].name = "one"
        enum_two = ClassFactory.enumeration(1, qname="inner")
        enum_two.attrs[0].default = "2"
        enum_two.attrs[0].name = "two"
        enum_three = ClassFactory.enumeration(2, qname="missing_member")
        enum_three.attrs[0].default = "4"
        enum_three.attrs[0].name = "four"
        enum_three.attrs[1].default = "5"
        enum_three.attrs[1].name = "five"

        mock_find_enum.side_effect = [
            None,
            enum_one,
            None,
            enum_two,
            enum_three,
            enum_three,
        ]

        target = ClassFactory.create(
            qname="target",
            attrs=[
                AttrFactory.create(
                    types=[
                        AttrTypeFactory.create(),
                        AttrTypeFactory.create(qname="foo"),
                    ],
                    default="1",
                ),
                AttrFactory.create(
                    types=[
                        AttrTypeFactory.create(),
                        AttrTypeFactory.create(qname="bar", forward=True),
                    ],
                    default="2",
                ),
                AttrFactory.create(default="3"),
                AttrFactory.create(default=" 4  5"),
            ],
        )

        actual = []
        for attr in target.attrs:
            self.processor.process_attribute(target, attr)
            actual.append(attr.default)

        self.assertEqual(
            [
                "@enum@{a}root::one",
                "@enum@inner::two",
                None,
                "@enum@missing_member::four@five",
            ],
            actual,
        )
        mock_logger_warning.assert_called_once_with(
            "No enumeration member matched %s.%s default value `%s`",
            target.name,
            target.attrs[2].local_name,
            "3",
        )

    def test_find_enum(self):
        native_type = AttrTypeFactory.create()
        matching_external = AttrTypeFactory.create("foo")
        missing_external = AttrTypeFactory.create("bar")
        enumeration = ClassFactory.enumeration(1, qname="foo")
        inner = ClassFactory.enumeration(1, qname="foobar")

        target = ClassFactory.create(
            attrs=[
                AttrFactory.create(
                    types=[
                        native_type,
                        matching_external,
                        missing_external,
                    ]
                )
            ],
            inner=[inner],
        )
        self.processor.container.extend([target, enumeration])

        actual = self.processor.find_enum(native_type)
        self.assertIsNone(actual)

        actual = self.processor.find_enum(matching_external)
        self.assertEqual(enumeration, actual)

        actual = self.processor.find_enum(missing_external)
        self.assertIsNone(actual)
