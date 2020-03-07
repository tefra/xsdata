from dataclasses import dataclass
from dataclasses import field
from typing import Dict
from typing import List

from xsdata.exceptions import CodeWriterError
from xsdata.formats.dataclass.generator import DataclassGenerator
from xsdata.formats.generators import AbstractGenerator
from xsdata.formats.plantuml.generator import PlantUmlGenerator
from xsdata.logger import logger
from xsdata.models.codegen import Class
from xsdata.models.elements import Schema


@dataclass
class CodeWriter:
    generators: Dict[str, AbstractGenerator] = field(default_factory=dict)

    @property
    def formats(self):
        return list(self.generators.keys())

    def register_format(self, name, generator: AbstractGenerator):
        self.generators[name] = generator

    def get_format(self, name) -> AbstractGenerator:
        if name in self.generators:
            return self.generators[name]
        raise CodeWriterError(f"Unknown code generator `{name}`")

    def write(self, schema: Schema, classes: List[Class], package: str, format: str):
        engine = self.get_format(format)
        for file, package, output in engine.render(schema, classes, package):
            if len(output.strip()) > 0:
                logger.info("Generating package: %s", package)

                file.parent.mkdir(parents=True, exist_ok=True)
                file.write_text(output)

    def print(self, schema: Schema, classes: List[Class], package: str, format: str):
        engine = self.get_format(format)
        for _, _, output in engine.render(schema, classes, package):
            print(output, end="")


writer = CodeWriter()
writer.register_format("pydata", DataclassGenerator())
writer.register_format("plantuml", PlantUmlGenerator())
