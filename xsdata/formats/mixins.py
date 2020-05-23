from abc import ABC
from abc import abstractmethod
from pathlib import Path
from typing import Dict
from typing import Iterator
from typing import List
from typing import Optional
from typing import Tuple

from jinja2 import Environment
from jinja2 import FileSystemLoader
from jinja2 import Template

from xsdata.codegen.models import Class
from xsdata.utils.collections import group_by
from xsdata.utils.package import module_path
from xsdata.utils.package import package_path


class AbstractGenerator(ABC):
    templates_dir: Optional[Path] = None

    def __init__(self):
        self.env = Environment(
            loader=FileSystemLoader(str(self.templates_dir)), autoescape=False
        )

    def template(self, name: str) -> Template:
        return self.env.get_template(f"{name}.jinja2")

    @abstractmethod
    def render(self, classes: List[Class]) -> Iterator[Tuple[Path, str, str]]:
        pass

    @classmethod
    def module_name(cls, name: str) -> str:
        return name

    @classmethod
    def package_name(cls, name: str) -> str:
        return name

    @classmethod
    def group_by_package(cls, classes: List[Class]) -> Dict[Path, List[Class]]:
        return group_by(classes, lambda x: package_path(x.target_module))

    @classmethod
    def group_by_module(cls, classes: List[Class]) -> Dict[Path, List[Class]]:
        return group_by(classes, lambda x: module_path(x.target_module))
