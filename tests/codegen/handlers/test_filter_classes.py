from unittest import mock

from xsdata.codegen.container import ClassContainer
from xsdata.codegen.handlers import FilterClasses
from xsdata.models.config import GeneratorConfig
from xsdata.models.enums import Tag
from xsdata.utils.testing import ClassFactory, FactoryTestCase


class FilterClassesTests(FactoryTestCase):
    maxDiff = None

    def setUp(self) -> None:
        super().setUp()

        self.container = ClassContainer(config=GeneratorConfig())
        self.handler = FilterClasses(self.container)

    def test_filter_all_globals(self) -> None:
        complex_type = ClassFactory.elements(1)
        enum_1 = ClassFactory.enumeration(2)
        complex_type.attrs[0].types[0].reference = enum_1.ref

        simple_type = ClassFactory.simple_type()
        enum_2 = ClassFactory.enumeration(3)
        simple_type.attrs[0].types[0].reference = enum_2.ref

        element = ClassFactory.create(tag=Tag.ELEMENT, abstract=True)

        expected = [complex_type, enum_1, element]
        self.container.extend([complex_type, enum_1, simple_type, enum_2, element])
        self.handler.run()
        self.assertEqual(expected, list(self.container))

    @mock.patch("xsdata.codegen.handlers.filter_classes.logger.warning")
    def test_run_with_no_global_types(self, mock_warning) -> None:
        classes = [ClassFactory.enumeration(2), ClassFactory.simple_type()]
        self.container.extend(classes)
        self.handler.run()
        self.assertEqual(classes, list(self.container))

        mock_warning.assert_called_once_with(
            "No global types exist, will generate all types.",
        )
