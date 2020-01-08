from pathlib import Path
from typing import Iterator, List, Tuple

from xsdata.generators import AbstractGenerator
from xsdata.models.codegen import Class
from xsdata.models.elements import Schema


class PlantUmlGenerator(AbstractGenerator):
    templates_dir = Path(__file__).parent.joinpath("templates")

    def render_module(self, output: str) -> str:
        return self.template("module").render(output=output)

    def render_class(self, obj: Class) -> str:
        template = "enum" if obj.is_enumeration else "class"
        return self.template(template).render(obj=obj)

    def render(
        self, schema: Schema, classes: List[Class], package: str
    ) -> Iterator[Tuple[Path, str]]:
        """Given a schema, a list of classes and a target package return to the
        writer factory the target file path and the rendered output."""
        module = schema.module
        package_arr = package.split(".")
        package = "{}.{}".format(".".join(package_arr), module)
        target = Path.cwd().joinpath(*package_arr)
        file_path = target.joinpath(f"{module}.pu")

        self.resolver.process(classes=classes, schema=schema, package=package)

        output = self.render_classes()

        yield file_path, self.render_module(output=output)

    def render_classes(self) -> str:
        """Sort classes by name and return the rendered output."""
        classes = sorted(self.resolver.sorted_classes(), key=lambda x: x.name)
        output = "\n".join(map(self.render_class, classes)).strip()
        return f"\n{output}\n"
