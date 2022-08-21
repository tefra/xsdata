from unittest import mock

from xsdata.codegen.container import ClassContainer
from xsdata.codegen.handlers import FilterClasses
from xsdata.models.config import ClassFilterStrategy
from xsdata.models.config import GeneratorConfig
from xsdata.models.enums import Tag
from xsdata.utils.testing import AttrFactory
from xsdata.utils.testing import ClassFactory
from xsdata.utils.testing import FactoryTestCase


class FilterClassesTests(FactoryTestCase):
    maxDiff = None

    def setUp(self):
        super().setUp()

        self.container = ClassContainer(config=GeneratorConfig())
        self.handler = FilterClasses(self.container)

    def test_filter_all_globals(self):
        complex_type = ClassFactory.elements(1)
        enum_1 = ClassFactory.enumeration(2)
        complex_type.attrs[0].types[0].reference = enum_1.ref

        simple_type = ClassFactory.simple_type()
        enum_2 = ClassFactory.enumeration(3)
        simple_type.attrs[0].types[0].reference = enum_2.ref

        element = ClassFactory.create(tag=Tag.ELEMENT, abstract=True)

        expected = [complex_type, enum_1]
        self.container.extend([complex_type, enum_1, simple_type, enum_2, element])
        self.handler.run()
        self.assertEqual(expected, list(self.container))

    def test_filter_referred_globals(self):
        self.container.config.output.filter_strategy = (
            ClassFilterStrategy.REFERRED_GLOBALS
        )

        element_1 = ClassFactory.create(tag=Tag.ELEMENT, attrs=AttrFactory.list(2))
        element_2 = ClassFactory.create(tag=Tag.ELEMENT, attrs=AttrFactory.list(2))
        enum_1 = ClassFactory.enumeration(2)
        element_2.attrs[0].types[0].reference = enum_1.ref

        expected = [element_2, enum_1]
        self.container.extend([element_1, element_2, enum_1])
        self.handler.run()
        self.assertEqual(expected, list(self.container))

    def test_filter_all(self):
        simple_type = ClassFactory.simple_type()
        enumeration = ClassFactory.enumeration(2)
        complex_type = ClassFactory.elements(2)
        self.container.extend([simple_type, enumeration, complex_type])
        self.container.config.output.filter_strategy = ClassFilterStrategy.ALL

        self.handler.run()
        self.assertEqual(3, len(list(self.container)))

    @mock.patch("xsdata.codegen.handlers.filter_classes.logger.warning")
    def test_run_with_strategy_not_all_with_no_classes(self, mock_warning):
        classes = [ClassFactory.enumeration(2), ClassFactory.simple_type()]
        self.container.extend(classes)
        self.handler.run()
        self.assertEqual(classes, list(self.container))

        mock_warning.assert_called_once_with(
            "The filter strategy '%s' returned no classes, will generate all types.",
            "allGlobals",
        )
