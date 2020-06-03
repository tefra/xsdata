import abc
from dataclasses import dataclass
from pathlib import Path
from typing import Dict
from typing import Iterator
from typing import List

from jinja2 import Environment
from jinja2 import FileSystemLoader
from jinja2 import Template

from xsdata.codegen.models import Class
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
    """
    Abstract code generator class.

    :param tpl_dir: Templates directory
    """

    def __init__(self, tpl_dir: str):
        """
        Generator constructor.

        Initialize jinja2 environment.
        """
        self.env = Environment(loader=FileSystemLoader(tpl_dir), autoescape=False)

    def template(self, name: str) -> Template:
        """Return the named template from the initialized environment."""
        return self.env.get_template(f"{name}.jinja2")

    @abc.abstractmethod
    def render(self, classes: List[Class]) -> Iterator[GeneratorResult]:
        """Return a iterator of the generated results."""

    @classmethod
    def module_name(cls, module: str) -> str:
        """Convert the given module name to match the generator conventions."""
        return module

    @classmethod
    def package_name(cls, package: str) -> str:
        """Convert the given module name to match the generator conventions."""
        return package

    @classmethod
    def group_by_package(cls, classes: List[Class]) -> Dict[Path, List[Class]]:
        """Group the given list of classes by the target package directory."""
        return group_by(classes, lambda x: package_path(x.target_module))

    @classmethod
    def group_by_module(cls, classes: List[Class]) -> Dict[Path, List[Class]]:
        """Group the given list of classes by the target module directory."""
        return group_by(classes, lambda x: module_path(x.target_module))
