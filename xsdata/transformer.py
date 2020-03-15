from dataclasses import dataclass
from dataclasses import field
from pathlib import Path
from typing import List
from typing import Optional
from typing import Union

from xsdata.analyzer import ClassAnalyzer
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
    output: str
    processed: List[Path] = field(init=False, default_factory=list)

    def process(self, schema_path: Path, package: str):
        classes = self.process_schema(schema_path, package)
        classes = self.analyze_classes(classes)
        class_num, inner_num = self.count_classes(classes)

        if not class_num:
            return logger.warning("Analyzer returned zero classes!")

        logger.info("Analyzer: %d main and %d inner classes", class_num, inner_num)

        writer.designate(classes, self.output)
        if self.print:
            writer.print(classes, self.output)
        else:
            writer.write(classes, self.output)

    def process_schema(
        self, schema_path: Path, package: str, target_namespace: Optional[str] = None,
    ) -> List[Class]:
        """Recursively parse the given schema and all it's included schemas and
        generate a list of classes."""
        classes = []
        if schema_path not in self.processed:
            self.processed.append(schema_path)
            logger.info("Parsing schema...")
            schema = self.parse_schema(schema_path, target_namespace)
            target_namespace = schema.target_namespace
            for sub in schema.included():
                included_classes = self.process_included(sub, package, target_namespace)
                classes.extend(included_classes)

            classes.extend(self.generate_classes(schema, package))
        else:
            logger.debug("Already processed skipping: %s", schema_path.name)
        return classes

    def process_included(
        self,
        included: Union[Import, Include, Redefine, Override],
        package: str,
        target_namespace: Optional[str],
    ) -> List[Class]:
        """Prepare the given included schema location and send it for
        processing."""
        classes = []
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
            package = self.adjust_package(package, included.schema_location)
            classes = self.process_schema(included.location, package, target_namespace)
        return classes

    def generate_classes(self, schema: Schema, package: str):
        """Convert the given schema tree to codegen classes and use the writer
        factory to either generate or print the result code."""
        logger.info("Compiling schema...")
        classes = ClassBuilder(schema=schema, package=package).build()

        class_num, inner_num = self.count_classes(classes)
        if class_num > 0:
            logger.info("Builder: %d main and %d inner classes", class_num, inner_num)

        return classes

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
    def analyze_classes(classes: List[Class]):
        """Analyzer the given class list and simplify attributes and
        extensions."""
        analyzer = ClassAnalyzer()
        return analyzer.process(classes)

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
