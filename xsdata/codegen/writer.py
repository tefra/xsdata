from dataclasses import dataclass
from dataclasses import field
from typing import Dict
from typing import List

from xsdata.codegen.models import Class
from xsdata.exceptions import CodeGenerationError
from xsdata.formats.dataclass.generator import DataclassGenerator
from xsdata.formats.mixins import AbstractGenerator
from xsdata.formats.plantuml.generator import PlantUmlGenerator
from xsdata.logger import logger


@dataclass
class CodeWriter:
    """
    Proxy to format generators and files structure creation.

    :param generators:
    """

    generators: Dict[str, AbstractGenerator] = field(default_factory=dict)

    @property
    def formats(self) -> List[str]:
        """Return a list of the registered generator names."""
        return list(self.generators.keys())

    def register_format(self, name: str, generator: AbstractGenerator):
        """Register a new generator by name."""
        self.generators[name] = generator

    def get_format(self, name: str) -> AbstractGenerator:
        """Get a generator by name."""
        return self.generators[name]

    def write(self, classes: List[Class], output: str):
        """Iterate over the designated generator outputs and create the
        necessary directories and files."""
        engine = self.get_format(output)
        for result in engine.render(classes):
            if len(result.source.strip()) > 0:
                logger.info("Generating package: %s", result.title)

                result.path.parent.mkdir(parents=True, exist_ok=True)
                result.path.write_text(result.source)

    def print(self, classes: List[Class], output: str):
        """Iterate over the designated generator outputs and print them to the
        console."""
        engine = self.get_format(output)
        for result in engine.render(classes):
            print(result.source, end="")

    def designate(
        self, classes: List[Class], output: str, package: str, ns_struct: bool
    ):
        """
        Normalize the target package and module names by the given output
        generator.

        :param classes: a list of codegen class instances
        :param output: target output format
        :param package: the original user provided package name
        :param ns_struct: use the target namespaces to group the classes in the same
            module.
        """
        modules = {}
        packages = {}

        for obj in classes:

            if ns_struct:
                if not obj.target_namespace:
                    raise CodeGenerationError(
                        f"Class `{obj.name}` target namespace "
                        f"is empty, avoid option `--ns-struct`"
                    )

                obj.package = package
                obj.module = obj.target_namespace

            if obj.package is None:
                raise CodeGenerationError(
                    f"Class `{obj.name}` has not been assign to a package."
                )

            if obj.module not in modules:
                modules[obj.module] = self.module_name(obj.module, output)

            if obj.package not in packages:
                packages[obj.package] = self.package_name(obj.package, output)

            obj.module = modules[obj.module]
            obj.package = packages[obj.package]

    def module_name(self, module: str, output: str) -> str:
        """Proxy method for the format generator."""
        engine = self.get_format(output)
        return engine.module_name(module)

    def package_name(self, package: str, output: str) -> str:
        """Proxy method for the format generator."""
        engine = self.get_format(output)
        return engine.package_name(package)


writer = CodeWriter()
writer.register_format("pydata", DataclassGenerator())
writer.register_format("plantuml", PlantUmlGenerator())
