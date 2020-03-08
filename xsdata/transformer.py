from dataclasses import dataclass
from dataclasses import field
from pathlib import Path
from typing import List
from typing import Optional
from typing import Union

from xsdata.analyzer import analyzer
from xsdata.builder import ClassBuilder
from xsdata.logger import logger
from xsdata.models.codegen import Class
from xsdata.models.elements import Import
from xsdata.models.elements import Include
from xsdata.models.elements import Override
from xsdata.models.elements import Redefine
from xsdata.models.elements import Schema
from xsdata.parser import SchemaParser
from xsdata.writer import writer


@dataclass
class SchemaTransformer:
    print: bool
    format: str
    processed: List[Path] = field(init=False, default_factory=list)
    included: List[Path] = field(init=False, default_factory=list)

    def process(
        self,
        schema_path: Path,
        package: str,
        target_namespace: Optional[str] = None,
        redefine: Optional[Redefine] = None,
    ):
        """Recursively parse the given schema and all it's included schemas and
        orchestrate the code generation to the target format."""
        if schema_path not in self.processed:
            logger.info("Parsing schema...")
            schema = self.parse_schema(schema_path, target_namespace)
            for sub in schema.included():
                self.process_included(sub, package, schema.target_namespace)

            self.processed.append(schema_path)
            self.generate_code(schema, package, redefine)
        else:
            logger.debug("Circular import skipping: %s", schema_path.name)

    def process_included(
        self,
        included: Union[Import, Include, Redefine, Override],
        package: str,
        target_namespace: Optional[str],
    ):
        """Prepare the given included schema location and send it for
        processing."""
        if not included.location:
            logger.warning(
                "%s: %s unresolved schema location..",
                included.class_name,
                included.schema_location,
            )
        elif included.location in self.included:
            logger.debug(
                "%s: %s already included skipping..",
                included.class_name,
                included.schema_location,
            )
        elif included.location not in self.included:
            self.included.append(included.location)
            package = self.adjust_package(package, included.schema_location)

            self.process(
                included.location,
                package=package,
                target_namespace=target_namespace,
                redefine=included if isinstance(included, Redefine) else None,
            )

    def generate_code(self, schema: Schema, package: str, redefine: Optional[Redefine]):
        """Convert the given schema tree to codegen classes and use the writer
        factory to either generate or print the result code."""
        logger.info("Compiling schema...")
        classes = ClassBuilder(schema, redefine).build()
        classes = analyzer.process(schema, classes)

        class_num, inner_num = self.count_classes(classes)
        if class_num > 0:
            logger.info("Compiled %d main and %d inner classes", class_num, inner_num)
            callback = writer.print if self.print else writer.write
            callback(schema, classes, package, self.format)

    @staticmethod
    def parse_schema(schema_path: Path, target_namespace: Optional[str]) -> Schema:
        """
        Parse the given schema path and return the schema tree object.

        Optionally add the target namespace if the schema is included
        and is missing a target namespace.
        """
        parser = SchemaParser(target_namespace=target_namespace)
        return parser.from_xsd_path(schema_path)

    @staticmethod
    def adjust_package(package: str, location: Optional[str]) -> str:
        """
        Adjust if possible the package name relatively to the schema location
        to make sense.

        eg. foo.bar, ../common/schema.xsd -> foo.common
        """
        if location and not location.startswith("http"):
            pp = package.split(".")
            for part in Path(location).parent.parts:
                if part == "..":
                    pp.pop()
                else:
                    pp.append(part)
            if pp:
                return ".".join(pp)
        return package

    def count_classes(self, classes: List[Class]):
        """Return a tuple of counters for the main and inner classes."""
        main = len(classes)
        inner = 0
        for cls in classes:
            inner += sum(self.count_classes(cls.inner))

        return main, inner
