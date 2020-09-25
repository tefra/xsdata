from dataclasses import dataclass
from enum import Enum
from pathlib import Path
from typing import Callable
from typing import List
from typing import Optional

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
    DATACLASS = "pydata"
    PLANTUML = "plantuml"


class OutputStructure(Enum):
    FILENAMES = "filenames"
    NAMESPACES = "namespaces"


class OverrideType(Enum):
    CLASS = "class"
    FIELD = "field"
    MODULE = "module"
    PACKAGE = "package"


class PropertyType(Enum):
    NAME = "name"
    HELP = "help"


class NameCase(Enum):
    PASCAL = "pascalCase"
    SNAKE = "snakeCase"
    MIXED = "mixedCase"
    CAMEL = "camelCase"

    @property
    def func(self) -> Callable:
        return __name_case_func__[self.value]


__name_case_func__ = {
    "pascalCase": text.pascal_case,
    "snakeCase": text.snake_case,
    "mixedCase": text.mixed_case,
    "camelCase": text.camel_case,
}


@dataclass
class GeneratorOutput:
    wsdl: bool = attribute(default=False)
    package: str = element(default="generated")
    format: OutputFormat = element(default=OutputFormat.DATACLASS)
    structure: OutputStructure = element(default=OutputStructure.FILENAMES)


@dataclass
class NameConvention:
    case: NameCase = attribute(optional=False)
    safe_prefix: str = attribute(optional=False)


@dataclass
class GeneratorConventions:
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
class Override:
    type: OverrideType = attribute(required=True)
    property: PropertyType = attribute(required=True)
    source: str = attribute(required=True)
    target: str = attribute(required=True)


@dataclass
class Alias:
    source: str = attribute(required=True)
    target: str = attribute(required=True)


@dataclass
class Aliases:
    class_name: List[Alias] = array_element()
    field_name: List[Alias] = array_element()
    package_name: List[Alias] = array_element()
    module_name: List[Alias] = array_element()


@dataclass
class GeneratorConfig:
    class Meta:
        name = "Config"
        namespace = "http://pypi.org/project/xsdata"

    version: str = attribute(init=False, default=get_distribution("xsdata").version)
    output: GeneratorOutput = element(default_factory=GeneratorOutput)
    conventions: GeneratorConventions = element(default_factory=GeneratorConventions)
    aliases: Aliases = element(default_factory=Aliases)

    @classmethod
    def read(
        cls, path: Path, context: Optional[XmlContext] = None
    ) -> "GeneratorConfig":
        context = context or cls.context()
        config = ParserConfig(fail_on_unknown_properties=False)
        parser = XmlParser(context=context, config=config)
        return parser.from_path(path, cls)

    @classmethod
    def create(cls, path: Path):
        obj = cls()
        obj.aliases.class_name.append(Alias("fooType", "Foo"))
        obj.aliases.class_name.append(Alias("ABCSomething", "ABCSomething"))
        obj.aliases.field_name.append(Alias("ChangeofGauge", "change_of_gauge"))
        obj.aliases.package_name.append(Alias("http://www.w3.org/1999/xhtml", "xtml"))
        obj.aliases.module_name.append(Alias("2010.1", "2020a"))
        cls.write(path, obj, cls.context())

    @classmethod
    def update(cls, path: Path):
        context = cls.context()
        obj = cls.read(path, context)
        cls.write(path, obj, context)

    @classmethod
    def write(cls, path: Path, obj: "GeneratorConfig", context: XmlContext):
        serializer = XmlSerializer(context=context, pretty_print=True)
        with path.open("w") as fp:
            serializer.write(fp, obj, ns_map={None: "http://pypi.org/project/xsdata"})

    @classmethod
    def context(cls) -> XmlContext:
        return XmlContext(element_name=text.pascal_case, attribute_name=text.camel_case)
