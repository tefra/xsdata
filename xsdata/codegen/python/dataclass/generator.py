from collections import defaultdict
from pathlib import Path
from typing import DefaultDict, Dict, Iterator, List, Tuple

from jinja2 import Environment, FileSystemLoader, Template

from xsdata.codegen.python.dataclass.filters import filters
from xsdata.codegen.python.generator import PythonAbstractGenerator
from xsdata.codegen.resolver import DependenciesResolver
from xsdata.models.codegen import Class, Package
from xsdata.models.elements import Schema
from xsdata.utils.text import snake_case


class DataclassGenerator(PythonAbstractGenerator):
    def __init__(self):
        templates_dir = Path(__file__).parent.joinpath("templates")
        self.env = Environment(loader=FileSystemLoader(str(templates_dir)),)
        self.env.filters.update(filters)
        self.resolver = DependenciesResolver()

    def template(self, name: str) -> Template:
        return self.env.get_template("{}.jinja2".format(name))

    def render_module(
        self, output: str, imports: Dict[str, List[Package]]
    ) -> str:
        return self.template("module").render(output=output, imports=imports)

    def render_class(self, obj: Class) -> str:
        return self.template("class").render(obj=obj)

    def render(
        self, schema: Schema, classes: List[Class], package: str
    ) -> Iterator[Tuple[Path, str]]:
        """Given a schema, a list of classes and a target package return to the
        writer factory the target file path and the rendered code."""
        module = snake_case(schema.module)
        package_arr = list(map(snake_case, package.split(".")))
        package = "{}.{}".format(".".join(package_arr), module)
        target = Path.cwd().joinpath(*package_arr)
        file_path = target.joinpath(f"{module}.py")

        self.resolver.process(classes=classes, schema=schema, package=package)
        target.mkdir(parents=True, exist_ok=True)

        imports = self.prepare_imports()
        output = self.render_classes()

        yield file_path, self.render_module(imports=imports, output=output)

    def render_classes(self) -> str:
        """Get a list of sorted classes from the imports resolver, apply the
        python code conventions and return the rendered output."""
        output = "\n".join(
            [
                self.render_class(self.process_class(obj))
                for obj in self.resolver.sorted_classes()
            ]
        ).strip()
        return f"\n\n{output}\n"

    def prepare_imports(self) -> Dict[str, List[Package]]:
        """Get a list of sorted packages from the imports resolver apply the
        python code conventions, group them by the source package and return
        them."""
        imports: DefaultDict[str, List[Package]] = defaultdict(list)
        for obj in self.resolver.sorted_imports():
            imports[obj.source].append(self.process_import(obj))
        return imports
