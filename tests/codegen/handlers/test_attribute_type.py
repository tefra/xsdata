from unittest import mock

from lxml.etree import QName

from tests.factories import AttrFactory
from tests.factories import AttrTypeFactory
from tests.factories import ClassFactory
from tests.factories import ExtensionFactory
from tests.factories import FactoryTestCase
from tests.factories import RestrictionsFactory
from xsdata.codegen.container import ClassContainer
from xsdata.codegen.handlers import AttributeTypeHandler
from xsdata.codegen.models import Class
from xsdata.codegen.models import Restrictions
from xsdata.codegen.models import Status
from xsdata.codegen.utils import ClassUtils
from xsdata.exceptions import AnalyzerValueError
from xsdata.models.xsd import ComplexType
from xsdata.models.xsd import Element
from xsdata.models.xsd import SimpleType


class AttributeTypeHandlerTests(FactoryTestCase):
    def setUp(self):
        super().setUp()

        container = ClassContainer()
        self.processor = AttributeTypeHandler(container=container)

    @mock.patch.object(AttributeTypeHandler, "process_type")
    def test_process(self, mock_process_type):
        xs_int = AttrTypeFactory.xs_int()
        xs_bool = AttrTypeFactory.xs_bool()
        xs_string = AttrTypeFactory.xs_string()

        target = ClassFactory.create(
            attrs=[
                AttrFactory.create(types=[xs_int, xs_bool]),
                AttrFactory.create(types=[xs_string, xs_string]),
            ]
        )

        self.processor.process(target)
        self.assertEqual(2, len(target.attrs[0].types))
        self.assertEqual(1, len(target.attrs[1].types))  # remove duplicate

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

    @mock.patch.object(AttributeTypeHandler, "process_dependency_type")
    @mock.patch.object(AttributeTypeHandler, "process_native_type")
    def test_process_type_with_inner_type(
        self, mock_process_native_type, mock_process_dependency_type
    ):
        attr = AttrFactory.create()
        target = ClassFactory.create()
        attr_type = AttrTypeFactory.create(forward=True)

        self.processor.process_type(target, attr, attr_type)
        self.assertEqual(0, mock_process_native_type.call_count)
        self.assertEqual(0, mock_process_dependency_type.call_count)

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
        self, mock_find_dependency, mock_reset_attribute_type,
    ):
        mock_find_dependency.return_value = None
        target = ClassFactory.create()
        attr = AttrFactory.create()
        attr_type = attr.types[0]

        self.processor.process_dependency_type(target, attr, attr_type)
        mock_reset_attribute_type.assert_called_once_with(attr_type)

    @mock.patch.object(AttributeTypeHandler, "process_simple_dependency")
    @mock.patch.object(AttributeTypeHandler, "find_dependency")
    def test_process_dependency_type_with_simple_type(
        self, mock_find_dependency, mock_process_simple_dependency,
    ):
        simple = ClassFactory.create(type=SimpleType)

        mock_find_dependency.return_value = simple

        target = ClassFactory.create()
        attr = AttrFactory.create()
        attr_type = attr.types[0]

        self.processor.process_dependency_type(target, attr, attr_type)
        mock_process_simple_dependency.assert_called_once_with(
            simple, target, attr, attr_type
        )

    @mock.patch.object(AttributeTypeHandler, "process_complex_dependency")
    @mock.patch.object(AttributeTypeHandler, "find_dependency")
    def test_process_dependency_type_with_complex_type(
        self, mock_find_dependency, mock_process_complex_dependency,
    ):
        complex = ClassFactory.create(type=ComplexType)
        element = ClassFactory.create(type=Element)

        mock_find_dependency.side_effect = [complex, element]

        target = ClassFactory.create()
        attr = AttrFactory.create()
        attr_type = attr.types[0]

        self.processor.process_dependency_type(target, attr, attr_type)
        self.processor.process_dependency_type(target, attr, attr_type)

        mock_process_complex_dependency.assert_has_calls(
            [
                mock.call(complex, target, attr, attr_type),
                mock.call(element, target, attr, attr_type),
            ]
        )

    @mock.patch.object(ClassUtils, "copy_inner_classes")
    def test_process_simple_dependency(self, mock_copy_inner_classes):
        source = ClassFactory.elements(1, name="Foobar")
        source.attrs[0].restrictions.max_length = 100
        source.attrs[0].restrictions.min_length = 1

        target = ClassFactory.elements(1)
        attr = target.attrs[0]
        attr.restrictions.min_length = 2
        attr.types.clear()
        attr.types.append(AttrTypeFactory.create(name=source.name))

        self.assertEqual("Foobar", attr.types[0].name)
        self.processor.process_simple_dependency(source, target, attr, attr.types[0])

        self.assertEqual("string", attr.types[0].name)
        self.assertEqual(Restrictions(min_length=2, max_length=100), attr.restrictions)
        mock_copy_inner_classes.assert_called_once_with(source, target)

    def test_process_simple_dependency_no_source_attributes(self):
        source = ClassFactory.create()
        target = ClassFactory.elements(1)
        attr = target.attrs[0]
        self.processor.process_simple_dependency(source, target, attr, attr.types[0])

        self.assertEqual("string", attr.types[0].name)

    def test_process_simple_dependency_with_more_than_one_attribute(self):
        source = ClassFactory.create(type=SimpleType, attrs=AttrFactory.list(2))
        target = ClassFactory.elements(1)
        attr = target.attrs[0]
        attr_type = attr.types[0]

        with self.assertRaises(AnalyzerValueError) as cm:
            self.processor.process_simple_dependency(source, target, attr, attr_type)

        self.assertEqual(
            "SimpleType with more than one attribute: `class_B`", str(cm.exception)
        )

    def test_process_simple_dependency_with_enumeration(self):
        source = ClassFactory.enumeration(2)
        target = ClassFactory.create()
        attr = AttrFactory.create()
        attr_type = attr.types[0]
        expected = attr_type.clone()

        self.processor.process_simple_dependency(source, target, attr, attr_type)
        self.assertEqual(expected, attr_type)

    @mock.patch.object(AttributeTypeHandler, "is_circular_dependency")
    def test_process_complex_dependency_with_non_abstract(
        self, mock_is_circular_dependency
    ):
        source = ClassFactory.create()
        target = ClassFactory.create()
        attr = AttrFactory.create()
        attr_type = attr.types[0]

        mock_is_circular_dependency.return_value = True

        self.processor.process_complex_dependency(source, target, attr, attr_type)
        self.assertTrue(attr_type.circular)

        mock_is_circular_dependency.assert_called_once_with(source, target)

    def test_process_complex_dependency_with_abstract_that_needs_override(self):
        source = ClassFactory.elements(2, abstract=True)
        target = ClassFactory.create()
        attr = AttrFactory.create()
        attr_type = attr.types[0]

        self.processor.process_complex_dependency(source, target, attr, attr_type)
        self.assertFalse(source.abstract)

        source = ClassFactory.create(abstract=True)
        self.processor.process_complex_dependency(source, target, attr, attr_type)
        self.assertFalse(source.abstract)

    def test_process_complex_dependency_with_derived_abstract(self):
        source = ClassFactory.create(
            abstract=True,
            extensions=[
                ExtensionFactory.create(
                    restrictions=RestrictionsFactory.create(max_length=3)
                ),
                ExtensionFactory.create(
                    restrictions=RestrictionsFactory.create(min_length=2)
                ),
            ],
        )
        target = ClassFactory.create()
        attr = AttrFactory.create(restrictions=RestrictionsFactory.create(min_length=1))
        attr_type = attr.types[0]

        self.processor.process_complex_dependency(source, target, attr, attr_type)
        self.assertTrue(source.abstract)

        self.assertEqual(source.extensions[0].type, attr.types[0])
        self.assertIsNot(source.extensions[0].type, attr.types[0])
        self.assertEqual(source.extensions[1].type, attr.types[1])
        self.assertIsNot(source.extensions[1].type, attr.types[1])

        self.assertEqual({"max_length": 3, "min_length": 2}, attr.restrictions.asdict())

    @mock.patch.object(ClassContainer, "find")
    @mock.patch.object(Class, "dependencies")
    def test_is_circular_dependency(self, mock_dependencies, mock_container_find):
        source = ClassFactory.create()
        target = ClassFactory.create()
        another = ClassFactory.create()
        processing = ClassFactory.create(status=Status.PROCESSING)

        find_classes = {QName("a"): another, QName("b"): target}

        mock_container_find.side_effect = lambda x: find_classes.get(x)
        mock_dependencies.side_effect = [
            [QName(x) for x in "ccde"],
            [QName(x) for x in "abc"],
            [QName(x) for x in "xy"],
        ]

        self.assertTrue(self.processor.is_circular_dependency(processing, target))

        self.processor.dependencies.clear()
        self.assertFalse(self.processor.is_circular_dependency(source, target))

        self.processor.dependencies.clear()
        self.assertTrue(self.processor.is_circular_dependency(source, target))

        self.processor.dependencies.clear()
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

    def test_find_dependency(self):
        target = ClassFactory.create()
        attr_type = AttrTypeFactory.create(name="a")

        self.assertIsNone(self.processor.find_dependency(target, attr_type))

        abstract = ClassFactory.create(name="a", type=ComplexType, abstract=True)
        self.processor.container.add(abstract)
        self.assertEqual(abstract, self.processor.find_dependency(target, attr_type))

        element = ClassFactory.create(name="a", type=Element)
        self.processor.container.add(element)
        self.assertEqual(element, self.processor.find_dependency(target, attr_type))

        simple = ClassFactory.create(name="a", type=SimpleType)
        self.processor.container.add(simple)
        self.assertEqual(simple, self.processor.find_dependency(target, attr_type))

    @mock.patch.object(Class, "dependencies")
    def test_cached_dependencies(self, mock_class_dependencies):
        a_qname = QName("a")
        b_qname = QName("b")

        mock_class_dependencies.return_value = [a_qname, b_qname]

        source = ClassFactory.create()
        self.processor.dependencies[id(source)] = (a_qname,)

        actual = self.processor.cached_dependencies(source)
        self.assertEqual((a_qname,), actual)

        self.processor.dependencies.clear()
        actual = self.processor.cached_dependencies(source)
        self.assertEqual((a_qname, b_qname), actual)
        mock_class_dependencies.assert_called_once_with()
