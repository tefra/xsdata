from pathlib import Path
from typing import Iterator
from typing import List
from typing import Optional

from jinja2 import Environment
from jinja2 import FileSystemLoader

from xsdata.codegen.models import Class
from xsdata.codegen.models import Import
from xsdata.codegen.resolver import DependenciesResolver
from xsdata.formats.dataclass.filters import Filters
from xsdata.formats.mixins import AbstractGenerator
from xsdata.formats.mixins import GeneratorResult
from xsdata.models.config import GeneratorConfig


class DataclassGenerator(AbstractGenerator):
    """Python dataclasses code generator."""

    __slots__ = ("env", "filters")

    def __init__(self, config: GeneratorConfig):
        """Override generator constructor to set templates directory and
        environment filters."""

        super().__init__(config)

        tpl_dir = Path(__file__).parent.joinpath("templates")
        self.env = Environment(loader=FileSystemLoader(str(tpl_dir)), autoescape=False)
        self.filters = self.init_filters(config)
        self.filters.register(self.env)

    def render(self, classes: List[Class]) -> Iterator[GeneratorResult]:
        """
        Return an iterator of the generated results.

        Group classes into modules and yield an output per module and
        per path __init__.py file.
        """
        packages = {obj.qname: obj.target_module for obj in classes}
        resolver = DependenciesResolver(packages=packages)

        # Generate packages
        for path, cluster in self.group_by_package(classes).items():
            module = ".".join(path.relative_to(Path.cwd()).parts)
            yield GeneratorResult(
                path=path.joinpath("__init__.py"),
                title="init",
                source=self.render_package(cluster, module),
            )
            yield from self.ensure_packages(path.parent)

        # Generate modules
        for path, cluster in self.group_by_module(classes).items():
            yield GeneratorResult(
                path=path.with_suffix(".py"),
                title=cluster[0].target_module,
                source=self.render_module(resolver, cluster),
            )

    def render_package(self, classes: List[Class], module: str) -> str:
        """Render the source code for the __init__.py with all the imports of
        the generated class names."""
        imports = [
            Import(qname=obj.qname, source=obj.target_module)
            for obj in sorted(classes, key=lambda x: x.name)
        ]
        DependenciesResolver.resolve_conflicts(imports, set())

        output = self.env.get_template("package.jinja2").render(
            imports=imports,
            module=module,
        )
        return f"{output.strip()}\n"

    def render_module(
        self, resolver: DependenciesResolver, classes: List[Class]
    ) -> str:
        """Render the source code for the target module of the given class
        list."""

        if len({x.target_namespace for x in classes}) == 1:
            module_namespace = classes[0].target_namespace
        else:
            module_namespace = None

        resolver.process(classes)
        imports = resolver.sorted_imports()
        output = self.render_classes(resolver.sorted_classes(), module_namespace)
        module = classes[0].target_module

        return self.env.get_template("module.jinja2").render(
            output=output,
            module=module,
            imports=imports,
            namespace=module_namespace,
        )

    def render_classes(
        self, classes: List[Class], module_namespace: Optional[str]
    ) -> str:
        """Render the source code of the classes."""
        load = self.env.get_template

        def render_class(obj: Class) -> str:
            """Render class or enumeration."""
            if obj.is_enumeration:
                template = load("enum.jinja2")
            elif obj.is_service:
                template = load("service.jinja2")
            else:
                template = load("class.jinja2")

            return template.render(
                obj=obj,
                module_namespace=module_namespace,
            ).strip()

        return "\n\n\n".join(map(render_class, classes)) + "\n"

    def module_name(self, name: str) -> str:
        """Convert the given module name to safe snake case."""
        return self.filters.module_name(name)

    def package_name(self, name: str) -> str:
        """Convert the given package name to safe snake case."""
        return self.filters.package_name(name)

    @classmethod
    def ensure_packages(cls, package: Path) -> Iterator[GeneratorResult]:
        """Ensure all the __init__ files exists for the target package path,
        otherwise yield the necessary filepath, name, source output that needs
        to be crated."""
        cwd = Path.cwd()
        while cwd < package:
            init = package.joinpath("__init__.py")
            if not init.exists():
                yield GeneratorResult(
                    path=init, title="init", source="# nothing here\n"
                )
            package = package.parent

    @classmethod
    def init_filters(cls, config: GeneratorConfig) -> Filters:
        return Filters(config)
