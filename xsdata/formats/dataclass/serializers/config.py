from typing import Callable
from typing import Dict
from typing import Optional


class SerializerConfig:
    """
    Serializer configuration options.

    Some options are not applicable for both xml or json documents.

    :param encoding: Text encoding
    :param xml_version: XML Version number (1.0|1.1)
    :param xml_declaration: Generate XML declaration
    :param pretty_print: Enable pretty output
    :param pretty_print_indent: Indentation string for each indent level
    :param ignore_default_attributes: Ignore optional attributes with
        default values
    :param schema_location: xsi:schemaLocation attribute value
    :param no_namespace_schema_location: xsi:noNamespaceSchemaLocation
        attribute value
    :param globalns: Dictionary containing global variables to extend or
        overwrite for typing
    """

    __slots__ = (
        "encoding",
        "xml_version",
        "xml_declaration",
        "pretty_print",
        "pretty_print_indent",
        "ignore_default_attributes",
        "schema_location",
        "no_namespace_schema_location",
        "globalns",
    )

    def __init__(
        self,
        encoding: str = "UTF-8",
        xml_version: str = "1.0",
        xml_declaration: bool = True,
        pretty_print: bool = False,
        pretty_print_indent: Optional[str] = None,
        ignore_default_attributes: bool = False,
        schema_location: Optional[str] = None,
        no_namespace_schema_location: Optional[str] = None,
        globalns: Optional[Dict[str, Callable]] = None,
    ):
        self.encoding = encoding
        self.xml_version = xml_version
        self.xml_declaration = xml_declaration
        self.pretty_print = pretty_print
        self.pretty_print_indent = pretty_print_indent
        self.ignore_default_attributes = ignore_default_attributes
        self.schema_location = schema_location
        self.no_namespace_schema_location = no_namespace_schema_location
        self.globalns = globalns
