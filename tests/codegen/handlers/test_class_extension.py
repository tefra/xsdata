import sys
from unittest import mock

from tests.factories import AttrFactory
from tests.factories import AttrTypeFactory
from tests.factories import ClassFactory
from tests.factories import ExtensionFactory
from tests.factories import FactoryTestCase
from xsdata.codegen.container import ClassContainer
from xsdata.codegen.handlers import ClassExtensionClassHandler
from xsdata.codegen.handlers.class_extension import simple_cond
from xsdata.utils.classes import ClassUtils


class ClassExtensionHandlerTests(FactoryTestCase):
    def setUp(self):
        super().setUp()

        container = ClassContainer()
        self.processor = ClassExtensionClassHandler(container=container)

    @mock.patch.object(ClassExtensionClassHandler, "process_native_extension")
    def test_process_extension_with_native_type(self, mock_flatten_extension_native):
        extension = ExtensionFactory.create(type=AttrTypeFactory.xs_string())
        target = ClassFactory.elements(1, extensions=[extension])

        self.processor.process_extension(target, extension)
        mock_flatten_extension_native.assert_called_once_with(target, extension)

    @mock.patch.object(ClassExtensionClassHandler, "process_simple_extension")
    @mock.patch.object(ClassContainer, "find")
    def test_process_extension_with_simple_source_extension(
        self, mock_container_find, mock_process_simple_extension
    ):
        extension = ExtensionFactory.create()
        target = ClassFactory.create(extensions=[extension])
        source = ClassFactory.create()
        mock_container_find.return_value = source

        self.processor.process_extension(target, extension)

        type_qname = target.source_qname(extension.type.name)
        mock_container_find.assert_called_once_with(type_qname, simple_cond)
        mock_process_simple_extension.assert_called_once_with(source, target, extension)

    @mock.patch.object(ClassExtensionClassHandler, "process_complex_extension")
    @mock.patch.object(ClassContainer, "find")
    def test_process_extension_with_complex_source_extension(
        self, mock_container_find, mock_process_complex_extension
    ):
        extension = ExtensionFactory.create()
        target = ClassFactory.create(extensions=[extension])
        source = ClassFactory.create()
        mock_container_find.side_effect = [None, source]

        self.processor.process_extension(target, extension)
        type_qname = target.source_qname(extension.type.name)
        mock_container_find.assert_has_calls(
            [mock.call(type_qname, simple_cond), mock.call(type_qname),]
        )
        mock_process_complex_extension.assert_called_once_with(
            source, target, extension
        )

    @mock.patch("xsdata.codegen.handlers.class_extension.logger.warning")
    def test_process_extension_with_unknown_extension_type(self, mock_logger_warning):
        extension = ExtensionFactory.create()
        target = ClassFactory.create(extensions=[extension])

        self.processor.process_extension(target, extension)
        self.assertEqual(0, len(target.extensions))
        mock_logger_warning.assert_called_once_with(
            "Missing extension type: %s", extension.type.name
        )

    @mock.patch.object(ClassUtils, "create_default_attribute")
    def test_process_extension_native(self, mock_create_default_attribute):
        extension = ExtensionFactory.create()
        target = ClassFactory.elements(1)

        self.processor.process_native_extension(target, extension)
        mock_create_default_attribute.assert_called_once_with(target, extension)

    @mock.patch.object(ClassUtils, "copy_extension_type")
    def test_process_native_extension_with_enumeration_target(
        self, mock_copy_extension_type
    ):
        extension = ExtensionFactory.create()
        target = ClassFactory.enumeration(1)

        self.processor.process_native_extension(target, extension)
        mock_copy_extension_type.assert_called_once_with(target, extension)

    def test_process_simple_extension_with_circularerences(self):
        extension = ExtensionFactory.create()
        target = ClassFactory.create(extensions=[extension])
        self.processor.process_simple_extension(target, target, extension)
        self.assertEqual(0, len(target.extensions))

    @mock.patch.object(ClassUtils, "create_default_attribute")
    def test_process_simple_extension_when_source_is_enumeration_and_target_is_not(
        self, mock_create_default_attribute
    ):
        source = ClassFactory.enumeration(2)
        target = ClassFactory.elements(1)
        extension = ExtensionFactory.create()

        self.processor.process_simple_extension(source, target, extension)
        mock_create_default_attribute.assert_called_once_with(target, extension)

    @mock.patch.object(ClassUtils, "copy_attributes")
    @mock.patch.object(ClassUtils, "create_default_attribute")
    def test_process_simple_extension_when_target_is_enumeration_and_source_is_not(
        self, mock_create_default_attribute, mock_copy_attributes
    ):
        extension = ExtensionFactory.create()
        source = ClassFactory.elements(2)
        target = ClassFactory.enumeration(1, extensions=[extension])

        self.processor.process_simple_extension(source, target, extension)
        self.assertEqual(0, mock_create_default_attribute.call_count)
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
    @mock.patch.object(ClassUtils, "compare_attributes")
    def test_process_complex_extension_when_target_includes_all_source_attrs(
        self, mock_compare_attributes, mock_copy_attributes
    ):
        mock_compare_attributes.return_value = ClassUtils.INCLUDES_ALL
        extension = ExtensionFactory.create()
        target = ClassFactory.create(extensions=[extension])
        source = ClassFactory.create()

        self.processor.process_complex_extension(source, target, extension)

        self.assertEqual(0, len(target.extensions))

        mock_compare_attributes.assert_called_once_with(source, target)
        self.assertEqual(0, mock_copy_attributes.call_count)

    @mock.patch.object(ClassUtils, "copy_attributes")
    @mock.patch.object(ClassUtils, "compare_attributes")
    def test_process_complex_extension_when_target_includes_some_source_attrs(
        self, mock_compare_attributes, mock_copy_attributes
    ):
        mock_compare_attributes.return_value = ClassUtils.INCLUDES_SOME
        extension = ExtensionFactory.create()
        target = ClassFactory.create()
        source = ClassFactory.create()

        self.processor.process_complex_extension(source, target, extension)
        mock_compare_attributes.assert_called_once_with(source, target)
        mock_copy_attributes.assert_called_once_with(source, target, extension)

    @mock.patch.object(ClassUtils, "copy_attributes")
    @mock.patch.object(ClassUtils, "compare_attributes")
    def test_process_complex_extension_when_target_includes_no_source_attrs(
        self, mock_compare_attributes, mock_copy_attributes
    ):
        mock_compare_attributes.return_value = ClassUtils.INCLUDES_NONE
        extension = ExtensionFactory.create()
        target = ClassFactory.create(extensions=[extension])
        source = ClassFactory.create()

        self.processor.process_complex_extension(source, target, extension)
        mock_compare_attributes.assert_called_once_with(source, target)
        self.assertEqual(0, mock_copy_attributes.call_count)
        self.assertEqual(1, len(target.extensions))

    @mock.patch.object(ClassUtils, "copy_attributes")
    @mock.patch.object(ClassUtils, "compare_attributes")
    def test_process_complex_extension_when_source_is_abstract(
        self, mock_compare_attributes, mock_copy_attributes
    ):
        mock_compare_attributes.return_value = ClassUtils.INCLUDES_NONE
        extension = ExtensionFactory.create()
        target = ClassFactory.create()
        source = ClassFactory.create(abstract=True)

        self.processor.process_complex_extension(source, target, extension)
        mock_compare_attributes.assert_called_once_with(source, target)
        mock_copy_attributes.assert_called_once_with(source, target, extension)

    @mock.patch.object(ClassUtils, "copy_attributes")
    @mock.patch.object(ClassUtils, "compare_attributes")
    def test_process_complex_extension_when_target_is_abstract(
        self, mock_compare_attributes, mock_copy_attributes
    ):
        mock_compare_attributes.return_value = ClassUtils.INCLUDES_NONE
        extension = ExtensionFactory.create()
        target = ClassFactory.create(abstract=True)
        source = ClassFactory.create()

        self.processor.process_complex_extension(source, target, extension)
        mock_compare_attributes.assert_called_once_with(source, target)
        mock_copy_attributes.assert_called_once_with(source, target, extension)

    @mock.patch.object(ClassUtils, "copy_attributes")
    @mock.patch.object(ClassUtils, "compare_attributes")
    def test_process_complex_extension_when_source_has_suffix_attr(
        self, mock_compare_attributes, mock_copy_attributes
    ):
        mock_compare_attributes.return_value = ClassUtils.INCLUDES_NONE
        extension = ExtensionFactory.create()
        target = ClassFactory.create()
        source = ClassFactory.create()
        source.attrs.append(AttrFactory.create(index=sys.maxsize))

        self.processor.process_complex_extension(source, target, extension)
        self.assertEqual(0, len(target.attrs))

        target.attrs.append(AttrFactory.create())
        self.processor.process_complex_extension(source, target, extension)

        self.assertEqual(2, mock_compare_attributes.call_count)
        mock_copy_attributes.assert_called_once_with(source, target, extension)

    @mock.patch.object(ClassUtils, "copy_attributes")
    @mock.patch.object(ClassUtils, "compare_attributes")
    def test_process_complex_extension_when_target_has_suffix_attr(
        self, mock_compare_attributes, mock_copy_attributes
    ):
        mock_compare_attributes.return_value = ClassUtils.INCLUDES_NONE
        extension = ExtensionFactory.create()
        target = ClassFactory.create()
        source = ClassFactory.create()
        target.attrs.append(AttrFactory.create(index=sys.maxsize))

        self.processor.process_complex_extension(source, target, extension)
        mock_compare_attributes.assert_called_once_with(source, target)
        mock_copy_attributes.assert_called_once_with(source, target, extension)
