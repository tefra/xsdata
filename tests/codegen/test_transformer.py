import pickle
import tempfile
from pathlib import Path
from unittest import mock

from toposort import CircularDependencyError

from xsdata import __version__
from xsdata.codegen.container import ClassContainer
from xsdata.codegen.exceptions import CodegenError
from xsdata.codegen.mappers import (
    DefinitionsMapper,
    DictMapper,
    DtdMapper,
    ElementMapper,
    SchemaMapper,
)
from xsdata.codegen.parsers import DefinitionsParser, DtdParser
from xsdata.codegen.transformer import ResourceTransformer
from xsdata.codegen.utils import ClassUtils
from xsdata.codegen.writer import CodeWriter
from xsdata.formats.dataclass.models.generics import AnyElement
from xsdata.formats.dataclass.parsers import TreeParser
from xsdata.models.config import GeneratorConfig
from xsdata.models.wsdl import Binding, Definitions, Types
from xsdata.models.xsd import Import, Include, Override, Schema
from xsdata.utils.testing import ClassFactory, DtdFactory, FactoryTestCase


class ResourceTransformerTests(FactoryTestCase):
    def setUp(self) -> None:
        config = GeneratorConfig()
        self.transformer = ResourceTransformer(config=config)
        super().setUp()

    @mock.patch.object(ResourceTransformer, "process_classes")
    @mock.patch.object(ResourceTransformer, "process_dtds")
    @mock.patch.object(ResourceTransformer, "process_json_documents")
    @mock.patch.object(ResourceTransformer, "process_xml_documents")
    @mock.patch.object(ResourceTransformer, "process_schemas")
    @mock.patch.object(ResourceTransformer, "process_definitions")
    def test_process(
        self,
        mock_process_definitions,
        mock_process_schemas,
        mock_process_xml_documents,
        mock_process_json_documents,
        mock_process_dtds,
        mock_process_classes,
    ) -> None:
        uris = [
            "a.wsdl",
            "b.wsdl",
            "c.xsd",
            "d.xsd",
            "e.xml",
            "f.xml",
            "g.json",
            "h.json",
            "i.dtd",
        ]

        self.transformer.process(uris)
        mock_process_definitions.assert_called_once_with(uris[:2])
        mock_process_schemas.assert_called_once_with(uris[2:4])
        mock_process_xml_documents.assert_called_once_with(uris[4:6])
        mock_process_json_documents.assert_called_once_with(uris[6:8])
        mock_process_dtds.assert_called_once_with(uris[8:])
        mock_process_classes.assert_called_once_with()

    @mock.patch.object(ResourceTransformer, "process_classes")
    @mock.patch.object(ResourceTransformer, "process_sources")
    @mock.patch.object(ResourceTransformer, "get_cache_file")
    def test_process_from_cache(
        self, mock_get_cache_file, mock_process_sources, mock_process_classes
    ) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            cache = Path(tmpdir).joinpath("foo.cache")
            classes = ClassFactory.list(2)
            cache.write_bytes(pickle.dumps(classes))

            mock_get_cache_file.return_value = cache
            uris = ["a.xml", "b.xml"]

            self.transformer.process(uris, cache=True)

            self.assertEqual(classes, self.transformer.classes)
            self.assertEqual(0, mock_process_sources.call_count)
            mock_process_classes.assert_called_once_with()

    @mock.patch.object(ResourceTransformer, "process_classes")
    @mock.patch.object(ResourceTransformer, "process_sources")
    @mock.patch.object(ResourceTransformer, "get_cache_file")
    def test_process_with_cache(
        self, mock_get_cache_file, mock_process_sources, mock_process_classes
    ) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            cache = Path(tmpdir).joinpath("foo.cache")
            classes = ClassFactory.list(2)
            self.transformer.classes = classes
            mock_get_cache_file.return_value = cache
            uris = ["a.xml", "b.xml"]

            self.transformer.process(uris, cache=True)
            self.assertEqual(1, mock_process_sources.call_count)

            self.assertEqual(classes, pickle.loads(cache.read_bytes()))
            mock_process_classes.assert_called_once_with()

    @mock.patch.object(ResourceTransformer, "process_classes")
    def test_process_with_circular_dependencies_error(
        self, mock_process_classes
    ) -> None:
        mock_process_classes.side_effect = CircularDependencyError({})
        with self.assertRaises(CodegenError):
            self.transformer.process([])

    @mock.patch("xsdata.codegen.transformer.logger.warning")
    @mock.patch.object(ResourceTransformer, "process_classes")
    def test_process_with_module_not_found_error(
        self, mock_process_classes, mock_warning
    ) -> None:
        mock_process_classes.side_effect = ModuleNotFoundError({})
        self.transformer.process([])
        mock_warning.assert_called_once_with(
            "Module not found on imports validation, please report it."
        )

    @mock.patch.object(ResourceTransformer, "convert_schema")
    @mock.patch.object(ResourceTransformer, "convert_definitions")
    @mock.patch.object(ResourceTransformer, "parse_definitions")
    def test_process_definitions(
        self,
        mock_parse_definitions,
        mock_convert_definitions,
        mock_convert_schema,
    ) -> None:
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

    @mock.patch.object(ResourceTransformer, "process_schema")
    def test_process_schemas(self, mock_process_schema) -> None:
        uris = ["http://xsdata/foo.xsd", "http://xsdata/bar.xsd"]

        self.transformer.process_schemas(uris)

        mock_process_schema.assert_has_calls([mock.call(uri) for uri in uris])

    @mock.patch.object(ClassUtils, "reduce_classes")
    @mock.patch.object(ElementMapper, "map")
    @mock.patch.object(TreeParser, "from_bytes")
    @mock.patch.object(ResourceTransformer, "load_resource")
    def test_process_xml_documents(
        self, mock_load_resource, mock_from_bytes, mock_map, mock_reduce_classes
    ) -> None:
        uris = ["foo/a.xml", "foo/b.xml", "foo/c.xml"]
        resources = [b"a", None, b"c"]
        elements = [AnyElement(), AnyElement()]

        classes_a = ClassFactory.list(2)
        classes_c = ClassFactory.list(3)

        mock_load_resource.side_effect = resources
        mock_from_bytes.side_effect = elements
        mock_map.side_effect = [classes_a, classes_c]
        mock_reduce_classes.return_value = classes_a + classes_c

        self.transformer.process_xml_documents(uris)

        self.assertEqual(5, len(self.transformer.classes))

        mock_from_bytes.assert_has_calls(
            [mock.call(resources[0]), mock.call(resources[2])]
        )
        mock_map.assert_has_calls([mock.call(x, "foo") for x in elements])
        mock_reduce_classes.assert_called_once_with(classes_a + classes_c)

    @mock.patch("xsdata.codegen.transformer.logger.warning")
    @mock.patch.object(ClassUtils, "reduce_classes")
    @mock.patch.object(DictMapper, "map")
    @mock.patch.object(ResourceTransformer, "load_resource")
    def test_process_json_documents(
        self, mock_load_resource, mock_map, mock_reduce_classes, mock_warning
    ) -> None:
        uris = ["foo/a.json", "foo/b.json", "foo/c.json", "bar.json"]
        resources = [b'{"foo": 1}', None, b'[{"foo": true}]', b"notjson"]

        classes_a = ClassFactory.list(2)
        classes_c = ClassFactory.list(3)

        mock_load_resource.side_effect = resources
        mock_map.side_effect = [classes_a, classes_c]
        mock_reduce_classes.return_value = classes_a + classes_c

        self.transformer.config.output.package = "some.books"
        self.transformer.process_json_documents(uris)

        self.assertEqual(5, len(self.transformer.classes))

        mock_map.assert_has_calls(
            [
                mock.call({"foo": 1}, "books", "foo"),
                mock.call({"foo": True}, "books", "foo"),
            ]
        )
        mock_reduce_classes.assert_called_once_with(classes_a + classes_c)
        mock_warning.assert_called_once_with(
            "JSON load failed for file: %s", uris[3], exc_info=mock.ANY
        )

    @mock.patch.object(DtdMapper, "map")
    @mock.patch.object(DtdParser, "parse")
    @mock.patch.object(ResourceTransformer, "load_resource")
    def test_process_dtds(self, mock_load_resource, mock_parse, mock_map) -> None:
        uris = ["foo/a.dtd", "foo/b.dtd", "foo/c.dtd"]
        resources = [b"a", None, b"c"]
        dtds = DtdFactory.list(2)

        classes_a = ClassFactory.list(2)
        classes_c = ClassFactory.list(3)

        mock_load_resource.side_effect = resources
        mock_parse.side_effect = dtds
        mock_map.side_effect = [classes_a, classes_c]

        self.transformer.process_dtds(uris)

        self.assertEqual(5, len(self.transformer.classes))

        mock_parse.assert_has_calls(
            [
                mock.call(resources[0], location=uris[0]),
                mock.call(resources[2], location=uris[2]),
            ]
        )
        mock_map.assert_has_calls(
            [
                mock.call(dtds[0]),
                mock.call(dtds[1]),
            ]
        )

    @mock.patch("xsdata.codegen.transformer.logger.info")
    @mock.patch.object(CodeWriter, "write")
    @mock.patch.object(ResourceTransformer, "analyze_classes")
    def test_process_classes(
        self,
        mock_analyze_classes,
        mock_writer_write,
        mock_logger_into,
    ) -> None:
        schema_classes = ClassFactory.list(3)
        analyzer_classes = ClassFactory.list(2)
        mock_analyze_classes.return_value = analyzer_classes

        self.transformer.classes = schema_classes
        self.transformer.process_classes()

        mock_analyze_classes.assert_called_once_with(schema_classes)
        mock_writer_write.assert_called_once_with(analyzer_classes)
        mock_logger_into.assert_has_calls(
            [
                mock.call("Analyzer input: %d main and %d inner classes", 3, 0),
                mock.call("Analyzer output: %d main and %d inner classes", 2, 0),
            ]
        )

    @mock.patch.object(ResourceTransformer, "convert_schema")
    @mock.patch.object(ResourceTransformer, "parse_schema")
    def test_process_schema(
        self,
        mock_parse_schema,
        mock_convert_schema,
    ) -> None:
        schema = Schema()
        mock_parse_schema.return_value = schema
        uri = "http://xsdata/services.xsd"
        namespace = "fooNS"

        self.transformer.process_schema(uri, namespace)

        mock_convert_schema.assert_called_once_with(schema)

    @mock.patch.object(ResourceTransformer, "convert_schema")
    @mock.patch.object(ResourceTransformer, "parse_schema")
    def test_process_schema_ignores_empty_schema(
        self,
        mock_parse_schema,
        mock_convert_schema,
    ) -> None:
        mock_parse_schema.return_value = None
        uri = "http://xsdata/services.xsd"
        namespace = "fooNS"

        self.transformer.process_schema(uri, namespace)
        self.assertEqual(0, mock_convert_schema.call_count)

    @mock.patch.object(ResourceTransformer, "generate_classes")
    @mock.patch.object(ResourceTransformer, "process_schema")
    def test_convert_schema(self, mock_process_schema, mock_generate_classes) -> None:
        schema = Schema(target_namespace="thug", location="main")
        schema.includes.append(Include(location="foo"))
        schema.overrides.append(Override())
        schema.imports.append(Import(location="bar"))
        schema.imports.append(Import(location="fails"))

        mock_generate_classes.return_value = ClassFactory.list(2)

        self.transformer.convert_schema(schema)

        self.assertEqual(2, len(self.transformer.classes))
        mock_process_schema.assert_has_calls(
            [
                mock.call("bar", "thug"),
                mock.call("fails", "thug"),
                mock.call("foo", "thug"),
            ]
        )

    @mock.patch.object(DefinitionsMapper, "map")
    def test_convert_definitions(self, mock_definitions_map) -> None:
        classes = ClassFactory.list(2)
        mock_definitions_map.return_value = classes
        definitions = Definitions(location="foo")

        self.transformer.convert_definitions(definitions)
        self.assertEqual(classes, self.transformer.classes)

    @mock.patch("xsdata.codegen.transformer.logger.info")
    @mock.patch.object(ResourceTransformer, "count_classes")
    @mock.patch.object(SchemaMapper, "map")
    def test_generate_classes(
        self, mock_mapper_map, mock_count_classes, mock_logger_info
    ) -> None:
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

    def test_parse_schema(self) -> None:
        uri = Path(__file__).parent.joinpath("../fixtures/books/schema.xsd").as_uri()
        schema = self.transformer.parse_schema(uri, "foo.bar")
        self.assertIsInstance(schema, Schema)
        self.assertEqual(2, len(schema.complex_types))
        self.assertIsNone(self.transformer.parse_schema(uri, None))  # Once

    @mock.patch.object(ResourceTransformer, "process_schema")
    @mock.patch.object(Definitions, "merge")
    @mock.patch.object(DefinitionsParser, "from_bytes")
    @mock.patch.object(ResourceTransformer, "load_resource")
    def test_parse_definitions(
        self,
        mock_load_resource,
        mock_definitions_parser,
        mock_definitions_merge,
        mock_process_schema,
    ) -> None:
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
    def test_load_resource(self, mock_debug) -> None:
        path = Path(__file__).as_uri()

        result = self.transformer.load_resource(path)

        self.assertIn(path, self.transformer.processed)
        self.assertTrue(len(result) > 0)

        result = self.transformer.load_resource(path)
        self.assertIsNone(result)
        mock_debug.assert_called_once_with("Skipping already processed: %s", path)

    def test_classify_resource(self) -> None:
        self.assertEqual(0, self.transformer.classify_resource("file://notexists"))
        self.assertEqual(1, self.transformer.classify_resource("a.xsd"))
        self.assertEqual(2, self.transformer.classify_resource("a.wsdl"))
        self.assertEqual(2, self.transformer.classify_resource("a?wsdl"))
        self.assertEqual(3, self.transformer.classify_resource("a.dtd"))
        self.assertEqual(4, self.transformer.classify_resource("a.xml"))
        self.assertEqual(5, self.transformer.classify_resource("a.json"))

        file_path = Path(tempfile.mktemp())
        file_path.write_bytes(b"</xs:schema>  \n")
        self.assertEqual(1, self.transformer.classify_resource(file_path.as_uri()))

        file_path.write_bytes(b"</xs:definitions>  \n")
        self.transformer.preloaded.clear()
        self.assertEqual(2, self.transformer.classify_resource(file_path.as_uri()))

        file_path.write_bytes(b"<!ELEMENT Tags ")
        self.transformer.preloaded.clear()
        self.assertEqual(3, self.transformer.classify_resource(file_path.as_uri()))

        file_path.write_bytes(b"</foobar>  \n")
        self.transformer.preloaded.clear()
        self.assertEqual(4, self.transformer.classify_resource(file_path.as_uri()))

        file_path.write_bytes(b"\n}  \n")
        self.transformer.preloaded.clear()
        self.assertEqual(5, self.transformer.classify_resource(file_path.as_uri()))

        file_path.write_bytes(b"aaa\n")
        self.transformer.preloaded.clear()
        self.assertEqual(0, self.transformer.classify_resource(file_path.as_uri()))

        file_path.unlink()

    @mock.patch("xsdata.codegen.transformer.logger.warning")
    def test_load_resource_missing(self, mock_warning) -> None:
        uri = Path.cwd().joinpath("foo/bar.xsd").as_uri()
        result = self.transformer.process([uri])
        self.assertIsNone(result)

        mock_warning.assert_called_once_with("Resource not found %s", uri)

    def test_count_classes(self) -> None:
        classes = ClassFactory.list(
            2, inner=ClassFactory.list(2, inner=ClassFactory.list(3))
        )

        self.assertEqual((2, 16), self.transformer.count_classes(classes))

    @mock.patch.object(ClassContainer, "process")
    def test_analyze_classes(self, mock_process) -> None:
        classes = ClassFactory.list(2)

        result = self.transformer.analyze_classes(classes)
        self.assertEqual(2, len(result))
        mock_process.assert_called_once()

    def test_get_cache_file(self) -> None:
        uris = ["a.xml", "b.json"]
        actual = self.transformer.get_cache_file(uris)
        tempdir = Path(tempfile.gettempdir())
        expected = tempdir.joinpath(
            f"xsdata.{__version__}.ae1bed744d3d3611e698a2d2ef5335d2.cache"
        )

        self.assertEqual(expected, actual)
