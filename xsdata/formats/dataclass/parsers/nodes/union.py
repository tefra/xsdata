import copy
import functools
from contextlib import suppress
from dataclasses import replace
from typing import Any, Optional

from xsdata.exceptions import ParserError
from xsdata.formats.dataclass.context import XmlContext
from xsdata.formats.dataclass.models.elements import XmlMeta, XmlVar
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
        "attrs",
        "candidates",
        "config",
        "context",
        "events",
        "level",
        "meta",
        "ns_map",
        "position",
        "var",
    )

    def __init__(
        self,
        meta: XmlMeta,
        var: XmlVar,
        attrs: dict,
        ns_map: dict,
        position: int,
        config: ParserConfig,
        context: XmlContext,
    ):
        """Initialize the xml node."""
        self.meta = meta
        self.var = var
        self.attrs = attrs
        self.ns_map = ns_map
        self.position = position
        self.config = config
        self.context = context
        self.level = 0
        self.candidates = self.filter_candidates()
        self.events: list[tuple[str, str, Any, Any]] = []

    def filter_candidates(self) -> list[type]:
        """Filter union candidates by fixed attributes."""
        candidates = list(self.var.types)
        fixed_attribute = functools.partial(
            self.filter_fixed_attrs, parent_ns=target_uri(self.var.qname)
        )

        return list(filter(fixed_attribute, candidates))

    def filter_fixed_attrs(self, candidate: type, parent_ns: str | None) -> bool:
        """Return whether the node attrs are incompatible with fixed attrs.

        Args:
            candidate: The candidate type
            parent_ns: The parent namespace
        """
        if not self.context.class_type.is_model(candidate):
            return not self.attrs

        meta = self.context.build(candidate, parent_ns=parent_ns)
        for qname, value in self.attrs.items():
            var = meta.find_attribute(qname)
            if not var or var.init:
                continue

            try:
                ParserUtils.validate_fixed_value(meta, var, value)
            except ParserError:
                return False

        return True

    def child(self, qname: str, attrs: dict, ns_map: dict, position: int) -> XmlNode:
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
        text: str | None,
        tail: str | None,
        objects: list,
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
        config = replace(self.config, fail_on_converter_warnings=True)

        for candidate in self.candidates:
            result: Any = None
            with suppress(Exception):
                if self.context.class_type.is_model(candidate):
                    self.context.build(candidate, parent_ns=parent_namespace)
                    parser = NodeParser(
                        config=config,
                        context=self.context,
                        handler=EventsHandler,
                    )
                    result = parser.parse(self.events, candidate)
                else:
                    result = ParserUtils.parse_var(
                        meta=self.meta,
                        var=self.var,
                        config=config,
                        value=text,
                        types=[candidate],
                        ns_map=self.ns_map,
                    )

            score = self.context.class_type.score_object(result)
            if score > max_score:
                max_score = score
                obj = result

        if obj:
            objects.append((self.var.qname, obj))

            return True

        raise ParserError(f"Failed to parse union node: {self.var.qname}")
