from dataclasses import dataclass
from typing import ClassVar
from typing import Dict
from typing import List
from typing import Type

from xsdata.codegen.models import Class
from xsdata.exceptions import CodeGenerationError
from xsdata.formats.dataclass.generator import DataclassGenerator
from xsdata.formats.mixins import AbstractGenerator
from xsdata.logger import logger
from xsdata.models.config import GeneratorConfig


@dataclass
class CodeWriter:
    """
    Proxy to format generators and files structure creation.

    :param generator:
    """

    generator: AbstractGenerator
    generators: ClassVar[Dict[str, Type[AbstractGenerator]]] = {
        "dataclasses": DataclassGenerator,
    }

    def write(self, classes: List[Class]):
        """Iterate over the designated generator outputs and create the
        necessary directories and files."""

        self.generator.designate(classes)
        for result in self.generator.render(classes):
            if result.source.strip():
                logger.info("Generating package: %s", result.title)

                result.path.parent.mkdir(parents=True, exist_ok=True)
                result.path.write_text(result.source, encoding="utf-8")

    def print(self, classes: List[Class]):
        """Iterate over the designated generator outputs and print them to the
        console."""
        self.generator.designate(classes)
        for result in self.generator.render(classes):
            if result.source.strip():
                print(result.source, end="")

    @classmethod
    def from_config(cls, config: GeneratorConfig) -> "CodeWriter":
        if config.output.format not in cls.generators:
            raise CodeGenerationError(
                f"Unknown output format: '{config.output.format}'"
            )

        generator_class = cls.generators[config.output.format]
        return cls(generator=generator_class(config))

    @classmethod
    def register_generator(cls, name: str, clazz: Type[AbstractGenerator]):
        cls.generators[name] = clazz

    @classmethod
    def unregister_generator(cls, name: str):
        cls.generators.pop(name)
