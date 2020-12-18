import copy
from dataclasses import dataclass
from dataclasses import field
from typing import Any
from typing import ClassVar
from typing import Dict
from typing import Iterable
from typing import Iterator
from typing import List
from typing import Optional
from typing import Tuple
from typing import Type

from xsdata.exceptions import ParserError
from xsdata.exceptions import XmlContextError
from xsdata.formats.bindings import T
from xsdata.formats.dataclass.context import XmlContext
from xsdata.formats.dataclass.models.elements import FindMode
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
from xsdata.models.enums import EventType

Parsed = Tuple[Optional[str], Any]
NoneStr = Optional[str]


@dataclass
class ElementNode(XmlNode):
    """
    XmlNode for complex elements and dataclasses.

    :param meta: Model xml metadata
    :param attrs: Key-value attribute mapping
    :param ns_map: Namespace prefix-URI map
    :param config: Parser configuration
    :param context: Model context provider
    :param position: The node position of objects cache
    :param derived: The xml element is derived from a base type
    """

    meta: XmlMeta
    attrs: Dict
    ns_map: Dict
    config: ParserConfig
    context: XmlContext
    position: int
    mixed: bool = False
    derived: bool = False

    FIND_MODES_ORDERED: ClassVar[Iterable[FindMode]] = (
        FindMode.NOT_WILDCARD,
        FindMode.WILDCARD,
    )

    def bind(self, qname: str, text: NoneStr, tail: NoneStr, objects: List) -> bool:
        params: Dict = {}
        wild_node = False
        text_node = False
        ParserUtils.bind_attrs(params, self.meta, self.attrs, self.ns_map)

        wild_var = self.meta.find_var(mode=FindMode.WILDCARD)
        if wild_var and wild_var.is_mixed_content:
            ParserUtils.bind_mixed_objects(params, wild_var, self.position, objects)
        else:
            ParserUtils.bind_objects(params, self.meta, self.position, objects)
            text_node = ParserUtils.bind_content(params, self.meta, text, self.ns_map)

        if not text_node and wild_var:
            ParserUtils.bind_wild_content(
                params, wild_var, text, tail, self.attrs, self.ns_map
            )

        obj = self.meta.clazz(**params)
        if self.derived:
            obj = DerivedElement(qname=qname, value=obj)

        objects.append((qname, obj))

        if not wild_var and self.mixed and not wild_node:
            tail = ParserUtils.normalize_content(tail)
            if tail:
                objects.append((None, tail))

        return True

    def child(self, qname: str, attrs: Dict, ns_map: Dict, position: int) -> XmlNode:
        for var in self.fetch_vars(qname):
            node = self.build_node(var, attrs, ns_map, position)
            if node:
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

        if var.clazz:
            return self.build_element_node(
                var.clazz, attrs, ns_map, position, var.derived
            )

        if var.is_any_type:
            node = self.build_element_node(None, attrs, ns_map, position, var.derived)
            if not node:
                node = AnyTypeNode(
                    var=var,
                    attrs=attrs,
                    ns_map=ns_map,
                    position=position,
                    mixed=self.meta.has_var(mode=FindMode.MIXED_CONTENT),
                )
            return node

        if var.is_wildcard:
            return WildcardNode(var=var, attrs=attrs, ns_map=ns_map, position=position)

        return PrimitiveNode(var=var, ns_map=ns_map)

    def fetch_vars(self, qname: str) -> Iterator[XmlVar]:
        for mode in self.FIND_MODES_ORDERED:
            var = self.meta.find_var(qname, mode)

            if not var:
                continue

            if var.is_elements:
                choice = var.find_choice(qname)
                assert choice is not None
                yield choice
            else:
                yield var

    def build_element_node(
        self,
        clazz: Optional[Type],
        attrs: Dict,
        ns_map: Dict,
        position: int,
        derived: bool,
    ) -> Optional[XmlNode]:
        xsi_type = ParserUtils.xsi_type(attrs, ns_map)

        if clazz is None:
            if not xsi_type:
                return None

            clazz = self.context.find_type(xsi_type)
            xsi_type = None

        if clazz is None:
            return None

        is_nillable = ParserUtils.is_nillable(attrs)
        meta = self.context.fetch(clazz, self.meta.namespace, xsi_type)

        if not is_nillable and meta.nillable:
            return None

        return ElementNode(
            meta=meta,
            config=self.config,
            attrs=attrs,
            ns_map=ns_map,
            context=self.context,
            position=position,
            derived=derived,
            mixed=self.meta.has_var(mode=FindMode.MIXED_CONTENT),
        )


@dataclass
class AnyTypeNode(XmlNode):
    """
    XmlNode for elements with an inline datatype declaration through the
    xsi:type attribute.

    :param var: Class field xml var instance
    :param attrs: Key-value attribute mapping
    :param ns_map: Namespace prefix-URI map
    :param position: The node position of objects cache
    :param mixed: Specify if the parent node supports mixed content
    :ivar has_children: Specifies whether the node has encounter any
        children so far
    """

    var: XmlVar
    attrs: Dict
    ns_map: Dict
    position: int
    mixed: bool = False
    has_children: bool = field(init=False, default=False)

    def child(self, qname: str, attrs: Dict, ns_map: Dict, position: int) -> "XmlNode":
        self.has_children = True
        return WildcardNode(position=position, var=self.var, attrs=attrs, ns_map=ns_map)

    def bind(self, qname: str, text: NoneStr, tail: NoneStr, objects: List) -> bool:
        obj: Any = None
        if self.has_children:
            obj = AnyElement(
                qname=qname,
                text=ParserUtils.normalize_content(text),
                tail=ParserUtils.normalize_content(tail),
                attributes=ParserUtils.parse_any_attributes(self.attrs, self.ns_map),
                children=ParserUtils.fetch_any_children(self.position, objects),
            )
            objects.append((self.var.qname, obj))
        else:
            var = self.var
            ns_map = self.ns_map
            datatype = ParserUtils.data_type(self.attrs, self.ns_map)
            obj = ParserUtils.parse_value(text, [datatype.type], var.default, ns_map)

            if var.derived:
                obj = DerivedElement(qname=qname, value=obj)

            objects.append((qname, obj))

            if self.mixed:
                tail = ParserUtils.normalize_content(tail)
                if tail:
                    objects.append((None, tail))

        return True


@dataclass
class WildcardNode(XmlNode):
    """
    XmlNode for extensible elements that can hold any attribute and content.

    The resulting object tree will be a
    :class:`~xsdata.formats.dataclass.models.generics.AnyElement`
    instance.

    :param var: Class field xml var instance
    :param attrs: Key-value attribute mapping
    :param ns_map: Namespace prefix-URI map
    :param position: The node position of objects cache
    """

    var: XmlVar
    attrs: Dict
    ns_map: Dict
    position: int

    def bind(self, qname: str, text: NoneStr, tail: NoneStr, objects: List) -> bool:
        obj = AnyElement(
            qname=qname,
            text=ParserUtils.normalize_content(text),
            tail=ParserUtils.normalize_content(tail),
            attributes=ParserUtils.parse_any_attributes(self.attrs, self.ns_map),
            children=ParserUtils.fetch_any_children(self.position, objects),
        )
        objects.append((self.var.qname, obj))

        return True

    def child(self, qname: str, attrs: Dict, ns_map: Dict, position: int) -> XmlNode:
        return WildcardNode(position=position, var=self.var, attrs=attrs, ns_map=ns_map)


@dataclass
class UnionNode(XmlNode):
    """
    XmlNode for fields with multiple possible types where at least one of them
    is a dataclass.

    The node will record all child events and in the end will replay
    them and try to build all possible objects and sort them by
    score before deciding the winner.

    :param var: Class field xml var instance
    :param attrs: Key-value attribute mapping
    :param ns_map: Namespace prefix-URI map
    :param position: The node position of objects cache
    :param context: Model context provider
    :param level: Current node level
    :param events: Record node events
    """

    var: XmlVar
    attrs: Dict
    ns_map: Dict
    position: int
    context: XmlContext
    level: int = field(default_factory=int)
    events: List = field(default_factory=list)

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
        for clazz in self.var.types:
            candidate = self.parse_class(clazz)
            score = ParserUtils.score_object(candidate)
            if score > max_score:
                max_score = score
                obj = candidate

        if obj:
            objects.append((self.var.qname, obj))

            return True

        raise ParserError(f"Failed to parse union node: {self.var.qname}")

    def parse_class(self, clazz: Type[T]) -> Optional[T]:
        """Initialize a new XmlParser and try to parse the given element."""
        try:
            parser = NodeParser(context=self.context)
            return parser.parse(self.events, clazz)
        except Exception:
            return None


@dataclass
class PrimitiveNode(XmlNode):
    """
    XmlNode for text elements with primitive values like str, int, float.

    :param var: Class field xml var instance
    :param ns_map: Namespace prefix-URI map
    """

    var: XmlVar
    ns_map: Dict

    def bind(self, qname: str, text: NoneStr, tail: NoneStr, objects: List) -> bool:
        var = self.var
        ns_map = self.ns_map
        obj = ParserUtils.parse_value(text, var.types, var.default, ns_map, var.tokens)

        if var.derived:
            obj = DerivedElement(qname=qname, value=obj)

        objects.append((qname, obj))
        return True

    def child(self, qname: str, attrs: Dict, ns_map: Dict, position: int) -> XmlNode:
        raise XmlContextError("Primitive node doesn't support child nodes!")


@dataclass
class SkipNode(XmlNode):
    """Utility node to skip parsing unknown properties."""

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
        """Parse the XML input stream and return the resulting object tree."""
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

            if clazz is None:
                clazz = self.context.find_type(qname)

            if clazz is None:
                raise ParserError(f"No class found matching root: {qname}")

            xsi_type = ParserUtils.xsi_type(attrs, ns_map)
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

    def start_prefix_mapping(self, prefix: NoneStr, uri: str):
        """
        Add the given prefix-URI namespaces mapping if the prefix is new.

        :param prefix: Namespace prefix
        :param uri: Namespace uri
        """
        prefix = prefix or None
        if prefix not in self.ns_map:
            self.ns_map[prefix] = uri


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

    def start_prefix_mapping(self, prefix: NoneStr, uri: str):
        self.events.append((EventType.START_NS, prefix, uri))
        super().start_prefix_mapping(prefix, uri)
