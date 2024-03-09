import subprocess
from pathlib import Path
from textwrap import indent
from typing import Iterator, List, Optional

from jinja2 import Environment, FileSystemLoader

from xsdata.codegen.exceptions import CodegenError
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

    __slots__ = ("env", "filters", "ruff_config")

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
        self.ruff_config = Path(__file__).parent / "ruff.toml"

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
            package_path = path.joinpath("__init__.py")
            src_code = self.render_package(cluster, module, package_path)

            yield GeneratorResult(
                path=package_path,
                title="init",
                source=src_code,
            )
            yield from self.ensure_packages(path.parent)

        # Generate modules
        for path, cluster in self.group_by_module(classes).items():
            module_path = path.with_suffix(".py")
            src_code = self.render_module(resolver, cluster, module_path)

            yield GeneratorResult(
                path=module_path,
                title=cluster[0].target_module,
                source=src_code,
            )

    def render_package(self, classes: List[Class], module: str, filename: Path) -> str:
        """Render the package for the given classes.

        Args:
            classes: A list of class instances
            module: The target dot notation path
            filename: The package path

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
        return self.ruff_code(output, filename)

    def render_module(
        self,
        resolver: DependenciesResolver,
        classes: List[Class],
        filename: Path,
    ) -> str:
        """Render the module for the given classes.

        Args:
            resolver: The dependencies resolver
            classes: A list of class instances
            filename: The module path

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

        result = self.env.get_template(self.module_template).render(
            output=output,
            classes=classes,
            module=module,
            imports=imports,
            namespace=module_namespace,
        )

        return self.ruff_code(result, filename)

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

    def ruff_code(self, src_code: str, file_path: Path) -> str:
        """Run ruff format on the src code.

        Args:
            src_code: The output source code
            file_path: The file path the source code will be written to

        Returns:
            The formatted output source code
        """
        commands = [
            [
                "ruff",
                "format",
                "--stdin-filename",
                str(file_path),
                "--line-length",
                str(self.config.output.max_line_length),
            ],
            [
                "ruff",
                "checks",
                "--stdin-filename",
                str(file_path),
                "--line-length",
                str(self.config.output.max_line_length),
                "--config",
                str(self.ruff_config),
                "--fix",
                "--unsafe-fixes",
                "--exit-zero",
            ],
        ]
        try:
            src_code_encoded = src_code.encode()
            for command in commands:
                result = subprocess.run(
                    command,
                    input=src_code_encoded,
                    capture_output=True,
                    check=True,
                )
                src_code_encoded = result.stdout

            return src_code_encoded.decode()
        except subprocess.CalledProcessError as e:
            error = indent(e.stderr.decode(), "  ")
            raise CodegenError("Ruff failed", details=error)
