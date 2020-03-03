from dataclasses import dataclass
from dataclasses import field
from pathlib import Path
from typing import List
from typing import Optional
from typing import Union

from xsdata.builder import ClassBuilder
from xsdata.logger import logger
from xsdata.models.elements import Import
from xsdata.models.elements import Include
from xsdata.models.elements import Override
from xsdata.models.elements import Redefine
from xsdata.models.elements import Schema
from xsdata.models.enums import Namespace
from xsdata.parser import SchemaParser
from xsdata.reducer import reducer
from xsdata.writer import writer

SchemaLocator = Union[Import, Include, Redefine, Override]


@dataclass
class ProcessTask:

    print: bool
    renderer: str
    processed: List[Path] = field(init=False, default_factory=list)
    imported: List[Path] = field(init=False, default_factory=list)

    def process(
        self,
        xsd: Path,
        package: str,
        target_namespace: Optional[str] = None,
        redefine: Optional[Redefine] = None,
    ):
        if xsd in self.processed:
            logger.debug("Circular import skipping: %s", xsd.name)
            return

        parser = SchemaParser(target_namespace=target_namespace)
        schema = parser.from_xsd_path(xsd)

        self.process_imports(schema, xsd, package, schema.target_namespace)

        logger.info("Schema: %s, elements: %d", xsd.name, schema.num)

        classes = ClassBuilder(schema=schema, redefine=redefine).build()
        logger.info("Class candidates: %d", len(classes))

        classes = reducer.process(schema=schema, classes=classes)
        logger.info("Class graduated: %d", len(classes))

        callback = writer.print if self.print else writer.write
        callback(
            schema=schema, classes=classes, package=package, renderer=self.renderer
        )
        self.processed.append(xsd)

    def process_imports(
        self, schema: Schema, xsd: Path, package: str, target_namespace: Optional[str]
    ):
        for sub_schema in schema.sub_schemas():

            sub_xsd_package = None
            sub_xsd_path = self.resolve_local_schema(sub_schema)

            if sub_schema.schema_location is None:
                continue
            elif sub_xsd_path is None:
                sub_xsd_path = self.resolve_schema(xsd, sub_schema)
                sub_xsd_package = self.adjust_package(package, sub_schema)

            if sub_xsd_path in self.imported:
                continue

            self.imported.append(sub_xsd_path)

            self.process(
                xsd=sub_xsd_path,
                package=sub_xsd_package or package,
                target_namespace=target_namespace,
                redefine=sub_schema if isinstance(sub_schema, Redefine) else None,
            )

    @staticmethod
    def resolve_local_schema(schema: SchemaLocator) -> Optional[Path]:
        if not isinstance(schema, (Override, Redefine)) and schema.namespace:
            ns = Namespace.get_enum(schema.namespace)
            uri = schema.schema_location
            if ns and (not uri or uri.startswith("http")):
                path = (
                    Path(__file__)
                    .absolute()
                    .parent.joinpath(f"schemas/{ns.prefix}.xsd")
                )
                schema.schema_location = str(path)
                return path

        return None

    @staticmethod
    def resolve_schema(xsd: Path, schema: SchemaLocator) -> Path:
        assert schema.schema_location is not None

        return xsd.parent.joinpath(schema.schema_location).resolve()

    @staticmethod
    def adjust_package(package: str, schema: SchemaLocator) -> str:
        assert schema.schema_location is not None

        pp = package.split(".")
        for part in Path(schema.schema_location).parent.parts:
            if part == "..":
                pp.pop()
            else:
                pp.append(part)
        return ".".join(pp)
