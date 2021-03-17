from unittest import mock

from xsdata.codegen.analyzer import ClassAnalyzer
from xsdata.codegen.container import ClassContainer
from xsdata.codegen.sanitizer import ClassSanitizer
from xsdata.codegen.validator import ClassValidator
from xsdata.exceptions import AnalyzerValueError
from xsdata.models.config import GeneratorConfig
from xsdata.utils.testing import AttrFactory
from xsdata.utils.testing import ClassFactory
from xsdata.utils.testing import ExtensionFactory
from xsdata.utils.testing import FactoryTestCase


class ClassAnalyzerTests(FactoryTestCase):
    @mock.patch.object(ClassAnalyzer, "validate_references")
    @mock.patch.object(ClassSanitizer, "process")
    @mock.patch.object(ClassContainer, "filter_classes")
    @mock.patch.object(ClassContainer, "process")
    @mock.patch.object(ClassValidator, "process")
    def test_process(
        self,
        mock_validator_process,
        mock_container_process,
        mock_container_filter_classes,
        mock_sanitizer_process,
        mock_validate_references,
    ):
        config = GeneratorConfig()
        classes = ClassFactory.list(2)
        container = ClassContainer(config=config)
        container.extend(classes)

        result = ClassAnalyzer.process(container)

        self.assertEqual(classes, result)

        mock_validator_process.assert_called_once_with()
        mock_container_process.assert_called_once_with()
        mock_container_filter_classes.assert_called_once_with()
        mock_sanitizer_process.assert_called_once_with()
        mock_validate_references.assert_called_once_with(classes)

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
