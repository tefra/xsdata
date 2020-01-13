from dataclasses import dataclass, field
from typing import Dict, List

from xsdata.formats.dataclass.generator import DataclassGenerator
from xsdata.formats.plantuml.generator import PlantUmlGenerator
from xsdata.generators import AbstractGenerator
from xsdata.logger import logger
from xsdata.models.codegen import Class
from xsdata.models.elements import Schema


@dataclass
class CodeWriter:
    generators: Dict[str, AbstractGenerator] = field(default_factory=dict)

    @property
    def formats(self):
        return list(self.generators.keys())

    def register_generator(self, name, renderer: AbstractGenerator):
        self.generators[name] = renderer

    def get_renderer(self, name) -> AbstractGenerator:
        if name in self.generators:
            return self.generators[name]
        raise ValueError(f"{name} is not a valid {AbstractGenerator.__name__}")

    def write(
        self, schema: Schema, classes: List[Class], package: str, renderer: str
    ):
        engine = self.get_renderer(renderer)
        for file, output in engine.render(schema, classes, package):
            if len(output.strip()) > 0:
                logger.info("Generating package: %s", package)

                file.parent.mkdir(parents=True, exist_ok=True)
                file.write_text(output)

    def print(
        self, schema: Schema, classes: List[Class], package: str, renderer: str
    ):
        engine = self.get_renderer(renderer)
        for _, output in engine.render(schema, classes, package):
            print(output, end="")


writer = CodeWriter()
writer.register_generator("pydata", DataclassGenerator())
writer.register_generator("plantuml", PlantUmlGenerator())
