from pathlib import Path
from unittest import mock

from tests.factories import ClassFactory
from tests.factories import FactoryTestCase
from xsdata.analyzer import ClassAnalyzer
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
    @mock.patch.object(Schema, "included")
    @mock.patch.object(SchemaTransformer, "generate_code")
    @mock.patch.object(SchemaTransformer, "process_included")
    @mock.patch.object(SchemaTransformer, "parse_schema")
    def test_process(
        self,
        mock_parse_schema,
        mock_process_included,
        mock_generate_code,
        mock_included,
        mock_logger_info,
    ):
        include = Include.create()
        override = Override.create()
        redefine = Redefine.create()
        schema = Schema.create(target_namespace="thug")

        mock_parse_schema.return_value = schema
        mock_included.return_value = [include, override]

        path = Path(__file__)
        self.transformer.process(
            path, package="foo.bar", target_namespace="foo-bar", redefine=redefine
        )

        self.assertTrue(path in self.transformer.processed)

        mock_parse_schema.assert_called_once_with(path, "foo-bar")
        mock_process_included.assert_has_calls(
            [
                mock.call(include, "foo.bar", schema.target_namespace),
                mock.call(override, "foo.bar", schema.target_namespace),
            ]
        )
        mock_generate_code.assert_called_once_with(schema, "foo.bar", redefine)

        self.transformer.process(path, None, None, None)
        mock_logger_info.assert_called_once_with("Parsing schema...")

    @mock.patch("xsdata.transformer.logger.debug")
    @mock.patch.object(SchemaTransformer, "parse_schema")
    def test_process_avoid_processing_twice_circular_imports(
        self, mock_parse_schema, mock_logger_debug
    ):
        path = Path(__file__)
        self.transformer.processed.append(path)
        self.transformer.process(path, "foo.bar", None, None)

        self.assertEqual(0, mock_parse_schema.call_count)
        mock_logger_debug.assert_called_once_with(
            "Circular import skipping: %s", path.name
        )

    @mock.patch.object(SchemaTransformer, "process")
    @mock.patch.object(SchemaTransformer, "adjust_package")
    def test_process_included(self, mock_adjust_package, mock_process):
        path = Path(__file__)
        include = Include.create(location=path, schema_location="foo.xsd")
        mock_adjust_package.return_value = "adjusted.foo.bar"

        self.transformer.process_included(include, "foo.bar", "thug")
        self.assertTrue(path in self.transformer.included)

        mock_adjust_package.assert_called_once_with("foo.bar", include.schema_location)
        mock_process.assert_called_once_with(
            path, package="adjusted.foo.bar", target_namespace="thug", redefine=None
        )

    @mock.patch.object(SchemaTransformer, "process")
    @mock.patch.object(SchemaTransformer, "adjust_package")
    def test_process_included_with_redefine(self, mock_adjust_package, mock_process):
        path = Path(__file__)
        redefine = Redefine.create(location=path)
        mock_adjust_package.return_value = "adjusted.foo.bar"

        self.transformer.process_included(redefine, "foo.bar", "thug")
        self.assertTrue(path in self.transformer.included)

        mock_process.assert_called_once_with(
            path, package="adjusted.foo.bar", target_namespace="thug", redefine=redefine
        )

    @mock.patch("xsdata.transformer.logger.debug")
    def test_process_included_skip_when_location_already_imported(
        self, mock_logger_debug
    ):
        path = Path(__file__)
        include = Include.create(location=path)
        self.transformer.included.append(path)

        self.transformer.process_included(include, "foo.bar", "thug")
        mock_logger_debug.assert_called_once_with(
            "%s: %s already included skipping..",
            include.class_name,
            include.schema_location,
        )

    @mock.patch("xsdata.transformer.logger.warning")
    def test_process_included_skip_when_location_is_missing(self, mock_logger_warning):
        include = Include.create()
        self.transformer.process_included(include, "foo.bar", "thug")

        mock_logger_warning.assert_called_once_with(
            "%s: %s unresolved schema location..",
            include.class_name,
            include.schema_location,
        )

    @mock.patch("xsdata.transformer.logger.info")
    @mock.patch.object(CodeWriter, "print")
    @mock.patch.object(SchemaTransformer, "count_classes")
    @mock.patch.object(ClassAnalyzer, "process")
    @mock.patch.object(ClassBuilder, "build")
    @mock.patch.object(ClassBuilder, "__init__", return_value=None)
    def test_generate_code(
        self,
        mock_builder_init,
        mock_builder_build,
        mock_analyzer_process,
        mock_count_classes,
        mock_writer_print,
        mock_logger_info,
    ):
        schema = Schema.create()
        redefine = Redefine.create()
        classes = ClassFactory.list(2)
        final_classes = classes[1:]

        mock_builder_build.return_value = classes
        mock_analyzer_process.return_value = final_classes
        mock_count_classes.return_value = 2, 4
        self.transformer.generate_code(schema, "foo.bar", redefine)

        mock_builder_init.assert_called_once_with(schema, redefine)
        mock_builder_build.assert_called_once_with()
        mock_analyzer_process.assert_called_once_with(classes)
        mock_logger_info.assert_has_calls(
            [
                mock.call("Compiling schema..."),
                mock.call("Compiled %d main and %d inner classes", 2, 4),
            ]
        )
        mock_writer_print(schema, final_classes, "foo.bar", self.transformer.format)

    @mock.patch.object(CodeWriter, "write")
    @mock.patch.object(SchemaTransformer, "count_classes")
    @mock.patch.object(ClassAnalyzer, "process")
    @mock.patch.object(ClassBuilder, "build")
    @mock.patch.object(ClassBuilder, "__init__", return_value=None)
    def test_generate_code_when_print_is_false(
        self,
        mock_builder_init,
        mock_builder_build,
        mock_analyzer_process,
        mock_count_classes,
        mock_writer_write,
    ):
        schema = Schema.create()
        redefine = Redefine.create()
        classes = ClassFactory.list(2)

        mock_builder_build.return_value = classes
        mock_analyzer_process.return_value = classes
        mock_count_classes.return_value = 2, 4
        self.transformer.print = False
        self.transformer.generate_code(schema, "foo.bar", redefine)

        mock_writer_write(schema, classes, "foo.bar", self.transformer.format)

    @mock.patch("xsdata.transformer.logger.info")
    @mock.patch.object(CodeWriter, "print")
    @mock.patch.object(ClassAnalyzer, "process")
    @mock.patch.object(ClassBuilder, "build")
    @mock.patch.object(ClassBuilder, "__init__", return_value=None)
    def test_generate_code_when_analyzer_returns_no_classes(
        self,
        mock_builder_init,
        mock_builder_build,
        mock_analyzer_process,
        mock_writer_print,
        mock_logger_info,
    ):
        schema = Schema.create()
        classes = ClassFactory.list(2)

        mock_builder_build.return_value = classes
        mock_analyzer_process.return_value = []
        self.transformer.generate_code(schema, "foo.bar", None)
        self.assertEqual(0, mock_writer_print.call_count)

        mock_builder_init.assert_called_once_with(schema, None)
        mock_builder_build.assert_called_once_with()
        mock_analyzer_process.assert_called_once_with(classes)
        mock_logger_info.assert_called_once_with("Compiling schema...")

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
