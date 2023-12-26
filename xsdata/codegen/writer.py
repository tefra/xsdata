import subprocess
from pathlib import Path
from textwrap import indent
from typing import ClassVar, Dict, List, Type

from xsdata.codegen.models import Class
from xsdata.exceptions import CodeGenerationError
from xsdata.formats.dataclass.generator import DataclassGenerator
from xsdata.formats.mixins import AbstractGenerator
from xsdata.logger import logger
from xsdata.models.config import GeneratorConfig


class CodeWriter:
    """
    Proxy to format generators and files structure creation.

    :param generator: Code generator instance
    """

    __slots__ = "generator"

    generators: ClassVar[Dict[str, Type[AbstractGenerator]]] = {
        "dataclasses": DataclassGenerator,
    }

    def __init__(self, generator: AbstractGenerator):
        self.generator = generator

    def write(self, classes: List[Class]):
        """Iterate over the designated generator outputs and create the
        necessary directories and files."""

        self.generator.normalize_packages(classes)
        header = self.generator.render_header()

        for result in self.generator.render(classes):
            if result.source.strip():
                logger.info("Generating package: %s", result.title)
                src_code = self.ruff_code(header + result.source, result.path)
                result.path.parent.mkdir(parents=True, exist_ok=True)
                result.path.write_text(src_code, encoding="utf-8")

    def print(self, classes: List[Class]):
        """Iterate over the designated generator outputs and print them to the
        console."""
        self.generator.normalize_packages(classes)
        header = self.generator.render_header()
        for result in self.generator.render(classes):
            if result.source.strip():
                src_code = self.ruff_code(header + result.source, result.path)
                print(src_code, end="")

    @classmethod
    def from_config(cls, config: GeneratorConfig) -> "CodeWriter":
        if config.output.format.value not in cls.generators:
            raise CodeGenerationError(
                f"Unknown output format: '{config.output.format.value}'"
            )

        generator_class = cls.generators[config.output.format.value]
        return cls(generator=generator_class(config))

    @classmethod
    def register_generator(cls, name: str, clazz: Type[AbstractGenerator]):
        cls.generators[name] = clazz

    @classmethod
    def unregister_generator(cls, name: str):
        cls.generators.pop(name)

    def ruff_code(self, src_code: str, file_path: Path) -> str:
        """Run ruff format on the src code."""
        commands = [
            [
                "ruff",
                "format",
                "--stdin-filename",
                str(file_path),
                "--line-length",
                str(self.generator.config.output.max_line_length),
            ],
        ]
        try:
            src_code_encoded = src_code.encode()
            for command in commands:
                result = subprocess.run(
                    command,
                    input=src_code_encoded,
                    capture_output=True,
                    check=True,
                )
                src_code_encoded = result.stdout

            return src_code_encoded.decode()
        except subprocess.CalledProcessError as e:
            error = indent(e.stderr.decode(), "  ")
            raise CodeGenerationError(f"Ruff failed:\n{error}")
