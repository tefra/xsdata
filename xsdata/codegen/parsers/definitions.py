from dataclasses import dataclass
from typing import Any
from typing import List
from typing import Tuple
from typing import TypeVar

from lxml.etree import Element
from lxml.etree import QName

from xsdata.codegen.parsers.schema import SchemaParser
from xsdata.formats.dataclass.parsers.nodes import XmlNode
from xsdata.models import wsdl

T = TypeVar("T")
ParsedObjects = List[Tuple[QName, Any]]
XmlNodes = List[XmlNode]


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
