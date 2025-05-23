import importlib
import pkgutil
import subprocess
import sys
from collections.abc import Iterator
from pathlib import Path
from typing import Optional

from jinja2 import Environment, FileSystemLoader

from xsdata.codegen.exceptions import CodegenError
from xsdata.codegen.models import Class, Import
from xsdata.codegen.resolver import DependenciesResolver
from xsdata.formats.dataclass.filters import Filters
from xsdata.formats.mixins import AbstractGenerator, GeneratorResult
from xsdata.logger import logger
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
        """Initialize the generator."""
        super().__init__(config)
        template_paths = self.get_template_paths()
        loader = FileSystemLoader(template_paths)
        self.env = Environment(loader=loader, autoescape=False)
        self.filters = self.init_filters(config)
        self.filters.register(self.env)

    @classmethod
    def get_template_paths(cls) -> list[str]:
        """Return a list of template paths to feed the jinja2 loader."""
        return [str(Path(__file__).parent.joinpath("templates"))]

    def render(self, classes: list[Class]) -> Iterator[GeneratorResult]:
        """Render the given classes to python packages and modules.

        Args:
              classes: A list of class instances

        Yields:
            An iterator of generator result instances.
        """
        packages = {obj.qname: obj.target_module for obj in classes}
        resolver = DependenciesResolver(registry=packages)
        package_dirs = set()
        # Generate packages
        for path, cluster in self.group_by_package(classes).items():
            module = ".".join(path.relative_to(Path.cwd()).parts)
            package_path = path.joinpath("__init__.py")
            src_code = self.render_package(cluster, module)
            package_dirs.add(str(path))

            yield GeneratorResult(
                path=package_path,
                title="init",
                source=src_code,
            )
            yield from self.ensure_packages(path.parent)

        # Generate modules
        for path, cluster in self.group_by_module(classes).items():
            module_path = path.with_suffix(".py")
            src_code = self.render_module(resolver, cluster)

            yield GeneratorResult(
                path=module_path,
                title=cluster[0].target_module,
                source=src_code,
            )

        self.ruff_code(list(package_dirs))
        self.validate_imports()

    def validate_imports(self) -> None:
        """Recursively import all generated packages.

        Raises:
            ImportError: On circular imports
        """

        def import_package(package_name: str) -> None:
            logger.debug(f"Importing: {package_name}")
            module = importlib.import_module(package_name)
            if hasattr(module, "__path__"):
                for _, name, _ in pkgutil.walk_packages(
                    module.__path__, module.__name__ + "."
                ):
                    logger.debug(f"Importing: {name}")
                    importlib.import_module(name)

        sys.path.insert(0, str(Path.cwd().absolute()))
        package = self.config.output.package
        import_package(self.package_name(package))

    def render_package(self, classes: list[Class], module: str) -> str:
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

        return self.env.get_template(self.package_template).render(
            imports=imports,
            module=module,
        )

    def render_module(
        self,
        resolver: DependenciesResolver,
        classes: list[Class],
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
        classes: list[Class],
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

        return "\n".join(map(render_class, classes))

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

    def ruff_code(self, file_paths: list[str]) -> None:
        """Run ruff lint and format on a list of file names.

        Args:
            file_paths: A list of files/directories to format and check
        """
        commands = [
            [
                "ruff",
                "format",
                "--config",
                f"line-length={self.config.output.max_line_length}",
                *file_paths,
            ],
            [
                "ruff",
                "check",
                "--config",
                f"line-length={self.config.output.max_line_length}",
                "--config",
                "lint.select = ['I']",
                "--config",
                "fixable = ['ALL']",
                "--fix",
                "--unsafe-fixes",
                "--exit-zero",
                *file_paths,
            ],
        ]
        try:
            for command in commands:
                subprocess.run(
                    command,
                    capture_output=True,
                    check=True,
                )
        except subprocess.CalledProcessError as e:
            details = e.stderr.decode().replace("error: ", "").strip()
            raise CodegenError(f"Ruff failed\n{details}")
