from dataclasses import dataclass
from dataclasses import field
from typing import Dict
from typing import List

from xsdata.codegen.models import Class
from xsdata.exceptions import CodeWriterError
from xsdata.formats.dataclass.generator import DataclassGenerator
from xsdata.formats.mixins import AbstractGenerator
from xsdata.formats.plantuml.generator import PlantUmlGenerator
from xsdata.logger import logger


@dataclass
class CodeWriter:
    generators: Dict[str, AbstractGenerator] = field(default_factory=dict)

    @property
    def formats(self) -> List[str]:
        return list(self.generators.keys())

    def register_format(self, name: str, generator: AbstractGenerator):
        self.generators[name] = generator

    def get_format(self, name: str) -> AbstractGenerator:
        return self.generators[name]

    def write(self, classes: List[Class], output: str):
        engine = self.get_format(output)
        for file, package, buffer in engine.render(classes):
            if len(buffer.strip()) > 0:
                logger.info("Generating package: %s", package)

                file.parent.mkdir(parents=True, exist_ok=True)
                file.write_text(buffer)

    def print(self, classes: List[Class], output: str):
        engine = self.get_format(output)
        for _, _, buffer in engine.render(classes):
            print(buffer, end="")

    def designate(self, classes: List[Class], output: str):
        modules = {}
        packages = {}

        for obj in classes:

            if obj.package is None:
                raise CodeWriterError(
                    f"Class `{obj.name}` has not been assign to a package."
                )

            if obj.module not in modules:
                modules[obj.module] = self.module_name(obj.module, output)

            if obj.package not in packages:
                packages[obj.package] = self.package_name(obj.package, output)

            obj.module = modules[obj.module]
            obj.package = packages[obj.package]

    def module_name(self, module: str, output: str) -> str:
        engine = self.get_format(output)
        return engine.module_name(module)

    def package_name(self, package: str, output: str) -> str:
        engine = self.get_format(output)
        return engine.package_name(package)


writer = CodeWriter()
writer.register_format("pydata", DataclassGenerator())
writer.register_format("plantuml", PlantUmlGenerator())
