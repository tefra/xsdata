import re
import sys
import warnings
from dataclasses import dataclass, field
from enum import Enum
from pathlib import Path
from typing import Any, Callable, Dict, List, Pattern, TextIO

from xsdata import __version__
from xsdata.codegen.exceptions import CodegenError, CodegenWarning
from xsdata.formats.dataclass.context import XmlContext
from xsdata.formats.dataclass.parsers import XmlParser
from xsdata.formats.dataclass.parsers.config import ParserConfig
from xsdata.formats.dataclass.serializers import XmlSerializer
from xsdata.formats.dataclass.serializers.config import SerializerConfig
from xsdata.formats.dataclass.serializers.writers import XmlEventWriter
from xsdata.models.enums import Namespace
from xsdata.models.mixins import array_element, attribute, element, text_node
from xsdata.utils import objects, text


class StructureStyle(Enum):
    """Output structure style enumeration.

    Attributes:
        FILENAMES: filenames: groups classes by the schema location
        NAMESPACES: namespaces: group classes by the target namespace
        CLUSTERS: clusters: group by strong connected dependencies
        SINGLE_PACKAGE: single-package: group all classes together
        NAMESPACE_CLUSTERS: namespace-clusters: group by strong
            connected dependencies and namespaces
    """

    FILENAMES = "filenames"
    NAMESPACES = "namespaces"
    CLUSTERS = "clusters"
    SINGLE_PACKAGE = "single-package"
    NAMESPACE_CLUSTERS = "namespace-clusters"


class NameCase(Enum):
    """Naming case convention enumeration.

    All schemes are using a processor that splits a string into words
    when it encounters non-alphanumerical characters or when an upper
    case letter follows a lower case letter.

    Attributes:
        ORIGINAL: originalCase
        PASCAL: pascalCase
        CAMEL: camelCase
        SNAKE: snakeCase
        SCREAMING_SNAKE: screamingSnakeCase
        MIXED: mixedCase
        MIXED_SNAKE: mixedSnakeCase
        MIXED_PASCAL: mixedPascalCase
    """

    ORIGINAL = "originalCase"
    PASCAL = "pascalCase"
    CAMEL = "camelCase"
    SNAKE = "snakeCase"
    SCREAMING_SNAKE = "screamingSnakeCase"
    MIXED = "mixedCase"
    MIXED_SNAKE = "mixedSnakeCase"
    MIXED_PASCAL = "mixedPascalCase"

    def __call__(self, string: str, **kwargs: Any) -> str:
        """Apply the callback to the input string."""
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
    """Docstring style enumeration.

    Attributes:
        RST: reStructuredText
        NUMPY: NumPy
        GOOGLE: Google
        ACCESSIBLE: Accessible
        BLANK: Blank
    """

    RST = "reStructuredText"
    NUMPY = "NumPy"
    GOOGLE = "Google"
    ACCESSIBLE = "Accessible"
    BLANK = "Blank"


class ObjectType(Enum):
    """Object type enumeration.

    Attributes:
        CLASS: class
        FIELD: field
        MODULE: module
        PACKAGE: package
    """

    CLASS = "class"
    FIELD = "field"
    MODULE = "module"
    PACKAGE = "package"


class ExtensionType(Enum):
    """Extension type enumeration.

    Attributes:
        CLASS: class
        DECORATOR: decorator
    """

    CLASS = "class"
    DECORATOR = "decorator"


@dataclass
class OutputFormat:
    """Output format model representation.

    Args:
        value: Output format name
        repr: Generate __repr__ method
        eq: Generate __eq__ method
        order: Generate __lt__, __le__, __gt__, and __ge__ methods
        unsafe_hash: Generate __hash__ method
        frozen: Enable read only properties
        slots: Enable __slots__, python>=3.10 Only
        kw_only: Enable keyword only arguments, python>=3.10 Only
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
        """Post initialization method."""
        self.validate()

    def validate(self):
        """Validate and reset configuration conflicts."""
        if self.order and not self.eq:
            self.eq = True
            warnings.warn(
                "Enabling eq because order is true",
                CodegenWarning,
            )

        if self.value == "dataclasses" and sys.version_info < (3, 10):
            if self.slots:
                self.slots = False
                warnings.warn(
                    "slots requires python >= 3.10, reverting...",
                    CodegenWarning,
                )

            if self.kw_only:
                self.kw_only = False
                warnings.warn(
                    "kw_only requires python >= 3.10, reverting...",
                    CodegenWarning,
                )


@dataclass
class CompoundFields:
    """Compound fields model representation.

    Args:
        enabled: Use compound fields for repeatable elements
        default_name: Default compound field name
        use_substitution_groups: Use substitution groups if they
            exist, instead of element names.
        force_default_name: Always use the default compound field
            name, or try to generate one by the list of element names if
            they are no longer than the max name parts. e.g.
            hat_or_dress_or_something.
        max_name_parts: Maximum number of element names before using
            the default name.
    """

    enabled: bool = text_node(default=False, cli="compound-fields")
    default_name: str = attribute(default="choice", cli=False)
    use_substitution_groups: bool = attribute(default=False, cli=False)
    force_default_name: bool = attribute(default=False, cli=False)
    max_name_parts: int = attribute(default=3, cli=False)


@dataclass
class GeneratorOutput:
    """Generator output model representation.

    Args:
        package: Target package
        format: Output format
        structure_style: Output structure style
        docstring_style: Docstring style
        relative_imports: Use relative imports
        compound_fields: Use compound fields for repeatable elements
        max_line_length: Adjust the maximum line length
        subscriptable_types: Use PEP-585 generics for standard
            collections, python>=3.9 Only
        union_type: Use PEP-604 union type, python>=3.10 Only
        postponed_annotations: Use 563 postponed evaluation of  annotations
        unnest_classes: Move inner classes to upper level
        ignore_patterns: Ignore pattern restrictions
        include_header: Include a header with codegen information in the output
    """

    package: str = element(default="generated")
    format: OutputFormat = element(default_factory=OutputFormat)
    structure_style: StructureStyle = element(
        default=StructureStyle.FILENAMES, name="Structure"
    )
    docstring_style: DocstringStyle = element(default=DocstringStyle.RST)
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
        """Post initialization method."""
        self.validate()

    def validate(self):
        """Reset configuration conflicts."""
        if self.subscriptable_types and sys.version_info < (3, 9):
            self.subscriptable_types = False
            warnings.warn(
                "Generics PEP 585 requires python >= 3.9, reverting...",
                CodegenWarning,
            )

        if self.union_type and sys.version_info < (3, 10):
            self.union_type = False
            warnings.warn(
                "UnionType PEP 604 requires python >= 3.10, reverting...",
                CodegenWarning,
            )

        if self.union_type and not self.postponed_annotations:
            self.postponed_annotations = True
            warnings.warn(
                "Enabling postponed annotations, because `union_type==True`",
                CodegenWarning,
            )

    def update(self, **kwargs: Any):
        """Update instance attributes recursively."""
        objects.update(self, **kwargs)
        self.format.validate()


@dataclass
class NameConvention:
    """Name convention model representation.

    Args:
        case: Naming scheme, e.g. camelCase, snakeCase
        safe_prefix: A prefix to be prepended into names that match
            one of the reserved words.
    """

    case: NameCase = attribute(optional=False)
    safe_prefix: str = attribute(optional=False)


@dataclass
class GeneratorConventions:
    """Generator naming conventions model representation.

    Args:
        class_name: Class naming conventions.
        field_name: Field naming conventions.
        module_name: Module naming conventions.
        package_name: Package naming conventions.
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
    """Generator alias model representation.

    Define an alias for a module, package, class and field Alias definition
    model.

    Each alias has a source attribute that refers to the original name
    in the schema definition and the target attribute for output name.
    For package and module aliases the source refers to the schema
    filename or target namespace depending on the selected output
    structure.

    Args:
        source: The source name from schema definition
        target: The target name of the object.
    """

    source: str = attribute(required=True)
    target: str = attribute(required=True)


@dataclass
class GeneratorAliases:
    """Generator aliases model representation.

    Generator aliases for classes, fields, packages and modules
    that bypass the global naming conventions. The aliases
    are not validated as valid python identifiers.

    Args:
        class_name: A list of class name aliases
        field_name: A list of field name aliases
        package_name: A list of package name aliases
        module_name: A list of module name aliases
    """

    class_name: List[GeneratorAlias] = array_element()
    field_name: List[GeneratorAlias] = array_element()
    package_name: List[GeneratorAlias] = array_element()
    module_name: List[GeneratorAlias] = array_element()


@dataclass
class GeneratorSubstitution:
    """Generator substitution model representation.

    Search and replace substitutions based on `re.sub`.

    Args:
        type: The target object type
        search: The search string or a pattern object
        replace: The replacement string or pattern object
    """

    type: ObjectType = attribute(required=True)
    search: str = attribute(required=True)
    replace: str = attribute(required=True)


@dataclass
class GeneratorExtension:
    """Generator extension model representation.

    Add decorators or base classes on the generated classes
    that match the class name pattern.

    Args:
        type: The extension type
        class_name: The class name or a pattern to apply the extension
        import_string: The import string of the extension type
        prepend: Prepend or append decorator or base class
        apply_if_derived: Apply or skip if the class is already a subclass

    Attributes:
        module_path: The module path of the base class or the annotation
        func_name: The annotation or base class name
        pattern: The compiled search class name pattern
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
        """Post initialization method.

        Set the module, func_name and pattern instance attributes.

        Raises:
            GeneratorConfigError: If the pattern can not be compiled.
        """
        try:
            self.module_path, self.func_name = self.import_string.rsplit(".", 1)
        except (ValueError, AttributeError):
            raise CodegenError(
                "Invalid extension import string", value=self.import_string
            )

        try:
            self.pattern = re.compile(self.class_name)
        except re.error:
            raise CodegenError(
                "Failed to compile extension pattern", pattern=self.class_name
            )


@dataclass
class GeneratorSubstitutions:
    """Generator substitutions model representation.

    Generator search and replace substitutions for classes, fields, packages
    and modules names. The process runs before and after the default naming
    conventions.

    Args:
        substitution: The list of substitution instances
    """

    substitution: List[GeneratorSubstitution] = array_element()


@dataclass
class GeneratorExtensions:
    """Generator extensions model representation.

    Generator extensions for classes. The process runs after the
    default naming conventions. The generator doesn't validate
    imports!

    Args:
        extension: The list of extension instances
    """

    extension: List[GeneratorExtension] = array_element()


@dataclass
class GeneratorConfig:
    """Generator configuration model representation.

    Args:
        output: Output options
        conventions: Generator conventions
        substitutions: Search and replace substitutions for
            classes, fields, packages and modules names.
        extensions: Generator custom base classes and decorators for classes.

    Attributes:
        version: The xsdata version number the config was created/updated
    """

    class Meta:
        """Metadata options."""

        name = "Config"
        namespace = "http://pypi.org/project/xsdata"

    version: str = attribute(init=False, default=__version__)
    output: GeneratorOutput = element(default_factory=GeneratorOutput)
    conventions: GeneratorConventions = element(default_factory=GeneratorConventions)
    substitutions: GeneratorSubstitutions = element(
        default_factory=GeneratorSubstitutions
    )
    extensions: GeneratorExtensions = element(default_factory=GeneratorExtensions)

    @classmethod
    def create(cls) -> "GeneratorConfig":
        """Initialize with default substitutions for common namespaces."""
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
        """Load configuration from a file path."""
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
        return parser.from_path(path, cls)

    @classmethod
    def write(cls, output: TextIO, obj: "GeneratorConfig"):
        """Write the configuration to the output stream as xml."""
        ctx = XmlContext(
            element_name_generator=text.pascal_case,
            attribute_name_generator=text.camel_case,
        )
        config = SerializerConfig(indent="  ")
        serializer = XmlSerializer(context=ctx, config=config, writer=XmlEventWriter)
        serializer.write(output, obj, ns_map={None: "http://pypi.org/project/xsdata"})
