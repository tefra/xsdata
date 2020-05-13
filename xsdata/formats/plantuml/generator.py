from collections import defaultdict
from pathlib import Path
from typing import Dict
from typing import Iterator
from typing import List
from typing import Tuple

from xsdata.formats.mixins import AbstractGenerator
from xsdata.models.codegen import Class
from xsdata.resolver import DependenciesResolver


class PlantUmlGenerator(AbstractGenerator):
    templates_dir = Path(__file__).parent.joinpath("templates")

    def render_module(self, output: str) -> str:
        return self.template("module").render(output=output)

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

        for target_module, cluster in groups.items():
            resolver.process(cluster)
            output = self.render_classes(resolver.sorted_classes())
            file_path = Path.cwd().joinpath(target_module.replace(".", "/") + ".pu")

            yield file_path, target_module, self.render_module(output=output)

    def render_classes(self, classes: List[Class]) -> str:
        """Sort classes by name and return the rendered output."""
        classes = sorted(classes, key=lambda x: x.name)
        output = "\n".join(map(self.render_class, classes)).strip()
        return f"\n{output}\n"
