from dataclasses import dataclass
from typing import Any, List, Optional

from xsdata.codegen.parsers.schema import SchemaParser
from xsdata.formats.bindings import T
from xsdata.formats.dataclass.parsers.bases import Parsed
from xsdata.formats.dataclass.parsers.mixins import XmlNode
from xsdata.models import wsdl


@dataclass
class DefinitionsParser(SchemaParser):
    """Parse a wsdl document into data models."""

    def end(
        self,
        queue: List[XmlNode],
        objects: List[Parsed],
        qname: str,
        text: Optional[str],
        tail: Optional[str],
    ) -> Any:
        """Parse the last xml node and bind any intermediate objects.

        Override parent method to set source location in every
        wsdl element.

        Args:
            queue: The XmlNode queue list
            objects: The list of all intermediate parsed objects
            qname: The element qualified name
            text: The element text content
            tail: The element tail content

        Returns:
            Whether the binding process was successful.
        """
        obj = super().end(queue, objects, qname, text, tail)
        if isinstance(obj, wsdl.WsdlElement):
            obj.location = self.location

        return obj

    def end_import(self, obj: T):
        """End import element entrypoint.

        Resolve the location path of import elements.

        Args:
            obj: The wsdl import element.
        """
        if isinstance(obj, wsdl.Import) and self.location:
            obj.location = self.resolve_path(obj.location)
