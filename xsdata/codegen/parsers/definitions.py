from dataclasses import dataclass

from lxml.etree import Element

from xsdata.codegen.parsers.schema import SchemaParser
from xsdata.formats.bindings import T
from xsdata.models import wsdl


@dataclass
class DefinitionsParser(SchemaParser):
    """A simple parser to convert a wsdl to an easy to handle data structure
    based on dataclasses."""

    def end_definitions(self, obj: T, element: Element):
        """Normalize various properties for the schema and it's children."""
        if isinstance(obj, wsdl.Definitions) and self.location:
            obj.location = self.location
            for imp in obj.imports:
                imp.location = self.resolve_path(imp.location)
