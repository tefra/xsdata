from dataclasses import dataclass
from enum import Enum
from pathlib import Path
from typing import Callable
from typing import List
from typing import TextIO

from pkg_resources import get_distribution

from xsdata.formats.dataclass.context import XmlContext
from xsdata.formats.dataclass.parsers import XmlParser
from xsdata.formats.dataclass.parsers.config import ParserConfig
from xsdata.formats.dataclass.serializers import XmlSerializer
from xsdata.models.mixins import array_element
from xsdata.models.mixins import attribute
from xsdata.models.mixins import element
from xsdata.utils import text


class OutputFormat(Enum):
    """Available output formats: pydata (dataclasses), PlantUML class
    diagram."""

    DATACLASS = "pydata"
    PLANTUML = "plantuml"


class OutputStructure(Enum):
    """Available output structure strategies, based on filenames or the target
    namespaces."""

    FILENAMES = "filenames"
    NAMESPACES = "namespaces"


class NameCase(Enum):
    """Available naming schemes, pascal, snake, camel, mixed and mixed
    underscore."""

    PASCAL = "pascalCase"
    CAMEL = "camelCase"
    SNAKE = "snakeCase"
    MIXED = "mixedCase"
    MIXED_SNAKE = "mixedSnakeCase"

    @property
    def func(self) -> Callable:
        """Return the actual callable of the scheme."""
        return __name_case_func__[self.value]


__name_case_func__ = {
    "pascalCase": text.pascal_case,
    "camelCase": text.camel_case,
    "snakeCase": text.snake_case,
    "mixedCase": text.mixed_case,
    "mixedSnakeCase": text.mixed_snake_case,
}


@dataclass
class GeneratorOutput:
    """
    Main generator output options.

    :param wsdl: Enable wsdl mode
    :param package: Package name eg foo.bar.models
    :param format: Select an output format
    :param structure: Select an output structure
    :param compound_fields: Use compound fields for repeating choices.
        Enable if elements ordering matters for your case.
    """

    wsdl: bool = attribute(default=False)
    package: str = element(default="generated")
    format: OutputFormat = element(default=OutputFormat.DATACLASS)
    structure: OutputStructure = element(default=OutputStructure.FILENAMES)
    compound_fields: bool = element(default=False)


@dataclass
class NameConvention:
    """
    Name convention model.

    :param case: Naming scheme, eg camelCase, snakeCase
    :param safe_prefix: A prefix to be prepended into names that match reserved words.
    """

    case: NameCase = attribute(optional=False)
    safe_prefix: str = attribute(optional=False)


@dataclass
class GeneratorConventions:
    """
    Generator global naming conventions.

    :param class_name: Class naming conventions.
    :param field_name: Field naming conventions.
    :param module_name: Module naming conventions.
    :param package_name: Package naming conventions.
    """

    class_name: NameConvention = element(
        default_factory=lambda: NameConvention(NameCase.PASCAL, "type")
    )
    field_name: NameConvention = element(
        default_factory=lambda: NameConvention(NameCase.SNAKE, "value")
    )
    module_name: NameConvention = element(
        default_factory=lambda: NameConvention(NameCase.SNAKE, "mod")
    )
    package_name: NameConvention = element(
        default_factory=lambda: NameConvention(NameCase.SNAKE, "pkg")
    )


@dataclass
class GeneratorAlias:
    """
    Alias definition model.

    :param source: The source name from schema definition
    :param target: The target name of the object.
    """

    source: str = attribute(required=True)
    target: str = attribute(required=True)


@dataclass
class GeneratorAliases:
    """
    Generator aliases for classes, fields, packages and modules that bypass the
    global naming conventions.

    :param class_name: list of class name aliases
    :param field_name: list of field name aliases
    :param package_name: list of package name aliases
    :param module_name: list of module name aliases
    """

    class_name: List[GeneratorAlias] = array_element()
    field_name: List[GeneratorAlias] = array_element()
    package_name: List[GeneratorAlias] = array_element()
    module_name: List[GeneratorAlias] = array_element()


@dataclass
class GeneratorConfig:
    """
    Generator configuration binding model.

    :param version: xsdata version number the config was created/updated
    :param output: output options
    :param conventions: generator conventions
    :param aliases: generator aliases
    """

    class Meta:
        name = "Config"
        namespace = "http://pypi.org/project/xsdata"

    version: str = attribute(init=False, default=get_distribution("xsdata").version)
    output: GeneratorOutput = element(default_factory=GeneratorOutput)
    conventions: GeneratorConventions = element(default_factory=GeneratorConventions)
    aliases: GeneratorAliases = element(default_factory=GeneratorAliases)

    @classmethod
    def create(cls) -> "GeneratorConfig":
        obj = cls()
        obj.aliases.class_name.append(GeneratorAlias("fooType", "Foo"))
        obj.aliases.class_name.append(GeneratorAlias("ABCSomething", "ABCSomething"))
        obj.aliases.field_name.append(
            GeneratorAlias("ChangeofGauge", "change_of_gauge")
        )
        obj.aliases.package_name.append(
            GeneratorAlias("http://www.w3.org/1999/xhtml", "xtml")
        )
        obj.aliases.module_name.append(GeneratorAlias("2010.1", "2020a"))
        return obj

    @classmethod
    def read(cls, path: Path) -> "GeneratorConfig":
        ctx = XmlContext(element_name=text.pascal_case, attribute_name=text.camel_case)
        config = ParserConfig(fail_on_unknown_properties=False)
        parser = XmlParser(context=ctx, config=config)
        return parser.from_path(path, cls)

    @classmethod
    def write(cls, output: TextIO, obj: "GeneratorConfig"):
        ctx = XmlContext(element_name=text.pascal_case, attribute_name=text.camel_case)
        serializer = XmlSerializer(context=ctx, pretty_print=True)
        serializer.write(output, obj, ns_map={None: "http://pypi.org/project/xsdata"})
