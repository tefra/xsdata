from collections import defaultdict
from pathlib import Path
from typing import DefaultDict
from typing import Dict
from typing import Iterator
from typing import List
from typing import Tuple

from xsdata.formats.dataclass.filters import filters
from xsdata.generators import PythonAbstractGenerator
from xsdata.models.codegen import Class
from xsdata.models.codegen import Package
from xsdata.models.elements import Schema
from xsdata.utils.text import snake_case


class DataclassGenerator(PythonAbstractGenerator):
    templates_dir = Path(__file__).parent.joinpath("templates")

    def __init__(self):
        super(DataclassGenerator, self).__init__()
        self.env.filters.update(filters)
        self.modules = defaultdict(int)

    def render_module(self, output: str, imports: Dict[str, List[Package]]) -> str:
        return self.template("module").render(output=output, imports=imports)

    def render_class(self, obj: Class) -> str:
        template = "enum" if obj.is_enumeration else "class"
        return self.template(template).render(obj=obj)

    def render(
        self, schema: Schema, classes: List[Class], package: str
    ) -> Iterator[Tuple[Path, str]]:
        """Given a schema, a list of classes and a target package return to the
        writer factory the target file path and the rendered code."""
        module = self.module_name(schema.module)
        package_arr = list(map(snake_case, package.split(".")))
        package = "{}.{}".format(".".join(package_arr), module)
        target = Path.cwd().joinpath(*package_arr)
        file_path = target.joinpath(f"{module}.py")

        self.resolver.process(classes=classes, schema=schema, package=package)

        imports = self.prepare_imports()
        output = self.render_classes()

        yield file_path, self.render_module(imports=imports, output=output)

    def module_name(self, module: str) -> str:
        """
        Return a unique and safe module name.

        In case of module name collisions append the module name index.
        """
        module = module[:-4] if module.endswith(".xsd") else module
        module = snake_case(module)
        self.modules[module] += 1
        if self.modules[module] > 1:
            module = f"{module}_{self.modules[module] - 1}"
        return module

    def render_classes(self) -> str:
        """Get a list of sorted classes from the imports resolver, apply the
        python code conventions and return the rendered output."""
        output = "\n".join(map(self.render_class, self.prepare_classes())).strip()
        return f"\n\n{output}\n"

    def prepare_classes(self):
        for obj in self.resolver.sorted_classes():
            yield self.process_class(obj.clone())

    def prepare_imports(self) -> Dict[str, List[Package]]:
        """Get a list of sorted packages from the imports resolver apply the
        python code conventions, group them by the source package and return
        them."""
        imports: DefaultDict[str, List[Package]] = defaultdict(list)
        for obj in self.resolver.sorted_imports():
            imports[obj.source].append(self.process_import(obj))
        return imports
