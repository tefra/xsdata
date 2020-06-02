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
    def __init__(self):
        tpl_dir = Path(__file__).parent.joinpath("templates")
        super().__init__(str(tpl_dir))
        self.env.filters.update(filters)

    def render(self, classes: List[Class]) -> Iterator[Tuple[Path, str, str]]:
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
        """Render the source code for the __init__.py with all the imports of
        the generated class names."""
        class_names = [
            (obj.target_module, obj.name)
            for obj in sorted(classes, key=lambda x: x.name)
        ]
        return self.template("package").render(class_names=class_names)

    def render_module(
        self, resolver: DependenciesResolver, classes: List[Class]
    ) -> str:
        """Render the source code for the target module of the given class
        list."""
        resolver.process(classes)
        imports = self.group_imports(resolver.sorted_imports())
        output = self.render_classes(resolver.sorted_classes())
        namespace = classes[0].source_namespace

        return self.template("module").render(
            output=output, imports=imports, namespace=namespace
        )

    def render_classes(self, classes: List[Class]) -> str:
        """Render the source code of the classes."""
        load = self.template

        def render_class(obj: Class) -> str:
            template = "enum" if obj.is_enumeration else "class"
            return load(template).render(obj=obj).strip()

        return "\n\n\n".join(map(render_class, classes)) + "\n"

    @classmethod
    def ensure_packages(cls, package: Path) -> Iterator[Tuple[Path, str, str]]:
        """Ensure all the __init__ files exists for the target package path,
        otherwise yield the necessary filepath, name, source output that needs
        to be crated."""
        cwd = Path.cwd()
        while cwd != package:
            init = package.joinpath("__init__.py")
            if not init.exists():
                yield init, "init", "# nothing here\n"

            package = package.parent

    @classmethod
    def group_imports(cls, imports: List[Package]) -> Dict[str, List[Package]]:
        """Group the given list of packages by the source path."""
        return group_by(imports, lambda x: x.source)

    @classmethod
    def module_name(cls, module: str) -> str:
        """Convert the given module name to safe snake case."""
        return text.snake_case(utils.safe_snake(module, default="mod"))

    @classmethod
    def package_name(cls, package: str) -> str:
        """Convert the given package name to safe snake case."""
        return ".".join(
            map(
                lambda x: text.snake_case(utils.safe_snake(x, default="pkg")),
                package.split("."),
            )
        )
