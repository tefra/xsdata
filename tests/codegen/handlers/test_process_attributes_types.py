from unittest import mock

from xsdata.codegen.container import ClassContainer
from xsdata.codegen.handlers import ProcessAttributeTypes
from xsdata.codegen.models import Class
from xsdata.codegen.models import Restrictions
from xsdata.codegen.models import Status
from xsdata.codegen.utils import ClassUtils
from xsdata.models.config import GeneratorConfig
from xsdata.models.enums import DataType
from xsdata.models.enums import Tag
from xsdata.utils.testing import AttrFactory
from xsdata.utils.testing import AttrTypeFactory
from xsdata.utils.testing import ClassFactory
from xsdata.utils.testing import FactoryTestCase


class ProcessAttributeTypesTests(FactoryTestCase):
    def setUp(self):
        super().setUp()

        container = ClassContainer(config=GeneratorConfig())
        self.processor = ProcessAttributeTypes(container=container)

    @mock.patch.object(ProcessAttributeTypes, "cascade_properties")
    @mock.patch.object(ProcessAttributeTypes, "process_types")
    def test_process(self, mock_process_types, mock_cascade_properties):
        target = ClassFactory.elements(2)

        self.processor.process(target)

        calls = [mock.call(target, attr) for attr in target.attrs]
        mock_process_types.assert_has_calls(calls)
        mock_cascade_properties.assert_has_calls(calls)
        self.assertEqual(2, len(calls))

    @mock.patch.object(ProcessAttributeTypes, "process_type")
    def test_process_types(self, mock_process_type):
        target = ClassFactory.create()
        attr = AttrFactory.create()
        types = [
            AttrTypeFactory.native(DataType.STRING),
            AttrTypeFactory.native(DataType.INT),
            AttrTypeFactory.native(DataType.STRING),
        ]

        attr.types = types

        self.processor.process_types(target, attr)

        mock_process_type.assert_has_calls(
            [mock.call(target, attr, tp) for tp in types]
        )

        self.assertEqual(types[:-1], attr.types)

    def test_process_types_with_ignore_patterns(self):
        target = ClassFactory.create()
        attr = AttrFactory.native(DataType.DECIMAL)
        attr.restrictions.pattern = r"\d{2}.\d{2}"

        self.processor.container.config.output.ignore_patterns = True
        self.processor.process_types(target, attr)
        self.assertEqual(DataType.DECIMAL, attr.types[0].datatype)

    def test_cascade_properties(self):
        target = ClassFactory.create(default="2", fixed=True, nillable=True)
        attr = AttrFactory.native(DataType.STRING, tag=Tag.EXTENSION)
        self.processor.cascade_properties(target, attr)

        self.assertEqual(target.default, attr.default)
        self.assertTrue(attr.fixed)
        self.assertTrue(attr.restrictions.nillable)

        target.default = "3"
        target.fixed = False
        target.nillable = False
        self.processor.cascade_properties(target, attr)
        self.assertNotEqual(target.default, attr.default)
        self.assertTrue(attr.fixed)
        self.assertTrue(attr.restrictions.nillable)

        attr = AttrFactory.native(DataType.STRING, tag=Tag.ELEMENT)
        self.processor.cascade_properties(target, attr)
        self.assertIsNone(attr.default)
        self.assertFalse(attr.fixed)
        self.assertFalse(attr.restrictions.nillable)

    @mock.patch.object(ProcessAttributeTypes, "process_dependency_type")
    @mock.patch.object(ProcessAttributeTypes, "process_native_type")
    def test_process_type_with_native_type(
        self, mock_process_native_type, mock_process_dependency_type
    ):
        attr = AttrFactory.create()
        target = ClassFactory.create()
        xs_int = AttrTypeFactory.native(DataType.INT)

        self.processor.process_type(target, attr, xs_int)
        self.assertEqual(0, mock_process_dependency_type.call_count)
        mock_process_native_type.assert_called_once_with(attr, xs_int)

    @mock.patch.object(ProcessAttributeTypes, "process_dependency_type")
    @mock.patch.object(ProcessAttributeTypes, "process_native_type")
    def test_process_type_with_dependency_type(
        self, mock_process_native_type, mock_process_dependency_type
    ):
        attr = AttrFactory.create()
        target = ClassFactory.create()
        attr_type = AttrTypeFactory.create()

        self.processor.process_type(target, attr, attr_type)
        self.assertEqual(0, mock_process_native_type.call_count)
        mock_process_dependency_type.assert_called_once_with(target, attr, attr_type)

    @mock.patch.object(ProcessAttributeTypes, "process_inner_type")
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

    @mock.patch.object(ProcessAttributeTypes, "reset_attribute_type")
    @mock.patch.object(ProcessAttributeTypes, "find_dependency")
    def test_process_dependency_type_with_absent_type(
        self, mock_find_dependency, mock_reset_attribute_type
    ):
        mock_find_dependency.return_value = None
        target = ClassFactory.create()
        attr = AttrFactory.create()
        attr_type = attr.types[0]

        self.processor.process_dependency_type(target, attr, attr_type)
        mock_reset_attribute_type.assert_called_once_with(attr_type, True)

    @mock.patch.object(ProcessAttributeTypes, "copy_attribute_properties")
    @mock.patch.object(ProcessAttributeTypes, "find_dependency")
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

    @mock.patch.object(ProcessAttributeTypes, "find_dependency")
    def test_process_dependency_type_with_enumeration_type(self, mock_find_dependency):
        enumeration = ClassFactory.enumeration(2)
        enumeration.attrs[1].restrictions.format = "base16"
        mock_find_dependency.return_value = enumeration

        target = ClassFactory.simple_type()
        attr = target.attrs[0]
        attr.restrictions.min_length = 10
        attr.restrictions.max_length = 12
        attr.types[0] = AttrTypeFactory.create(qname=enumeration.qname)

        self.processor.process_dependency_type(target, attr, attr.types[0])
        self.assertEqual("base16", attr.restrictions.format)
        self.assertIsNone(attr.restrictions.min_length)
        self.assertIsNone(attr.restrictions.max_length)

    @mock.patch.object(ProcessAttributeTypes, "set_circular_flag")
    @mock.patch.object(ProcessAttributeTypes, "find_dependency")
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

        self.assertFalse(attr.restrictions.nillable)

        complex_type.nillable = True
        self.processor.process_dependency_type(target, attr, attr_type)
        self.assertTrue(attr.restrictions.nillable)

    @mock.patch.object(ProcessAttributeTypes, "find_dependency")
    def test_process_dependency_type_with_abstract_type_type(
        self, mock_find_dependency
    ):
        complex_type = ClassFactory.create(tag=Tag.ELEMENT, abstract=True)
        mock_find_dependency.return_value = complex_type

        attr = AttrFactory.create()
        attr_type = attr.types[0]
        target = ClassFactory.create()
        target.attrs.append(attr)

        self.assertEqual(1, len(target.attrs))
        self.processor.process_dependency_type(target, attr, attr_type)
        self.assertEqual(0, len(target.attrs))

    @mock.patch.object(ProcessAttributeTypes, "update_restrictions")
    @mock.patch.object(ProcessAttributeTypes, "copy_attribute_properties")
    def test_process_inner_type_with_simple_type(
        self, mock_copy_attribute_properties, mock_update_restrictions
    ):
        attr = AttrFactory.create(types=[AttrTypeFactory.create(qname="{bar}a")])
        inner = ClassFactory.simple_type(qname="{bar}a", status=Status.FLATTENED)
        target = ClassFactory.create(inner=[inner])

        self.processor.process_inner_type(target, attr, attr.types[0])
        self.assertNotIn(inner, target.inner)

        self.assertEqual(0, mock_update_restrictions.call_count)
        mock_copy_attribute_properties.assert_called_once_with(
            inner, target, attr, attr.types[0]
        )

    @mock.patch.object(ProcessAttributeTypes, "update_restrictions")
    @mock.patch.object(ProcessAttributeTypes, "copy_attribute_properties")
    def test_process_inner_type_with_complex_type(
        self, mock_copy_attribute_properties, mock_update_restrictions
    ):
        target = ClassFactory.create()
        inner = ClassFactory.elements(2, qname="a", status=Status.FLATTENED)
        attr = AttrFactory.create(types=[AttrTypeFactory.create(qname="a")])

        target.inner.append(inner)
        self.processor.process_inner_type(target, attr, attr.types[0])
        self.assertIn(inner, target.inner)
        self.assertEqual(0, mock_copy_attribute_properties.call_count)
        self.assertEqual(0, mock_update_restrictions.call_count)

    @mock.patch.object(ProcessAttributeTypes, "update_restrictions")
    @mock.patch.object(ProcessAttributeTypes, "copy_attribute_properties")
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
        source.attrs[0].restrictions.min_occurs = 0
        source.attrs[0].restrictions.max_occurs = 10
        source.attrs[0].help = "foo"
        source.attrs[0].types = [
            AttrTypeFactory.create(qname="first"),
            AttrTypeFactory.create(qname="second"),
        ]

        target = ClassFactory.elements(1)
        attr = target.attrs[0]
        attr.restrictions.min_occurs = 1
        attr.restrictions.max_occurs = 2
        attr.restrictions.min_length = 2
        attr.types.clear()
        attr.types.append(AttrTypeFactory.create(qname=source.name))

        self.assertEqual("Foobar", attr.types[0].name)
        self.processor.copy_attribute_properties(source, target, attr, attr.types[0])

        self.assertEqual("first", attr.types[0].name)
        self.assertEqual("second", attr.types[1].name)
        self.assertEqual("foo", attr.help)
        self.assertEqual(
            Restrictions(min_length=2, min_occurs=1, max_occurs=2, max_length=100),
            attr.restrictions,
        )
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

    def test_copy_attribute_properties_set_default_value_if_none(self):
        target = ClassFactory.create(attrs=AttrFactory.list(1, tag=Tag.ATTRIBUTE))
        attr = target.attrs[0]

        source = ClassFactory.elements(1)
        source.attrs[0].default = "foo"
        source.attrs[0].fixed = True

        self.processor.copy_attribute_properties(source, target, attr, attr.types[0])
        self.assertEqual("foo", attr.default)
        self.assertTrue("foo", attr.fixed)

        source.attrs[0].default = "bar"
        source.attrs[0].fixed = False
        self.processor.copy_attribute_properties(source, target, attr, attr.types[0])
        self.assertEqual("foo", attr.default)
        self.assertTrue("foo", attr.fixed)

    @mock.patch.object(ProcessAttributeTypes, "is_circular_dependency")
    def test_set_circular_flag(self, mock_is_circular_dependency):
        source = ClassFactory.create()
        target = ClassFactory.create()
        attr = AttrFactory.create()
        attr_type = attr.types[0]

        mock_is_circular_dependency.return_value = True

        self.processor.set_circular_flag(source, target, attr_type)
        self.assertTrue(attr_type.circular)
        self.assertEqual(id(source), attr_type.reference)

        mock_is_circular_dependency.assert_called_once_with(source, target, set())

    @mock.patch.object(ClassContainer, "find")
    @mock.patch.object(Class, "dependencies")
    def test_is_circular_dependency(self, mock_dependencies, mock_container_find):
        source = ClassFactory.create()
        target = ClassFactory.create()
        another = ClassFactory.create()
        processing = ClassFactory.create(status=Status.FLATTENING)

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

        element = ClassFactory.create(qname="a", tag=Tag.ELEMENT)
        complex_type = ClassFactory.create(qname="a", tag=Tag.COMPLEX_TYPE)
        simple_type = ClassFactory.create(qname="a", tag=Tag.SIMPLE_TYPE)

        actual = self.processor.find_dependency(attr_type, Tag.ELEMENT)
        self.assertIsNone(actual)

        self.processor.container.add(simple_type)
        actual = self.processor.find_dependency(attr_type, Tag.ELEMENT)
        self.assertEqual(simple_type, actual)

        self.processor.container.add(complex_type)
        actual = self.processor.find_dependency(attr_type, Tag.ELEMENT)
        self.assertEqual(complex_type, actual)

        self.processor.container.add(element)
        actual = self.processor.find_dependency(attr_type, Tag.ELEMENT)
        self.assertEqual(element, actual)

        actual = self.processor.find_dependency(attr_type, Tag.SIMPLE_TYPE)
        self.assertEqual(simple_type, actual)

        actual = self.processor.find_dependency(attr_type, Tag.EXTENSION)
        self.assertEqual(simple_type, actual)

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
        attr = AttrFactory.native(DataType.NMTOKENS)
        self.processor.update_restrictions(attr, attr.types[0].datatype)
        self.assertTrue(attr.restrictions.tokens)

        attr = AttrFactory.native(DataType.IDREFS)
        self.processor.update_restrictions(attr, attr.types[0].datatype)
        self.assertTrue(attr.restrictions.tokens)

        attr = AttrFactory.native(DataType.BASE64_BINARY)
        self.processor.update_restrictions(attr, attr.types[0].datatype)
        self.assertEqual("base64", attr.restrictions.format)

        attr = AttrFactory.native(DataType.HEX_BINARY)
        self.processor.update_restrictions(attr, attr.types[0].datatype)
        self.assertEqual("base16", attr.restrictions.format)

    def test_detect_lazy_namespace(self):
        source = ClassFactory.create(namespace="foo", tag=Tag.ELEMENT)
        target = ClassFactory.create()
        attr = AttrFactory.create(namespace="##lazy")

        self.processor.detect_lazy_namespace(source, target, attr)
        self.assertEqual("foo", attr.namespace)

        attr.namespace = "##lazy"
        source.namespace = None
        self.processor.detect_lazy_namespace(source, target, attr)
        self.assertIsNone(attr.namespace)

        attr.namespace = "##lazy"
        target.namespace = "foo"
        self.processor.detect_lazy_namespace(source, target, attr)
        self.assertEqual("", attr.namespace)
