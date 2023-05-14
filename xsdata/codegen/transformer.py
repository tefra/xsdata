import hashlib
import io
import json
import os
import pickle
import tempfile
from collections import defaultdict
from pathlib import Path
from typing import Callable
from typing import Dict
from typing import List
from typing import NamedTuple
from typing import Optional
from typing import Tuple
from urllib.request import urlopen

from xsdata.codegen.analyzer import ClassAnalyzer
from xsdata.codegen.container import ClassContainer
from xsdata.codegen.mappers.definitions import DefinitionsMapper
from xsdata.codegen.mappers.dict import DictMapper
from xsdata.codegen.mappers.dtd import DtdMapper
from xsdata.codegen.mappers.element import ElementMapper
from xsdata.codegen.mappers.schema import SchemaMapper
from xsdata.codegen.models import Class
from xsdata.codegen.parsers.definitions import DefinitionsParser
from xsdata.codegen.parsers.dtd import DtdParser
from xsdata.codegen.parsers.schema import SchemaParser
from xsdata.codegen.utils import ClassUtils
from xsdata.codegen.writer import CodeWriter
from xsdata.exceptions import CodeGenerationError
from xsdata.formats.dataclass.models.generics import AnyElement
from xsdata.formats.dataclass.parsers import TreeParser
from xsdata.logger import logger
from xsdata.models.config import GeneratorConfig
from xsdata.models.wsdl import Definitions
from xsdata.models.xsd import Schema
from xsdata.utils import collections

TYPE_UNKNOWN = 0
TYPE_SCHEMA = 1
TYPE_DEFINITION = 2
TYPE_DTD = 3
TYPE_XML = 4
TYPE_JSON = 5


class SupportedType(NamedTuple):
    id: int
    name: str
    match_uri: Callable
    match_content: Callable


supported_types = [
    SupportedType(
        id=TYPE_DEFINITION,
        name="wsdl",
        match_uri=lambda x: x.endswith("wsdl"),
        match_content=lambda x: x.endswith("definitions>"),
    ),
    SupportedType(
        id=TYPE_SCHEMA,
        name="xsd",
        match_uri=lambda x: x.endswith("xsd"),
        match_content=lambda x: x.endswith("schema>"),
    ),
    SupportedType(
        id=TYPE_DTD,
        name="dtd",
        match_uri=lambda x: x.endswith("dtd"),
        match_content=lambda x: "<!ELEMENT" in x,
    ),
    SupportedType(
        id=TYPE_XML,
        name="xml",
        match_uri=lambda x: x.endswith("xml"),
        match_content=lambda x: x.endswith(">"),
    ),
    SupportedType(
        id=TYPE_JSON,
        name="json",
        match_uri=lambda x: x.endswith("json"),
        match_content=lambda x: x.endswith("}"),
    ),
]


class SchemaTransformer:
    """
    Orchestrate the code generation from a list of sources to the output
    format.

    :param print: Print to stdout the generated output
    :param config: Generator configuration
    """

    __slots__ = ("print", "config", "classes", "processed", "preloaded")

    def __init__(self, print: bool, config: GeneratorConfig):
        self.print = print
        self.config = config
        self.classes: List[Class] = []
        self.processed: List[str] = []
        self.preloaded: Dict = {}

    def process(self, uris: List[str], cache: bool = False):
        cache_file = self.get_cache_file(uris) if cache else None
        if cache_file and cache_file.exists():
            logger.info(f"Loading from cache {cache_file}")

            self.classes = pickle.loads(cache_file.read_bytes())
        else:
            self.process_sources(uris)

        if cache_file and not cache_file.exists():
            cache_file.write_bytes(pickle.dumps(self.classes))

        self.process_classes()

    def process_sources(self, uris: List[str]):
        sources = defaultdict(list)
        for uri in uris:
            tp = self.classify_resource(uri)
            sources[tp].append(uri)

        self.process_definitions(sources[TYPE_DEFINITION])
        self.process_schemas(sources[TYPE_SCHEMA])
        self.process_dtds(sources[TYPE_DTD])
        self.process_xml_documents(sources[TYPE_XML])
        self.process_json_documents(sources[TYPE_JSON])

    def process_definitions(self, uris: List[str]):
        """Process a list of wsdl resources."""
        definitions = None
        for uri in uris:
            services = self.parse_definitions(uri, namespace=None)
            if definitions is None:
                definitions = services
            elif services:
                definitions.merge(services)

        if definitions is not None:
            collections.apply(definitions.schemas, self.convert_schema)
            self.convert_definitions(definitions)

    def process_schemas(self, uris: List[str]):
        """Process a list of xsd resources."""
        for uri in uris:
            self.process_schema(uri)

    def process_dtds(self, uris: List[str]):
        """Process a list of dtd resources."""
        classes: List[Class] = []

        for uri in uris:
            input_stream = self.load_resource(uri)
            if input_stream:
                logger.info("Parsing dtd %s", uri)
                dtd = DtdParser.parse(input_stream, location=uri)

                classes.extend(DtdMapper.map(dtd))

        self.classes.extend(classes)

    def process_schema(self, uri: str, namespace: Optional[str] = None):
        """Parse and convert schema to codegen models."""
        schema = self.parse_schema(uri, namespace)
        if schema:
            self.convert_schema(schema)

    def process_xml_documents(self, uris: List[str]):
        """Process a list of xml resources."""
        classes = []
        parser = TreeParser()
        location = os.path.dirname(uris[0]) if uris else ""
        for uri in uris:
            input_stream = self.load_resource(uri)
            if input_stream:
                logger.info("Parsing document %s", uri)
                any_element: AnyElement = parser.from_bytes(input_stream)
                classes.extend(ElementMapper.map(any_element, location))

        self.classes.extend(ClassUtils.reduce_classes(classes))

    def process_json_documents(self, uris: List[str]):
        """Process a list of json resources."""
        classes = []
        name = self.config.output.package.split(".")[-1]
        dirname = os.path.dirname(uris[0]) if uris else ""

        for uri in uris:
            input_stream = self.load_resource(uri)
            if input_stream:
                try:
                    data = json.load(io.BytesIO(input_stream))
                    logger.info("Parsing document %s", uri)
                    if isinstance(data, dict):
                        data = [data]

                    for obj in data:
                        classes.extend(DictMapper.map(obj, name, dirname))
                except ValueError as exc:
                    logger.warning("JSON load failed for file: %s", uri, exc_info=exc)

        self.classes.extend(ClassUtils.reduce_classes(classes))

    def process_classes(self):
        """Process the generated classes and write or print the final
        output."""
        class_num, inner_num = self.count_classes(self.classes)
        if class_num:
            logger.info(
                "Analyzer input: %d main and %d inner classes", class_num, inner_num
            )

            classes = self.analyze_classes(self.classes)
            class_num, inner_num = self.count_classes(classes)
            logger.info(
                "Analyzer output: %d main and %d inner classes", class_num, inner_num
            )

            writer = CodeWriter.from_config(self.config)
            if self.print:
                writer.print(classes)
            else:
                writer.write(classes)
        else:
            raise CodeGenerationError("Nothing to generate.")

    def convert_schema(self, schema: Schema):
        """Convert a schema instance to codegen classes and process imports to
        other schemas."""
        for sub in schema.included():
            if sub.location:
                self.process_schema(sub.location, schema.target_namespace)

        self.classes.extend(self.generate_classes(schema))

    def convert_definitions(self, definitions: Definitions):
        """Convert a definitions instance to codegen classes."""
        self.classes.extend(DefinitionsMapper.map(definitions))

    def generate_classes(self, schema: Schema) -> List[Class]:
        """Convert the given schema tree to a list of classes."""
        uri = schema.location
        logger.info("Compiling schema %s", "..." if not uri else uri)
        classes = SchemaMapper.map(schema)

        class_num, inner_num = self.count_classes(classes)
        if class_num > 0:
            logger.info("Builder: %d main and %d inner classes", class_num, inner_num)

        return classes

    def parse_schema(self, uri: str, namespace: Optional[str]) -> Optional[Schema]:
        """Parse the given schema uri and return the schema tree object."""
        input_stream = self.load_resource(uri)
        if input_stream is None:
            return None

        logger.info("Parsing schema %s", uri)
        parser = SchemaParser(target_namespace=namespace, location=uri)
        return parser.from_bytes(input_stream, Schema)

    def parse_definitions(
        self, uri: str, namespace: Optional[str]
    ) -> Optional[Definitions]:
        """Parse recursively the given wsdl uri and return the definitions'
        tree object."""

        input_stream = self.load_resource(uri)
        if input_stream is None:
            return None

        parser = DefinitionsParser(target_namespace=namespace, location=uri)
        definitions = parser.from_bytes(input_stream, Definitions)
        namespace = definitions.target_namespace

        for imp in definitions.imports:
            if not imp.location:
                continue

            if imp.location.endswith("wsdl"):
                sub_definition = self.parse_definitions(imp.location, namespace)
                if sub_definition:
                    definitions.merge(sub_definition)
            else:
                self.process_schema(imp.location)

        return definitions

    def load_resource(self, uri: str) -> Optional[bytes]:
        """Read and return the contents of the given uri."""
        if uri not in self.processed:
            try:
                self.processed.append(uri)
                return self.preloaded.pop(uri, None) or urlopen(uri).read()  # nosec
            except OSError:
                logger.warning("Resource not found %s", uri)
        else:
            logger.debug("Skipping already processed: %s", uri)

        return None

    def classify_resource(self, uri: str) -> int:
        """Detect the resource type by the uri extension or the file
        contents."""

        for supported_type in supported_types:
            if supported_type.match_uri(uri):
                return supported_type.id

        src = self.load_resource(uri)
        if src is not None:
            self.preloaded[uri] = src
            self.processed.clear()
            text = src.decode("utf-8").strip()

            for supported_type in supported_types:
                if supported_type.match_content(text):
                    return supported_type.id

        return TYPE_UNKNOWN

    def analyze_classes(self, classes: List[Class]) -> List[Class]:
        """Analyzer the given class list and simplify attributes and
        extensions."""

        container = ClassContainer(config=self.config)
        container.extend(classes)

        return ClassAnalyzer.process(container)

    def count_classes(self, classes: List[Class]) -> Tuple[int, int]:
        """Return a tuple of counters for the main and inner classes."""
        main = len(classes)
        inner = 0
        for cls in classes:
            inner += sum(self.count_classes(cls.inner))

        return main, inner

    @classmethod
    def get_cache_file(cls, uris: List[str]) -> Path:
        key = hashlib.md5("".join(uris).encode()).hexdigest()
        tempdir = tempfile.gettempdir()
        return Path(tempdir).joinpath(f"{key}.cache")
