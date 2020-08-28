import copy
from dataclasses import dataclass
from dataclasses import field
from dataclasses import fields
from typing import Any
from typing import ClassVar
from typing import Dict
from typing import Iterable
from typing import List
from typing import Optional
from typing import Tuple
from typing import Type

from lxml.etree import iterwalk

from xsdata.exceptions import ParserError
from xsdata.exceptions import XmlContextError
from xsdata.formats.bindings import T
from xsdata.formats.dataclass.context import XmlContext
from xsdata.formats.dataclass.models.elements import FindMode
from xsdata.formats.dataclass.models.elements import XmlMeta
from xsdata.formats.dataclass.models.elements import XmlVar
from xsdata.formats.dataclass.models.generics import AnyElement
from xsdata.formats.dataclass.models.generics import Namespaces
from xsdata.formats.dataclass.parsers.config import ParserConfig
from xsdata.formats.dataclass.parsers.utils import ParserUtils
from xsdata.models.enums import EventType

Parsed = Tuple[Optional[str], Any]
XmlNodes = List["XmlNode"]
NoneStr = Optional[str]


@dataclass
class XmlNode:
    """
    A generic interface for xml nodes that need to implement the two public
    methods to be used in an event based parser with start/end element events.

    The parser needs to maintain a queue for these nodes and a list of
    objects that these nodes return.
    """

    def child(self, qname: str, attrs: Dict, ns_map: Dict, position: int) -> "XmlNode":
        """
        Initialize the next child node to be queued, when a new xml element
        starts.

        This entry point is responsible to create the next node type
        with all the necessary information on how to bind the incoming
        input data.
        """
        raise NotImplementedError("Not Implemented")

    def bind(self, qname: str, text: NoneStr, tail: NoneStr, objects: List) -> bool:
        """
        Parse the current element bind child objects and return the result.

        This entry point is called when an xml element ends and is responsible to parse
        the current element attributes/text, bind any children objects and initialize
        a new object.

        :return: Whether or not anything was appended in the objects list.
        """
        raise NotImplementedError(f"Not Implemented {qname}.")


@dataclass
class ElementNode(XmlNode):
    """
    Element type node is equivalent to xml elements and is used to bind user
    defined dataclasses.

    :param meta: xml metadata of a dataclass model.
    :param attrs: Map of element attributes.
    :param ns_map: Map of prefixes to namespaces.
    :param config: Parser config instance passed down from the root node.
    :param context: Model metadata builder.
    :param position: The current objects size, when the node is created.
    """

    meta: XmlMeta
    attrs: Dict
    ns_map: Dict
    config: ParserConfig
    context: XmlContext
    position: int
    mixed: bool = False

    FIND_MODES_ORDERED: ClassVar[Iterable[FindMode]] = (
        FindMode.NOT_WILDCARD,
        FindMode.WILDCARD,
    )

    def bind(self, qname: str, text: NoneStr, tail: NoneStr, objects: List) -> bool:
        """
        Parse the given element attributes/text, find all child objects and
        mixed content and initialize a new dataclass instance.

        :return: A tuple of the object's qualified name and the new object.
        """
        params: Dict = {}
        ParserUtils.bind_element_attrs(params, self.meta, self.attrs, self.ns_map)

        mixed_var = self.meta.find_var(mode=FindMode.MIXED_CONTENT)
        if mixed_var:
            ParserUtils.bind_mixed_content(params, mixed_var, self.position, objects)
            ParserUtils.bind_wildcard_element(
                params, mixed_var, text, tail, self.attrs, self.ns_map
            )
        else:
            ParserUtils.bind_element_children(params, self.meta, self.position, objects)
            ParserUtils.bind_element(
                params, self.meta, text, tail, self.attrs, self.ns_map,
            )

        objects.append((qname, self.meta.clazz(**params)))

        if not mixed_var and self.mixed:
            tail = ParserUtils.string_value(tail)
            if tail:
                objects.append((None, tail))

        return True

    def child(self, qname: str, attrs: Dict, ns_map: Dict, position: int) -> XmlNode:
        """
        Initialize the next node to be queued for the given starting element.

        Search by the given element tag for a matching variable and create the next
        node by the variable type.

        :return: The next node to be queued.
        :raises: ParserError if the element is unknown and parser config is strict.
        """

        var = self.find_var(qname)
        if not var:
            if self.config.fail_on_unknown_properties:
                raise ParserError(f"Unknown property {self.meta.qname}:{qname}")
            return SkipNode()

        if var.is_clazz_union:
            return UnionNode(
                var=var,
                attrs=attrs,
                ns_map=ns_map,
                context=self.context,
                position=position,
            )

        if var.clazz:
            xsi_type = ParserUtils.parse_xsi_type(attrs, ns_map)
            meta = self.context.fetch(var.clazz, self.meta.namespace, xsi_type)
            mixed = self.meta.find_var(mode=FindMode.MIXED_CONTENT)

            return ElementNode(
                meta=meta,
                config=self.config,
                attrs=attrs,
                ns_map=ns_map,
                context=self.context,
                position=position,
                mixed=mixed is not None,
            )

        if var.is_any_type:
            return WildcardNode(var=var, attrs=attrs, ns_map=ns_map, position=position)

        return PrimitiveNode(var=var, ns_map=ns_map)

    def find_var(self, qname: str) -> Optional[XmlVar]:
        for mode in self.FIND_MODES_ORDERED:
            var = self.meta.find_var(qname, mode)
            if var:
                return var

        return None


@dataclass
class WildcardNode(XmlNode):
    """
    Wildcard nodes are used for extensible elements that can hold any attribute
    and content and don't have a specific dataclass or primitive type.

    Notes:
        In the future this node should check all known user defined models in the
        target namespace and use that instead of the generic.

    :param var: Xml var instance.
    :param attrs: Map of element attributes.
    :param ns_map: Map of prefixes to namespaces.
    :param position: The current objects size, when the node is created.
    """

    var: XmlVar
    attrs: Dict
    ns_map: Dict
    position: int

    def bind(self, qname: str, text: NoneStr, tail: NoneStr, objects: List) -> bool:
        """
        Parse the given element attributes/text/tail, find all child objects
        and mixed content and initialize a new generic element instance.

        :return: A tuple of the object's qualified name and a new
            :class:`xsdata.formats.dataclass.models.generics.AnyElement` instance.
        """
        obj = AnyElement(
            qname=qname,
            text=ParserUtils.string_value(text),
            tail=ParserUtils.string_value(tail),
            ns_map=self.ns_map,
            attributes=ParserUtils.parse_any_attributes(self.attrs, self.ns_map),
            children=ParserUtils.fetch_any_children(self.position, objects),
        )
        objects.append((self.var.qname, obj))

        return True

    def child(self, qname: str, attrs: Dict, ns_map: Dict, position: int) -> XmlNode:
        """Initialize the next wildcard node to be queued for the given
        starting element."""
        return WildcardNode(position=position, var=self.var, attrs=attrs, ns_map=ns_map)


@dataclass
class UnionNode(XmlNode):
    """
    Union nodes are used for variables with more than one possible types where
    at least one of them is a dataclass.

    :param var: Xml var instance.
    :param attrs: Map of element attributes.
    :param ns_map: Map of prefixes to namespaces.
    :param position: The current objects size, when the node is created.
    :param context: Model metadata builder.
    :param level: Current node level.
    :param events: Record node events.
    """

    var: XmlVar
    attrs: Dict
    ns_map: Dict
    position: int
    context: XmlContext
    level: int = field(default_factory=int)
    events: List = field(default_factory=list)

    def __post_init__(self):
        self.attrs = copy.deepcopy(self.attrs)

    def child(self, qname: str, attrs: Dict, ns_map: Dict, position: int) -> XmlNode:
        """Skip all child nodes as we are going to parse the complete element
        tree."""

        self.level += 1
        self.events.append(("start", qname, copy.deepcopy(attrs), ns_map.copy()))
        return self

    def bind(self, qname: str, text: NoneStr, tail: NoneStr, objects: List) -> bool:
        """
        The handler will make multiple tries to bind the given element to one
        of the available dataclass var types convert it to one of the available
        primitive types.

        The first shoe that fits wins!

        :raise ParserError: When all attempts fail
        :return: A tuple of the object's qualified name and the new object.
        """
        self.events.append(("end", qname, text, tail))

        if self.level > 0:
            self.level -= 1
            return False

        self.events.insert(0, ("start", qname, self.attrs, self.ns_map))

        obj = None
        max_score = -1
        for clazz in self.var.types:
            candidate = self.parse_class(clazz)
            score = self.score_object(candidate)
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
            parser = EventParser(context=self.context)
            return parser.parse(self.events, clazz)
        except Exception:
            return None

    @classmethod
    def score_object(cls, obj: Any) -> int:
        """Sum all not None field values for the given object."""
        return (
            sum(1 for var in fields(obj) if getattr(obj, var.name) is not None)
            if obj
            else -1
        )


@dataclass
class PrimitiveNode(XmlNode):
    """
    XmlNode for text elements with primitive values eg str, int, float.

    :param var: xml var instance
    :param ns_map: Map of prefixes to namespaces.
    """

    var: XmlVar
    ns_map: Dict

    def bind(self, qname: str, text: NoneStr, tail: NoneStr, objects: List) -> bool:
        """
        Parse the given element text according to the node possible types.

        :return: A tuple of the object's qualified name and the new object.
        """
        objects.append(
            (
                qname,
                ParserUtils.parse_value(
                    text, self.var.types, self.var.default, self.ns_map, self.var.tokens
                ),
            )
        )
        return True

    def child(self, qname: str, attrs: Dict, ns_map: Dict, position: int) -> XmlNode:
        raise XmlContextError("Primitive node doesn't support child nodes!")


@dataclass
class SkipNode(XmlNode):
    """The skip node should be used when we want to skip parsing child
    elements."""

    def child(self, qname: str, attrs: Dict, ns_map: Dict, position: int) -> XmlNode:
        """Skip the current child."""
        return self

    def bind(self, qname: str, text: NoneStr, tail: NoneStr, objects: List) -> bool:
        """Skip parsing the current element."""
        return False


@dataclass
class NodeParserMixin:
    """
    Xml node data binding mixin.

    :param config: Parser configuration
    :param context: Model metadata builder
    :param namespaces: Store the prefix/namespace as they are parsed.
    """

    config: ParserConfig = field(default_factory=ParserConfig)
    context: XmlContext = field(default_factory=XmlContext)
    namespaces: Namespaces = field(init=False, default_factory=Namespaces)

    def start(
        self,
        queue: XmlNodes,
        qname: str,
        attrs: Dict,
        ns_map: Dict,
        position: int,
        clazz: Type[T],
    ):
        """Queue the next xml node for parsing based on the given element
        qualified name."""
        try:
            item = queue[-1]
            child = item.child(qname, attrs, ns_map, position)
        except IndexError:
            meta = self.context.build(clazz)
            child = ElementNode(
                position=0,
                meta=meta,
                config=self.config,
                attrs=attrs,
                ns_map=ns_map,
                context=self.context,
            )

        queue.append(child)

    def end(
        self,
        queue: XmlNodes,
        qname: str,
        text: Optional[str],
        tail: Optional[str],
        objects: List[Parsed],
    ) -> Any:
        """
        Use the last xml node to parse the given element and bind any child
        objects.

        :return: Any: Return the last obj in the stack If the bind was successful.
        """
        item = queue.pop()
        if item.bind(qname, text, tail, objects):
            return objects[-1][1]

        return None


@dataclass
class EventParser(NodeParserMixin):
    """Basic event based parser."""

    def parse(self, source: Iterable, clazz: Type[T]) -> T:
        obj = None
        objects: List[Parsed] = []
        queue: XmlNodes = []

        self.namespaces.clear()

        for event in source:
            if event[0] == EventType.START:
                _, qname, attrs, ns_map = event
                position = len(objects)
                self.start(queue, qname, attrs, ns_map, position, clazz)
            elif event[0] == EventType.END:
                _, qname, text, tail = event
                obj = self.end(queue, qname, text, tail, objects)

        if not obj:
            raise ParserError(f"Failed to create target class `{clazz.__name__}`")

        return obj


@dataclass
class ElementParser(NodeParserMixin):
    """Event based parser for lxml element tree."""

    def parse(self, source: Any, clazz: Type[T]) -> T:
        events = EventType.START, EventType.END, EventType.START_NS
        context = iterwalk(source, events=events)
        return self.parse_context(context, clazz)

    def parse_context(self, context: Iterable, clazz: Type[T]) -> T:
        """
        Dispatch elements to handlers as they arrive and are fully parsed.

        :raises ParserError: When the requested type doesn't match the result object
        """
        obj = None
        objects: List[Parsed] = []
        queue: XmlNodes = []

        self.namespaces.clear()

        for event, element in context:
            if event == EventType.START:
                position = len(objects)
                self.start(
                    queue, element.tag, element.attrib, element.nsmap, position, clazz
                )
            elif event == EventType.END:
                obj = self.end(queue, element.tag, element.text, element.tail, objects)
                element.clear()
            elif event == EventType.START_NS:
                self.add_namespace(element)

        if not obj:
            raise ParserError(f"Failed to create target class `{clazz.__name__}`")

        return obj

    def add_namespace(self, namespace: Tuple):
        """Add the given namespace in the registry."""
        prefix, uri = namespace
        self.namespaces.add(uri, prefix)
