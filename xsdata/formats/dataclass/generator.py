from pathlib import Path
from typing import Dict
from typing import Iterator
from typing import List
from typing import Tuple

from xsdata.codegen.models import Class
from xsdata.codegen.models import Package
from xsdata.codegen.resolver import DependenciesResolver
from xsdata.formats.dataclass import utils
from xsdata.formats.dataclass.filters import filters
from xsdata.formats.mixins import AbstractGenerator
from xsdata.utils import text
from xsdata.utils.collections import group_by


class DataclassGenerator(AbstractGenerator):
    templates_dir = Path(__file__).parent.joinpath("templates")

    def __init__(self):
        super().__init__()
        self.env.filters.update(filters)

    def render(self, classes: List[Class]) -> Iterator[Tuple[Path, str, str]]:
        """Given  a list of classes return to the writer factory the target
        file path full module path and the rendered code."""

        packages = {obj.source_qname(): obj.target_module for obj in classes}
        resolver = DependenciesResolver(packages=packages)

        # Generate packages
        for package, cluster in self.group_by_package(classes).items():
            output = self.render_package(cluster)
            pck = "init"
            yield package.joinpath("__init__.py"), pck, output
            yield from self.ensure_packages(package.parent)

        # Generate modules
        for module, cluster in self.group_by_module(classes).items():
            output = self.render_module(resolver, cluster)
            pck = cluster[0].target_module
            yield module.with_suffix(".py"), pck, output

    def render_package(self, classes: List[Class]) -> str:
        class_names = [
            (obj.target_module, obj.name)
            for obj in sorted(classes, key=lambda x: x.name)
        ]
        return self.template("package").render(class_names=class_names)

    def render_module(
        self, resolver: DependenciesResolver, classes: List[Class]
    ) -> str:
        resolver.process(classes)
        imports = self.group_imports(resolver.sorted_imports())
        output = self.render_classes(resolver.sorted_classes())
        namespace = classes[0].source_namespace

        return self.template("module").render(
            output=output, imports=imports, namespace=namespace
        )

    def render_classes(self, classes: List[Class]) -> str:
        return "\n\n\n".join(map(str.strip, map(self.render_class, classes))) + "\n"

    def render_class(self, obj: Class) -> str:
        template = "enum" if obj.is_enumeration else "class"
        return self.template(template).render(obj=obj)

    @classmethod
    def ensure_packages(cls, package: Path):
        cwd = Path.cwd()
        while cwd != package:
            init = package.joinpath("__init__.py")
            if not init.exists():
                yield init, "init", "# nothing here\n"

            package = package.parent

    @classmethod
    def group_imports(cls, imports: List[Package]) -> Dict[str, List[Package]]:
        return group_by(imports, lambda x: x.source)

    @classmethod
    def module_name(cls, name: str) -> str:
        return text.snake_case(utils.safe_snake(name, default="mod"))

    @classmethod
    def package_name(cls, name: str) -> str:
        return ".".join(
            map(
                lambda x: text.snake_case(utils.safe_snake(x, default="pkg")),
                name.split("."),
            )
        )
