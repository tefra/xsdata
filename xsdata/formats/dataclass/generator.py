from pathlib import Path
from typing import Iterator, List, Optional

from jinja2 import Environment, FileSystemLoader

from xsdata.codegen.models import Class, Import
from xsdata.codegen.resolver import DependenciesResolver
from xsdata.formats.dataclass.filters import Filters
from xsdata.formats.mixins import AbstractGenerator, GeneratorResult
from xsdata.models.config import GeneratorConfig


class DataclassGenerator(AbstractGenerator):
    """Python dataclasses code generator.

    Args:
        config: The generator config instance

    Attributes:
        env: The jinja2 environment instance
        filters: The template filters instance
    """

    __slots__ = ("env", "filters")

    package_template = "package.jinja2"
    module_template = "module.jinja2"
    enum_template = "enum.jinja2"
    service_template = "service.jinja2"
    class_template = "class.jinja2"

    def __init__(self, config: GeneratorConfig):
        super().__init__(config)
        template_paths = self.get_template_paths()
        loader = FileSystemLoader(template_paths)
        self.env = Environment(loader=loader, autoescape=False)
        self.filters = self.init_filters(config)
        self.filters.register(self.env)

    @classmethod
    def get_template_paths(cls) -> List[str]:
        """Return a list of template paths to feed the jinja2 loader."""
        return [str(Path(__file__).parent.joinpath("templates"))]

    def render(self, classes: List[Class]) -> Iterator[GeneratorResult]:
        """Render the given classes to python packages and modules.

        Args:
              classes: A list of class instances

        Yields:
            An iterator of generator result instances.
        """
        packages = {obj.qname: obj.target_module for obj in classes}
        resolver = DependenciesResolver(registry=packages)

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
        """Render the package for the given classes.

        Args:
            classes: A list of class instances
            module: The target dot notation path

        Returns:
            The rendered package output.
        """
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
        self,
        resolver: DependenciesResolver,
        classes: List[Class],
    ) -> str:
        """Render the module for the given classes.

        Args:
            resolver: The dependencies resolver
            classes: A list of class instances

        Returns:
            The rendered module output.
        """
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
        self,
        classes: List[Class],
        module_namespace: Optional[str],
    ) -> str:
        """Render the classes source code in a module.

        Args:
            classes: A list of class instances
            module_namespace: The module namespace URI

        Returns:
            The rendered classes source code output.
        """

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
        """Ensure __init__.py files exists recursively in the package.

        Args:
            package: The package file path

        Yields:
            An iterator of generator result instances.
        """
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
        """Initialize the filters instance by the generator configuration."""
        return Filters(config)
