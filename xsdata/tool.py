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
from xsdata.models.elements import Redefine
from xsdata.models.enums import Namespace
from xsdata.parser import SchemaParser
from xsdata.reducer import reducer
from xsdata.writer import writer


@dataclass
class ProcessTask:

    print: bool
    renderer: str
    processed: List[Path] = field(init=False, default_factory=list)

    def process(self, xsd: Path, package: str, target_namespace: Optional[str] = None):
        if xsd in self.processed:
            logger.debug("Circular import skipping: %s", xsd.name)
            return
        self.processed.append(xsd)

        parser = SchemaParser(target_namespace=target_namespace)
        schema = parser.from_xsd_path(xsd)
        for sub_schema in schema.sub_schemas():
            self.process_import(sub_schema, xsd, package, schema.target_namespace)

        logger.info("Schema: %s, elements: %d", xsd.name, schema.num)

        classes = ClassBuilder(schema=schema).build()
        logger.info("Class candidates: %d", len(classes))

        classes = reducer.process(schema=schema, classes=classes)
        logger.info("Class graduated: %d", len(classes))

        callback = writer.print if self.print else writer.write
        callback(
            schema=schema, classes=classes, package=package, renderer=self.renderer
        )

    def process_import(
        self,
        schema: Union[Import, Include, Redefine],
        path: Path,
        package: str,
        target_namespace: Optional[str],
    ):
        sub_xsd_package = None
        sub_xsd_path = self.resolve_local_schema(schema)

        if schema.schema_location is None:
            return
        elif sub_xsd_path is None:
            sub_xsd_path = self.resolve_schema(path, schema)
            sub_xsd_package = self.adjust_package(package, schema)

        if isinstance(schema, Redefine):
            target_namespace = None

        self.process(
            xsd=sub_xsd_path,
            package=sub_xsd_package or package,
            target_namespace=target_namespace,
        )

    @staticmethod
    def resolve_local_schema(
        schema: Union[Import, Include, Redefine]
    ) -> Optional[Path]:
        try:
            namespace = Namespace(schema.namespace)  # type: ignore
            path = (
                Path(__file__)
                .absolute()
                .parent.joinpath(f"schemas/{namespace.prefix}.xsd")
            )
            schema.schema_location = str(path)
            return path
        except (ValueError, AttributeError):
            return None

    @staticmethod
    def resolve_schema(xsd: Path, schema: Union[Import, Include, Redefine]) -> Path:
        assert schema.schema_location is not None

        return xsd.parent.joinpath(schema.schema_location).resolve()

    @staticmethod
    def adjust_package(package: str, schema: Union[Import, Include, Redefine]) -> str:
        assert schema.schema_location is not None

        pp = package.split(".")
        for part in Path(schema.schema_location).parent.parts:
            if part == "..":
                pp.pop()
            else:
                pp.append(part)
        return ".".join(pp)
