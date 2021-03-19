import sys
from unittest import mock

from xsdata.codegen.container import ClassContainer
from xsdata.codegen.handlers import ClassExtensionHandler
from xsdata.codegen.models import Restrictions
from xsdata.codegen.models import Status
from xsdata.codegen.utils import ClassUtils
from xsdata.exceptions import CodeGenerationError
from xsdata.models.enums import DataType
from xsdata.models.enums import Tag
from xsdata.utils.testing import AttrFactory
from xsdata.utils.testing import AttrTypeFactory
from xsdata.utils.testing import ClassFactory
from xsdata.utils.testing import ExtensionFactory
from xsdata.utils.testing import FactoryTestCase


class ClassExtensionHandlerTests(FactoryTestCase):
    def setUp(self):
        super().setUp()

        container = ClassContainer()
        self.processor = ClassExtensionHandler(container=container)

    @mock.patch.object(ClassExtensionHandler, "process_extension")
    def test_process_with_no_extensions(self, mock_process_extension):
        target = ClassFactory.elements(1)
        self.processor.process(target)
        self.assertEqual(0, mock_process_extension.call_count)

    @mock.patch.object(ClassExtensionHandler, "process_native_extension")
    def test_process_extension_with_native_type(self, mock_flatten_extension_native):
        extension = ExtensionFactory.native(DataType.STRING)
        target = ClassFactory.elements(1, extensions=[extension])

        self.processor.process_extension(target, extension)
        mock_flatten_extension_native.assert_called_once_with(target, extension)

    @mock.patch.object(ClassExtensionHandler, "process_dependency_extension")
    def test_process_extension_with_dependency_type(
        self, mock_process_dependency_extension
    ):
        extension = ExtensionFactory.create(AttrTypeFactory.create("foo"))
        target = ClassFactory.elements(1, extensions=[extension])

        self.processor.process_extension(target, extension)
        mock_process_dependency_extension.assert_called_once_with(target, extension)

    @mock.patch.object(ClassExtensionHandler, "process_complex_extension")
    @mock.patch.object(ClassExtensionHandler, "process_simple_extension")
    @mock.patch.object(ClassExtensionHandler, "find_dependency")
    def test_process_dependency_extension_with_absent_type(
        self,
        mock_find_dependency,
        mock_process_simple_extension,
        mock_process_complex_extension,
    ):
        extension = ExtensionFactory.create()
        target = ClassFactory.create(extensions=[extension])
        mock_find_dependency.return_value = None

        self.processor.process_extension(target, extension)
        self.assertEqual(0, len(target.extensions))
        self.assertEqual(0, mock_process_simple_extension.call_count)
        self.assertEqual(0, mock_process_complex_extension.call_count)

    @mock.patch.object(ClassExtensionHandler, "process_complex_extension")
    @mock.patch.object(ClassExtensionHandler, "process_simple_extension")
    @mock.patch.object(ClassExtensionHandler, "find_dependency")
    def test_process_dependency_extension_with_simple_type(
        self,
        mock_find_dependency,
        mock_process_simple_extension,
        mock_process_complex_extension,
    ):
        extension = ExtensionFactory.create()
        target = ClassFactory.create(extensions=[extension])
        source = ClassFactory.create(tag=Tag.SIMPLE_TYPE)
        mock_find_dependency.return_value = source

        self.processor.process_extension(target, extension)
        self.assertEqual(0, mock_process_complex_extension.call_count)

        mock_process_simple_extension.assert_called_once_with(source, target, extension)

    @mock.patch.object(ClassExtensionHandler, "process_complex_extension")
    @mock.patch.object(ClassExtensionHandler, "process_simple_extension")
    @mock.patch.object(ClassExtensionHandler, "find_dependency")
    def test_process_dependency_extension_with_enum_type(
        self,
        mock_find_dependency,
        mock_process_simple_extension,
        mock_process_complex_extension,
    ):
        extension = ExtensionFactory.create()
        target = ClassFactory.create(extensions=[extension])
        source = ClassFactory.create(tag=Tag.COMPLEX_TYPE)
        source.attrs.append(AttrFactory.enumeration())
        mock_find_dependency.return_value = source

        self.processor.process_extension(target, extension)
        self.assertEqual(0, mock_process_complex_extension.call_count)

        mock_process_simple_extension.assert_called_once_with(source, target, extension)

    def test_process_enum_extension_with_enum_source(self):
        source = ClassFactory.enumeration(3)
        target = ClassFactory.enumeration(2)
        target.attrs[1].name = source.attrs[2].name
        extension = ExtensionFactory.reference(source.qname)
        target.extensions.append(extension)

        self.processor.container.add(source)
        self.processor.container.add(target)
        self.processor.process_dependency_extension(target, extension)

        self.assertEqual(2, len(target.attrs))
        self.assertEqual(0, len(target.extensions))
        self.assertEqual(source.attrs[2], target.attrs[1])

    def test_process_enum_extension_with_simple_source(self):
        qname_type = AttrTypeFactory.native(DataType.QNAME)
        source = ClassFactory.create(
            tag=Tag.SIMPLE_TYPE,
            attrs=[
                AttrFactory.create(
                    types=[qname_type], restrictions=Restrictions(length=10)
                )
            ],
        )
        target = ClassFactory.enumeration(2)
        extension = ExtensionFactory.reference(source.qname)
        target.extensions.append(extension)

        self.processor.container.add(source)
        self.processor.container.add(target)
        self.processor.process_dependency_extension(target, extension)

        for attr in target.attrs:
            self.assertIn(qname_type, attr.types)
            self.assertEqual(10, attr.restrictions.length)

    def test_process_enum_extension_with_complex_source(self):
        source = ClassFactory.create(
            tag=Tag.COMPLEX_TYPE,
            attrs=[
                AttrFactory.create(tag=Tag.ATTRIBUTE),
                AttrFactory.create(tag=Tag.RESTRICTION),
            ],
            extensions=ExtensionFactory.list(2),
            status=Status.PROCESSED,
        )
        target = ClassFactory.enumeration(1)
        target.attrs[0].default = "Yes"
        extension = ExtensionFactory.reference(source.qname)
        target.extensions.append(extension)
        expected = target.clone()

        self.processor.container.add(source)
        self.processor.container.add(target)
        self.processor.process_dependency_extension(target, extension)

        expected.attrs = [attr.clone() for attr in source.attrs]
        expected.extensions = [ext.clone() for ext in source.extensions]
        expected.attrs[1].default = "Yes"
        expected.attrs[1].fixed = True

        self.assertEqual(expected, target)

        self.assertIsNone(target.attrs[0].default)
        self.assertFalse(target.attrs[0].fixed)
        self.assertEqual("Yes", target.attrs[1].default)
        self.assertTrue(target.attrs[1].fixed)

    def test_process_enum_extension_raises_exception(self):
        source = ClassFactory.elements(2)
        target = ClassFactory.enumeration(2)
        extension = ExtensionFactory.reference(source.qname)
        target.extensions.append(extension)
        self.processor.container.add(source)
        self.processor.container.add(target)

        with self.assertRaises(CodeGenerationError):
            self.processor.process_dependency_extension(target, extension)

    @mock.patch.object(ClassExtensionHandler, "process_complex_extension")
    @mock.patch.object(ClassExtensionHandler, "process_simple_extension")
    @mock.patch.object(ClassExtensionHandler, "find_dependency")
    def test_process_dependency_extension_with_complex_type(
        self,
        mock_find_dependency,
        mock_process_simple_extension,
        mock_process_complex_extension,
    ):
        extension = ExtensionFactory.create()
        target = ClassFactory.create(extensions=[extension])
        source = ClassFactory.create(tag=Tag.COMPLEX_TYPE)
        mock_find_dependency.return_value = source

        self.processor.process_extension(target, extension)
        self.assertEqual(0, mock_process_simple_extension.call_count)

        mock_process_complex_extension.assert_called_once_with(
            source, target, extension
        )

    @mock.patch.object(ClassExtensionHandler, "add_default_attribute")
    def test_process_extension_native(self, mock_add_default_attribute):
        extension = ExtensionFactory.create()
        target = ClassFactory.elements(1)

        self.processor.process_native_extension(target, extension)
        mock_add_default_attribute.assert_called_once_with(target, extension)

    @mock.patch.object(ClassExtensionHandler, "replace_attributes_type")
    def test_process_native_extension_with_enumeration_target(
        self, mock_replace_attributes_type
    ):
        extension = ExtensionFactory.create()
        target = ClassFactory.enumeration(1)

        self.processor.process_native_extension(target, extension)
        mock_replace_attributes_type.assert_called_once_with(target, extension)

    def test_process_simple_extension_with_circular_refence(self):
        extension = ExtensionFactory.create()
        target = ClassFactory.create(extensions=[extension])
        self.processor.process_simple_extension(target, target, extension)
        self.assertEqual(0, len(target.extensions))

    @mock.patch.object(ClassExtensionHandler, "add_default_attribute")
    def test_process_simple_extension_when_source_is_enumeration_and_target_is_not(
        self, mock_add_default_attribute
    ):
        source = ClassFactory.enumeration(2)
        target = ClassFactory.elements(1)
        extension = ExtensionFactory.create()

        self.processor.process_simple_extension(source, target, extension)
        mock_add_default_attribute.assert_called_once_with(target, extension)

    @mock.patch.object(ClassUtils, "copy_attributes")
    @mock.patch.object(ClassExtensionHandler, "add_default_attribute")
    def test_process_simple_extension_when_target_is_enumeration_and_source_is_not(
        self, mock_add_default_attribute, mock_copy_attributes
    ):
        extension = ExtensionFactory.create()
        source = ClassFactory.elements(2)
        target = ClassFactory.enumeration(1, extensions=[extension])

        self.processor.process_simple_extension(source, target, extension)
        self.assertEqual(0, mock_add_default_attribute.call_count)
        self.assertEqual(0, mock_copy_attributes.call_count)
        self.assertEqual(0, len(target.extensions))

    @mock.patch.object(ClassUtils, "copy_attributes")
    def test_process_simple_extension_when_source_and_target_are_enumerations(
        self, mock_copy_attributes
    ):
        source = ClassFactory.enumeration(2)
        target = ClassFactory.enumeration(1)
        extension = ExtensionFactory.create()

        self.processor.process_simple_extension(source, target, extension)
        mock_copy_attributes.assert_called_once_with(source, target, extension)

    @mock.patch.object(ClassUtils, "copy_attributes")
    def test_process_simple_extension_when_source_and_target_are_not_enumerations(
        self, mock_copy_attributes
    ):
        source = ClassFactory.elements(2)
        target = ClassFactory.elements(1)
        extension = ExtensionFactory.create()

        self.processor.process_simple_extension(source, target, extension)
        mock_copy_attributes.assert_called_once_with(source, target, extension)

    @mock.patch.object(ClassUtils, "copy_attributes")
    @mock.patch.object(ClassExtensionHandler, "should_remove_extension")
    def test_process_complex_extension_removes_extension(
        self, mock_should_remove_extension, mock_copy_attributes
    ):
        mock_should_remove_extension.return_value = True
        extension = ExtensionFactory.create()
        target = ClassFactory.elements(1, extensions=[extension])
        source = ClassFactory.elements(5)

        self.processor.process_complex_extension(source, target, extension)

        self.assertEqual(0, len(target.extensions))
        self.assertEqual(1, len(target.attrs))

        mock_should_remove_extension.assert_called_once_with(source, target)
        self.assertEqual(0, mock_copy_attributes.call_count)

    @mock.patch.object(ClassUtils, "copy_attributes")
    @mock.patch.object(ClassExtensionHandler, "should_flatten_extension")
    def test_process_complex_extension_copies_attributes(
        self, mock_compare_attributes, mock_should_flatten_extension
    ):
        mock_should_flatten_extension.return_value = True
        extension = ExtensionFactory.create()
        target = ClassFactory.create()
        source = ClassFactory.create()

        self.processor.process_complex_extension(source, target, extension)
        mock_compare_attributes.assert_called_once_with(source, target)
        mock_should_flatten_extension.assert_called_once_with(source, target, extension)

    @mock.patch.object(ClassExtensionHandler, "should_flatten_extension")
    @mock.patch.object(ClassExtensionHandler, "should_remove_extension")
    def test_process_complex_extension_ignores_extension(
        self, mock_should_remove_extension, mock_should_flatten_extension
    ):
        mock_should_remove_extension.return_value = False
        mock_should_flatten_extension.return_value = False
        extension = ExtensionFactory.create()
        target = ClassFactory.create(extensions=[extension])
        source = ClassFactory.create()

        self.processor.process_complex_extension(source, target, extension)
        self.assertEqual(1, len(target.extensions))

    def test_find_dependency(self):
        attr_type = AttrTypeFactory.create(qname="a")

        self.assertIsNone(self.processor.find_dependency(attr_type))

        complex = ClassFactory.create(qname="a", tag=Tag.COMPLEX_TYPE)
        self.processor.container.add(complex)
        self.assertEqual(complex, self.processor.find_dependency(attr_type))

        simple = ClassFactory.create(qname="a", tag=Tag.SIMPLE_TYPE)
        self.processor.container.add(simple)
        self.assertEqual(simple, self.processor.find_dependency(attr_type))

    def test_should_remove_extension(self):
        source = ClassFactory.create()
        target = ClassFactory.create()

        # source is target
        self.assertTrue(self.processor.should_remove_extension(source, source))
        self.assertFalse(self.processor.should_remove_extension(source, target))

        # Source is parent class
        source.inner.append(target)
        self.assertTrue(self.processor.should_remove_extension(target, target))

        # MRO Violation
        source.inner.clear()
        target.extensions.append(ExtensionFactory.reference("foo"))
        target.extensions.append(ExtensionFactory.reference("bar"))
        self.assertFalse(self.processor.should_remove_extension(source, target))

        source.extensions.append(ExtensionFactory.reference("bar"))
        self.assertTrue(self.processor.should_remove_extension(source, target))

    def test_should_flatten_extension(self):
        source = ClassFactory.create()
        target = ClassFactory.create()

        self.assertFalse(self.processor.should_flatten_extension(source, target))

        # Source has suffix attr and target has its own attrs
        source = ClassFactory.elements(1)
        source.attrs[0].index = sys.maxsize
        target.attrs.append(AttrFactory.create())
        self.assertTrue(self.processor.should_flatten_extension(source, target))

        # Target has suffix attr
        source = ClassFactory.create()
        target = ClassFactory.elements(1)
        target.attrs[0].index = sys.maxsize
        self.assertTrue(self.processor.should_flatten_extension(source, target))

        # Source is a simple type
        source = ClassFactory.create(attrs=[AttrFactory.create(tag=Tag.SIMPLE_TYPE)])
        target = ClassFactory.elements(1)
        self.assertTrue(self.processor.should_flatten_extension(source, target))

        # Sequential violation
        source = ClassFactory.elements(3)
        target = source.clone()
        self.assertFalse(self.processor.should_flatten_extension(source, target))

        for attr in target.attrs:
            attr.restrictions.sequential = True

        self.assertFalse(self.processor.should_flatten_extension(source, target))

        target.attrs = [target.attrs[1], target.attrs[0], target.attrs[2]]
        self.assertTrue(self.processor.should_flatten_extension(source, target))

        # Types violation
        target = source.clone()
        target.attrs[1].types = [
            AttrTypeFactory.native(DataType.INT),
            AttrTypeFactory.native(DataType.FLOAT),
        ]

        source.attrs[1].types = [
            AttrTypeFactory.native(DataType.INT),
            AttrTypeFactory.native(DataType.FLOAT),
            AttrTypeFactory.native(DataType.DECIMAL),
        ]
        self.assertFalse(self.processor.should_flatten_extension(source, target))
        target.attrs[1].types.append(AttrTypeFactory.native(DataType.QNAME))
        self.assertTrue(self.processor.should_flatten_extension(source, target))

    def test_replace_attributes_type(self):
        extension = ExtensionFactory.create()
        target = ClassFactory.elements(2)
        target.extensions.append(extension)

        ClassExtensionHandler.replace_attributes_type(target, extension)

        self.assertEqual(1, len(target.attrs[0].types))
        self.assertEqual(1, len(target.attrs[1].types))
        self.assertEqual(extension.type, target.attrs[0].types[0])
        self.assertEqual(extension.type, target.attrs[1].types[0])
        self.assertEqual(0, len(target.extensions))

    def test_add_default_attribute(self):
        xs_string = AttrTypeFactory.native(DataType.STRING)
        extension = ExtensionFactory.create(xs_string, Restrictions(required=True))
        item = ClassFactory.elements(1, extensions=[extension])

        ClassExtensionHandler.add_default_attribute(item, extension)
        expected = AttrFactory.create(
            name="@value", default=None, types=[xs_string], tag=Tag.EXTENSION
        )

        self.assertEqual(2, len(item.attrs))
        self.assertEqual(0, len(item.extensions))
        self.assertEqual(expected, item.attrs[0])

        xs_int = AttrTypeFactory.native(DataType.INT)
        extension = ExtensionFactory.create(xs_int, Restrictions(tokens=True))
        item.extensions.append(extension)
        ClassExtensionHandler.add_default_attribute(item, extension)

        expected.types.append(xs_int)
        expected_restrictions = Restrictions(
            tokens=True, required=True, min_occurs=1, max_occurs=1
        )

        self.assertEqual(2, len(item.attrs))
        self.assertEqual(0, len(item.extensions))
        self.assertEqual(expected, item.attrs[0])
        self.assertEqual(expected_restrictions, item.attrs[0].restrictions)

    def test_add_default_attribute_with_any_type(self):
        extension = ExtensionFactory.create(
            AttrTypeFactory.native(DataType.ANY_TYPE),
            Restrictions(min_occurs=1, max_occurs=1, required=True),
        )
        item = ClassFactory.create(extensions=[extension])

        ClassExtensionHandler.add_default_attribute(item, extension)
        expected = AttrFactory.create(
            name="@any_element",
            default=None,
            types=[extension.type.clone()],
            tag=Tag.ANY,
            namespace="##any",
            restrictions=Restrictions(min_occurs=1, max_occurs=1, required=True),
        )

        self.assertEqual(1, len(item.attrs))
        self.assertEqual(0, len(item.extensions))
        self.assertEqual(expected, item.attrs[0])
