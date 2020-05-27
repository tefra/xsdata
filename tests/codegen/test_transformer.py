from pathlib import Path
from unittest import mock

from tests.factories import ClassFactory
from tests.factories import FactoryTestCase
from xsdata.codegen.builder import ClassBuilder
from xsdata.codegen.transformer import SchemaTransformer
from xsdata.codegen.writer import CodeWriter
from xsdata.models.enums import Namespace
from xsdata.models.xsd import Include
from xsdata.models.xsd import Override
from xsdata.models.xsd import Schema


class SchemaTransformerTests(FactoryTestCase):
    def setUp(self):
        self.transformer = SchemaTransformer(print=True, output="pydata")

    @mock.patch("xsdata.codegen.transformer.logger.info")
    @mock.patch.object(CodeWriter, "print")
    @mock.patch.object(CodeWriter, "designate")
    @mock.patch.object(SchemaTransformer, "analyze_classes")
    @mock.patch.object(SchemaTransformer, "process_schemas")
    def test_process_with_print_true(
        self,
        mock_process_schemas,
        mock_analyze_classes,
        mock_writer_designate,
        mock_writer_print,
        mock_logger_into,
    ):
        path = Path(__file__)
        package = "test"
        schema_classes = ClassFactory.list(3)
        analyzer_classes = ClassFactory.list(2)
        mock_process_schemas.return_value = schema_classes
        mock_analyze_classes.return_value = analyzer_classes

        self.transformer.process(path, package)
        mock_process_schemas.assert_called_once_with(path, package)
        mock_analyze_classes.assert_called_once_with(schema_classes)
        mock_writer_designate.assert_called_once_with(analyzer_classes, "pydata")
        mock_writer_print.assert_called_once_with(analyzer_classes, "pydata")
        mock_logger_into.assert_has_calls(
            [
                mock.call("Analyzer input: %d main and %d inner classes", 3, 0),
                mock.call("Analyzer output: %d main and %d inner classes", 2, 0),
            ]
        )

    @mock.patch("xsdata.codegen.transformer.logger.info")
    @mock.patch.object(CodeWriter, "write")
    @mock.patch.object(CodeWriter, "designate")
    @mock.patch.object(SchemaTransformer, "analyze_classes")
    @mock.patch.object(SchemaTransformer, "process_schemas")
    def test_process_with_print_false(
        self,
        mock_process_schemas,
        mock_analyze_classes,
        mock_writer_designate,
        mock_writer_write,
        mock_logger_into,
    ):
        path = Path(__file__)
        package = "test"
        schema_classes = ClassFactory.list(3)
        analyzer_classes = ClassFactory.list(2)
        mock_process_schemas.return_value = schema_classes
        mock_analyze_classes.return_value = analyzer_classes

        self.transformer.print = False
        self.transformer.process(path, package)
        mock_process_schemas.assert_called_once_with(path, package)
        mock_analyze_classes.assert_called_once_with(schema_classes)
        mock_writer_designate.assert_called_once_with(analyzer_classes, "pydata")
        mock_writer_write.assert_called_once_with(analyzer_classes, "pydata")
        mock_logger_into.assert_has_calls(
            [
                mock.call("Analyzer input: %d main and %d inner classes", 3, 0),
                mock.call("Analyzer output: %d main and %d inner classes", 2, 0),
            ]
        )

    @mock.patch("xsdata.codegen.transformer.logger.warning")
    @mock.patch.object(SchemaTransformer, "analyze_classes")
    @mock.patch.object(SchemaTransformer, "process_schemas")
    def test_process_with_zero_classes_after_analyze(
        self, mock_process_schemas, mock_analyze_classes, mock_logger_warning,
    ):
        path = Path(__file__)
        package = "test"
        schema_classes = []
        mock_process_schemas.return_value = schema_classes

        self.transformer.process(path, package)
        self.assertEqual(0, mock_analyze_classes.call_count)
        mock_process_schemas.assert_called_once_with(path, package)
        mock_logger_warning.assert_called_once_with("Analyzer returned zero classes!")

    @mock.patch.object(SchemaTransformer, "assign_packages")
    @mock.patch.object(SchemaTransformer, "process_schema")
    def test_process_schemas(self, mock_process_schema, mock_assign_packages):
        classes = ClassFactory.list(5)
        mock_process_schema.side_effect = [dict(foo=classes[:2]), dict(bar=classes[2:])]
        schemas = [Path(), Path()]

        result = self.transformer.process_schemas(schemas, "foo")
        self.assertEqual(classes, result)
        mock_process_schema.assert_has_calls(
            [mock.call(schemas[0]), mock.call(schemas[1])]
        )
        mock_assign_packages.assert_called_once_with(
            dict(foo=classes[:2], bar=classes[2:]), "foo"
        )

    @mock.patch("xsdata.codegen.transformer.logger.info")
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
        schema = Schema.create(target_namespace="thug")
        schema.includes.append(include)
        schema.overrides.append(override)
        mock_process_included.side_effect = [
            dict(foo=ClassFactory.list(2)),
            dict(bar=ClassFactory.list(3)),
        ]
        mock_generate_classes.return_value = ClassFactory.list(4)

        mock_parse_schema.return_value = schema

        path = Path(__file__)
        result = self.transformer.process_schema(path, "foo-bar")
        self.assertEqual(3, len(result))
        self.assertEqual(2, len(result["foo"]))
        self.assertEqual(3, len(result["bar"]))
        self.assertEqual(4, len(result[path]))

        self.assertTrue(path in self.transformer.processed)

        mock_parse_schema.assert_called_once_with(path, "foo-bar")
        mock_process_included.assert_has_calls(
            [
                mock.call(include, schema.target_namespace),
                mock.call(override, schema.target_namespace),
            ]
        )

        self.transformer.process_schema(path, None)
        mock_logger_info.assert_called_once_with("Parsing schema...")

    @mock.patch("xsdata.codegen.transformer.logger.debug")
    @mock.patch.object(SchemaTransformer, "parse_schema")
    def test_process_schema_avoid_circular_imports(
        self, mock_parse_schema, mock_logger_debug
    ):
        path = Path(__file__).as_uri()
        self.transformer.processed.append(path)
        self.transformer.process_schema(path, None)

        self.assertEqual(0, mock_parse_schema.call_count)
        mock_logger_debug.assert_called_once_with(
            "Already processed skipping: %s", path
        )

    @mock.patch.object(SchemaTransformer, "parse_schema")
    def test_process_schema_skip_when_parse_schema_returns_none(
        self, mock_parse_schema
    ):
        path = Path(__file__).as_uri()
        mock_parse_schema.return_value = None
        result = self.transformer.process_schema(path, "ns")
        self.assertEqual(0, len(result))
        mock_parse_schema.assert_called_once_with(path, "ns")

    @mock.patch.object(SchemaTransformer, "process_schema")
    def test_process_included(self, mock_process_schema):
        path = Path(__file__)
        include = Include.create(location=path, schema_location="foo.xsd")
        mock_process_schema.return_value = ClassFactory.list(2)

        result = self.transformer.process_included(include, "thug")

        self.assertEqual(2, len(result))
        mock_process_schema.assert_called_once_with(path, "thug")

    @mock.patch("xsdata.codegen.transformer.logger.debug")
    def test_process_included_skip_when_location_already_imported(
        self, mock_logger_debug
    ):
        path = Path(__file__)
        include = Include.create(location=path)
        self.transformer.processed.append(path)

        result = self.transformer.process_included(include, "thug")

        self.assertIsInstance(result, dict)
        self.assertEqual(0, len(result))
        mock_logger_debug.assert_called_once_with(
            "%s: %s already included skipping..",
            include.class_name,
            include.schema_location,
        )

    @mock.patch("xsdata.codegen.transformer.logger.warning")
    def test_process_included_skip_when_location_is_missing(self, mock_logger_warning):
        include = Include.create()
        result = self.transformer.process_included(include, "thug")

        self.assertIsInstance(result, dict)
        self.assertEqual(0, len(result))
        mock_logger_warning.assert_called_once_with(
            "%s: %s unresolved schema location..",
            include.class_name,
            include.schema_location,
        )

    @mock.patch("xsdata.codegen.transformer.logger.info")
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
        schema = Schema.create(location="edo.xsd")
        classes = ClassFactory.list(2)

        mock_builder_build.return_value = classes
        mock_count_classes.return_value = 2, 4
        self.transformer.generate_classes(schema)

        mock_builder_init.assert_called_once_with(schema=schema)
        mock_builder_build.assert_called_once_with()
        mock_logger_info.assert_has_calls(
            [
                mock.call("Compiling schema %s", schema.location),
                mock.call("Builder: %d main and %d inner classes", 2, 4),
            ]
        )

    def test_parse_schema(self):
        path = Path(__file__).parent.joinpath("../fixtures/books.xsd").as_uri()
        schema = self.transformer.parse_schema(path, "foo.bar")
        self.assertIsInstance(schema, Schema)
        self.assertEqual(2, len(schema.complex_types))

    @mock.patch("xsdata.codegen.transformer.logger.warning")
    @mock.patch("xsdata.codegen.transformer.urlopen")
    def test_parse_schema_with_os_exception(self, mock_urlopen, mock_logger_warning):
        mock_urlopen.side_effect = FileNotFoundError

        path = Path(__file__).parent.joinpath("fixtures/books.xsd").as_uri()
        schema = self.transformer.parse_schema(path, "foo")
        self.assertIsNone(schema)
        mock_logger_warning.assert_called_once_with("Schema not found %s", path)

    def test_count_classes(self):
        classes = ClassFactory.list(
            2, inner=ClassFactory.list(2, inner=ClassFactory.list(3))
        )

        self.assertEqual((2, 16), self.transformer.count_classes(classes))

    def test_assign_packages(self):
        core = "file://HL7V3/NE2008/coreschemas/voc.xsd"
        multi_one = "file://HL7V3/NE2008/multicacheschemas/PRPA_MT201307UV02.xsd"
        multi_two = "file://HL7V3/NE2008/multicacheschemas/COCT_MT080000UV.xsd"
        http_one = "http://xsdata/foo/bar/schema.xsd"
        http_two = "http://xsdata/foo/common.xsd"
        local_one = Namespace.XSI.location
        local_two = Namespace.XLINK.location

        class_map = {
            core: ClassFactory.list(1, inner=[ClassFactory.create()]),
            multi_one: ClassFactory.list(2),
            multi_two: ClassFactory.list(1),
            http_one: ClassFactory.list(1),
            http_two: ClassFactory.list(1),
            local_one: ClassFactory.list(1),
            local_two: ClassFactory.list(1),
        }

        self.transformer.assign_packages(class_map, "foo.bar")

        self.assertEqual("foo.bar.coreschemas", class_map[core][0].package)
        self.assertEqual("foo.bar.coreschemas", class_map[core][0].inner[0].package)
        self.assertEqual("foo.bar.multicacheschemas", class_map[multi_one][0].package)
        self.assertEqual("foo.bar.multicacheschemas", class_map[multi_one][1].package)
        self.assertEqual("foo.bar.multicacheschemas", class_map[multi_two][0].package)
        self.assertEqual("foo.bar.bar", class_map[http_one][0].package)
        self.assertEqual("foo.bar", class_map[http_two][0].package)
        self.assertEqual("foo.bar", class_map[local_one][0].package)
        self.assertEqual("foo.bar", class_map[local_two][0].package)
