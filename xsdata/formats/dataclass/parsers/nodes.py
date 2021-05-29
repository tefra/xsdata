import copy
import warnings
from dataclasses import dataclass
from dataclasses import field
from dataclasses import is_dataclass
from typing import Any
from typing import Dict
from typing import List
from typing import Optional
from typing import Set
from typing import Tuple
from typing import Type

from xsdata.exceptions import ConverterWarning
from xsdata.exceptions import ParserError
from xsdata.exceptions import XmlContextError
from xsdata.formats.bindings import T
from xsdata.formats.dataclass.context import XmlContext
from xsdata.formats.dataclass.models.elements import XmlMeta
from xsdata.formats.dataclass.models.elements import XmlVar
from xsdata.formats.dataclass.models.generics import AnyElement
from xsdata.formats.dataclass.models.generics import DerivedElement
from xsdata.formats.dataclass.parsers.config import ParserConfig
from xsdata.formats.dataclass.parsers.mixins import EventsHandler
from xsdata.formats.dataclass.parsers.mixins import PushParser
from xsdata.formats.dataclass.parsers.mixins import XmlHandler
from xsdata.formats.dataclass.parsers.mixins import XmlNode
from xsdata.formats.dataclass.parsers.utils import ParserUtils
from xsdata.models.enums import DataType
from xsdata.models.enums import EventType
from xsdata.utils.namespaces import target_uri

Parsed = Tuple[Optional[str], Any]
NoneStr = Optional[str]


class ElementNode(XmlNode):
    """XmlNode for complex elements and dataclasses."""

    __slots__ = (
        "meta",
        "attrs",
        "ns_map",
        "config",
        "context",
        "position",
        "mixed",
        "derived",
        "xsi_type",
        "assigned",
    )

    def __init__(
        self,
        meta: XmlMeta,
        attrs: Dict,
        ns_map: Dict,
        config: ParserConfig,
        context: XmlContext,
        position: int,
        mixed: bool = False,
        derived: bool = False,
        xsi_type: Optional[str] = None,
    ):
        """
        :param meta: Model xml metadata
        :param attrs: Key-value attribute mapping
        :param ns_map: Namespace prefix-URI map
        :param config: Parser configuration
        :param context: Model context provider
        :param position: The node position of objects cache
        :param mixed: The node supports mixed content
        :param derived: The xml element is derived from a base type
        :param xsi_type: The xml type substitution
        """

        self.meta = meta
        self.attrs = attrs
        self.ns_map = ns_map
        self.config = config
        self.context = context
        self.position = position
        self.mixed = mixed
        self.derived = derived
        self.xsi_type = xsi_type
        self.assigned: Set[int] = set()

    def bind(self, qname: str, text: NoneStr, tail: NoneStr, objects: List) -> bool:
        params: Dict = {}
        ParserUtils.bind_attrs(params, self.meta, self.attrs, self.ns_map)

        wild_var = self.meta.find_any_wildcard()
        if wild_var and wild_var.mixed:
            ParserUtils.bind_mixed_objects(params, wild_var, self.position, objects)
            bind_text = False
        else:
            ParserUtils.bind_objects(params, self.meta, self.position, objects)
            bind_text = ParserUtils.bind_content(params, self.meta, text, self.ns_map)

        if not bind_text and wild_var:
            ParserUtils.bind_wild_content(
                params, wild_var, text, tail, self.attrs, self.ns_map
            )

        obj = self.meta.clazz(**params)
        if self.derived:
            obj = DerivedElement(qname=qname, value=obj, type=self.xsi_type)

        objects.append((qname, obj))

        if self.mixed and not wild_var:
            tail = ParserUtils.normalize_content(tail)
            if tail:
                objects.append((None, tail))

        return True

    def child(self, qname: str, attrs: Dict, ns_map: Dict, position: int) -> XmlNode:
        for var in self.meta.find_children(qname):
            unique = 0 if not var.is_element or var.list_element else var.index
            if not unique or unique not in self.assigned:
                node = self.build_node(var, attrs, ns_map, position)

                if node:
                    if unique:
                        self.assigned.add(unique)

                    return node

        if self.config.fail_on_unknown_properties:
            raise ParserError(f"Unknown property {self.meta.qname}:{qname}")

        return SkipNode()

    def build_node(
        self, var: XmlVar, attrs: Dict, ns_map: Dict, position: int
    ) -> Optional[XmlNode]:
        if var.is_clazz_union:
            return UnionNode(
                var=var,
                attrs=attrs,
                ns_map=ns_map,
                context=self.context,
                position=position,
            )

        xsi_type = ParserUtils.xsi_type(attrs, ns_map)

        if var.clazz:
            return self.build_element_node(
                var.clazz,
                attrs,
                ns_map,
                position,
                var.derived,
                xsi_type,
            )

        if not var.any_type and not var.is_wildcard:
            return PrimitiveNode(var, ns_map)

        datatype = DataType.from_qname(xsi_type) if xsi_type else None
        derived = var.derived or var.is_wildcard
        if datatype:
            return StandardNode(datatype, ns_map, derived, var.nillable)

        node = None
        clazz = None
        if xsi_type:
            clazz = self.context.find_type(xsi_type)

        if clazz:
            node = self.build_element_node(
                clazz, attrs, ns_map, position, derived, xsi_type
            )

        if node:
            return node

        return WildcardNode(var=var, attrs=attrs, ns_map=ns_map, position=position)

    def build_element_node(
        self,
        clazz: Type,
        attrs: Dict,
        ns_map: Dict,
        position: int,
        derived: bool,
        xsi_type: Optional[str] = None,
    ) -> Optional[XmlNode]:

        meta = self.context.fetch(clazz, self.meta.namespace, xsi_type)

        if not meta or (meta.nillable and not ParserUtils.is_nillable(attrs)):
            return None

        return ElementNode(
            meta=meta,
            config=self.config,
            attrs=attrs,
            ns_map=ns_map,
            context=self.context,
            position=position,
            derived=derived,
            xsi_type=xsi_type,
            mixed=self.meta.mixed_content,
        )


class WildcardNode(XmlNode):
    """
    XmlNode for extensible elements that can hold any attribute and content.

    The resulting object tree will be a
    :class:`~xsdata.formats.dataclass.models.generics.AnyElement`
    instance.
    """

    __slots__ = "var", "attrs", "ns_map", "position"

    def __init__(self, var: XmlVar, attrs: Dict, ns_map: Dict, position: int):
        """

        :param var: Class field xml var instance
        :param attrs: Key-value attribute mapping
        :param ns_map: Namespace prefix-URI map
        :param position: The node position of objects cache
        """

        self.var = var
        self.attrs = attrs
        self.ns_map = ns_map
        self.position = position

    def bind(self, qname: str, text: NoneStr, tail: NoneStr, objects: List) -> bool:
        children = ParserUtils.fetch_any_children(self.position, objects)
        attributes = ParserUtils.parse_any_attributes(self.attrs, self.ns_map)
        derived = self.var.derived or qname != self.var.qname
        text = ParserUtils.normalize_content(text) if children else text
        text = "" if text is None and not self.var.nillable else text
        tail = ParserUtils.normalize_content(tail)

        if tail or attributes or children or self.var.is_wildcard or derived:
            obj = AnyElement(
                qname=qname,
                text=text,
                tail=tail,
                attributes=attributes,
                children=children,
            )
            objects.append((self.var.qname, obj))
        else:
            objects.append((self.var.qname, text))

        return True

    def child(self, qname: str, attrs: Dict, ns_map: Dict, position: int) -> XmlNode:
        return WildcardNode(position=position, var=self.var, attrs=attrs, ns_map=ns_map)


class UnionNode(XmlNode):
    """
    XmlNode for fields with multiple possible types where at least one of them
    is a dataclass.

    The node will record all child events and in the end will replay
    them and try to build all possible objects and sort them by score
    before deciding the winner.
    """

    __slots__ = "var", "attrs", "ns_map", "position", "context", "level", "events"

    def __init__(
        self, var: XmlVar, attrs: Dict, ns_map: Dict, position: int, context: XmlContext
    ):
        """
        :param var: Class field xml var instance
        :param attrs: Key-value attribute mapping
        :param ns_map: Namespace prefix-URI map
        :param position: The node position of objects cache
        :param context: Model context provider
        """

        self.var = var
        self.attrs = attrs
        self.ns_map = ns_map
        self.position = position
        self.context = context
        self.level = 0
        self.events: List[Tuple[str, str, Any, Any]] = []

    def child(self, qname: str, attrs: Dict, ns_map: Dict, position: int) -> XmlNode:
        self.level += 1
        self.events.append(("start", qname, copy.deepcopy(attrs), ns_map))
        return self

    def bind(self, qname: str, text: NoneStr, tail: NoneStr, objects: List) -> bool:
        self.events.append(("end", qname, text, tail))

        if self.level > 0:
            self.level -= 1
            return False

        self.events.insert(0, ("start", qname, copy.deepcopy(self.attrs), self.ns_map))

        obj = None
        max_score = -1.0
        parent_namespace = target_uri(qname)
        for clazz in self.var.types:

            if is_dataclass(clazz):
                self.context.build(clazz, parent_ns=parent_namespace)
                candidate = self.parse_class(clazz)
            else:
                candidate = self.parse_value(text, [clazz])

            score = ParserUtils.score_object(candidate)
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
                parser = NodeParser(context=self.context, handler=EventsHandler)
                return parser.parse(self.events, clazz)
        except Exception:
            return None

    def parse_value(self, value: Any, types: List[Type]) -> Any:
        """Parse simple values, treat warnings as errors and return None."""
        try:
            with warnings.catch_warnings():
                warnings.filterwarnings("error", category=ConverterWarning)
                return ParserUtils.parse_value(value, types, ns_map=self.ns_map)
        except Exception:
            return None


class PrimitiveNode(XmlNode):
    """XmlNode for text elements with primitive values like str, int, float."""

    __slots__ = ("var", "ns_map")

    def __init__(self, var: XmlVar, ns_map: Dict):
        """
        :param var: Class field xml var instance
        :param ns_map: Namespace prefix-URI map
        """
        self.var = var
        self.ns_map = ns_map

    def bind(self, qname: str, text: NoneStr, tail: NoneStr, objects: List) -> bool:
        obj = ParserUtils.parse_value(
            text,
            self.var.types,
            self.var.default,
            self.ns_map,
            self.var.tokens,
            self.var.format,
        )

        if obj is None and not self.var.nillable:
            obj = ""

        if self.var.derived:
            obj = DerivedElement(qname=qname, value=obj)

        objects.append((qname, obj))
        return True

    def child(self, qname: str, attrs: Dict, ns_map: Dict, position: int) -> XmlNode:
        raise XmlContextError("Primitive node doesn't support child nodes!")


class StandardNode(XmlNode):
    """XmlNode for any type elements with a standard xsi:type."""

    __slots__ = ("datatype", "ns_map", "derived", "nillable")

    def __init__(self, datatype: DataType, ns_map: Dict, derived: bool, nillable: bool):
        """

        :param datatype: Standard xsi data type
        :param ns_map: Namespace prefix-URI map
        :param derived: Specify whether the value needs to be wrapped with
            :class:`~xsdata.formats.dataclass.models.generics.DerivedElement`
        :param nillable: Specify whether the node supports nillable content
        """
        self.datatype = datatype
        self.ns_map = ns_map
        self.derived = derived
        self.nillable = nillable

    def bind(self, qname: str, text: NoneStr, tail: NoneStr, objects: List) -> bool:
        obj = ParserUtils.parse_value(
            text,
            [self.datatype.type],
            None,
            self.ns_map,
            False,
            self.datatype.format,
        )

        if obj is None and not self.nillable:
            obj = ""

        if self.datatype.wrapper:
            obj = self.datatype.wrapper(obj)

        if self.derived:
            obj = DerivedElement(qname=qname, value=obj)

        objects.append((qname, obj))
        return True

    def child(self, qname: str, attrs: Dict, ns_map: Dict, position: int) -> XmlNode:
        raise XmlContextError("Primitive node doesn't support child nodes!")


class SkipNode(XmlNode):
    """Utility node to skip parsing unknown properties."""

    __slots__ = ("ns_map",)

    def __init__(self):
        self.ns_map = {}

    def child(self, qname: str, attrs: Dict, ns_map: Dict, position: int) -> XmlNode:
        """Skip nodes children are skipped as well."""
        return self

    def bind(self, qname: str, text: NoneStr, tail: NoneStr, objects: List) -> bool:
        """Skip nodes are not building any objects."""
        return False


@dataclass
class NodeParser(PushParser):
    """
    Bind xml nodes to dataclasses.

    :param config: Parser configuration
    :param context: Model context provider
    :param handler: Override default XmlHandler
    :ivar ms_map: Namespace registry of parsed prefix-URI mappings
    """

    config: ParserConfig = field(default_factory=ParserConfig)
    context: XmlContext = field(default_factory=XmlContext)
    handler: Type[XmlHandler] = field(default=EventsHandler)
    ns_map: Dict = field(init=False, default_factory=dict)

    def parse(self, source: Any, clazz: Optional[Type[T]] = None) -> T:
        """Parse the input stream or filename and return the resulting object
        tree."""
        handler = self.handler(clazz=clazz, parser=self)
        result = handler.parse(source)

        if result is not None:
            return result

        target_class = clazz.__name__ if clazz else ""
        raise ParserError(f"Failed to create target class `{target_class}`")

    def start(
        self,
        clazz: Optional[Type],
        queue: List[XmlNode],
        objects: List[Parsed],
        qname: str,
        attrs: Dict,
        ns_map: Dict,
    ):
        """
        Start element notification receiver.

        Build and queue the XmlNode for the starting element.

        :param clazz: Root class type, if it's missing look for any
            suitable models from the current context.
        :param queue: The active XmlNode queue
        :param objects: The list of all intermediate parsed objects
        :param qname: Qualified name
        :param attrs: Attribute key-value map
        :param ns_map: Namespace prefix-URI map
        """
        try:
            item = queue[-1]
            child = item.child(qname, attrs, ns_map, len(objects))
        except IndexError:
            xsi_type = ParserUtils.xsi_type(attrs, ns_map)

            # Match element qname directly
            if clazz is None:
                clazz = self.context.find_type(qname)

            # Root is xs:anyType try xsi:type
            if clazz is None and xsi_type:
                clazz = self.context.find_type(xsi_type)

            # Exit if we still have no binding model
            if clazz is None:
                raise ParserError(f"No class found matching root: {qname}")

            meta = self.context.fetch(clazz, xsi_type=xsi_type)
            derived = xsi_type is not None and meta.qname != qname

            child = ElementNode(
                position=0,
                meta=meta,
                config=self.config,
                attrs=attrs,
                ns_map=ns_map,
                context=self.context,
                derived=derived,
                xsi_type=xsi_type if derived else None,
            )

        queue.append(child)

    def end(
        self,
        queue: List[XmlNode],
        objects: List[Parsed],
        qname: str,
        text: NoneStr,
        tail: NoneStr,
    ) -> Any:
        """
        End element notification receiver.

        Pop the last XmlNode from the queue and use it to build and
        return the resulting object tree with its text and tail
        content.

        :param queue: Xml nodes queue
        :param objects: List of parsed objects
        :param qname: Qualified name
        :param text: Text content
        :param tail: Tail content
        """
        obj = None
        item = queue.pop()
        if item.bind(qname, text, tail, objects):
            obj = objects[-1][1]

        return obj


@dataclass
class RecordParser(NodeParser):
    """
    Bind xml nodes to dataclasses and store the intermediate events.

    :ivar events: List of pushed events
    """

    events: List = field(init=False, default_factory=list)

    def start(
        self,
        clazz: Optional[Type],
        queue: List[XmlNode],
        objects: List[Parsed],
        qname: str,
        attrs: Dict,
        ns_map: Dict,
    ):
        """
        Start element notification receiver.

        Build and queue the XmlNode for the starting element, append
        the event with the attributes and ns map to the events list.

        :param clazz: Root class type, if it's missing look for any
            suitable models from the current context.
        :param queue: The active XmlNode queue
        :param objects: The list of all intermediate parsed objects
        :param qname: Qualified name
        :param attrs: Attributes key-value map
        :param ns_map: Namespace prefix-URI map
        """
        self.events.append((EventType.START, qname, copy.deepcopy(attrs), ns_map))
        super().start(clazz, queue, objects, qname, attrs, ns_map)

    def end(
        self,
        queue: List[XmlNode],
        objects: List[Parsed],
        qname: str,
        text: NoneStr,
        tail: NoneStr,
    ) -> Any:
        """
        End element notification receiver.

        Pop the last XmlNode from the queue and use it to build and
        return the resulting object tree with its text and tail
        content. Append the end event with the text,tail content to
        the events list.

        :param queue: Xml nodes queue
        :param objects: List of parsed objects
        :param qname: Qualified name
        :param text: Text content
        :param tail: Tail content
        """
        self.events.append((EventType.END, qname, text, tail))
        return super().end(queue, objects, qname, text, tail)

    def register_namespace(self, prefix: NoneStr, uri: str):
        self.events.append((EventType.START_NS, prefix, uri))
        super().register_namespace(prefix, uri)
