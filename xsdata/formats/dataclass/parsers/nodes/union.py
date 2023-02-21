import copy
import warnings
from typing import Any
from typing import Dict
from typing import List
from typing import Optional
from typing import Tuple
from typing import Type

from xsdata.exceptions import ConverterWarning
from xsdata.exceptions import ParserError
from xsdata.formats.bindings import T
from xsdata.formats.dataclass.context import XmlContext
from xsdata.formats.dataclass.models.elements import XmlVar
from xsdata.formats.dataclass.parsers.bases import NodeParser
from xsdata.formats.dataclass.parsers.config import ParserConfig
from xsdata.formats.dataclass.parsers.mixins import EventsHandler
from xsdata.formats.dataclass.parsers.mixins import XmlNode
from xsdata.formats.dataclass.parsers.utils import ParserUtils
from xsdata.utils.namespaces import target_uri


class UnionNode(XmlNode):
    """
    XmlNode for fields with multiple possible types where at least one of them
    is a dataclass.

    The node will record all child events and in the end will replay
    them and try to build all possible objects and sort them by score
    before deciding the winner.

    :param var: Class field xml var instance
    :param attrs: Key-value attribute mapping
    :param ns_map: Namespace prefix-URI map
    :param position: The node position of objects cache
    :param config: Parser configuration
    :param context: Model context provider
    """

    __slots__ = (
        "var",
        "attrs",
        "ns_map",
        "position",
        "config",
        "context",
        "level",
        "events",
    )

    def __init__(
        self,
        var: XmlVar,
        attrs: Dict,
        ns_map: Dict,
        position: int,
        config: ParserConfig,
        context: XmlContext,
    ):
        self.var = var
        self.attrs = attrs
        self.ns_map = ns_map
        self.position = position
        self.config = config
        self.context = context
        self.level = 0
        self.events: List[Tuple[str, str, Any, Any]] = []

    def child(self, qname: str, attrs: Dict, ns_map: Dict, position: int) -> XmlNode:
        self.level += 1
        self.events.append(("start", qname, copy.deepcopy(attrs), ns_map))
        return self

    def bind(
        self, qname: str, text: Optional[str], tail: Optional[str], objects: List
    ) -> bool:
        self.events.append(("end", qname, text, tail))

        if self.level > 0:
            self.level -= 1
            return False

        self.events.insert(0, ("start", qname, copy.deepcopy(self.attrs), self.ns_map))

        obj = None
        max_score = -1.0
        parent_namespace = target_uri(qname)
        for clazz in self.var.types:
            if self.context.class_type.is_model(clazz):
                self.context.build(clazz, parent_ns=parent_namespace)
                candidate = self.parse_class(clazz)
            else:
                candidate = self.parse_value(text, [clazz])

            score = self.context.class_type.score_object(candidate)
            if score > max_score:
                max_score = score
                obj = candidate

        if obj:
            objects.append((self.var.qname, obj))

            return True

        raise ParserError(f"Failed to parse union node: {self.var.qname}")

    def parse_class(self, clazz: Type[T]) -> Optional[T]:
        """Initialize a new XmlParser and try to parse the given element, treat
        converter warnings as errors and return None."""
        try:
            with warnings.catch_warnings():
                warnings.filterwarnings("error", category=ConverterWarning)

                parser = NodeParser(
                    config=self.config, context=self.context, handler=EventsHandler
                )
                return parser.parse(self.events, clazz)
        except Exception:
            return None

    def parse_value(self, value: Any, types: List[Type]) -> Any:
        """Parse simple values, treat warnings as errors and return None."""
        try:
            with warnings.catch_warnings():
                warnings.filterwarnings("error", category=ConverterWarning)
                return ParserUtils.parse_value(
                    value=value, types=types, ns_map=self.ns_map
                )
        except Exception:
            return None
