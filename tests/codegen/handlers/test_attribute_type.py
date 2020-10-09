from unittest import mock

from tests.factories import AttrFactory
from tests.factories import AttrTypeFactory
from tests.factories import ClassFactory
from tests.factories import FactoryTestCase
from xsdata.codegen.container import ClassContainer
from xsdata.codegen.handlers import AttributeTypeHandler
from xsdata.codegen.models import Class
from xsdata.codegen.models import Restrictions
from xsdata.codegen.models import Status
from xsdata.codegen.utils import ClassUtils
from xsdata.exceptions import AnalyzerValueError
from xsdata.models.enums import Tag
from xsdata.models.xsd import ComplexType
from xsdata.models.xsd import Element
from xsdata.models.xsd import SimpleType


class AttributeTypeHandlerTests(FactoryTestCase):
    def setUp(self):
        super().setUp()

        container = ClassContainer()
        self.processor = AttributeTypeHandler(container=container)

    @mock.patch.object(AttributeTypeHandler, "filter_types")
    @mock.patch.object(AttributeTypeHandler, "process_type")
    def test_process(self, mock_process_type, mock_filter_types):
        xs_int = AttrTypeFactory.xs_int()
        xs_bool = AttrTypeFactory.xs_bool()
        xs_string = AttrTypeFactory.xs_string()
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
        xs_int = AttrTypeFactory.xs_int()

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
    def test_process_type_with_inner_type(self, mock_process_inner_type):
        attr = AttrFactory.create()
        target = ClassFactory.create()
        attr_type = AttrTypeFactory.create(forward=True)

        self.processor.process_type(target, attr, attr_type)
        mock_process_inner_type.assert_called_once_with(target, attr, attr_type)

    def test_process_native_type(self):
        attr = AttrFactory.create()
        xs_int = AttrTypeFactory.xs_int()
        xs_int_clone = xs_int.clone()

        self.processor.process_native_type(attr, xs_int)
        self.assertEqual(xs_int_clone, xs_int)

        attr.restrictions.pattern = "[a-z]"
        self.processor.process_native_type(attr, xs_int)
        self.assertEqual(AttrTypeFactory.xs_string(), xs_int)

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
        mock_reset_attribute_type.assert_called_once_with(attr_type)

    @mock.patch.object(AttributeTypeHandler, "reset_attribute_type")
    @mock.patch.object(AttributeTypeHandler, "find_dependency")
    def test_process_dependency_type_with_dummy_type(
        self, mock_find_dependency, mock_reset_attribute_type
    ):
        mock_find_dependency.return_value = ClassFactory.create()
        target = ClassFactory.create()
        attr = AttrFactory.create()
        attr_type = attr.types[0]

        self.processor.process_dependency_type(target, attr, attr_type)
        mock_reset_attribute_type.assert_called_once_with(attr_type)

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

    @mock.patch.object(AttributeTypeHandler, "set_circular_flag")
    @mock.patch.object(AttributeTypeHandler, "find_dependency")
    def test_process_dependency_type_with_complex_type(
        self, mock_find_dependency, mock_set_circular_flag
    ):
        complex_type = ClassFactory.elements(1)
        enumeration = ClassFactory.enumeration(1)

        mock_find_dependency.side_effect = [complex_type, enumeration]

        target = ClassFactory.create()
        attr = AttrFactory.create()
        attr_type = attr.types[0]

        self.processor.process_dependency_type(target, attr, attr_type)
        self.processor.process_dependency_type(target, attr, attr_type)

        mock_set_circular_flag.assert_called_once_with(complex_type, target, attr_type)

    @mock.patch.object(AttributeTypeHandler, "copy_attribute_properties")
    def test_process_inner_type(self, mock_copy_attribute_properties):
        target = ClassFactory.create()
        enumeration = ClassFactory.enumeration(2, qname="{bar}a")
        simple_type = ClassFactory.simple_type(qname="{bar}a")
        attr = AttrFactory.create(types=[AttrTypeFactory.create(qname="{foo}a")])

        target.inner.extend((enumeration, simple_type))
        self.processor.process_inner_type(target, attr, attr.types[0])
        self.assertNotIn(simple_type, target.inner)
        mock_copy_attribute_properties.assert_called_once_with(
            simple_type, target, attr, attr.types[0]
        )

    @mock.patch.object(AttributeTypeHandler, "copy_attribute_properties")
    def test_process_inner_type_with_absent_type(self, mock_copy_attribute_properties):
        target = ClassFactory.create()
        simple_type = ClassFactory.simple_type(qname="b")
        attr = AttrFactory.create(types=[AttrTypeFactory.create(qname="{foo}a")])

        target.inner.append(simple_type)
        self.processor.process_inner_type(target, attr, attr.types[0])
        self.assertIn(simple_type, target.inner)
        self.assertEqual(0, mock_copy_attribute_properties.call_count)

    @mock.patch.object(ClassUtils, "copy_inner_classes")
    def test_copy_attribute_properties(self, mock_copy_inner_classes):
        source = ClassFactory.elements(1, qname="Foobar")
        source.attrs[0].restrictions.max_length = 100
        source.attrs[0].restrictions.min_length = 1

        target = ClassFactory.elements(1)
        attr = target.attrs[0]
        attr.restrictions.min_length = 2
        attr.types.clear()
        attr.types.append(AttrTypeFactory.create(qname=source.name))

        self.assertEqual("Foobar", attr.types[0].name)
        self.processor.copy_attribute_properties(source, target, attr, attr.types[0])

        self.assertEqual("string", attr.types[0].name)
        self.assertEqual(Restrictions(min_length=2, max_length=100), attr.restrictions)
        mock_copy_inner_classes.assert_called_once_with(source, target)

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

        self.assertIsNone(self.processor.find_dependency(attr_type))

        abstract = ClassFactory.create(qname="a", type=ComplexType, abstract=True)
        self.processor.container.add(abstract)
        self.assertEqual(abstract, self.processor.find_dependency(attr_type))

        element = ClassFactory.create(qname="a", type=Element)
        self.processor.container.add(element)
        self.assertEqual(element, self.processor.find_dependency(attr_type))

        simple = ClassFactory.create(qname="a", type=SimpleType)
        self.processor.container.add(simple)
        self.assertEqual(simple, self.processor.find_dependency(attr_type))

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

    def test_filter_types(self):
        xs_string = AttrTypeFactory.xs_string()
        xs_error = AttrTypeFactory.xs_error()
        xs_any = AttrTypeFactory.xs_any()

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
