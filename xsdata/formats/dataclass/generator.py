from collections import defaultdict
from pathlib import Path
from typing import DefaultDict
from typing import Dict
from typing import Iterator
from typing import List
from typing import Tuple

from xsdata.formats.dataclass.filters import filters
from xsdata.formats.generators import PythonAbstractGenerator
from xsdata.models.codegen import Class
from xsdata.models.codegen import Package
from xsdata.resolver import DependenciesResolver


class DataclassGenerator(PythonAbstractGenerator):
    templates_dir = Path(__file__).parent.joinpath("templates")

    def __init__(self):
        super(DataclassGenerator, self).__init__()
        self.env.filters.update(filters)

    def render_module(self, output: str, imports: Dict[str, List[Package]]) -> str:
        return self.template("module").render(output=output, imports=imports)

    def render_class(self, obj: Class) -> str:
        template = "enum" if obj.is_enumeration else "class"
        return self.template(template).render(obj=obj)

    def render(self, classes: List[Class]) -> Iterator[Tuple[Path, str, str]]:
        """Given  a list of classes return to the writer factory the target
        file path full module path and the rendered code."""

        packages = {obj.source_qname(): obj.target_module for obj in classes}
        resolver = DependenciesResolver(packages=packages)

        groups: Dict[str, List] = defaultdict(list)
        for obj in classes:
            groups[obj.target_module].append(obj)

        for target_module, classes in groups.items():
            resolver.process(classes)
            imports = self.prepare_imports(resolver.sorted_imports())
            output = self.render_classes(resolver.sorted_classes())
            file_path = Path.cwd().joinpath(target_module.replace(".", "/") + ".py")

            yield file_path, target_module, self.render_module(
                imports=imports, output=output
            )

    def render_classes(self, classes: List[Class]) -> str:
        """Get a list of sorted classes from the imports resolver, apply the
        python code conventions and return the rendered output."""
        output = "\n".join(
            map(self.render_class, self.prepare_classes(classes))
        ).strip()
        return f"\n\n{output}\n"

    def prepare_classes(self, classes: List[Class]):
        for obj in classes:
            yield self.process_class(obj.clone())

    def prepare_imports(self, imports: List[Package]) -> Dict[str, List[Package]]:
        """Get a list of sorted packages from the imports resolver apply the
        python code conventions, group them by the source package and return
        them."""
        result: DefaultDict[str, List[Package]] = defaultdict(list)
        for obj in imports:
            result[obj.source].append(self.process_import(obj))
        return result
