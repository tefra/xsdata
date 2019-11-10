import logging
from dataclasses import dataclass, field
from pathlib import Path
from typing import List, Set, Union

from jinja2 import Environment, FileSystemLoader, Template
from toposort import toposort_flatten

from xsdata.models.elements import Import, Include, Schema
from xsdata.models.templates import Class
from xsdata.templates.dataclass.filters import arguments
from xsdata.utils.text import snake_case

logger = logging.getLogger(__name__)


@dataclass
class CodeWriter:
    classes: List[Class]
    imports: List[Union[Import, Include]]
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
            ),
        )
        self.env.filters["arguments"] = arguments

        if isinstance(self.target, str):
            self.target = Path(self.target)

    def template(self, name: str) -> Template:
        return self.env.get_template("{}.jinja2".format(name))

    def write(self):
        classes = self.sort_class_vars(self.classes)

        self.target.mkdir(parents=True, exist_ok=True)
        file_path = self.target.joinpath(f"{snake_case(self.module)}.py")
        with open(str(file_path), "w") as fp:
            fp.write(
                self.template("module").render(
                    output="\n".join(map(self.render, classes)),
                    imports=self.organize_imports(self.imports),
                )
            )

    def render(self, obj: Class) -> str:
        return self.template("class").render(obj=obj)

    @staticmethod
    def organize_imports(imports):
        def convert(value):
            if "value" == "..":
                return ".."
            else:
                return snake_case(value)

        result = []
        for import_ in imports:
            path = Path(import_.schema_location)
            parts = list(path.parent.parts)
            parts.append(path.stem)
            result.append(
                "from .{} import *".format(".".join(map(convert, parts)))
            )
        return result

    @classmethod
    def sort_class_vars(cls, objects: List[Class]) -> List[Class]:
        index = {obj.name: obj for obj in objects}
        deps = {obj.name: cls.collect_deps(obj) for obj in objects}

        return [index[name] for name in toposort_flatten(deps) if name in deps]

    @classmethod
    def collect_deps(cls, obj: Class) -> Set[str]:
        dependencies = {attr.type for attr in obj.attrs}
        if obj.extends:
            dependencies.add(obj.extends)
        for inner in obj.inner:
            dependencies.update(cls.collect_deps(inner))
        return dependencies

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
