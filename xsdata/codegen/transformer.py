import os
from collections import defaultdict
from dataclasses import dataclass
from dataclasses import field
from pathlib import Path
from typing import Dict
from typing import List
from typing import Optional
from typing import Tuple
from typing import Union
from urllib.parse import urlparse
from urllib.request import urlopen

from xsdata.codegen.analyzer import ClassAnalyzer
from xsdata.codegen.container import ClassContainer
from xsdata.codegen.mappers.definitions import DefinitionsMapper
from xsdata.codegen.mappers.schema import SchemaMapper
from xsdata.codegen.models import Class
from xsdata.codegen.parsers.definitions import DefinitionsParser
from xsdata.codegen.parsers.schema import SchemaParser
from xsdata.codegen.writer import CodeWriter
from xsdata.exceptions import CodeGenerationError
from xsdata.logger import logger
from xsdata.models.config import GeneratorConfig
from xsdata.models.enums import COMMON_SCHEMA_DIR
from xsdata.models.wsdl import Definitions
from xsdata.models.xsd import Import
from xsdata.models.xsd import Include
from xsdata.models.xsd import Override
from xsdata.models.xsd import Redefine
from xsdata.models.xsd import Schema
from xsdata.utils import collections

Included = Union[Import, Include, Redefine, Override]


@dataclass
class SchemaTransformer:
    """
    Orchestrate the code generation from a list of sources to the output
    format.

    :param print: Print to stdout the generated output
    :param config: Generator configuration
    """

    print: bool
    config: GeneratorConfig
    class_map: Dict[str, List[Class]] = field(init=False, default_factory=dict)
    processed: List[str] = field(init=False, default_factory=list)

    def process(self, uris: List[str]):
        self.process_definitions([uri for uri in uris if uri.endswith("wsdl")])
        self.process_schemas([uri for uri in uris if uri.endswith("xsd")])
        # self.process_schemas([uri for uri in uris if uri.endswith("xml")])
        self.process_classes()

    def process_definitions(self, uris: List[str]):
        """Process a single wsdl resource."""
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
        collections.apply(uris, self.process_schema)

    def process_classes(self):
        """Process the generated classes and write or print the final
        output."""
        classes = [cls for classes in self.class_map.values() for cls in classes]
        class_num, inner_num = self.count_classes(classes)
        if class_num:
            logger.info(
                "Analyzer input: %d main and %d inner classes", class_num, inner_num
            )
            self.assign_packages()

            classes = self.analyze_classes(classes)
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

    def process_schema(self, uri: str, namespace: Optional[str] = None):
        """Parse and convert schema to codegen models."""
        schema = self.parse_schema(uri, namespace)
        if schema:
            self.convert_schema(schema)

    def convert_schema(self, schema: Schema):
        """Convert a schema instance to codegen classes and process imports to
        other schemas."""
        for sub in schema.included():
            if sub.location:
                self.process_schema(sub.location, schema.target_namespace)

        assert schema.location is not None

        self.class_map[schema.location] = self.generate_classes(schema)

    def convert_definitions(self, definitions: Definitions):
        """Convert a definitions instance to codegen classes."""
        assert definitions.location is not None

        key = definitions.location
        classes = DefinitionsMapper.map(definitions)
        self.class_map.setdefault(key, []).extend(classes)

    def generate_classes(self, schema: Schema) -> List[Class]:
        """Convert and return the given schema tree to classes."""
        uri = schema.location
        logger.info("Compiling schema %s", "..." if not uri else os.path.basename(uri))
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

        logger.info("Parsing schema %s", os.path.basename(uri))
        parser = SchemaParser(target_namespace=namespace, location=uri)
        return parser.from_bytes(input_stream, Schema)

    def parse_definitions(
        self, uri: str, namespace: Optional[str]
    ) -> Optional[Definitions]:
        """Parse recursively the given wsdl uri and return the definitions tree
        object."""

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

        # except OSError:
        # except RecursionError:

        if uri not in self.processed:
            try:
                self.processed.append(uri)
                return urlopen(uri).read()  # nosec
            except OSError:
                logger.warning("Resource not found %s", uri)
        else:
            logger.debug("Skipping already processed: %s", os.path.basename(uri))

        return None

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

    def assign_packages(self):
        """Group uris by common path and auto assign package names to all
        classes."""
        prev = ""
        index = 0
        groups = defaultdict(list)
        package = self.config.output.package
        common_schemas_dir = COMMON_SCHEMA_DIR.as_uri()
        for key in sorted(self.class_map.keys()):
            if key.startswith(common_schemas_dir):
                groups[0].append(key)
            else:
                key_parsed = urlparse(key)
                common_path = os.path.commonpath((prev, key))
                if not common_path or common_path == key_parsed.scheme:
                    index += 1

                prev = key
                groups[index].append(key)

        for keys in groups.values():
            common_path = (
                os.path.dirname(keys[0]) if len(keys) == 1 else os.path.commonpath(keys)
            )
            for key in keys:
                items = self.class_map[key]
                suffix = ".".join(Path(key).parent.relative_to(common_path).parts)
                package_name = f"{package}.{suffix}" if suffix else package
                self.assign_package(items, package_name)

    @classmethod
    def assign_package(cls, classes: List[Class], package: str):
        """Assign the given package to all the classes and their inners."""
        for obj in classes:
            obj.package = package
            cls.assign_package(obj.inner, package)
