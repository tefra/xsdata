import re
import sys
import warnings
from dataclasses import dataclass
from dataclasses import field
from enum import Enum
from pathlib import Path
from typing import Any
from typing import Callable
from typing import Dict
from typing import List
from typing import Optional
from typing import Pattern
from typing import TextIO

from xsdata import __version__
from xsdata.exceptions import CodeGenerationWarning
from xsdata.exceptions import GeneratorConfigError
from xsdata.formats.dataclass.context import XmlContext
from xsdata.formats.dataclass.parsers import XmlParser
from xsdata.formats.dataclass.parsers.config import ParserConfig
from xsdata.formats.dataclass.serializers import XmlSerializer
from xsdata.formats.dataclass.serializers.config import SerializerConfig
from xsdata.formats.dataclass.serializers.writers import XmlEventWriter
from xsdata.logger import logger
from xsdata.models.enums import Namespace
from xsdata.models.mixins import array_element
from xsdata.models.mixins import attribute
from xsdata.models.mixins import element
from xsdata.models.mixins import text_node
from xsdata.utils import objects
from xsdata.utils import text


class StructureStyle(Enum):
    """
    Code writer output structure strategies.

    :cvar FILENAMES: filenames: groups classes by the schema location
    :cvar NAMESPACES: namespaces: group classes by the target namespace
    :cvar CLUSTERS: clusters: group by strong connected dependencies
    :cvar SINGLE_PACKAGE: single-package: group all classes together
    :cvar NAMESPACE_CLUSTERS: namespace-clusters: group by strong
        connected dependencies and namespaces
    """

    FILENAMES = "filenames"
    NAMESPACES = "namespaces"
    CLUSTERS = "clusters"
    SINGLE_PACKAGE = "single-package"
    NAMESPACE_CLUSTERS = "namespace-clusters"


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
    "originalCase": text.original_case,
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
    :cvar BLANK: Blank
    """

    RST = "reStructuredText"
    NUMPY = "NumPy"
    GOOGLE = "Google"
    ACCESSIBLE = "Accessible"
    BLANK = "Blank"


class ClassFilterStrategy(Enum):
    """
    Class filter strategy.

    :cvar ALL: all: Generate all types, discouraged!!!
    :cvar ALL_GLOBALS: allGlobals: Generate all global types
    :cvar REFERRED_GLOBALS: referredGlobals: Generate all global types
        with at least one reference.
    """

    ALL = "all"
    ALL_GLOBALS = "allGlobals"
    REFERRED_GLOBALS = "referredGlobals"


class ObjectType(Enum):
    """
    Object type enumeration.

    :cvar CLASS: class
    :cvar FIELD: field
    :cvar MODULE: module
    :cvar PACKAGE: package
    """

    CLASS = "class"
    FIELD = "field"
    MODULE = "module"
    PACKAGE = "package"


class ExtensionType(Enum):
    """
    Extension type enumeration.

    :cvar CLASS: class
    :cvar DECORATOR: decorator
    """

    CLASS = "class"
    DECORATOR = "decorator"


@dataclass
class OutputFormat:
    """
    Output format options.

    :param value: Output format name, default: dataclasses
    :param repr: Generate __repr__ method, default: true
    :param eq: Generate __eq__ method, default: true
    :param order: Generate __lt__, __le__, __gt__, and __ge__ methods,
        default: false
    :param unsafe_hash: Generate __hash__ method if not frozen, default:
        false
    :param frozen: Enable read only properties, default false
    :param slots: Enable __slots__, default: false, python>=3.10 Only
    :param kw_only: Enable keyword only arguments, default: false,
        python>=3.10 Only
    """

    value: str = text_node(default="dataclasses", cli="output")
    repr: bool = attribute(default=True)
    eq: bool = attribute(default=True)
    order: bool = attribute(default=False)
    unsafe_hash: bool = attribute(default=False)
    frozen: bool = attribute(default=False)
    slots: bool = attribute(default=False)
    kw_only: bool = attribute(default=False)

    def __post_init__(self):
        self.validate()

    def validate(self):
        if self.order and not self.eq:
            raise GeneratorConfigError("eq must be true if order is true")

        if self.value == "dataclasses" and sys.version_info < (3, 10):
            if self.slots:
                self.slots = False
                warnings.warn(
                    "slots requires python >= 3.10, reverting...",
                    CodeGenerationWarning,
                )

            if self.kw_only:
                self.kw_only = False
                warnings.warn(
                    "kw_only requires python >= 3.10, reverting...",
                    CodeGenerationWarning,
                )


@dataclass
class CompoundFields:
    """
    Compound fields options.

    :param enabled: Use compound fields for repeatable elements,
        default: false
    :param default_name: Default compound field name, default: choice
    :param force_default_name: Always use the default compound field,
        otherwise if the number of elements is less than 4 the generator
        will try to dynamically create the field name eg.
        hat_or_dress_or_something.
    """

    enabled: bool = text_node(default=False, cli="compound-fields")
    default_name: str = attribute(default="choice", cli=False)
    force_default_name: bool = attribute(default=False, cli=False)


@dataclass
class GeneratorOutput:
    """
    Main generator output options.

    :param package: Target package, default: generated
    :param format: Output format
    :param structure_style: Output structure style, default: filenames
    :param docstring_style: Docstring style, default: reStructuredText
    :param filter_strategy: Class filter strategy, default: globals
    :param relative_imports: Use relative imports, default: false
    :param compound_fields: Use compound fields for repeatable elements,
        default: false
    :param max_line_length: Adjust the maximum line length, default: 79
    :param subscriptable_types: Use PEP-585 generics for standard collections,
        default: false, python>=3.9 Only
    :param union_type: Use PEP-604 union type, default: false, python>=3.10 Only
    :param postponed_annotations: Enable postponed evaluation of annotations,
        default: false, python>=3.7 Only
    :param unnest_classes: Move inner classes to upper level, default: false
    :param ignore_patterns: Ignore pattern restrictions, default: false
    :param include_header: Include a header with codegen information in the output,
        default: false
    """

    package: str = element(default="generated")
    format: OutputFormat = element(default_factory=OutputFormat)
    structure_style: StructureStyle = element(
        default=StructureStyle.FILENAMES, name="Structure"
    )
    docstring_style: DocstringStyle = element(default=DocstringStyle.RST)
    filter_strategy: ClassFilterStrategy = element(
        default=ClassFilterStrategy.ALL_GLOBALS
    )
    relative_imports: bool = element(default=False)
    compound_fields: CompoundFields = element(default_factory=CompoundFields)
    max_line_length: int = attribute(default=79)
    subscriptable_types: bool = attribute(default=False)
    union_type: bool = attribute(default=False)
    postponed_annotations: bool = element(default=False)
    unnest_classes: bool = element(default=False)
    ignore_patterns: bool = element(default=False)
    include_header: bool = element(default=False)

    def __post_init__(self):
        self.validate()

    def validate(self):
        if self.subscriptable_types and sys.version_info < (3, 9):
            self.subscriptable_types = False
            warnings.warn(
                "Generics PEP 585 requires python >= 3.9, reverting...",
                CodeGenerationWarning,
            )

        if self.union_type and sys.version_info < (3, 10):
            self.union_type = False
            warnings.warn(
                "UnionType PEP 604 requires python >= 3.10, reverting...",
                CodeGenerationWarning,
            )

        if self.union_type and not self.postponed_annotations:
            self.postponed_annotations = True
            warnings.warn(
                "Enabling postponed annotations, because `union_type==True`",
                CodeGenerationWarning,
            )

    def update(self, **kwargs: Any):
        objects.update(self, **kwargs)
        self.format.validate()


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
class GeneratorSubstitution:
    """
    Search and replace substitution for a specific target type based on
    :func:`re.sub`

    :param type: The target object type
    :param search: The search string or a pattern object
    :param replace: The replacement string or pattern object
    """

    type: ObjectType = attribute(required=True)
    search: str = attribute(required=True)
    replace: str = attribute(required=True)


@dataclass
class GeneratorExtension:
    """
    Add decorators or base classes on the generated classes that match the
    class name pattern.

    :param type: The extension type
    :param class_name: The class name or a pattern to apply the
        extension
    :param import_string: The import string of the extension type
    :param prepend: Prepend or append decorator or base class
    :param apply_if_derived: Apply or skip if the class is already a
        subclass
    """

    type: ExtensionType = attribute(required=True)
    class_name: str = attribute(required=True, name="class")
    import_string: str = attribute(required=True, name="import")
    prepend: bool = attribute(default=False)
    apply_if_derived: bool = attribute(default=False, name="applyIfDerived")

    module_path: str = field(
        init=False,
        metadata={"type": "Ignore"},
    )
    func_name: str = field(
        init=False,
        metadata={"type": "Ignore"},
    )
    pattern: Pattern = field(
        init=False,
        metadata={"type": "Ignore"},
    )

    def __post_init__(self):
        try:
            self.module_path, self.func_name = self.import_string.rsplit(".", 1)
        except (ValueError, AttributeError):
            raise GeneratorConfigError(
                f"Invalid extension import '{self.import_string}'"
            )

        try:
            self.pattern = re.compile(self.class_name)
        except re.error:
            raise GeneratorConfigError(f"Failed to compile pattern '{self.class_name}'")


@dataclass
class GeneratorSubstitutions:
    """
    Generator search and replace substitutions for classes, fields, packages
    and modules names. The process runs before and after the default naming
    conventions.

    .. warning:: The generator doesn't validate substitutions.

    :param substitution: The list of substitutions
    """

    substitution: List[GeneratorSubstitution] = array_element()


@dataclass
class GeneratorExtensions:
    """
    Generator extensions for classes. The process runs after the default naming
    conventions.

    .. warning:: The generator doesn't validate imports!

    :param extension: The list of extensions
    """

    extension: List[GeneratorExtension] = array_element()


@dataclass
class GeneratorConfig:
    """
    Generator configuration binding model.

    :cvar version: xsdata version number the config was created/updated
    :param output: Output options
    :param conventions: Generator conventions
    :param aliases: Generator aliases, Deprecated since v21.12, use
        substitutions
    :param substitutions: Generator search and replace substitutions for
        classes, fields, packages and modules names.
    :param extensions: Generator custom base classes and decorators for
        classes.
    """

    class Meta:
        name = "Config"
        namespace = "http://pypi.org/project/xsdata"

    version: str = attribute(init=False, default=__version__)
    output: GeneratorOutput = element(default_factory=GeneratorOutput)
    conventions: GeneratorConventions = element(default_factory=GeneratorConventions)
    aliases: Optional[GeneratorAliases] = element(default=None)
    substitutions: GeneratorSubstitutions = element(
        default_factory=GeneratorSubstitutions
    )
    extensions: GeneratorExtensions = element(default_factory=GeneratorExtensions)

    def __post_init__(self):
        if self.aliases:
            alias_map = {
                ObjectType.CLASS: self.aliases.class_name,
                ObjectType.FIELD: self.aliases.field_name,
                ObjectType.PACKAGE: self.aliases.package_name,
                ObjectType.MODULE: self.aliases.module_name,
            }
            for object_type, aliases in alias_map.items():
                for alias in aliases:
                    self.substitutions.substitution.append(
                        GeneratorSubstitution(
                            type=object_type, search=alias.source, replace=alias.target
                        )
                    )

    @classmethod
    def create(cls) -> "GeneratorConfig":
        obj = cls()

        for ns in Namespace:
            obj.substitutions.substitution.append(
                GeneratorSubstitution(
                    type=ObjectType.PACKAGE, search=ns.uri, replace=ns.prefix
                )
            )

        obj.substitutions.substitution.append(
            GeneratorSubstitution(
                type=ObjectType.CLASS, search="(.*)Class$", replace="\\1Type"
            )
        )

        return obj

    @classmethod
    def read(cls, path: Path) -> "GeneratorConfig":
        if not path.exists():
            return cls()

        ctx = XmlContext(
            element_name_generator=text.pascal_case,
            attribute_name_generator=text.camel_case,
        )
        parser = XmlParser(
            context=ctx,
            config=ParserConfig(
                fail_on_unknown_properties=False,
                fail_on_converter_warnings=True,
            ),
        )
        config = parser.from_path(path, cls)

        if config.aliases and (
            config.aliases.class_name
            or config.aliases.field_name
            or config.aliases.package_name
            or config.aliases.module_name
        ):
            config.aliases = None
            logger.warning("Migrating aliases to substitutions config, verify output!")
            with path.open("w") as fp:
                config.write(fp, config)

        return config

    @classmethod
    def write(cls, output: TextIO, obj: "GeneratorConfig"):
        ctx = XmlContext(
            element_name_generator=text.pascal_case,
            attribute_name_generator=text.camel_case,
        )
        config = SerializerConfig(pretty_print=True)
        serializer = XmlSerializer(context=ctx, config=config, writer=XmlEventWriter)
        serializer.write(output, obj, ns_map={None: "http://pypi.org/project/xsdata"})
