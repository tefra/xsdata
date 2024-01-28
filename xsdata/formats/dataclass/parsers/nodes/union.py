import copy
import warnings
from typing import Any, Dict, List, Optional, Tuple, Type

from xsdata.exceptions import ConverterWarning, ParserError
from xsdata.formats.bindings import T
from xsdata.formats.dataclass.context import XmlContext
from xsdata.formats.dataclass.models.elements import XmlVar
from xsdata.formats.dataclass.parsers.bases import NodeParser
from xsdata.formats.dataclass.parsers.config import ParserConfig
from xsdata.formats.dataclass.parsers.mixins import EventsHandler, XmlNode
from xsdata.formats.dataclass.parsers.utils import ParserUtils
from xsdata.utils.namespaces import target_uri


class UnionNode(XmlNode):
    """XmlNode for union fields with at least one data class.

    The node will record all child events and in the end will replay
    them and try to build all possible objects and sort them by score
    before deciding the winner.

    Args:
        var: The xml var instance
        attrs: The element attributes
        ns_map: The element namespace prefix-URI map
        position: The current objects length, everything after
            this position are considered children of this node.
        config: The parser config instance
        context: The xml context instance
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
        """Record the event for the child element.

        This entry point records all events, as it's not possible
        to detect the target parsed object type just yet. When
        this node ends, it will replay all events and attempt
        to find the best matching type for the parsed object.

        Args:
            qname: The element qualified name
            attrs: The element attributes
            ns_map: The element namespace prefix-URI map
            position: The current length of the intermediate objects
        """
        self.level += 1
        self.events.append(("start", qname, copy.deepcopy(attrs), ns_map))
        return self

    def bind(
        self,
        qname: str,
        text: Optional[str],
        tail: Optional[str],
        objects: List,
    ) -> bool:
        """Bind the parsed data into an object for the ending element.

        This entry point is called when a xml element ends and is
        responsible to replay all xml events and parse/bind all
        the children objects.

        Args:
            qname: The element qualified name
            text: The element text content
            tail: The element tail content
            objects: The list of intermediate parsed objects

        Returns:
            Always returns true, if the binding process fails
            it raises an exception.

        Raises:
            ParserError: If none of the candidate types matched
                the replayed events.
        """
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
        """Replay the recorded events and attempt to build the target class.

        Args:
            clazz: The target class

        Returns:
             The target class instance or None if the recorded
             xml events didn't fit the class.
        """
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
        """Parse simple values.

        Args:
            value: The xml value
            types: The list of the candidate simple types

        Returns:
            The parsed value or None if value didn't match
            with any of the given types.
        """
        try:
            with warnings.catch_warnings():
                warnings.filterwarnings("error", category=ConverterWarning)
                return ParserUtils.parse_value(
                    value=value, types=types, ns_map=self.ns_map
                )
        except Exception:
            return None
