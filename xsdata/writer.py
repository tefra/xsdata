import logging
from dataclasses import dataclass, field
from pathlib import Path
from typing import List

import black
from jinja2 import Environment, FileSystemLoader, Template
from toposort import toposort_flatten

from xsdata.models.elements import Schema
from xsdata.models.templates import Class
from xsdata.utils.text import snake_case

logger = logging.getLogger(__name__)


@dataclass
class CodeWriter:
    classes: List[Class]
    theme: str
    target: str
    module: str
    env: Environment = field(init=False)

    def __post_init__(self):
        self.env = Environment(
            loader=FileSystemLoader(
                str(
                    Path(__file__)
                    .parent.joinpath("templates")
                    .joinpath(self.theme)
                )
            )
        )
        if isinstance(self.target, str):
            self.target = Path(self.target)

    def template(self, name: str) -> Template:
        return self.env.get_template("{}.tpl".format(name))

    def write(self):
        classes = self.sort_class_vars(self.classes)
        output = "\n\n".join(map(self.render, classes))
        output = self.black_code(output)

        self.target.mkdir(parents=True, exist_ok=True)
        file_path = self.target.joinpath(
            "{}.py".format(snake_case(self.module))
        )
        with open(str(file_path), "w") as fp:
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

    @staticmethod
    def adjust_target(target: Path, xsd_path: Path, schema: Schema) -> Path:
        """
        From the number of parent directories in the path of the schema import
        location attempt to figure how many levels of the origin xsd path to
        include in the target path.

        Example:
            target: ./
            schema: ./v20/air/Air.xsd imports
                        ../common/CommonTypes.xsd
                        ../../security/Header.xsd
            adjusted target: ./v20/air/

        :param target: The original requested target path
        :type target: :class:`pathlib.Path`
        :param xsd_path: The file path of the xsd
        :type xsd_path: :class:`pathlib.Path`
        :param schema: The parsed Schema instance
        :type schema: :class:`xsdata.models.elements.Schema`
        :return: The adjusted target path
        :rtype: :class:`pathlib.Path`
        """
        sub: List[str] = []
        for _import in schema.imports:
            if _import.schema_location is None:
                continue

            spp = (
                xsd_path.parent.joinpath(_import.schema_location)
                .resolve()
                .parent.parts
            )
            ppp = xsd_path.parent.parts

            i = 0
            while i < len(ppp) and i < len(spp) and ppp[i] == spp[i]:
                i += 1

            if len(ppp[i:]) > len(sub):
                sub = list(ppp[i:])

        if len(sub):
            return target.joinpath(*sub)
        return target
