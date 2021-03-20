from unittest import mock

from xsdata.codegen.container import ClassContainer
from xsdata.codegen.handlers import AttributeTypeHandler
from xsdata.codegen.models import Class
from xsdata.codegen.models import Restrictions
from xsdata.codegen.models import Status
from xsdata.codegen.utils import ClassUtils
from xsdata.models.enums import DataType
from xsdata.models.enums import Tag
from xsdata.utils.testing import AttrFactory
from xsdata.utils.testing import AttrTypeFactory
from xsdata.utils.testing import ClassFactory
from xsdata.utils.testing import FactoryTestCase


class AttributeTypeHandlerTests(FactoryTestCase):
    def setUp(self):
        super().setUp()

        container = ClassContainer()
        self.processor = AttributeTypeHandler(container=container)

    @mock.patch.object(AttributeTypeHandler, "filter_types")
    @mock.patch.object(AttributeTypeHandler, "process_type")
    def test_process(self, mock_process_type, mock_filter_types):
        xs_int = AttrTypeFactory.native(DataType.INT)
        xs_bool = AttrTypeFactory.native(DataType.BOOLEAN)
        xs_string = AttrTypeFactory.native(DataType.STRING)
        mock_filter_types.side_effect = lambda x: x

        target = ClassFactory.create(
            attrs=[
                AttrFactory.create(types=[xs_int, xs_bool]),
                AttrFactory.create(types=[xs_string, xs_string]),
            ]
        )

        self.processor.process(target)
        self.assertEqual(2, len(target.attrs[0].types))
        self.assertEqual(2, len(target.attrs[1].types))

        mock_filter_types.assert_has_calls(
            [
                mock.call(target.attrs[0].types),
                mock.call(target.attrs[1].types),
            ]
        )

        mock_process_type.assert_has_calls(
            [
                mock.call(target, target.attrs[0], xs_int),
                mock.call(target, target.attrs[0], xs_bool),
                mock.call(target, target.attrs[1], xs_string),
                mock.call(target, target.attrs[1], xs_string),
            ]
        )

    @mock.patch.object(AttributeTypeHandler, "process_dependency_type")
    @mock.patch.object(AttributeTypeHandler, "process_native_type")
    def test_process_type_with_native_type(
        self, mock_process_native_type, mock_process_dependency_type
    ):
        attr = AttrFactory.create()
        target = ClassFactory.create()
        xs_int = AttrTypeFactory.native(DataType.INT)

        self.processor.process_type(target, attr, xs_int)
        self.assertEqual(0, mock_process_dependency_type.call_count)
        mock_process_native_type.assert_called_once_with(attr, xs_int)

    @mock.patch.object(AttributeTypeHandler, "process_dependency_type")
    @mock.patch.object(AttributeTypeHandler, "process_native_type")
    def test_process_type_with_dependency_type(
        self, mock_process_native_type, mock_process_dependency_type
    ):
        attr = AttrFactory.create()
        target = ClassFactory.create()
        attr_type = AttrTypeFactory.create()

        self.processor.process_type(target, attr, attr_type)
        self.assertEqual(0, mock_process_native_type.call_count)
        mock_process_dependency_type.assert_called_once_with(target, attr, attr_type)

    @mock.patch.object(AttributeTypeHandler, "process_inner_type")
    def test_process_type_with_forward_reference(self, mock_process_inner_type):
        attr = AttrFactory.create()
        target = ClassFactory.create()
        attr_type = AttrTypeFactory.create(forward=True)

        self.processor.process_type(target, attr, attr_type)
        mock_process_inner_type.assert_called_once_with(target, attr, attr_type)

    def test_process_native_type(self):
        attr = AttrFactory.native(DataType.INT)
        nm_tokens_type = AttrTypeFactory.native(DataType.NMTOKENS)

        self.processor.process_native_type(attr, attr.types[0])
        self.assertEqual(str(DataType.INT), attr.types[0].qname)

        attr.restrictions.pattern = "[a-z]"
        self.processor.process_native_type(attr, attr.types[0])
        self.assertEqual(str(DataType.STRING), attr.types[0].qname)

        self.processor.process_native_type(attr, nm_tokens_type)
        self.assertTrue(attr.restrictions.tokens)

    @mock.patch.object(AttributeTypeHandler, "reset_attribute_type")
    @mock.patch.object(AttributeTypeHandler, "find_dependency")
    def test_process_dependency_type_with_absent_type(
        self, mock_find_dependency, mock_reset_attribute_type
    ):
        mock_find_dependency.return_value = None
        target = ClassFactory.create()
        attr = AttrFactory.create()
        attr_type = attr.types[0]

        self.processor.process_dependency_type(target, attr, attr_type)
        mock_reset_attribute_type.assert_called_once_with(attr_type, True)

    @mock.patch.object(AttributeTypeHandler, "reset_attribute_type")
    @mock.patch.object(AttributeTypeHandler, "find_dependency")
    def test_process_dependency_type_with_dummy_type(
        self, mock_find_dependency, mock_reset_attribute_type
    ):
        mock_find_dependency.return_value = ClassFactory.create(tag=Tag.ELEMENT)
        target = ClassFactory.create()
        attr = AttrFactory.create()
        attr_type = attr.types[0]

        self.processor.process_dependency_type(target, attr, attr_type)
        mock_reset_attribute_type.assert_called_once_with(attr_type, False)

    @mock.patch.object(AttributeTypeHandler, "copy_attribute_properties")
    @mock.patch.object(AttributeTypeHandler, "find_dependency")
    def test_process_dependency_type_with_simple_type(
        self, mock_find_dependency, mock_copy_attribute_properties
    ):
        simple = ClassFactory.simple_type()
        target = ClassFactory.create()
        attr = AttrFactory.create()
        attr_type = attr.types[0]
        mock_find_dependency.return_value = simple

        self.processor.process_dependency_type(target, attr, attr_type)
        mock_copy_attribute_properties.assert_called_once_with(
            simple, target, attr, attr_type
        )

    @mock.patch.object(AttributeTypeHandler, "find_dependency")
    def test_process_dependency_type_with_enumeration_type(self, mock_find_dependency):
        enumeration = ClassFactory.enumeration(2)
        enumeration.attrs[1].restrictions.format = "base16"
        mock_find_dependency.return_value = enumeration

        target = ClassFactory.simple_type()
        attr = target.attrs[0]
        attr.types[0] = AttrTypeFactory.create(qname=enumeration.qname)

        self.processor.process_dependency_type(target, attr, attr.types[0])
        self.assertEqual("base16", attr.restrictions.format)

    @mock.patch.object(AttributeTypeHandler, "set_circular_flag")
    @mock.patch.object(AttributeTypeHandler, "find_dependency")
    def test_process_dependency_type_with_complex_type(
        self, mock_find_dependency, mock_set_circular_flag
    ):
        complex_type = ClassFactory.elements(1)
        mock_find_dependency.return_value = complex_type

        target = ClassFactory.create()
        attr = AttrFactory.create()
        attr_type = attr.types[0]

        self.processor.process_dependency_type(target, attr, attr_type)
        mock_set_circular_flag.assert_called_once_with(complex_type, target, attr_type)

    @mock.patch.object(AttributeTypeHandler, "update_restrictions")
    @mock.patch.object(AttributeTypeHandler, "copy_attribute_properties")
    def test_process_inner_type_with_simple_type(
        self, mock_copy_attribute_properties, mock_update_restrictions
    ):
        attr = AttrFactory.create(types=[AttrTypeFactory.create(qname="{bar}a")])
        inner = ClassFactory.simple_type(qname="{bar}a", status=Status.PROCESSED)
        target = ClassFactory.create(inner=[inner])

        self.processor.process_inner_type(target, attr, attr.types[0])
        self.assertNotIn(inner, target.inner)

        self.assertEqual(0, mock_update_restrictions.call_count)
        mock_copy_attribute_properties.assert_called_once_with(
            inner, target, attr, attr.types[0]
        )

    @mock.patch.object(AttributeTypeHandler, "update_restrictions")
    @mock.patch.object(AttributeTypeHandler, "copy_attribute_properties")
    def test_process_inner_type_with_complex_type(
        self, mock_copy_attribute_properties, mock_update_restrictions
    ):
        target = ClassFactory.create()
        inner = ClassFactory.elements(2, qname="a", status=Status.PROCESSED)
        attr = AttrFactory.create(types=[AttrTypeFactory.create(qname="a")])

        target.inner.append(inner)
        self.processor.process_inner_type(target, attr, attr.types[0])
        self.assertIn(inner, target.inner)
        self.assertEqual(0, mock_copy_attribute_properties.call_count)
        self.assertEqual(0, mock_update_restrictions.call_count)

    @mock.patch.object(AttributeTypeHandler, "update_restrictions")
    @mock.patch.object(AttributeTypeHandler, "copy_attribute_properties")
    def test_process_inner_type_with_circular_reference(
        self, mock_copy_attribute_properties, mock_update_restrictions
    ):
        target = ClassFactory.create()
        attr = AttrFactory.create()
        attr_type = AttrTypeFactory.create(circular=True)

        self.processor.process_inner_type(target, attr, attr_type)
        self.assertEqual(0, mock_copy_attribute_properties.call_count)
        self.assertEqual(0, mock_update_restrictions.call_count)

    @mock.patch.object(ClassUtils, "copy_inner_class")
    def test_copy_attribute_properties(self, mock_copy_inner_class):
        source = ClassFactory.elements(1, qname="Foobar")
        source.attrs[0].restrictions.max_length = 100
        source.attrs[0].restrictions.min_length = 1
        source.attrs[0].help = "foo"
        source.attrs[0].types = [
            AttrTypeFactory.create(qname="first"),
            AttrTypeFactory.create(qname="second"),
        ]

        target = ClassFactory.elements(1)
        attr = target.attrs[0]
        attr.restrictions.min_length = 2
        attr.types.clear()
        attr.types.append(AttrTypeFactory.create(qname=source.name))

        self.assertEqual("Foobar", attr.types[0].name)
        self.processor.copy_attribute_properties(source, target, attr, attr.types[0])

        self.assertEqual("first", attr.types[0].name)
        self.assertEqual("second", attr.types[1].name)
        self.assertEqual("foo", attr.help)
        self.assertEqual(Restrictions(min_length=2, max_length=100), attr.restrictions)
        mock_copy_inner_class.assert_has_calls(
            [
                mock.call(source, target, attr, source.attrs[0].types[0]),
                mock.call(source, target, attr, source.attrs[0].types[1]),
            ]
        )

    def test_copy_attribute_properties_from_nillable_source(self):
        source = ClassFactory.elements(1, nillable=True)
        target = ClassFactory.elements(1)
        attr = target.attrs[0]

        self.processor.copy_attribute_properties(source, target, attr, attr.types[0])
        self.assertTrue(attr.restrictions.nillable)

    @mock.patch.object(AttributeTypeHandler, "is_circular_dependency")
    def test_set_circular_flag(self, mock_is_circular_dependency):
        source = ClassFactory.create()
        target = ClassFactory.create()
        attr = AttrFactory.create()
        attr_type = attr.types[0]

        mock_is_circular_dependency.return_value = True

        self.processor.set_circular_flag(source, target, attr_type)
        self.assertTrue(attr_type.circular)

        mock_is_circular_dependency.assert_called_once_with(source, target, set())

    @mock.patch.object(ClassContainer, "find")
    @mock.patch.object(Class, "dependencies")
    def test_is_circular_dependency(self, mock_dependencies, mock_container_find):
        source = ClassFactory.create()
        target = ClassFactory.create()
        another = ClassFactory.create()
        processing = ClassFactory.create(status=Status.PROCESSING)

        find_classes = {"a": another, "b": target}

        mock_container_find.side_effect = lambda x: find_classes.get(x)
        mock_dependencies.side_effect = [
            list("ccde"),
            list("abc"),
            list("xy"),
        ]

        self.assertTrue(
            self.processor.is_circular_dependency(processing, target, set())
        )

        self.processor.dependencies.clear()
        self.assertFalse(self.processor.is_circular_dependency(source, target, set()))

        self.processor.dependencies.clear()
        self.assertTrue(self.processor.is_circular_dependency(source, target, set()))

        self.processor.dependencies.clear()
        self.assertTrue(self.processor.is_circular_dependency(source, source, set()))

        mock_container_find.assert_has_calls(
            [
                mock.call("c"),
                mock.call("d"),
                mock.call("e"),
                mock.call("a"),
                mock.call("x"),
                mock.call("y"),
                mock.call("b"),
            ]
        )

    def test_find_dependency(self):
        attr_type = AttrTypeFactory.create(qname="a")

        self.assertIsNone(self.processor.find_dependency(attr_type, Tag.ELEMENT))

        abstract = ClassFactory.create(qname="a", tag=Tag.COMPLEX_TYPE, abstract=True)
        self.processor.container.add(abstract)
        self.assertEqual(
            abstract, self.processor.find_dependency(attr_type, Tag.ELEMENT)
        )

        element = ClassFactory.create(qname="a", tag=Tag.ELEMENT)
        self.processor.container.add(element)
        self.assertEqual(
            element, self.processor.find_dependency(attr_type, Tag.SIMPLE_TYPE)
        )

        simple = ClassFactory.create(qname="a", tag=Tag.SIMPLE_TYPE)
        self.processor.container.add(simple)
        self.assertEqual(
            simple, self.processor.find_dependency(attr_type, Tag.SIMPLE_TYPE)
        )

    @mock.patch.object(Class, "dependencies")
    def test_cached_dependencies(self, mock_class_dependencies):
        mock_class_dependencies.return_value = ["a", "b"]

        source = ClassFactory.create()
        self.processor.dependencies[id(source)] = ("a",)

        actual = self.processor.cached_dependencies(source)
        self.assertEqual(("a",), actual)

        self.processor.dependencies.clear()
        actual = self.processor.cached_dependencies(source)
        self.assertEqual(("a", "b"), actual)
        mock_class_dependencies.assert_called_once_with()

    def test_update_restrictions(self):
        attr = AttrFactory.create()
        self.processor.update_restrictions(attr, DataType.NMTOKENS)
        self.assertTrue(attr.restrictions.tokens)

        attr = AttrFactory.create()
        self.processor.update_restrictions(attr, DataType.IDREFS)
        self.assertTrue(attr.restrictions.tokens)

        attr = AttrFactory.create()
        self.processor.update_restrictions(attr, DataType.BASE64_BINARY)
        self.assertEqual("base64", attr.restrictions.format)

        attr = AttrFactory.create()
        self.processor.update_restrictions(attr, DataType.HEX_BINARY)
        self.assertEqual("base16", attr.restrictions.format)

    def test_filter_types(self):
        xs_string = AttrTypeFactory.native(DataType.STRING)
        xs_error = AttrTypeFactory.native(DataType.ERROR)
        xs_any = AttrTypeFactory.native(DataType.ANY_TYPE)

        types = [
            xs_string.clone(),
            xs_string.clone(),
            xs_string.clone(),
            xs_error.clone(),
        ]

        actual = self.processor.filter_types(types)

        self.assertEqual(1, len(actual))

        types.append(xs_any)
        actual = self.processor.filter_types(types)
        self.assertEqual(1, len(actual))
        self.assertEqual(xs_string, actual[0])

        actual = self.processor.filter_types([])
        self.assertEqual(xs_string, actual[0])

        types = [xs_any]
        actual = self.processor.filter_types(types)
        self.assertEqual(1, len(actual))
