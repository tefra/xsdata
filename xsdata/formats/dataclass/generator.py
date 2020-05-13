from collections import defaultdict
from pathlib import Path
from typing import Dict
from typing import Iterator
from typing import List
from typing import Tuple

from xsdata.formats.dataclass import utils
from xsdata.formats.dataclass.filters import filters
from xsdata.formats.mixins import AbstractGenerator
from xsdata.models.codegen import Class
from xsdata.models.codegen import Package
from xsdata.resolver import DependenciesResolver
from xsdata.utils import text


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

        for target_package, cluster in self.group_by_package(classes).items():
            yield target_package, "init", self.render_package(cluster)

        for target_module, cluster in self.group_by_module(classes).items():
            file_path = Path.cwd().joinpath(target_module.replace(".", "/") + ".py")
            yield file_path, target_module, self.render_module(resolver, cluster)

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
        imports = self.prepare_imports(resolver.sorted_imports())
        output = self.render_classes(resolver.sorted_classes())
        namespace = classes[0].source_namespace

        return self.template("module").render(
            output=output, imports=imports, namespace=namespace
        )

    def render_class(self, obj: Class) -> str:
        template = "enum" if obj.is_enumeration else "class"
        return self.template(template).render(obj=obj)

    @classmethod
    def group_by_package(cls, classes: List[Class]) -> Dict[Path, List[Class]]:
        groups: Dict[Path, List] = defaultdict(list)
        init_paths: Dict = dict()
        for obj in classes:
            if obj.target_module not in init_paths:
                init_paths[obj.target_module] = (
                    Path.cwd()
                    .joinpath(obj.target_module.replace(".", "/"))
                    .parent.joinpath("__init__.py")
                )
            key = init_paths[obj.target_module]
            groups[key].append(obj)

        return groups

    @classmethod
    def group_by_module(cls, classes: List[Class]) -> Dict[str, List[Class]]:
        groups: Dict[str, List] = defaultdict(list)
        for obj in classes:
            groups[obj.target_module].append(obj)

        return groups

    def render_classes(self, classes: List[Class]) -> str:
        """Get a list of sorted classes from the imports resolver, apply the
        python code conventions and return the rendered output."""
        output = map(str.strip, map(self.render_class, classes))
        return "\n\n\n".join(output) + "\n"

    def prepare_imports(self, imports: List[Package]) -> Dict[str, List[Package]]:
        """Get a list of sorted packages from the imports resolver apply the
        python code conventions, group them by the source package and return
        them."""
        result: Dict[str, List[Package]] = dict()
        for obj in imports:
            result.setdefault(obj.source, []).append(obj)
        return result

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
