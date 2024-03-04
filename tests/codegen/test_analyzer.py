from unittest import mock

from xsdata.codegen.analyzer import ClassAnalyzer
from xsdata.codegen.container import ClassContainer
from xsdata.codegen.validator import ClassValidator
from xsdata.exceptions import AnalyzerValueError
from xsdata.models.config import GeneratorConfig
from xsdata.utils.testing import (
    AttrFactory,
    ClassFactory,
    FactoryTestCase,
)


class ClassAnalyzerTests(FactoryTestCase):
    @mock.patch.object(ClassAnalyzer, "validate_references")
    @mock.patch.object(ClassContainer, "process")
    @mock.patch.object(ClassValidator, "process")
    def test_process(
        self,
        mock_validator_process,
        mock_container_process,
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
        mock_validate_references.assert_called_once_with(classes)

    def test_validate_with_cross_references(self):
        first = ClassFactory.elements(2)
        second = ClassFactory.create(attrs=first.attrs)

        ClassAnalyzer.validate_references([first])

        with self.assertRaises(AnalyzerValueError) as cm:
            ClassAnalyzer.validate_references([first, second])

        self.assertEqual("Cross reference detected", str(cm.exception))

    def test_validate_unresolved_references(self):
        first = ClassFactory.create()
        first.attrs.append(AttrFactory.reference("foo"))

        with self.assertRaises(AnalyzerValueError) as cm:
            ClassAnalyzer.validate_references([first])

        self.assertEqual("Unresolved reference", str(cm.exception))
