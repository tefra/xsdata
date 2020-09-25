from pathlib import Path
from typing import Iterator
from typing import List

from xsdata.codegen.models import Class
from xsdata.codegen.resolver import DependenciesResolver
from xsdata.formats.mixins import AbstractGenerator
from xsdata.formats.mixins import GeneratorResult
from xsdata.models.config import GeneratorConfig


class PlantUmlGenerator(AbstractGenerator):
    """PlantUML generator."""

    def __init__(self, config: GeneratorConfig):
        tpl_dir = Path(__file__).parent.joinpath("templates")
        super().__init__(str(tpl_dir), config)

    def render(self, classes: List[Class]) -> Iterator[GeneratorResult]:
        """Return a iterator of the generated results."""
        packages = {obj.qname: obj.target_module for obj in classes}
        resolver = DependenciesResolver(packages=packages)

        for module, cluster in self.group_by_module(classes).items():
            yield GeneratorResult(
                path=module.with_suffix(".pu"),
                title=cluster[0].target_module,
                source=self.render_module(resolver, cluster),
            )

    def render_module(
        self, resolver: DependenciesResolver, classes: List[Class]
    ) -> str:
        """Render the source code for the target module of the given class
        list."""
        resolver.process(classes)
        output = self.render_classes(resolver.sorted_classes())
        return self.template("module").render(output=output)

    def render_classes(self, classes: List[Class]) -> str:
        """Render the source code of the classes."""
        load = self.template
        classes = sorted(classes, key=lambda x: x.name)

        def render_class(obj: Class) -> str:
            """Render class or enumeration."""
            template = "enum" if obj.is_enumeration else "class"
            return load(template).render(obj=obj).strip()

        output = "\n".join(map(render_class, classes))
        return f"\n{output}\n"
