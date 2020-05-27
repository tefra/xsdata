from pathlib import Path
from typing import Iterator
from typing import List
from typing import Tuple

from xsdata.codegen.models import Class
from xsdata.codegen.resolver import DependenciesResolver
from xsdata.formats.mixins import AbstractGenerator


class PlantUmlGenerator(AbstractGenerator):
    templates_dir = Path(__file__).parent.joinpath("templates")

    def render(self, classes: List[Class]) -> Iterator[Tuple[Path, str, str]]:
        """Given  a list of classes return to the writer factory the target
        file path full module path and the rendered code."""

        packages = {obj.source_qname(): obj.target_module for obj in classes}
        resolver = DependenciesResolver(packages=packages)

        for module, cluster in self.group_by_module(classes).items():
            output = self.render_module(resolver, cluster)
            pck = cluster[0].target_module
            yield module.with_suffix(".pu"), pck, output

    def render_module(
        self, resolver: DependenciesResolver, classes: List[Class]
    ) -> str:
        resolver.process(classes)
        output = self.render_classes(resolver.sorted_classes())
        return self.template("module").render(output=output)

    def render_classes(self, classes: List[Class]) -> str:
        classes = sorted(classes, key=lambda x: x.name)
        output = "\n".join(map(self.render_class, classes)).strip()
        return f"\n{output}\n"

    def render_class(self, obj: Class) -> str:
        template = "enum" if obj.is_enumeration else "class"
        return self.template(template).render(obj=obj)
