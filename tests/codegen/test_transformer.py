import tempfile
from pathlib import Path
from unittest import mock

from xsdata.codegen.analyzer import ClassAnalyzer
from xsdata.codegen.container import ClassContainer
from xsdata.codegen.mappers.definitions import DefinitionsMapper
from xsdata.codegen.mappers.element import ElementMapper
from xsdata.codegen.mappers.schema import SchemaMapper
from xsdata.codegen.parsers import DefinitionsParser
from xsdata.codegen.transformer import SchemaTransformer
from xsdata.codegen.writer import CodeWriter
from xsdata.exceptions import CodeGenerationError
from xsdata.formats.dataclass.models.generics import AnyElement
from xsdata.formats.dataclass.parsers import TreeParser
from xsdata.models.config import GeneratorConfig
from xsdata.models.enums import Namespace
from xsdata.models.wsdl import Binding
from xsdata.models.wsdl import Definitions
from xsdata.models.wsdl import Types
from xsdata.models.xsd import Import
from xsdata.models.xsd import Include
from xsdata.models.xsd import Override
from xsdata.models.xsd import Schema
from xsdata.utils.testing import ClassFactory
from xsdata.utils.testing import FactoryTestCase


class SchemaTransformerTests(FactoryTestCase):
    def setUp(self):
        config = GeneratorConfig()
        self.transformer = SchemaTransformer(print=True, config=config)
        super().setUp()

    @mock.patch.object(SchemaTransformer, "process_classes")
    @mock.patch.object(SchemaTransformer, "process_documents")
    @mock.patch.object(SchemaTransformer, "process_schemas")
    @mock.patch.object(SchemaTransformer, "process_definitions")
    def test_process(
        self,
        mock_process_definitions,
        mock_process_schemas,
        mock_process_documents,
        mock_process_classes,
    ):
        uris = [
            "a.wsdl",
            "b.wsdl",
            "c.xsd",
            "d.xsd",
            "e.xml",
            "f.xml",
        ]

        self.transformer.process(uris)
        mock_process_definitions.assert_called_once_with(uris[:2])
        mock_process_schemas.assert_called_once_with(uris[2:4])
        mock_process_documents.assert_called_once_with(uris[4:])
        mock_process_classes.assert_called_once_with()

    @mock.patch.object(SchemaTransformer, "convert_schema")
    @mock.patch.object(SchemaTransformer, "convert_definitions")
    @mock.patch.object(SchemaTransformer, "parse_definitions")
    def test_process_definitions(
        self,
        mock_parse_definitions,
        mock_convert_definitions,
        mock_convert_schema,
    ):
        uris = [
            "http://xsdata/services.wsdl",
            "http://xsdata/abstractServices.wsdl",
            "http://xsdata/notfound.wsdl",
        ]
        fist_def = Definitions(types=Types(schemas=[Schema(), Schema()]))
        second_def = Definitions(bindings=[Binding()])
        mock_parse_definitions.side_effect = [fist_def, second_def, None]
        self.transformer.process_definitions(uris)

        mock_convert_schema.assert_has_calls([mock.call(x) for x in fist_def.schemas])
        mock_parse_definitions.assert_has_calls(
            [mock.call(uris[0], namespace=None), mock.call(uris[1], namespace=None)]
        )
        mock_convert_definitions.assert_called_once_with(fist_def)

    @mock.patch.object(SchemaTransformer, "process_schema")
    def test_process_schemas(self, mock_process_schema):
        uris = ["http://xsdata/foo.xsd", "http://xsdata/bar.xsd"]

        self.transformer.process_schemas(uris)

        mock_process_schema.assert_has_calls([mock.call(uri) for uri in uris])

    @mock.patch.object(ElementMapper, "reduce")
    @mock.patch.object(ElementMapper, "map")
    @mock.patch.object(TreeParser, "from_bytes")
    @mock.patch.object(SchemaTransformer, "load_resource")
    def test_process_documents(
        self, mock_load_resource, mock_from_bytes, mock_map, mock_reduce
    ):
        uris = ["foo/a.xml", "foo/b.xml", "foo/c.xml"]
        resources = [b"a", None, b"c"]
        elements = [AnyElement(), AnyElement()]

        classes_a = ClassFactory.list(2)
        classes_c = ClassFactory.list(3)

        mock_load_resource.side_effect = resources
        mock_from_bytes.side_effect = elements
        mock_map.side_effect = [classes_a, classes_c]
        mock_reduce.return_value = classes_a + classes_c

        self.transformer.process_documents(uris)

        self.assertIn("foo", self.transformer.class_map)
        self.assertEqual(5, len(self.transformer.class_map["foo"]))

        mock_from_bytes.assert_has_calls(
            [mock.call(resources[0]), mock.call(resources[2])]
        )
        mock_map.assert_has_calls([mock.call(x) for x in elements])
        mock_reduce.assert_called_once_with(classes_a + classes_c)

    @mock.patch("xsdata.codegen.transformer.logger.info")
    @mock.patch.object(CodeWriter, "print")
    @mock.patch.object(SchemaTransformer, "analyze_classes")
    @mock.patch.object(SchemaTransformer, "assign_packages")
    def test_process_classes_with_print_true(
        self,
        mock_assign_packages,
        mock_analyze_classes,
        mock_writer_print,
        mock_logger_into,
    ):
        schema_classes = ClassFactory.list(3)
        analyzer_classes = ClassFactory.list(2)
        mock_analyze_classes.return_value = analyzer_classes

        self.transformer.class_map = {
            "http://xsdata/foo.xsd": schema_classes[:1],
            "http://xsdata/bar.xsd": schema_classes[1:],
        }

        self.transformer.process_classes()

        mock_assign_packages.assert_called_once_with()
        mock_analyze_classes.assert_called_once_with(schema_classes)
        mock_writer_print.assert_called_once_with(analyzer_classes)
        mock_logger_into.assert_has_calls(
            [
                mock.call("Analyzer input: %d main and %d inner classes", 3, 0),
                mock.call("Analyzer output: %d main and %d inner classes", 2, 0),
            ]
        )

    @mock.patch("xsdata.codegen.transformer.logger.info")
    @mock.patch.object(CodeWriter, "write")
    @mock.patch.object(SchemaTransformer, "analyze_classes")
    @mock.patch.object(SchemaTransformer, "assign_packages")
    def test_process_classes_with_print_false(
        self,
        mock_assign_packages,
        mock_analyze_classes,
        mock_writer_write,
        mock_logger_into,
    ):
        schema_classes = ClassFactory.list(3)
        analyzer_classes = ClassFactory.list(2)
        mock_analyze_classes.return_value = analyzer_classes

        self.transformer.print = False
        self.transformer.class_map = {
            "http://xsdata/foo.xsd": schema_classes[:1],
            "http://xsdata/bar.xsd": schema_classes[1:],
        }

        self.transformer.process_classes()

        mock_assign_packages.assert_called_once_with()
        mock_analyze_classes.assert_called_once_with(schema_classes)
        mock_writer_write.assert_called_once_with(analyzer_classes)
        mock_logger_into.assert_has_calls(
            [
                mock.call("Analyzer input: %d main and %d inner classes", 3, 0),
                mock.call("Analyzer output: %d main and %d inner classes", 2, 0),
            ]
        )

    def test_process_classes_with_zero_classes_after_analyze(self):
        with self.assertRaises(CodeGenerationError) as cm:
            self.transformer.process_classes()

        self.assertEqual("Nothing to generate.", str(cm.exception))

    @mock.patch.object(SchemaTransformer, "convert_schema")
    @mock.patch.object(SchemaTransformer, "parse_schema")
    def test_process_schema(
        self,
        mock_parse_schema,
        mock_convert_schema,
    ):
        schema = Schema()
        mock_parse_schema.return_value = schema
        uri = "http://xsdata/services.xsd"
        namespace = "fooNS"

        self.transformer.process_schema(uri, namespace)

        mock_convert_schema.assert_called_once_with(schema)

    @mock.patch.object(SchemaTransformer, "convert_schema")
    @mock.patch.object(SchemaTransformer, "parse_schema")
    def test_process_schema_ignores_empty_schema(
        self,
        mock_parse_schema,
        mock_convert_schema,
    ):
        mock_parse_schema.return_value = None
        uri = "http://xsdata/services.xsd"
        namespace = "fooNS"

        self.transformer.process_schema(uri, namespace)
        self.assertEqual(0, mock_convert_schema.call_count)

    @mock.patch.object(SchemaTransformer, "generate_classes")
    @mock.patch.object(SchemaTransformer, "process_schema")
    def test_convert_schema(self, mock_process_schema, mock_generate_classes):
        schema = Schema(target_namespace="thug", location="main")
        schema.includes.append(Include(location="foo"))
        schema.overrides.append(Override())
        schema.imports.append(Import(location="bar"))
        schema.imports.append(Import(location="fails"))

        mock_generate_classes.return_value = ClassFactory.list(2)

        self.transformer.convert_schema(schema)

        self.assertEqual(1, len(self.transformer.class_map))
        self.assertEqual(2, len(self.transformer.class_map["main"]))
        mock_process_schema.assert_has_calls(
            [
                mock.call("bar", "thug"),
                mock.call("fails", "thug"),
                mock.call("foo", "thug"),
            ]
        )

    @mock.patch.object(DefinitionsMapper, "map")
    def test_convert_definitions(self, mock_definitions_map):
        classes = ClassFactory.list(2)
        mock_definitions_map.return_value = classes
        definitions = Definitions(location="foo")

        self.transformer.convert_definitions(definitions)
        self.assertEqual(classes, self.transformer.class_map[definitions.location])

    @mock.patch("xsdata.codegen.transformer.logger.info")
    @mock.patch.object(SchemaTransformer, "count_classes")
    @mock.patch.object(SchemaMapper, "map")
    def test_generate_classes(
        self, mock_mapper_map, mock_count_classes, mock_logger_info
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
        uri = Path(__file__).parent.joinpath("../fixtures/books/schema.xsd").as_uri()
        schema = self.transformer.parse_schema(uri, "foo.bar")
        self.assertIsInstance(schema, Schema)
        self.assertEqual(2, len(schema.complex_types))
        self.assertIsNone(self.transformer.parse_schema(uri, None))  # Once

    @mock.patch.object(SchemaTransformer, "process_schema")
    @mock.patch.object(Definitions, "merge")
    @mock.patch.object(DefinitionsParser, "from_bytes")
    @mock.patch.object(SchemaTransformer, "load_resource")
    def test_parse_definitions(
        self,
        mock_load_resource,
        mock_definitions_parser,
        mock_definitions_merge,
        mock_process_schema,
    ):
        def_one = Definitions(
            imports=[
                Import(),
                Import(location="file://sub.wsdl"),
                Import(location="file://sub.wsdl"),
                Import(location="file://types.xsd"),
            ]
        )
        def_two = Definitions()

        mock_load_resource.side_effect = ["a", "b", None]
        mock_definitions_parser.side_effect = [def_one, def_two]
        actual = self.transformer.parse_definitions("main.wsdl", "fooNS")

        self.assertEqual(def_one, actual)
        mock_definitions_merge.assert_called_once_with(def_two)
        mock_process_schema.assert_called_once_with("file://types.xsd")

    @mock.patch("xsdata.codegen.transformer.logger.debug")
    def test_load_resource(self, mock_debug):
        path = Path(__file__).as_uri()

        result = self.transformer.load_resource(path)

        self.assertIn(path, self.transformer.processed)
        self.assertTrue(len(result) > 0)

        result = self.transformer.load_resource(path)
        self.assertIsNone(result)
        mock_debug.assert_called_once_with(
            "Skipping already processed: %s", "test_transformer.py"
        )

    def test_classify_resource(self):
        self.assertEqual(0, self.transformer.classify_resource("file://notexists"))
        self.assertEqual(1, self.transformer.classify_resource("a.xsd"))
        self.assertEqual(2, self.transformer.classify_resource("a.wsdl"))
        self.assertEqual(2, self.transformer.classify_resource("a?wsdl"))
        self.assertEqual(3, self.transformer.classify_resource("a.xml"))

        file_path = Path(tempfile.mktemp())
        file_path.write_bytes(b"</xs:schema>  \n")
        self.assertEqual(1, self.transformer.classify_resource(file_path.as_uri()))

        file_path.write_bytes(b"</xs:definitions>  \n")
        self.transformer.preloaded.clear()
        self.assertEqual(2, self.transformer.classify_resource(file_path.as_uri()))

        file_path.write_bytes(b"</foobar>  \n")
        self.transformer.preloaded.clear()
        self.assertEqual(3, self.transformer.classify_resource(file_path.as_uri()))

        file_path.unlink()

    @mock.patch("xsdata.codegen.transformer.logger.warning")
    def test_load_resource_missing(self, mock_warning):
        uri = "file://foo/bar.xsd"
        result = self.transformer.load_resource(uri)
        self.assertIsNone(result)

        mock_warning.assert_called_once_with("Resource not found %s", uri)

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
        self.transformer.config.output.package = "foo.bar"

        self.transformer.assign_packages()

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

        actual = mock_process.call_args[0][0]

        self.assertIsInstance(actual, ClassContainer)
        self.assertEqual(2, len(actual.data))
        self.assertEqual(self.transformer.config, actual.config)
