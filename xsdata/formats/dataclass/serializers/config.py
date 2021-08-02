from typing import Optional


class SerializerConfig:
    """
    Serializer configuration options.

    Some options are not applicable for both xml or json documents.

    :param encoding: Text encoding
    :param xml_version: XML Version number (1.0|1.1)
    :param xml_declaration: Generate XML declaration
    :param pretty_print: Enable pretty output
    :param ignore_default_attributes: Ignore optional attributes with
        default values
    :param schema_location: xsi:schemaLocation attribute value
    :param no_namespace_schema_location: xsi:noNamespaceSchemaLocation
        attribute value
    """

    __slots__ = (
        "encoding",
        "xml_version",
        "xml_declaration",
        "pretty_print",
        "ignore_default_attributes",
        "schema_location",
        "no_namespace_schema_location",
    )

    def __init__(
        self,
        encoding: str = "UTF-8",
        xml_version: str = "1.0",
        xml_declaration: bool = True,
        pretty_print: bool = False,
        ignore_default_attributes: bool = False,
        schema_location: Optional[str] = None,
        no_namespace_schema_location: Optional[str] = None,
    ):
        self.encoding = encoding
        self.xml_version = xml_version
        self.xml_declaration = xml_declaration
        self.pretty_print = pretty_print
        self.ignore_default_attributes = ignore_default_attributes
        self.schema_location = schema_location
        self.no_namespace_schema_location = no_namespace_schema_location
