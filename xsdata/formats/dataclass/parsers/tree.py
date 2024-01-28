from dataclasses import dataclass, field
from typing import Dict, List, Optional, Type

from xsdata.formats.dataclass.models.elements import XmlType, XmlVar
from xsdata.formats.dataclass.parsers.bases import NodeParser, Parsed
from xsdata.formats.dataclass.parsers.handlers import default_handler
from xsdata.formats.dataclass.parsers.mixins import XmlHandler, XmlNode
from xsdata.formats.dataclass.parsers.nodes.wildcard import WildcardNode


@dataclass
class TreeParser(NodeParser):
    """Bind xml nodes to a tree of AnyElement objects."""

    handler: Type[XmlHandler] = field(default=default_handler())

    def start(
        self,
        clazz: Optional[Type],
        queue: List[XmlNode],
        objects: List[Parsed],
        qname: str,
        attrs: Dict,
        ns_map: Dict,
    ):
        """Build and queue the XmlNode for the starting element.

        Args:
            clazz: The target class type, auto locate if omitted
            queue: The XmlNode queue list
            objects: The list of all intermediate parsed objects
            qname: The element qualified name
            attrs: The element attributes
            ns_map: The element namespace prefix-URI map
        """
        try:
            item = queue[-1]
            child = item.child(qname, attrs, ns_map, len(objects))
        except IndexError:
            var = XmlVar(
                name=qname,
                qname=qname,
                xml_type=XmlType.WILDCARD,
                index=0,
                types=(object,),
                clazz=None,
                init=True,
                mixed=False,
                factory=None,
                tokens_factory=None,
                format=None,
                derived=False,
                any_type=False,
                process_contents="strict",
                required=False,
                nillable=False,
                sequence=None,
                default=None,
                namespaces=(),
                elements={},
                wildcards=(),
            )

            child = WildcardNode(
                var=var,
                attrs=attrs,
                ns_map=ns_map,
                position=0,
                factory=self.context.class_type.any_element,
            )
        queue.append(child)
