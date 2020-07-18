from unittest import mock

from tests.factories import AttrFactory
from tests.factories import ClassFactory
from tests.factories import ExtensionFactory
from tests.factories import FactoryTestCase
from xsdata.codegen.analyzer import ClassAnalyzer
from xsdata.codegen.container import ClassContainer
from xsdata.codegen.models import Class
from xsdata.codegen.sanitizer import ClassSanitizer
from xsdata.codegen.validator import ClassValidator
from xsdata.exceptions import AnalyzerValueError
from xsdata.models.xsd import ComplexType
from xsdata.models.xsd import Element
from xsdata.models.xsd import SimpleType


class ClassAnalyzerTests(FactoryTestCase):
    @mock.patch.object(ClassAnalyzer, "select_classes")
    @mock.patch.object(ClassSanitizer, "process")
    @mock.patch.object(ClassContainer, "process")
    @mock.patch.object(ClassValidator, "process")
    def test_process(
        self,
        mock_validator_process,
        mock_container_process,
        mock_sanitizer_process,
        mock_select_classes,
    ):
        original_classes = ClassFactory.list(2)
        container = ClassContainer.from_list(original_classes)
        result_classes = ClassFactory.list(1)
        mock_select_classes.return_value = result_classes

        result = ClassAnalyzer.process(original_classes)

        self.assertEqual(result_classes, result)

        mock_validator_process.assert_called_once_with(container)
        mock_container_process.assert_called_once_with()
        mock_sanitizer_process.assert_called_once_with(container)
        mock_select_classes.assert_called_once_with(container)

    @mock.patch.object(Class, "should_generate", new_callable=mock.PropertyMock)
    @mock.patch.object(Class, "is_complex", new_callable=mock.PropertyMock)
    @mock.patch.object(ClassAnalyzer, "validate_references")
    def test_select_classes(
        self,
        mock_validate_references,
        mock_class_is_complex,
        mock_class_should_generate,
    ):
        mock_class_is_complex.return_value = True
        mock_class_should_generate.side_effect = [True, False, False, True, False]

        classes = ClassFactory.list(5)
        container = ClassContainer.from_list(classes)

        expected = [
            classes[0],
            classes[3],
        ]

        self.assertEqual(expected, ClassAnalyzer.select_classes(container))
        mock_validate_references.assert_called_once_with(expected)

    @mock.patch.object(Class, "is_complex", new_callable=mock.PropertyMock)
    def test_select_classes_when_no_complex_class_available(
        self, mock_class_is_complex
    ):
        mock_class_is_complex.return_value = False
        classes = [ClassFactory.enumeration(2), ClassFactory.create(type=SimpleType)]
        container = ClassContainer.from_list(classes)

        self.assertEqual(classes, ClassAnalyzer.select_classes(container))

    def test_class_references(self):
        target = ClassFactory.elements(
            2,
            inner=ClassFactory.list(2, attrs=AttrFactory.list(1)),
            extensions=ExtensionFactory.list(1),
        )

        actual = ClassAnalyzer.class_references(target)
        # +1 target
        # +2 attrs
        # +2 attr types
        # +1 extension
        # +1 extension type
        # +2 inner classes
        # +2 inner classes attrs
        # +2 inner classes attr types
        self.assertEqual(13, len(actual))
        self.assertEqual(id(target), actual[0])

    def test_validate_references(self):
        first = ClassFactory.elements(2)
        second = ClassFactory.create(attrs=first.attrs)

        ClassAnalyzer.validate_references([first])

        with self.assertRaises(AnalyzerValueError) as cm:
            ClassAnalyzer.validate_references([first, second])

        self.assertEqual("Cross references detected!", str(cm.exception))
