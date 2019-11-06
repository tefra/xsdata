import logging
import os
from dataclasses import dataclass, field
from typing import List

import black
from jinja2 import Environment, FileSystemLoader, Template
from toposort import toposort_flatten

from xsdata.models.templates import Class

template_dir = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "templates"
)

logger = logging.getLogger(__name__)


@dataclass
class CodeWriter:

    properties: List[Class]
    theme: str
    target: str
    module: str
    env: Environment = field(init=False)

    def __post_init__(self):
        self.env = Environment(
            loader=FileSystemLoader(os.path.join(template_dir, self.theme))
        )

    def template(self, name: str) -> Template:
        return self.env.get_template("{}.tpl".format(name))

    def write(self):
        classes = self.sort_class_vars(self.properties)
        output = "\n\n".join(map(self.render, classes))
        output = self.black_code(output)

        file_path = os.path.join(self.target, "{}.py".format(self.module))
        with open(file_path, "w") as fp:
            fp.write(self.template("module").render(output=output))

    def render(self, obj: Class) -> str:
        return self.template("class").render(obj=obj)

    @staticmethod
    def black_code(string: str) -> str:
        try:
            mode = black.FileMode(
                is_pyi=False, string_normalization=True, line_length=79
            )
            return black.format_file_contents(string, fast=False, mode=mode)
        except Exception as e:
            logger.exception(e)
            return string

    @staticmethod
    def sort_class_vars(objects: List[Class]) -> List[Class]:
        index = {}
        deps = {}

        for obj in objects:
            index[obj.name] = obj
            deps[obj.name] = {attr.type for attr in obj.attrs}
            if obj.extends:
                deps[obj.name].add(obj.extends)

        return [index[name] for name in toposort_flatten(deps) if name in deps]
