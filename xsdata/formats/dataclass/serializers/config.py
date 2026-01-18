import warnings
from collections.abc import Callable
from dataclasses import InitVar, dataclass
from typing import Any


@dataclass
class SerializerConfig:
    """Serializer configuration options.

    Not all options are applicable for both xml and json documents.

    Args:
        encoding: Text encoding
        xml_version: XML Version number (1.0|1.1)
        xml_declaration: Generate XML declaration
        indent: Indent output by the given string
        ignore_default_attributes: Ignore optional attributes with default values
        schema_location: xsi:schemaLocation attribute value
        no_namespace_schema_location: xsi:noNamespaceSchemaLocation attribute value
        globalns: Dictionary containing global variables to extend or
            overwrite for typing
    """

    encoding: str = "UTF-8"
    xml_version: str = "1.0"
    xml_declaration: bool = True
    indent: str | None = None
    ignore_default_attributes: bool = False
    schema_location: str | None = None
    no_namespace_schema_location: str | None = None
    globalns: dict[str, Callable] | None = None

    # Deprecated
    pretty_print: InitVar[bool] = False
    pretty_print_indent: InitVar[str | None] = None

    def __post_init__(self, pretty_print: bool, pretty_print_indent: str | None):
        """Handle deprecated pretty print/indent behaviour."""
        if pretty_print:
            self.__setattr__("pretty_print", pretty_print)
        if pretty_print_indent:
            self.__setattr__("pretty_print_indent", pretty_print_indent)

    def __setattr__(self, key: str, value: Any):
        """Handle deprecated pretty print/indent behaviour."""
        if key == "pretty_print":
            warnings.warn(
                "Setting `pretty_print` is deprecated, use `indent` instead",
                DeprecationWarning,
            )
            self.indent = "  "
        elif key == "pretty_print_indent":
            warnings.warn(
                "Setting `pretty_print_indent` is deprecated, use `indent` instead",
                DeprecationWarning,
            )
            self.indent = value
        else:
            super().__setattr__(key, value)
