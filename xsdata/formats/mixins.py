import abc
from dataclasses import dataclass
from pathlib import Path
from typing import Dict
from typing import Iterator
from typing import List

from xsdata.codegen.models import Class
from xsdata.exceptions import CodeGenerationError
from xsdata.models.config import GeneratorConfig
from xsdata.models.config import OutputStructure
from xsdata.utils.collections import group_by
from xsdata.utils.package import module_path
from xsdata.utils.package import package_path


@dataclass(frozen=True)
class GeneratorResult:
    """
    Generator easy access output wrapper.

    :param path: file path to be written
    :param title: result title for misc usage
    :param source: source code/output to be written
    """

    path: Path
    title: str
    source: str


class AbstractGenerator(metaclass=abc.ABCMeta):
    """Abstract code generator class."""

    def __init__(self, config: GeneratorConfig):
        """
        Generator constructor.

        :param config Generator configuration
        """
        self.config = config

    def module_name(self, module: str) -> str:
        """Convert the given module name to match the generator conventions."""
        return module

    def package_name(self, package: str) -> str:
        """Convert the given module name to match the generator conventions."""
        return package

    @abc.abstractmethod
    def render(self, classes: List[Class]) -> Iterator[GeneratorResult]:
        """Return a iterator of the generated results."""

    @classmethod
    def group_by_package(cls, classes: List[Class]) -> Dict[Path, List[Class]]:
        """Group the given list of classes by the target package directory."""
        return group_by(classes, lambda x: package_path(x.target_module))

    @classmethod
    def group_by_module(cls, classes: List[Class]) -> Dict[Path, List[Class]]:
        """Group the given list of classes by the target module directory."""
        return group_by(classes, lambda x: module_path(x.target_module))

    def designate(self, classes: List[Class]):
        """
        Normalize the target package and module names by the given output
        generator.

        :param classes: a list of codegen class instances
        """
        modules = {}
        packages = {}
        ns_struct = self.config.output.structure == OutputStructure.NAMESPACES
        for obj in classes:

            if ns_struct:
                obj.package = self.config.output.package
                obj.module = obj.target_namespace or ""

            if obj.package is None:
                raise CodeGenerationError(
                    f"Class `{obj.name}` has not been assign to a package."
                )

            if obj.module not in modules:
                modules[obj.module] = self.module_name(obj.module)

            if obj.package not in packages:
                packages[obj.package] = self.package_name(obj.package)

            obj.module = modules[obj.module]
            obj.package = packages[obj.package]
