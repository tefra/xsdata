from pathlib import Path
from unittest import mock

from tests.factories import ClassFactory
from tests.factories import FactoryTestCase
from xsdata.codegen.analyzer import ClassAnalyzer
from xsdata.codegen.mappers.schema import SchemaMapper
from xsdata.codegen.transformer import SchemaTransformer
from xsdata.codegen.writer import CodeWriter
from xsdata.models.enums import Namespace
from xsdata.models.xsd import Import
from xsdata.models.xsd import Include
from xsdata.models.xsd import Override
from xsdata.models.xsd import Schema


class SchemaTransformerTests(FactoryTestCase):
    def setUp(self):
        self.transformer = SchemaTransformer(
            print=True, output="pydata", ns_struct=False
        )
        super().setUp()

    @mock.patch("xsdata.codegen.transformer.logger.info")
    @mock.patch.object(CodeWriter, "print")
    @mock.patch.object(CodeWriter, "designate")
    @mock.patch.object(SchemaTransformer, "analyze_classes")
    @mock.patch.object(SchemaTransformer, "assign_packages")
    @mock.patch.object(SchemaTransformer, "process_schema")
    def test_process_with_print_true(
        self,
        mock_process_schema,
        mock_assign_packages,
        mock_analyze_classes,
        mock_writer_designate,
        mock_writer_print,
        mock_logger_into,
    ):
        urls = ["http://xsdata/foo.xsd", "http://xsdata/bar.xsd"]
        package = "test"
        schema_classes = ClassFactory.list(3)
        analyzer_classes = ClassFactory.list(2)
        mock_analyze_classes.return_value = analyzer_classes

        self.transformer.class_map = {
            "http://xsdata/foo.xsd": schema_classes[:1],
            "http://xsdata/bar.xsd": schema_classes[1:],
        }

        self.transformer.process(urls, package)

        mock_process_schema.assert_has_calls(list(map(mock.call, urls)))
        mock_assign_packages.assert_called_once_with(package)
        mock_analyze_classes.assert_called_once_with(schema_classes)
        mock_writer_designate.assert_called_once_with(
            analyzer_classes, "pydata", package, self.transformer.ns_struct
        )
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
    @mock.patch.object(SchemaTransformer, "assign_packages")
    @mock.patch.object(SchemaTransformer, "process_schema")
    def test_process_with_print_false(
        self,
        mock_process_schema,
        mock_assign_packages,
        mock_analyze_classes,
        mock_writer_designate,
        mock_writer_write,
        mock_logger_into,
    ):
        urls = ["http://xsdata/foo.xsd", "http://xsdata/bar.xsd"]
        package = "test"
        schema_classes = ClassFactory.list(3)
        analyzer_classes = ClassFactory.list(2)
        mock_analyze_classes.return_value = analyzer_classes

        self.transformer.print = False
        self.transformer.class_map = {
            "http://xsdata/foo.xsd": schema_classes[:1],
            "http://xsdata/bar.xsd": schema_classes[1:],
        }

        self.transformer.process(urls, package)

        mock_process_schema.assert_has_calls(list(map(mock.call, urls)))
        mock_assign_packages.assert_called_once_with(package)
        mock_analyze_classes.assert_called_once_with(schema_classes)
        mock_writer_designate.assert_called_once_with(
            analyzer_classes, "pydata", package, self.transformer.ns_struct
        )
        mock_writer_write.assert_called_once_with(analyzer_classes, "pydata")
        mock_logger_into.assert_has_calls(
            [
                mock.call("Analyzer input: %d main and %d inner classes", 3, 0),
                mock.call("Analyzer output: %d main and %d inner classes", 2, 0),
            ]
        )

    @mock.patch("xsdata.codegen.transformer.logger.warning")
    @mock.patch.object(SchemaTransformer, "analyze_classes")
    @mock.patch.object(SchemaTransformer, "assign_packages")
    @mock.patch.object(SchemaTransformer, "process_schema")
    def test_process_with_zero_classes_after_analyze(
        self,
        mock_process_schema,
        mock_assign_packages,
        mock_analyze_classes,
        mock_logger_warning,
    ):
        urls = ["http://xsdata/foo.xsd", "http://xsdata/bar.xsd"]
        package = "test"

        self.transformer.process(urls, package)
        self.assertEqual(0, mock_analyze_classes.call_count)
        self.assertEqual(0, mock_assign_packages.call_count)

        mock_process_schema.assert_has_calls(list(map(mock.call, urls)))
        mock_logger_warning.assert_called_once_with("Analyzer returned zero classes!")

    @mock.patch("xsdata.codegen.transformer.logger.info")
    @mock.patch.object(SchemaTransformer, "generate_classes")
    @mock.patch.object(SchemaTransformer, "parse_schema")
    def test_process_schema(
        self, mock_parse_schema, mock_generate_classes, mock_logger_info,
    ):
        schema = Schema(target_namespace="thug")
        schema.includes.append(Include(location="foo"))
        schema.overrides.append(Override())
        schema.imports.append(Import(location="bar"))
        schema.imports.append(Import(location="fails"))
        schema_foo = Schema()
        schema_bar = Schema()

        mock_generate_classes.side_effect = [
            ClassFactory.list(1),
            ClassFactory.list(2),
            ClassFactory.list(3),
        ]

        mock_parse_schema.side_effect = [schema, schema_bar, None, schema_foo]

        self.transformer.process_schema("main", "foo-bar")

        self.assertEqual(["main", "bar", "fails", "foo"], self.transformer.processed)

        self.assertEqual(3, len(self.transformer.class_map))
        self.assertEqual(3, len(self.transformer.class_map["main"]))
        self.assertEqual(2, len(self.transformer.class_map["foo"]))
        self.assertEqual(1, len(self.transformer.class_map["bar"]))

        mock_logger_info.assert_has_calls(
            [
                mock.call("Parsing schema %s", "main"),
                mock.call("Parsing schema %s", "bar"),
                mock.call("Parsing schema %s", "fails"),
                mock.call("Parsing schema %s", "foo"),
            ]
        )

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

    @mock.patch("xsdata.codegen.transformer.logger.info")
    @mock.patch.object(SchemaTransformer, "count_classes")
    @mock.patch.object(SchemaMapper, "map")
    def test_generate_classes(
        self, mock_mapper_map, mock_count_classes, mock_logger_info,
    ):
        schema = Schema(location="edo.xsd")
        classes = ClassFactory.list(2)

        mock_mapper_map.return_value = classes
        mock_count_classes.return_value = 2, 4
        self.transformer.generate_classes(schema)

        mock_mapper_map.assert_called_once_with(schema)
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
        self.transformer.class_map = class_map

        self.transformer.assign_packages("foo.bar")

        self.assertEqual("foo.bar.coreschemas", class_map[core][0].package)
        self.assertEqual("foo.bar.coreschemas", class_map[core][0].inner[0].package)
        self.assertEqual("foo.bar.multicacheschemas", class_map[multi_one][0].package)
        self.assertEqual("foo.bar.multicacheschemas", class_map[multi_one][1].package)
        self.assertEqual("foo.bar.multicacheschemas", class_map[multi_two][0].package)
        self.assertEqual("foo.bar.bar", class_map[http_one][0].package)
        self.assertEqual("foo.bar", class_map[http_two][0].package)
        self.assertEqual("foo.bar", class_map[local_one][0].package)
        self.assertEqual("foo.bar", class_map[local_two][0].package)

    @mock.patch.object(ClassAnalyzer, "process")
    def test_analyze_classes(self, mock_process):
        classes = ClassFactory.list(2)
        mock_process.return_value = classes[1:]

        result = self.transformer.analyze_classes(classes)
        self.assertEqual(1, len(result))
        mock_process.assert_called_once_with(classes)
