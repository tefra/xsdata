from pathlib import Path
from typing import Iterator, List, Tuple

from jinja2 import Environment, FileSystemLoader, Template

from xsdata.codegen.python.dataclass.filters import filters
from xsdata.codegen.python.generator import PythonAbstractGenerator
from xsdata.codegen.python.resolver import ImportResolver
from xsdata.models.codegen import Class
from xsdata.models.elements import Schema
from xsdata.utils.text import snake_case


class DataclassGenerator(PythonAbstractGenerator):
    def __init__(self):
        templates_dir = Path(__file__).parent.joinpath("templates")
        self.env = Environment(
            loader=FileSystemLoader(str(templates_dir)),
            extensions=["jinja2.ext.do"],
        )
        self.env.filters.update(filters)
        self.resolver = ImportResolver()

    def template(self, name: str) -> Template:
        return self.env.get_template("{}.jinja2".format(name))

    def render_module(self, output: str, imports: List[str]) -> str:
        return self.template("module").render(output=output, imports=imports)

    def render_class(self, obj: Class) -> str:
        return self.template("class").render(obj=obj)

    def render(
        self, schema: Schema, classes: List[Class], package: str
    ) -> Iterator[Tuple[Path, str]]:
        module = snake_case(schema.module)
        package_arr = list(map(snake_case, package.split(".")))
        package = "{}.{}".format(".".join(package_arr), module)
        target = Path.cwd().joinpath(*package_arr)

        self.resolver.current(classes, schema)
        overrides = self.resolver.type_overrides()

        imports = [
            self.process_import(obj) for obj in self.resolver.import_packages()
        ]

        output = [
            self.render_class(self.process_class(obj, overrides))
            for obj in self.resolver.process_classes(package)
        ]

        target.mkdir(parents=True, exist_ok=True)
        file_path = target.joinpath(f"{module}.py")

        yield file_path, self.render_module(
            imports=imports, output="\n".join(output)
        )
