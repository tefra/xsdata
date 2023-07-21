from dataclasses import dataclass
from typing import Any
from typing import List
from typing import Optional

from xsdata.codegen.parsers.schema import SchemaParser
from xsdata.formats.bindings import T
from xsdata.formats.dataclass.parsers.bases import Parsed
from xsdata.formats.dataclass.parsers.mixins import XmlNode
from xsdata.models import wsdl


@dataclass
class DefinitionsParser(SchemaParser):
    """A simple parser to convert a wsdl to an easy to handle data structure
    based on dataclasses."""

    def end(
        self,
        queue: List[XmlNode],
        objects: List[Parsed],
        qname: str,
        text: Optional[str],
        tail: Optional[str],
    ) -> Any:
        """Override parent method to set element location."""
        obj = super().end(queue, objects, qname, text, tail)
        if isinstance(obj, wsdl.WsdlElement):
            obj.location = self.location

        return obj

    def end_import(self, obj: T):
        if isinstance(obj, wsdl.Import) and self.location:
            obj.location = self.resolve_path(obj.location)
