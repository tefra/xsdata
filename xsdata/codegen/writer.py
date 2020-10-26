from dataclasses import dataclass
from typing import List

from xsdata.codegen.models import Class
from xsdata.formats.dataclass.generator import DataclassGenerator
from xsdata.formats.mixins import AbstractGenerator
from xsdata.formats.plantuml.generator import PlantUmlGenerator
from xsdata.logger import logger
from xsdata.models.config import GeneratorConfig
from xsdata.models.config import OutputFormat


@dataclass
class CodeWriter:
    """
    Proxy to format generators and files structure creation.

    :param generator:
    """

    generator: AbstractGenerator

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
        if config.output.format == OutputFormat.PLANTUML:
            return cls(generator=PlantUmlGenerator(config))

        return cls(generator=DataclassGenerator(config))
