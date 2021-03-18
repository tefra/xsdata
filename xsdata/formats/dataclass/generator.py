import re
from pathlib import Path
from typing import Iterator
from typing import List

from jinja2 import Environment
from jinja2 import FileSystemLoader

from xsdata.codegen.models import Class
from xsdata.codegen.models import Import
from xsdata.codegen.resolver import DependenciesResolver
from xsdata.formats.dataclass.filters import Filters
from xsdata.formats.mixins import AbstractGenerator
from xsdata.formats.mixins import GeneratorResult
from xsdata.models.config import GeneratorConfig
from xsdata.utils.collections import group_by


class DataclassGenerator(AbstractGenerator):
    """Python dataclasses code generator."""

    def __init__(self, config: GeneratorConfig):
        """Override generator constructor to set templates directory and
        environment filters."""

        super().__init__(config)

        tpl_dir = Path(__file__).parent.joinpath("templates")
        self.env = Environment(loader=FileSystemLoader(tpl_dir), autoescape=False)
        self.filters = Filters.from_config(config)
        self.filters.register(self.env)

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

        imports = [
            Import(name=obj.name, source=obj.target_module)
            for obj in sorted(classes, key=lambda x: x.name)
        ]

        for group in group_by(imports, key=lambda x: x.name).values():
            if len(group) == 1:
                continue

            for index, cur in enumerate(group):
                cmp = group[index + 1] if index == 0 else group[index - 1]
                parts = re.split("[_.]", cur.source)
                diff = set(parts) - set(re.split("[_.]", cmp.source))

                add = "_".join(part for part in parts if part in diff)
                cur.alias = f"{add}:{cur.name}"

        return self.env.get_template("imports.jinja2").render(imports=imports)

    def render_module(
        self, resolver: DependenciesResolver, classes: List[Class]
    ) -> str:
        """Render the source code for the target module of the given class
        list."""
        resolver.process(classes)
        imports = resolver.sorted_imports()
        output = self.render_classes(resolver.sorted_classes())
        namespace = classes[0].target_namespace

        return self.env.get_template("module.jinja2").render(
            output=output, imports=imports, namespace=namespace
        )

    def render_classes(self, classes: List[Class]) -> str:
        """Render the source code of the classes."""
        load = self.env.get_template
        config = self.config

        def render_class(obj: Class) -> str:
            """Render class or enumeration."""

            if obj.is_enumeration:
                template = "enum.jinja2"
            elif obj.is_service:
                template = "service.jinja2"
            else:
                template = "class.jinja2"

            return (
                load(template)
                .render(
                    obj=obj, docstring_style=config.output.docstring_style.name.lower()
                )
                .strip()
            )

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

    def module_name(self, name: str) -> str:
        """Convert the given module name to safe snake case."""
        return self.filters.module_name(name)

    def package_name(self, name: str) -> str:
        """Convert the given package name to safe snake case."""
        return self.filters.package_name(name)
