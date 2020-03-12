from pathlib import Path
from unittest import mock

from tests.factories import ClassFactory
from tests.factories import FactoryTestCase
from xsdata.builder import ClassBuilder
from xsdata.models.elements import Include
from xsdata.models.elements import Override
from xsdata.models.elements import Redefine
from xsdata.models.elements import Schema
from xsdata.transformer import SchemaTransformer
from xsdata.writer import CodeWriter


class SchemaTransformerTests(FactoryTestCase):
    def setUp(self) -> None:
        self.transformer = SchemaTransformer(print=True, format="pydata")

    @mock.patch("xsdata.transformer.logger.info")
    @mock.patch.object(CodeWriter, "print")
    @mock.patch.object(CodeWriter, "designate")
    @mock.patch.object(SchemaTransformer, "count_classes")
    @mock.patch.object(SchemaTransformer, "analyze_classes")
    @mock.patch.object(SchemaTransformer, "process_schema")
    def test_process_with_print_true(
        self,
        mock_process_schema,
        mock_analyze_classes,
        mock_count_classes,
        mock_writer_designate,
        mock_writer_print,
        mock_logger_into,
    ):
        path = Path(__file__)
        package = "test"
        schema_classes = ClassFactory.list(2)
        analyzer_classes = ClassFactory.list(2)
        mock_count_classes.return_value = 1, 2
        mock_process_schema.return_value = schema_classes
        mock_analyze_classes.return_value = analyzer_classes

        self.transformer.process(path, package)
        mock_process_schema.assert_called_once_with(path, package)
        mock_analyze_classes.assert_called_once_with(schema_classes)
        mock_count_classes.assert_called_once_with(analyzer_classes)
        mock_writer_designate.assert_called_once_with(analyzer_classes, "pydata")
        mock_writer_print.assert_called_once_with(analyzer_classes, "pydata")
        mock_logger_into.assert_called_once_with(
            "Analyzer: %d main and %d inner classes", 1, 2
        )

    @mock.patch("xsdata.transformer.logger.info")
    @mock.patch.object(CodeWriter, "write")
    @mock.patch.object(CodeWriter, "designate")
    @mock.patch.object(SchemaTransformer, "count_classes")
    @mock.patch.object(SchemaTransformer, "analyze_classes")
    @mock.patch.object(SchemaTransformer, "process_schema")
    def test_process_with_print_false(
        self,
        mock_process_schema,
        mock_analyze_classes,
        mock_count_classes,
        mock_writer_designate,
        mock_writer_write,
        mock_logger_into,
    ):
        path = Path(__file__)
        package = "test"
        schema_classes = ClassFactory.list(2)
        analyzer_classes = ClassFactory.list(2)
        mock_count_classes.return_value = 1, 2
        mock_process_schema.return_value = schema_classes
        mock_analyze_classes.return_value = analyzer_classes

        self.transformer.print = False
        self.transformer.process(path, package)
        mock_process_schema.assert_called_once_with(path, package)
        mock_analyze_classes.assert_called_once_with(schema_classes)
        mock_count_classes.assert_called_once_with(analyzer_classes)
        mock_writer_designate.assert_called_once_with(analyzer_classes, "pydata")
        mock_writer_write.assert_called_once_with(analyzer_classes, "pydata")
        mock_logger_into.assert_called_once_with(
            "Analyzer: %d main and %d inner classes", 1, 2
        )

    @mock.patch("xsdata.transformer.logger.warning")
    @mock.patch.object(SchemaTransformer, "count_classes")
    @mock.patch.object(SchemaTransformer, "analyze_classes")
    @mock.patch.object(SchemaTransformer, "process_schema")
    def test_process_with_zero_classes_after_analyze(
        self,
        mock_process_schema,
        mock_analyze_classes,
        mock_count_classes,
        mock_logger_warning,
    ):
        path = Path(__file__)
        package = "test"
        schema_classes = ClassFactory.list(2)
        analyzer_classes = []
        mock_count_classes.return_value = 0, 0
        mock_process_schema.return_value = schema_classes
        mock_analyze_classes.return_value = analyzer_classes

        self.transformer.process(path, package)
        mock_process_schema.assert_called_once_with(path, package)
        mock_analyze_classes.assert_called_once_with(schema_classes)
        mock_count_classes.assert_called_once_with(analyzer_classes)
        mock_logger_warning.assert_called_once_with("Analyzer returned zero classes!")

    @mock.patch("xsdata.transformer.logger.info")
    @mock.patch.object(SchemaTransformer, "generate_classes")
    @mock.patch.object(SchemaTransformer, "process_included")
    @mock.patch.object(SchemaTransformer, "parse_schema")
    def test_process_schema(
        self,
        mock_parse_schema,
        mock_process_included,
        mock_generate_classes,
        mock_logger_info,
    ):
        include = Include.create()
        override = Override.create()
        redefine = Redefine.create()
        schema = Schema.create(target_namespace="thug")
        schema.includes.append(include)
        schema.overrides.append(override)
        mock_process_included.side_effect = [ClassFactory.list(2), ClassFactory.list(3)]
        mock_generate_classes.return_value = ClassFactory.list(4)

        mock_parse_schema.return_value = schema

        path = Path(__file__)
        result = self.transformer.process_schema(
            path, package="foo.bar", target_namespace="foo-bar", redefine=redefine
        )

        self.assertEqual(9, len(result))
        self.assertTrue(path in self.transformer.processed)

        mock_parse_schema.assert_called_once_with(path, "foo-bar")
        mock_process_included.assert_has_calls(
            [
                mock.call(include, "foo.bar", schema.target_namespace),
                mock.call(override, "foo.bar", schema.target_namespace),
            ]
        )

        self.transformer.process_schema(path, None, None, None)
        mock_logger_info.assert_called_once_with("Parsing schema...")

    @mock.patch("xsdata.transformer.logger.debug")
    @mock.patch.object(SchemaTransformer, "parse_schema")
    def test_process_schema_avoid_circular_imports(
        self, mock_parse_schema, mock_logger_debug
    ):
        path = Path(__file__)
        self.transformer.processed.append(path)
        self.transformer.process_schema(path, "foo.bar", None, None)

        self.assertEqual(0, mock_parse_schema.call_count)
        mock_logger_debug.assert_called_once_with(
            "Already processed skipping: %s", path.name
        )

    @mock.patch.object(SchemaTransformer, "process_schema")
    @mock.patch.object(SchemaTransformer, "adjust_package")
    def test_process_included(self, mock_adjust_package, mock_process_schema):
        path = Path(__file__)
        include = Include.create(location=path, schema_location="foo.xsd")
        mock_adjust_package.return_value = "adjusted.foo.bar"
        mock_process_schema.return_value = ClassFactory.list(2)

        result = self.transformer.process_included(include, "foo.bar", "thug")

        self.assertEqual(2, len(result))
        mock_adjust_package.assert_called_once_with("foo.bar", include.schema_location)
        mock_process_schema.assert_called_once_with(
            path, package="adjusted.foo.bar", target_namespace="thug", redefine=None
        )

    @mock.patch.object(SchemaTransformer, "process_schema")
    @mock.patch.object(SchemaTransformer, "adjust_package")
    def test_process_included_with_redefine(
        self, mock_adjust_package, mock_process_schema
    ):
        path = Path(__file__)
        redefine = Redefine.create(location=path)
        mock_adjust_package.return_value = "adjusted.foo.bar"
        mock_process_schema.return_value = ClassFactory.list(2)

        result = self.transformer.process_included(redefine, "foo.bar", "thug")

        self.assertEqual(2, len(result))
        mock_process_schema.assert_called_once_with(
            path, package="adjusted.foo.bar", target_namespace="thug", redefine=redefine
        )

    @mock.patch("xsdata.transformer.logger.debug")
    def test_process_included_skip_when_location_already_imported(
        self, mock_logger_debug
    ):
        path = Path(__file__)
        include = Include.create(location=path)
        self.transformer.processed.append(path)

        result = self.transformer.process_included(include, "foo.bar", "thug")

        self.assertIsInstance(result, list)
        self.assertEqual(0, len(result))
        mock_logger_debug.assert_called_once_with(
            "%s: %s already included skipping..",
            include.class_name,
            include.schema_location,
        )

    @mock.patch("xsdata.transformer.logger.warning")
    def test_process_included_skip_when_location_is_missing(self, mock_logger_warning):
        include = Include.create()
        result = self.transformer.process_included(include, "foo.bar", "thug")

        self.assertIsInstance(result, list)
        self.assertEqual(0, len(result))
        mock_logger_warning.assert_called_once_with(
            "%s: %s unresolved schema location..",
            include.class_name,
            include.schema_location,
        )

    @mock.patch("xsdata.transformer.logger.info")
    @mock.patch.object(SchemaTransformer, "count_classes")
    @mock.patch.object(ClassBuilder, "build")
    @mock.patch.object(ClassBuilder, "__init__", return_value=None)
    def test_generate_classes(
        self,
        mock_builder_init,
        mock_builder_build,
        mock_count_classes,
        mock_logger_info,
    ):
        schema = Schema.create()
        redefine = Redefine.create()
        classes = ClassFactory.list(2)

        mock_builder_build.return_value = classes
        mock_count_classes.return_value = 2, 4
        self.transformer.generate_classes(schema, "foo.bar", redefine)

        mock_builder_init.assert_called_once_with(
            schema=schema, package="foo.bar", redefine=redefine
        )
        mock_builder_build.assert_called_once_with()
        mock_logger_info.assert_has_calls(
            [
                mock.call("Compiling schema..."),
                mock.call("Builder: %d main and %d inner classes", 2, 4),
            ]
        )

    def test_parse_schema(self):
        path = Path(__file__).parent.joinpath("fixtures/books.xsd")
        schema = self.transformer.parse_schema(path, target_namespace="foo.bar")
        self.assertIsInstance(schema, Schema)
        self.assertEqual(2, len(schema.complex_types))

    def test_adjust_package(self):
        actual = self.transformer.adjust_package("foo.bar", "../common.xsd")
        self.assertEqual("foo", actual)

        actual = self.transformer.adjust_package("foo.bar", "../common/bar.xsd")
        self.assertEqual("foo.common", actual)

        actual = self.transformer.adjust_package("foo.bar", "")
        self.assertEqual("foo.bar", actual)

        actual = self.transformer.adjust_package("foo.bar", "http://www.yes.no")
        self.assertEqual("foo.bar", actual)

    def test_count_classes(self):
        classes = ClassFactory.list(
            2, inner=ClassFactory.list(2, inner=ClassFactory.list(3))
        )

        self.assertEqual((2, 16), self.transformer.count_classes(classes))
