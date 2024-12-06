import abc
import datetime
from collections.abc import Iterator
from pathlib import Path
from typing import NamedTuple

from xsdata import __version__
from xsdata.codegen.exceptions import CodegenError
from xsdata.codegen.models import Class
from xsdata.models.config import GeneratorConfig
from xsdata.utils.collections import group_by
from xsdata.utils.package import module_path, package_path


class GeneratorResult(NamedTuple):
    """Generator result transfer object.

    Attributes:
        path: The target file path
        title: The result title for misc usage
        source: The source code/output to be written
    """

    path: Path
    title: str
    source: str


class AbstractGenerator(abc.ABC):
    """Abstract code generator class.

    Args:
        config: The generator config instance
    """

    __slots__ = "config"

    def __init__(self, config: GeneratorConfig):
        self.config = config

    def module_name(self, module: str) -> str:
        """Convert the given module name to match the generator conventions."""
        return module

    def package_name(self, package: str) -> str:
        """Convert the given module name to match the generator conventions."""
        return package

    @abc.abstractmethod
    def render(self, classes: list[Class]) -> Iterator[GeneratorResult]:
        """Return an iterator of the generated results."""

    @classmethod
    def group_by_package(cls, classes: list[Class]) -> dict[Path, list[Class]]:
        """Group the given list of classes by the target package directory."""
        return group_by(classes, lambda x: package_path(x.target_module))

    @classmethod
    def group_by_module(cls, classes: list[Class]) -> dict[Path, list[Class]]:
        """Group the given list of classes by the target module directory."""
        return group_by(classes, lambda x: module_path(x.target_module))

    def render_header(self) -> str:
        """Generate a header for the writer to prepend on the output files."""
        if not self.config.output.include_header:
            return ""

        now = datetime.datetime.now().isoformat(sep=" ", timespec="seconds")
        return (
            f'"""This file was generated by xsdata, v{__version__}, on {now}'
            f"\n\nGenerator: {self.__class__.__qualname__}\n"
            f"See: https://xsdata.readthedocs.io/\n"
            '"""\n'
        )

    def normalize_packages(self, classes: list[Class]):
        """Normalize the classes module and package names.

        Args:
            classes: A list of class instances

        Raises:
            CodeGenerationError: If the analyzer failed to
                designate a class to a package and module.
        """
        modules = {}
        packages = {}
        for obj in classes:
            if obj.package is None or obj.module is None:
                raise CodegenError(
                    f"Class `{obj.name}` has not been assigned to a package"
                )

            if obj.module not in modules:
                modules[obj.module] = self.module_name(obj.module)

            if obj.package not in packages:
                packages[obj.package] = self.package_name(obj.package)

            obj.module = modules[obj.module]
            obj.package = packages[obj.package]
