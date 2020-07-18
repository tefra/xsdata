from pathlib import Path
from typing import Dict
from typing import Iterator
from typing import List

from xsdata.codegen.models import Class
from xsdata.codegen.models import Package
from xsdata.codegen.resolver import DependenciesResolver
from xsdata.formats.dataclass import utils
from xsdata.formats.dataclass.filters import filters
from xsdata.formats.mixins import AbstractGenerator
from xsdata.formats.mixins import GeneratorResult
from xsdata.utils import text
from xsdata.utils.collections import group_by


class DataclassGenerator(AbstractGenerator):
    """Python dataclasses code generator."""

    def __init__(self):
        """Override generator constructor to set templates directory and
        environment filters."""
        tpl_dir = Path(__file__).parent.joinpath("templates")
        super().__init__(str(tpl_dir))
        self.env.filters.update(filters)

    def render(self, classes: List[Class]) -> Iterator[GeneratorResult]:
        """
        Return a iterator of the generated results.

        Group classes into modules and yield an output per module and
        per package __init__.py file.
        """
        packages = {obj.qname: obj.target_module for obj in classes}
        resolver = DependenciesResolver(packages=packages)

        # Generate packages
        for package, cluster in self.group_by_package(classes).items():
            yield GeneratorResult(
                path=package.joinpath("__init__.py"),
                title="init",
                source=self.render_package(cluster),
            )
            yield from self.ensure_packages(package.parent)

        # Generate modules
        for module, cluster in self.group_by_module(classes).items():
            yield GeneratorResult(
                path=module.with_suffix(".py"),
                title=cluster[0].target_module,
                source=self.render_module(resolver, cluster),
            )

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
        namespace = classes[0].qname.namespace

        return self.template("module").render(
            output=output, imports=imports, namespace=namespace
        )

    def render_classes(self, classes: List[Class]) -> str:
        """Render the source code of the classes."""
        load = self.template

        def render_class(obj: Class) -> str:
            """Render class or enumeration."""

            if obj.is_enumeration:
                template = "enum"
            elif obj.is_service:
                template = "service"
            else:
                template = "class"

            return load(template).render(obj=obj).strip()

        return "\n\n\n".join(map(render_class, classes)) + "\n"

    @classmethod
    def ensure_packages(cls, package: Path) -> Iterator[GeneratorResult]:
        """Ensure all the __init__ files exists for the target package path,
        otherwise yield the necessary filepath, name, source output that needs
        to be crated."""
        cwd = Path.cwd()
        while cwd != package:
            init = package.joinpath("__init__.py")
            if not init.exists():
                yield GeneratorResult(
                    path=init, title="init", source="# nothing here\n"
                )
            package = package.parent

    @classmethod
    def group_imports(cls, imports: List[Package]) -> Dict[str, List[Package]]:
        """Group the given list of packages by the source path."""
        return group_by(imports, lambda x: x.source)

    @classmethod
    def module_name(cls, module: str) -> str:
        """Convert the given module name to safe snake case."""
        return text.snake_case(utils.safe_snake(text.clean_uri(module), default="mod"))

    @classmethod
    def package_name(cls, package: str) -> str:
        """Convert the given package name to safe snake case."""
        return ".".join(
            map(
                lambda x: text.snake_case(utils.safe_snake(x, default="pkg")),
                package.split("."),
            )
        )
