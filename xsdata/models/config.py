import warnings
from dataclasses import dataclass
from enum import Enum
from pathlib import Path
from typing import Any
from typing import Callable
from typing import Dict
from typing import List
from typing import TextIO

from pkg_resources import get_distribution

from xsdata.formats.dataclass.context import XmlContext
from xsdata.formats.dataclass.parsers import XmlParser
from xsdata.formats.dataclass.parsers.config import ParserConfig
from xsdata.formats.dataclass.serializers import XmlSerializer
from xsdata.formats.dataclass.serializers.config import SerializerConfig
from xsdata.formats.dataclass.serializers.writers import XmlEventWriter
from xsdata.models.mixins import array_element
from xsdata.models.mixins import attribute
from xsdata.models.mixins import element
from xsdata.utils import constants
from xsdata.utils import text


class OutputStructure(Enum):
    """
    Code writer output structure strategies.

    :cvar FILENAMES: filenames
    :cvar NAMESPACES: namespaces
    """

    FILENAMES = "filenames"
    NAMESPACES = "namespaces"


class NameCase(Enum):
    """
    Code writer naming schemes.

    All schemes are using a processor that splits a string into words
    when it encounters non alphanumerical characters or when an upper
    case letter follows a lower case letter.

    +-----------+-----------+-----------+------------+-----------------+-----------+-------------+--------------+
    | Original  | Pascal    | Camel     | Snake      | Screaming Snake | Mixed     | Mixed Snake | Mixed Pascal |
    +===========+===========+===========+============+=================+===========+=============+==============+
    | p00p      | P00P      | p00P      | p00p       | P00P            | p00p      | p00p        | P00p         |
    +-----------+-----------+-----------+------------+-----------------+-----------+-------------+--------------+
    | USERName  | Username  | username  | username   | USERNAME        | USERName  | USERName    | USERName     |
    +-----------+-----------+-----------+------------+-----------------+-----------+-------------+--------------+
    | UserNAME  | UserName  | userName  | user_name  | USER_NAME       | UserNAME  | User_NAME   | UserNAME     |
    +-----------+-----------+-----------+------------+-----------------+-----------+-------------+--------------+
    | USER_name | UserName  | userName  | user_name  | USER_NAME       | USERname  | USER_name   | USERname     |
    +-----------+-----------+-----------+------------+-----------------+-----------+-------------+--------------+
    | USER-NAME | UserName  | userName  | user_name  | USER_NAME       | USERNAME  | USER_NAME   | USERNAME     |
    +-----------+-----------+-----------+------------+-----------------+-----------+-------------+--------------+
    | User_Name | UserName  | userName  | user_name  | USER_NAME       | UserName  | User_Name   | UserName     |
    +-----------+-----------+-----------+------------+-----------------+-----------+-------------+--------------+
    | user_name | UserName  | userName  | user_name  | USER_NAME       | username  | user_name   | Username     |
    +-----------+-----------+-----------+------------+-----------------+-----------+-------------+--------------+
    | SUserNAME | SuserName | suserName | suser_name | SUSER_NAME      | SUserNAME | SUser_NAME  | SUserNAME    |
    +-----------+-----------+-----------+------------+-----------------+-----------+-------------+--------------+

    :cvar ORIGINAL: originalCase
    :cvar PASCAL: pascalCase
    :cvar CAMEL: camelCase
    :cvar SNAKE: snakeCase
    :cvar SCREAMING_SNAKE: screamingSnakeCase
    :cvar MIXED: mixedCase mixedCase
    :cvar MIXED_SNAKE: mixedSnakeCase
    :cvar MIXED_PASCAL: mixedPascalCase
    """  # noqa

    ORIGINAL = "originalCase"
    PASCAL = "pascalCase"
    CAMEL = "camelCase"
    SNAKE = "snakeCase"
    SCREAMING_SNAKE = "screamingSnakeCase"
    MIXED = "mixedCase"
    MIXED_SNAKE = "mixedSnakeCase"
    MIXED_PASCAL = "mixedPascalCase"

    def __call__(self, string: str, **kwargs: Any) -> str:
        return self.callback(string, **kwargs)

    @property
    def callback(self) -> Callable:
        """Return the actual callable of the scheme."""
        return __name_case_func__[self.value]


__name_case_func__: Dict[str, Callable] = {
    "originalCase": constants.return_input,
    "pascalCase": text.pascal_case,
    "camelCase": text.camel_case,
    "snakeCase": text.snake_case,
    "screamingSnakeCase": text.screaming_snake_case,
    "mixedCase": text.mixed_case,
    "mixedSnakeCase": text.mixed_snake_case,
    "mixedPascalCase": text.mixed_pascal_case,
}


class DocstringStyle(Enum):
    """
    Code writer docstring styles.

    :cvar RST: reStructuredText
    :cvar NUMPY: NumPy
    :cvar GOOGLE: Google
    :cvar ACCESSIBLE: Accessible
    """

    RST = "reStructuredText"
    NUMPY = "NumPy"
    GOOGLE = "Google"
    ACCESSIBLE = "Accessible"


@dataclass
class GeneratorOutput:
    """
    Main generator output options.

    :param max_line_length: Maximum line length
    :param package: Package name eg foo.bar.models
    :param format: Code generator output format name
    :param structure: Select an output structure
    :param docstring_style: Select a docstring style
    :param compound_fields: Use compound fields for repeating choices.
        Enable if elements ordering matters for your case.
    """

    max_line_length: int = attribute(default=79)
    package: str = element(default="generated")
    format: str = element(default="dataclasses")
    structure: OutputStructure = element(default=OutputStructure.FILENAMES)
    docstring_style: DocstringStyle = element(default=DocstringStyle.RST)
    compound_fields: bool = element(default=False)

    def __post_init__(self):
        if self.format == "pydata":
            warnings.warn(
                "Output format 'pydata' renamed to 'dataclasses'",
                DeprecationWarning,
            )
            self.format = "dataclasses"


@dataclass
class NameConvention:
    """
    Name convention model.

    :param case: Naming scheme, eg camelCase, snakeCase
    :param safe_prefix: A prefix to be prepended into names that match
        one of the reserved words: and, except, lambda, with, as,
        finally, nonlocal, while, assert, false, none, yield, break,
        for, not, class, from, or, continue, global, pass, def, if,
        raise, del, import, return, elif, in, true, else, is, try,
        str, int, bool, float, list, optional, dict, field
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
    constant_name: NameConvention = element(
        default_factory=lambda: NameConvention(NameCase.SCREAMING_SNAKE, "value")
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
    Define an alias for a module, package, class and field Alias definition
    model.

    Each alias has a source attribute that refers to the original name
    in the schema definition and the target attribute for output name.
    For package and module aliases the source refers to the schema
    filename or target namespace depending the selected output
    structure.

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

    .. warning::
        The generator doesn't validate aliases.

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

    :cvar version: xsdata version number the config was created/updated
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
        ctx = XmlContext(
            element_name_generator=text.pascal_case,
            attribute_name_generator=text.camel_case,
        )
        config = ParserConfig(fail_on_unknown_properties=False)
        parser = XmlParser(context=ctx, config=config)
        return parser.from_path(path, cls)

    @classmethod
    def write(cls, output: TextIO, obj: "GeneratorConfig"):
        ctx = XmlContext(
            element_name_generator=text.pascal_case,
            attribute_name_generator=text.camel_case,
        )
        config = SerializerConfig(pretty_print=True)
        serializer = XmlSerializer(context=ctx, config=config, writer=XmlEventWriter)
        serializer.write(output, obj, ns_map={None: "http://pypi.org/project/xsdata"})
