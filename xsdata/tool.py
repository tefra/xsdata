from dataclasses import dataclass, field
from pathlib import Path
from typing import List, Union

from xsdata.builder import ClassBuilder
from xsdata.models.elements import Import, Include
from xsdata.models.enums import Namespace
from xsdata.parser import SchemaParser
from xsdata.reducer import reducer
from xsdata.writer import writer


@dataclass
class ProcessTask:

    print: bool
    renderer: str
    processed: List[Path] = field(init=False, default_factory=list)

    def process(self, xsd: Path, package: str):
        if xsd in self.processed:
            return
        self.processed.append(xsd)

        schema = SchemaParser.from_file(xsd)
        for sub_schema in schema.sub_schemas():
            if self.is_valid(sub_schema):
                self.process(
                    xsd=self.resolve_schema(xsd, sub_schema),
                    package=self.adjust_package(package, sub_schema),
                )

        classes = ClassBuilder(schema=schema).build()
        classes = reducer.process(schema=schema, classes=classes)

        callback = writer.print if self.print else writer.write
        callback(
            schema=schema,
            classes=classes,
            package=package,
            renderer=self.renderer,
        )

    @staticmethod
    def is_valid(schema: Union[Import, Include]) -> bool:
        return schema.namespace == Namespace.XML or not schema.schema_location

    @staticmethod
    def resolve_schema(xsd: Path, schema: Union[Import, Include]) -> Path:
        assert schema.schema_location is not None

        return xsd.parent.joinpath(schema.schema_location).resolve()

    @staticmethod
    def adjust_package(package: str, schema: Union[Import, Include]) -> str:
        assert schema.schema_location is not None

        pp = package.split(".")
        for part in Path(schema.schema_location).parent.parts:
            if part == "..":
                pp.pop()
            else:
                pp.append(part)
        return ".".join(pp)
