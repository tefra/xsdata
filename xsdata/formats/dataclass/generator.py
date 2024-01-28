from pathlib import Path
from typing import Iterator, List, Optional

from jinja2 import Environment, FileSystemLoader

from xsdata.codegen.models import Class, Import
from xsdata.codegen.resolver import DependenciesResolver
from xsdata.formats.dataclass.filters import Filters
from xsdata.formats.mixins import AbstractGenerator, GeneratorResult
from xsdata.models.config import GeneratorConfig


class DataclassGenerator(AbstractGenerator):
    """Python dataclasses code generator."""

    __slots__ = ("env", "filters")

    package_template = "package.jinja2"
    module_template = "module.jinja2"
    enum_template = "enum.jinja2"
    service_template = "service.jinja2"
    class_template = "class.jinja2"

    def __init__(self, config: GeneratorConfig):
        """Override generator constructor to set templates directory and
        environment filters."""

        super().__init__(config)
        template_paths = self.get_template_paths()
        loader = FileSystemLoader(template_paths)
        self.env = Environment(loader=loader, autoescape=False)
        self.filters = self.init_filters(config)
        self.filters.register(self.env)

    @classmethod
    def get_template_paths(cls) -> List[str]:
        return [str(Path(__file__).parent.joinpath("templates"))]

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

        output = self.env.get_template(self.package_template).render(
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
        classes = resolver.sorted_classes()
        output = self.render_classes(classes, module_namespace)
        module = classes[0].target_module

        return self.env.get_template(self.module_template).render(
            output=output,
            classes=classes,
            module=module,
            imports=imports,
            namespace=module_namespace,
        )

    def render_classes(
        self, classes: List[Class], module_namespace: Optional[str]
    ) -> str:
        """Render the source code of the classes."""

        def render_class(obj: Class) -> str:
            """Render class or enumeration."""
            if obj.is_enumeration:
                template = self.enum_template
            elif obj.is_service:
                template = self.service_template
            else:
                template = self.class_template

            return (
                self.env.get_template(template)
                .render(
                    obj=obj,
                    module_namespace=module_namespace,
                )
                .strip()
            )

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
        to be created."""
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
