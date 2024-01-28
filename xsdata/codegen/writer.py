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
    """Code writer class.

    Args:
        generator: The code generator instance

    Attributes:
        generators: A map of registered code generators
    """

    __slots__ = "generator"

    generators: ClassVar[Dict[str, Type[AbstractGenerator]]] = {
        "dataclasses": DataclassGenerator,
    }

    def __init__(self, generator: AbstractGenerator):
        self.generator = generator

    def write(self, classes: List[Class]):
        """Write the classes to the designated modules.

        The classes may be written in the same module or
        different ones, the entrypoint must create the
        directory structure write the file outputs.

        Args:
            classes: A list of class instances
        """
        self.generator.normalize_packages(classes)
        header = self.generator.render_header()

        for result in self.generator.render(classes):
            if result.source.strip():
                logger.info("Generating package: %s", result.title)
                src_code = self.ruff_code(header + result.source, result.path)
                result.path.parent.mkdir(parents=True, exist_ok=True)
                result.path.write_text(src_code, encoding="utf-8")

    def print(self, classes: List[Class]):
        """Print the generated code for the given classes.

        Args:
            classes: A list of class instances
        """
        self.generator.normalize_packages(classes)
        header = self.generator.render_header()
        for result in self.generator.render(classes):
            if result.source.strip():
                src_code = self.ruff_code(header + result.source, result.path)
                print(src_code, end="")

    @classmethod
    def from_config(cls, config: GeneratorConfig) -> "CodeWriter":
        """Instance the code writer from the generator configuration instance.

        Validates that the output format is registered as a generator.

        Args:
            config: The generator configuration instance

        Returns:
            A new code writer instance.
        """
        if config.output.format.value not in cls.generators:
            raise CodeGenerationError(
                f"Unknown output format: '{config.output.format.value}'"
            )

        generator_class = cls.generators[config.output.format.value]
        return cls(generator=generator_class(config))

    @classmethod
    def register_generator(cls, name: str, clazz: Type[AbstractGenerator]):
        """Register a generator by name.

        Args:
            name: The generator name
            clazz: The generator class
        """
        cls.generators[name] = clazz

    @classmethod
    def unregister_generator(cls, name: str):
        """Remove a generator by name.

        Args:
            name: The generator name
        """
        cls.generators.pop(name)

    def ruff_code(self, src_code: str, file_path: Path) -> str:
        """Run ruff format on the src code.

        Args:
            src_code: The output source code
            file_path: The file path the source code will be written to

        Returns:
            The formatted output source code
        """
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
