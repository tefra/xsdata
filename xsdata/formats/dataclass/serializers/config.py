from dataclasses import dataclass
from dataclasses import field
from typing import Optional


@dataclass
class SerializerConfig:
    """
    Serializing configuration options.

    :param encoding: Text encoding
    :param xml_version: XML Version number (1.0|1.1)
    :param xml_declaration: Generate XML declaration
    :param pretty_print: Enable pretty output
    :param schema_location: Specify the xsi:schemaLocation attribute value
    :param no_namespace_schema_location: Specify the xsi:noNamespaceSchemaLocation
        attribute value
    """

    encoding: str = field(default="UTF-8")
    xml_version: str = field(default="1.0")
    xml_declaration: bool = field(default=True)
    pretty_print: bool = field(default=False)
    schema_location: Optional[str] = field(default=None)
    no_namespace_schema_location: Optional[str] = field(default=None)
