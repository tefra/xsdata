import abc
from pathlib import Path
from typing import Dict
from typing import Iterator
from typing import List
from typing import Tuple

from jinja2 import Environment
from jinja2 import FileSystemLoader
from jinja2 import Template

from xsdata.codegen.models import Class
from xsdata.utils.collections import group_by
from xsdata.utils.package import module_path
from xsdata.utils.package import package_path


class AbstractGenerator(metaclass=abc.ABCMeta):
    """
    Abstract code generator class.

    :param tpl_dir: Templates directory
    """

    def __init__(self, tpl_dir: str):
        self.env = Environment(loader=FileSystemLoader(tpl_dir), autoescape=False)

    def template(self, name: str) -> Template:
        """Return the named template from the initialized environment."""
        return self.env.get_template(f"{name}.jinja2")

    @abc.abstractmethod
    def render(self, classes: List[Class]) -> Iterator[Tuple[Path, str, str]]:
        """Return a tuple iterator that consists of the target filepath, module
        name and the rendered source code for the given list of classes."""

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
