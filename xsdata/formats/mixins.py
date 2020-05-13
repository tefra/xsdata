from abc import ABC
from abc import abstractmethod
from pathlib import Path
from typing import Iterator
from typing import List
from typing import Optional
from typing import Tuple

from jinja2 import Environment
from jinja2 import FileSystemLoader
from jinja2 import Template

from xsdata.models.codegen import Class


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
