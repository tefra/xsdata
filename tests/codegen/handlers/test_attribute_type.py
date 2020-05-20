from unittest import mock

from lxml.etree import QName

from tests.factories import AttrFactory
from tests.factories import AttrTypeFactory
from tests.factories import ClassFactory
from tests.factories import ExtensionFactory
from tests.factories import FactoryTestCase
from xsdata.codegen.container import ClassContainer
from xsdata.codegen.handlers import AttributeTypeClassHandler
from xsdata.codegen.handlers.attribute_type import simple_cond
from xsdata.models.codegen import Class
from xsdata.models.codegen import Restrictions
from xsdata.models.enums import DataType
from xsdata.utils.classes import ClassUtils


class AttributeTypeHandlerTests(FactoryTestCase):
    def setUp(self):
        super().setUp()

        container = ClassContainer()
        self.processor = AttributeTypeClassHandler(container=container)

    def test_process_attribute_when_type_is_native(self):
        xs_bool = AttrTypeFactory.xs_bool()
        xs_decimal = AttrTypeFactory.xs_decimal()
        attr = AttrFactory.create(types=[xs_bool, xs_decimal])
        target = ClassFactory.create()
        self.processor.process_attribute(target, attr)

        self.assertEqual([xs_bool, xs_decimal], attr.types)

        self.processor.process_attribute(target, attr)
        self.assertEqual([xs_bool, xs_decimal], attr.types)

    def test_process_attribute_with_restriction_pattern(self):
        xs_bool = AttrTypeFactory.xs_bool()
        xs_decimal = AttrTypeFactory.xs_decimal()
        attr = AttrFactory.create(types=[xs_bool, xs_decimal])
        target = ClassFactory.create()
        self.processor.process_attribute(target, attr)

        self.assertEqual([xs_bool, xs_decimal], attr.types)

        attr.restrictions.pattern = r"[0-1]"
        self.processor.process_attribute(target, attr)
        self.assertEqual([AttrTypeFactory.xs_string()], attr.types)

    @mock.patch.object(AttributeTypeClassHandler, "process_attribute_type")
    def test_process_attribute_ignores_forward_types(self, mock_flatten_attribute_type):
        parent = ClassFactory.create()
        type_a = AttrTypeFactory.create()
        type_b = AttrTypeFactory.create(forward=True)

        attr = AttrFactory.create(name="a", types=[type_a, type_b])
        self.processor.process_attribute(parent, attr)

        mock_flatten_attribute_type.assert_called_once_with(parent, attr, type_a)

    def test_process_attribute_filters_duplicate_types(self):
        target = ClassFactory.create(
            attrs=[
                AttrFactory.create(
                    types=[
                        AttrTypeFactory.xs_string(),
                        AttrTypeFactory.xs_string(),
                        AttrTypeFactory.xs_bool(),
                    ]
                )
            ]
        )
        self.processor.process_attribute(target, target.attrs[0])
        self.assertEqual(["string", "boolean"], [x.name for x in target.attrs[0].types])

    @mock.patch.object(AttributeTypeClassHandler, "merge_attribute_type")
    @mock.patch.object(ClassContainer, "find")
    def test_process_attribute_type_with_simple_source(
        self, mock_container_find, mock_merge_attribute_type
    ):
        target = ClassFactory.create()
        attr = AttrFactory.create()
        attr_type = AttrTypeFactory.create()
        source = ClassFactory.create()

        mock_container_find.return_value = source

        self.processor.process_attribute_type(target, attr, attr_type)

        qname = target.source_qname(attr_type.name)
        mock_container_find.assert_called_once_with(qname, simple_cond)
        mock_merge_attribute_type.assert_called_once_with(
            source, target, attr, attr_type
        )

    @mock.patch.object(AttributeTypeClassHandler, "is_circular_dependency")
    @mock.patch.object(AttributeTypeClassHandler, "merge_attribute_type")
    @mock.patch.object(ClassContainer, "find")
    def test_process_attribute_type_with_complex_source(
        self,
        mock_container_find,
        mock_merge_attribute_type,
        mock_is_circular_dependency,
    ):
        target = ClassFactory.create()
        attr = AttrFactory.create()
        attr_type = AttrTypeFactory.create()
        source = ClassFactory.create()

        mock_container_find.side_effect = [None, source]
        mock_is_circular_dependency.return_value = True

        self.processor.process_attribute_type(target, attr, attr_type)
        self.assertTrue(attr_type.circular)
        self.assertEqual(0, mock_merge_attribute_type.call_count)

        qname = target.source_qname(attr_type.name)
        mock_container_find.assert_has_calls(
            [mock.call(qname, simple_cond), mock.call(qname)]
        )
        mock_is_circular_dependency.assert_called_once_with(source, target)

    @mock.patch.object(AttributeTypeClassHandler, "is_circular_dependency")
    @mock.patch.object(AttributeTypeClassHandler, "merge_attribute_type")
    @mock.patch.object(ClassContainer, "find")
    def test_process_attribute_type_with_circularerence(
        self,
        mock_container_find,
        mock_merge_attribute_type,
        mock_is_circular_dependency,
    ):
        source = ClassFactory.create()
        target = ClassFactory.create()
        attr = AttrFactory.create()
        attr_type = AttrTypeFactory.create(name="foo", circular=True)
        mock_is_circular_dependency.return_value = False
        mock_container_find.return_value = source

        self.processor.process_attribute_type(target, attr, attr_type)
        self.assertFalse(attr_type.circular)

        qname = target.source_qname(attr_type.name)
        mock_container_find.assert_called_once_with(qname)
        mock_is_circular_dependency.assert_called_once_with(source, target)

    @mock.patch("xsdata.codegen.handlers.attribute_type.logger.warning")
    def test_process_attribute_type_with_missing_source(self, mock_logger_warning):
        target = ClassFactory.create()
        attr = AttrFactory.create()
        attr_type = AttrTypeFactory.create(name="foo")

        self.processor.process_attribute_type(target, attr, attr_type)
        self.assertEqual(DataType.STRING.code, attr_type.name)
        self.assertTrue(attr_type.native)
        self.assertFalse(attr_type.circular)
        self.assertFalse(attr_type.forward)
        mock_logger_warning.assert_called_once_with("Missing type: %s", "foo")

    @mock.patch.object(ClassContainer, "find")
    @mock.patch.object(Class, "dependencies")
    def test_is_circular_dependency(self, mock_dependencies, mock_container_find):
        source = ClassFactory.create()
        target = ClassFactory.create()
        another = ClassFactory.create()

        find_classes = {QName("a"): another, QName("b"): target}

        mock_container_find.side_effect = lambda x: find_classes.get(x)
        mock_dependencies.side_effect = [
            [QName(x) for x in "ccde"],
            [QName(x) for x in "abc"],
            [QName(x) for x in "xy"],
        ]

        self.assertFalse(self.processor.is_circular_dependency(source, target))
        self.assertTrue(self.processor.is_circular_dependency(source, target))
        self.assertTrue(self.processor.is_circular_dependency(source, source))

        mock_container_find.assert_has_calls(
            [
                mock.call(QName("c")),
                mock.call(QName("d")),
                mock.call(QName("e")),
                mock.call(QName("a")),
                mock.call(QName("x")),
                mock.call(QName("y")),
                mock.call(QName("b")),
            ]
        )

    @mock.patch.object(ClassUtils, "copy_inner_classes")
    def test_merge_attribute_type(self, mock_copy_inner_classes):
        source = ClassFactory.elements(1, name="Foobar")
        source.attrs[0].restrictions.max_length = 100
        source.attrs[0].restrictions.min_length = 1

        target = ClassFactory.elements(1)
        attr = target.attrs[0]
        attr.restrictions.min_length = 2
        attr.types.clear()
        attr.types.append(AttrTypeFactory.create(name=source.name))

        self.assertEqual("Foobar", attr.types[0].name)
        self.processor.merge_attribute_type(source, target, attr, attr.types[0])

        self.assertEqual("string", attr.types[0].name)
        self.assertEqual(Restrictions(min_length=2, max_length=100), attr.restrictions)
        mock_copy_inner_classes.assert_called_once_with(source, target)

    @mock.patch("xsdata.codegen.handlers.attribute_type.logger.warning")
    def test_merge_attribute_type_when_source_attrs_is_not_one(
        self, mock_logger_warning
    ):
        source = ClassFactory.create()
        target = ClassFactory.elements(1)
        attr = target.attrs[0]
        self.processor.merge_attribute_type(source, target, attr, attr.types[0])

        self.assertEqual("string", attr.types[0].name)
        mock_logger_warning.assert_called_once_with(
            "Missing implementation: %s", source.type.__name__
        )

        attr.types = [AttrTypeFactory.create(name="foo")]
        source.attrs = AttrFactory.list(2)
        self.processor.merge_attribute_type(source, target, attr, attr.types[0])
        self.assertEqual("string", attr.types[0].name)
