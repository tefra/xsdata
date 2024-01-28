from dataclasses import dataclass
from typing import Callable, Dict, Optional


@dataclass
class SerializerConfig:
    """Serializer configuration options.

    Not all options are applicable for both xml and json documents.

    Args:
        encoding: Text encoding
        xml_version: XML Version number (1.0|1.1)
        xml_declaration: Generate XML declaration
        pretty_print: Enable pretty output
        pretty_print_indent: Indentation string for each indent level
        ignore_default_attributes: Ignore optional attributes with default values
        schema_location: xsi:schemaLocation attribute value
        no_namespace_schema_location: xsi:noNamespaceSchemaLocation attribute value
        globalns: Dictionary containing global variables to extend or
            overwrite for typing
    """

    encoding: str = "UTF-8"
    xml_version: str = "1.0"
    xml_declaration: bool = True
    pretty_print: bool = False
    pretty_print_indent: Optional[str] = None
    ignore_default_attributes: bool = False
    schema_location: Optional[str] = None
    no_namespace_schema_location: Optional[str] = None
    globalns: Optional[Dict[str, Callable]] = None
