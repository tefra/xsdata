from unittest import mock

from tests.factories import AttrFactory
from tests.factories import ClassFactory
from tests.factories import ExtensionFactory
from tests.factories import FactoryTestCase
from xsdata.codegen.analyzer import ClassAnalyzer
from xsdata.codegen.container import ClassContainer
from xsdata.codegen.sanitizer import ClassSanitizer
from xsdata.codegen.validator import ClassValidator
from xsdata.exceptions import AnalyzerError
from xsdata.models.xsd import ComplexType
from xsdata.models.xsd import Element
from xsdata.models.xsd import SimpleType


class ClassAnalyzerTests(FactoryTestCase):
    def test__init__(self):
        classes = ClassFactory.list(2)
        analyzer = ClassAnalyzer(classes)
        self.assertEqual(classes, list(analyzer.container.iterate()))

    @mock.patch.object(ClassAnalyzer, "select_classes")
    @mock.patch.object(ClassAnalyzer, "post_process")
    @mock.patch.object(ClassContainer, "process")
    @mock.patch.object(ClassAnalyzer, "pre_process")
    def test_process(
        self, mock_pre_process, mock_process, mock_post_process, mock_select_classes
    ):
        classes = ClassFactory.list(1)
        mock_select_classes.return_value = classes
        analyzer = ClassAnalyzer([])

        self.assertEqual(classes, analyzer.process())
        mock_pre_process.assert_called_once_with()
        mock_process.assert_called_once_with()
        mock_post_process.assert_called_once_with()
        mock_select_classes.assert_called_once_with()

    @mock.patch.object(ClassValidator, "process")
    @mock.patch.object(ClassValidator, "__init__", return_value=None)
    def test_pre_process(self, mock_validator, mock_validator_process):
        analyzer = ClassAnalyzer([])

        self.assertIsNone(analyzer.pre_process())
        mock_validator.assert_called_once_with(analyzer.container)
        mock_validator_process.assert_called_once_with()

    @mock.patch.object(ClassSanitizer, "process")
    @mock.patch.object(ClassSanitizer, "__init__", return_value=None)
    def test_post_process(self, mock_sanitizer, mock_sanitizer_process):
        analyzer = ClassAnalyzer([])

        self.assertIsNone(analyzer.post_process())
        mock_sanitizer.assert_called_once_with(analyzer.container)
        mock_sanitizer_process.assert_called_once_with()

    @mock.patch.object(ClassAnalyzer, "validate_references")
    def test_select_classes(self, mock_validate_references):
        classes = [
            ClassFactory.create(abstract=True, type=Element),
            ClassFactory.create(type=Element),
            ClassFactory.create(type=ComplexType),
            ClassFactory.create(type=SimpleType),
            ClassFactory.enumeration(2),
        ]

        analyzer = ClassAnalyzer(classes)

        expected = [
            classes[1],
            classes[2],
            classes[4],
        ]

        result = analyzer.select_classes()
        self.assertEqual(expected, result)
        mock_validate_references.assert_called_once_with(result)

    def test_select_classes_when_no_complex_class_available(self):
        classes = [ClassFactory.enumeration(2), ClassFactory.create(type=SimpleType)]
        analyzer = ClassAnalyzer(classes)

        self.assertEqual(classes, analyzer.select_classes())

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

        analyzer = ClassAnalyzer([])
        analyzer.validate_references([first])

        with self.assertRaises(AnalyzerError) as cm:
            analyzer.validate_references([first, second])

        self.assertEqual("Cross references detected!", str(cm.exception))
