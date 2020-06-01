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
from xsdata.codegen.builder import ClassBuilder
from xsdata.codegen.models import Class
from xsdata.codegen.parser import SchemaParser
from xsdata.codegen.writer import writer
from xsdata.logger import logger
from xsdata.models.enums import COMMON_SCHEMA_DIR
from xsdata.models.xsd import Import
from xsdata.models.xsd import Include
from xsdata.models.xsd import Override
from xsdata.models.xsd import Redefine
from xsdata.models.xsd import Schema


Included = Union[Import, Include, Redefine, Override]
String = Optional[str]
Classes = List[Class]
ClassMap = Dict[str, Classes]


@dataclass
class SchemaTransformer:
    print: bool
    output: str
    processed: List[str] = field(init=False, default_factory=list)

    def process(self, urls: List[str], package: str):
        classes = self.process_schemas(urls, package)
        class_num, inner_num = self.count_classes(classes)
        if class_num:
            logger.info(
                "Analyzer input: %d main and %d inner classes", class_num, inner_num
            )

            classes = self.analyze_classes(classes)
            class_num, inner_num = self.count_classes(classes)
            logger.info(
                "Analyzer output: %d main and %d inner classes", class_num, inner_num
            )

            writer.designate(classes, self.output)
            if self.print:
                writer.print(classes, self.output)
            else:
                writer.write(classes, self.output)
        else:
            logger.warning("Analyzer returned zero classes!")

    def process_schemas(self, urls: List[str], package: str) -> Classes:
        class_map = {}
        for url in urls:
            class_map.update(self.process_schema(url))

        self.assign_packages(class_map, package)

        classes = []
        for items in class_map.values():
            classes.extend(items)

        return classes

    def process_schema(self, url: str, namespace: String = None) -> ClassMap:
        """Recursively parse the given schema url and the included schemas and
        generate a list of classes."""
        classes = {}
        if url not in self.processed:
            self.processed.append(url)
            logger.info("Parsing schema...")
            schema = self.parse_schema(url, namespace)
            if schema:
                namespace = schema.target_namespace
                for sub in schema.included():
                    classes.update(self.process_included(sub, namespace))

                classes[url] = self.generate_classes(schema)
        else:
            logger.debug("Already processed skipping: %s", url)
        return classes

    def process_included(self, included: Included, namespace: String) -> ClassMap:
        """Prepare the given included schema location and send it for
        processing."""
        classes = {}
        if not included.location:
            logger.warning(
                "%s: %s unresolved schema location..",
                included.class_name,
                included.schema_location,
            )
        elif included.location in self.processed:
            logger.debug(
                "%s: %s already included skipping..",
                included.class_name,
                included.schema_location,
            )
        else:
            classes = self.process_schema(included.location, namespace)

        return classes

    def generate_classes(self, schema: Schema) -> Classes:
        """Convert the given schema tree to codegen classes and use the writer
        factory to either generate or print the result code."""
        logger.info("Compiling schema %s", schema.location)
        classes = ClassBuilder(schema=schema).build()

        class_num, inner_num = self.count_classes(classes)
        if class_num > 0:
            logger.info("Builder: %d main and %d inner classes", class_num, inner_num)

        return classes

    @staticmethod
    def parse_schema(url: str, namespace: String) -> Optional[Schema]:
        """
        Parse the given schema url and return the schema tree object.

        Optionally add the target namespace if the schema is included
        and is missing a target namespace.
        """

        try:
            schema = urlopen(url).read()
        except OSError:
            logger.warning("Schema not found %s", url)
        else:
            parser = SchemaParser(target_namespace=namespace, schema_location=url)
            return parser.from_bytes(schema, Schema)

        return None

    @staticmethod
    def analyze_classes(classes: Classes) -> Classes:
        """Analyzer the given class list and simplify attributes and
        extensions."""
        return ClassAnalyzer(classes).process()

    def count_classes(self, classes: Classes) -> Tuple[int, int]:
        """Return a tuple of counters for the main and inner classes."""
        main = len(classes)
        inner = 0
        for cls in classes:
            inner += sum(self.count_classes(cls.inner))

        return main, inner

    @classmethod
    def assign_packages(cls, class_map: ClassMap, package: str):
        """Group uris by common path and auto assign package names to all
        classes."""
        prev = ""
        index = 0
        groups = defaultdict(list)
        common_schemas_dir = COMMON_SCHEMA_DIR.as_uri()
        for key in sorted(class_map.keys()):
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
                items = class_map[key]
                suffix = ".".join(Path(key).parent.relative_to(common_path).parts)
                package_name = f"{package}.{suffix}" if suffix else package
                cls.assign_package(items, package_name)

    @classmethod
    def assign_package(cls, classes: Classes, package: str):
        for obj in classes:
            obj.package = package
            cls.assign_package(obj.inner, package)
