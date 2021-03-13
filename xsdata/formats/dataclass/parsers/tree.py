from dataclasses import dataclass
from dataclasses import field
from typing import Dict
from typing import List
from typing import Optional
from typing import Type

from xsdata.formats.dataclass.models.elements import XmlVar
from xsdata.formats.dataclass.parsers.handlers import default_handler
from xsdata.formats.dataclass.parsers.mixins import XmlHandler
from xsdata.formats.dataclass.parsers.mixins import XmlNode
from xsdata.formats.dataclass.parsers.nodes import NodeParser
from xsdata.formats.dataclass.parsers.nodes import Parsed
from xsdata.formats.dataclass.parsers.nodes import WildcardNode


@dataclass
class TreeParser(NodeParser):
    """
    Bind xml nodes to a tree of AnyElement objects.

    :param handler: Override default XmlHandler
    """

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
        try:
            item = queue[-1]
            child = item.child(qname, attrs, ns_map, len(objects))
        except IndexError:
            child = WildcardNode(
                var=XmlVar(name=qname, qname=qname, wildcard=True),
                attrs=attrs,
                ns_map=ns_map,
                position=0,
            )
        queue.append(child)
