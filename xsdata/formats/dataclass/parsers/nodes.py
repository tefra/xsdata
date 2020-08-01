from dataclasses import dataclass
from dataclasses import field
from dataclasses import fields
from typing import Any
from typing import Dict
from typing import Iterable
from typing import List
from typing import Optional
from typing import Tuple
from typing import Type
from typing import Union

from lxml.etree import _Element
from lxml.etree import _ElementTree
from lxml.etree import Element
from lxml.etree import iterwalk
from lxml.etree import QName

from xsdata.exceptions import ParserError
from xsdata.exceptions import XmlContextError
from xsdata.formats.bindings import T
from xsdata.formats.dataclass.context import XmlContext
from xsdata.formats.dataclass.models.elements import FindMode
from xsdata.formats.dataclass.models.elements import XmlMeta
from xsdata.formats.dataclass.models.elements import XmlVar
from xsdata.formats.dataclass.models.generics import Namespaces
from xsdata.formats.dataclass.parsers.config import ParserConfig
from xsdata.formats.dataclass.parsers.utils import ParserUtils
from xsdata.models.enums import EventType

Parsed = Tuple[Optional[QName], Any]
ParsedObjects = List[Tuple[QName, Any]]
XmlNodes = List["XmlNode"]


@dataclass(frozen=True)
class XmlNode:
    """
    A generic interface for xml nodes that need to implement the two public
    methods to be used in an event based parser with start/end element events.
    The parser needs to maintain a queue for these nodes and a list of objects
    that these nodes return.

    :param position: The current objects size, when the node is created.
    """

    position: int

    def next_node(self, element: Element, position: int, ctx: XmlContext) -> "XmlNode":
        """
        Initialize the next node to be queued, when a new xml element starts.

        This entry point is responsible to create the next node type
        with all the necessary information on how to bind the incoming
        input data.
        """
        raise NotImplementedError("Not Implemented")

    def parse_element(self, element: Element, objects: List[Any]) -> Parsed:
        """
        Parse the current element bind child objects and return the result.

        This entry point is called when an xml element ends and is responsible to parse
        the current element attributes/text, bind any children objects and initialize
        a new object.

        :return: A tuple of the object's qualified name and the new object.
        """
        raise NotImplementedError(f"Not Implemented {element.tag}.")


@dataclass(frozen=True)
class ElementNode(XmlNode):
    """
    Element type node is equivalent to xml elements and is used to bind user
    defined dataclasses.

    :param meta: xml metadata of a dataclass model.
    :param config: Parser config instance passed down from the root node.
    """

    meta: XmlMeta
    config: ParserConfig

    def parse_element(self, element: Element, objects: List[Any]) -> Parsed:
        """
        Parse the given element attributes/text, find all child objects and
        mixed content and initialize a new dataclass instance.

        :return: A tuple of the object's qualified name and the new object.
        """
        params: Dict = {}
        ParserUtils.bind_element_attrs(params, self.meta, element)

        var = self.meta.find_var(mode=FindMode.MIXED_CONTENT)
        if var:
            ParserUtils.bind_mixed_content(params, var, self.position, objects)
            ParserUtils.bind_wildcard_text(params, var, element)
        else:
            ParserUtils.bind_element_children(params, self.meta, self.position, objects)
            ParserUtils.bind_element_text(params, self.meta, element)

        qname = QName(element.tag)
        obj = self.meta.clazz(**params)

        return qname, obj

    def next_node(self, element: Element, position: int, ctx: XmlContext) -> XmlNode:
        """
        Initialize the next node to be queued for the given starting element.

        Search by the given element tag for a matching variable and create the next
        node by the variable type.

        :return: The next node to be queued.
        :raises: XmlContextError if the element is unknown and parser config is strict.
        """
        qname = QName(element.tag)
        var = self.meta.find_var(qname, FindMode.NOT_WILDCARD)
        if not var:
            var = self.meta.find_var(qname, FindMode.WILDCARD)

        if not var:
            if self.config.fail_on_unknown_properties:
                raise ParserError(f"Unknown property {self.meta.qname}:{qname}")
            return SkipNode(position=position)

        if var.is_clazz_union:
            return UnionNode(position=position, var=var, ctx=ctx)

        if var.clazz:
            xsi_type = ParserUtils.parse_xsi_type(element)
            meta = ctx.fetch(var.clazz, self.meta.qname.namespace, xsi_type)
            return ElementNode(position=position, meta=meta, config=self.config)

        if var.is_any_type:
            return WildcardNode(position=position, var=var)

        return PrimitiveNode(position=position, var=var)


@dataclass(frozen=True)
class RootNode(ElementNode):
    def next_node(self, element: Element, position: int, ctx: XmlContext) -> XmlNode:
        """Override parent to return itself if the current element is root."""
        if element.getparent() is None:
            return self
        return super().next_node(element, position, ctx)


@dataclass(frozen=True)
class WildcardNode(XmlNode):
    """
    Wildcard nodes are used for extensible elements that can hold any attribute
    and content and don't have a specific dataclass or primitive type.

    Notes:
        In the future this node should check all known user defined models in the
        target namespace and use that instead of the generic.

    :param var: xml var instance
    """

    var: XmlVar

    def parse_element(self, element: Element, objects: List[Any]) -> Parsed:
        """
        Parse the given element attributes/text/tail, find all child objects
        and mixed content and initialize a new generic element instance.

        :return: A tuple of the object's qualified name and a new
            :class:`xsdata.formats.dataclass.models.generics.AnyElement` instance.
        """
        obj = ParserUtils.parse_any_element(element)
        obj.children = ParserUtils.fetch_any_children(self.position, objects)

        return self.var.qname, obj

    def next_node(self, element: Element, position: int, ctx: XmlContext) -> XmlNode:
        """
        Initialize the next wildcard node to be queued for the given starting
        element.

        Notes:     Wildcard nodes can only queue other wildcard nodes.
        """
        return WildcardNode(position=position, var=self.var)


@dataclass(frozen=True)
class UnionNode(XmlNode):
    """Union nodes are used for variables with more than one possible types
    where at least one of them is a dataclass."""

    var: XmlVar
    ctx: XmlContext

    def next_node(self, element: Element, position: int, ctx: XmlContext) -> XmlNode:
        """Skip all child nodes as we are going to parse the complete element
        tree."""
        return SkipNode(position=position)

    def parse_element(self, element: Element, objects: List[Any]) -> Parsed:
        """
        The handler will make multiple tries to bind the given element to one
        of the available dataclass var types convert it to one of the available
        primitive types.

        The first shoe that fits wins!

        :raise ParserError: When all attempts fail
        :return: A tuple of the object's qualified name and the new object.
        """

        parent = element.getparent()
        if parent is not None:
            parent.remove(element)  # detach element from parent

        obj = None
        max_score = -1
        for clazz in self.var.types:
            candidate = self.parse_class(element, clazz)
            score = self.score_object(candidate)
            if score > max_score:
                max_score = score
                obj = candidate

        if obj:
            return self.var.qname, obj

        raise ParserError(f"Failed to parse union node: {self.var.qname}")

    def parse_class(self, element: Element, clazz: Type[T]) -> Optional[T]:
        """Initialize a new XmlParser and try to parse the given element."""
        try:
            parser = NodeParser(context=self.ctx)
            return parser.parse(element, clazz)
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


@dataclass(frozen=True)
class PrimitiveNode(XmlNode):
    """
    XmlNode for text elements with primitive values eg str, int, float.

    :param var: xml var instance
    """

    var: XmlVar

    def parse_element(self, element: Element, objects: List) -> Parsed:
        """
        Parse the given element text according to the node possible types.

        :return: A tuple of the object's qualified name and the new object.
        """
        qname = QName(element.tag)
        value = element.text
        ns_map = element.nsmap
        obj = ParserUtils.parse_value(
            value, self.var.types, self.var.default, ns_map, self.var.is_tokens
        )

        return qname, obj

    def next_node(self, element: Element, position: int, ctx: XmlContext) -> XmlNode:
        raise XmlContextError("Primitive node doesn't support child nodes!")


@dataclass(frozen=True)
class SkipNode(XmlNode):
    """The skip node should be used when we want to skip parsing child
    elements."""

    def next_node(self, element: Element, position: int, ctx: XmlContext) -> XmlNode:
        """Skip the current child."""
        return SkipNode(position=position)

    def parse_element(self, element: Element, objects: List[Any]) -> Parsed:
        """Skip parsing the current element."""
        return None, None


@dataclass
class NodeParser:
    """
    Xml parsing and binding for dataclasses.

    :param config: Parser configuration
    :param context: Model metadata builder
    :param namespaces: Store the prefix/namespace as they are parsed.
    """

    config: ParserConfig = field(default_factory=ParserConfig)
    context: XmlContext = field(default_factory=XmlContext)
    namespaces: Namespaces = field(init=False, default_factory=Namespaces)

    def parse(self, source: Union[_Element, _ElementTree], clazz: Type[T]) -> T:
        events = EventType.START, EventType.END, EventType.START_NS
        context = iterwalk(source, events=events)
        return self.parse_context(context, clazz)

    def parse_context(self, context: Iterable, clazz: Type[T]) -> T:
        """
        Dispatch elements to handlers as they arrive and are fully parsed.

        :raises ParserError: When the requested type doesn't match the result object
        """
        obj = None
        meta = self.context.build(clazz)
        objects: ParsedObjects = []
        queue: XmlNodes = [RootNode(position=0, meta=meta, config=self.config)]

        self.namespaces.clear()

        for event, element in context:
            if event == EventType.START_NS:
                self.add_namespace(element)
            if event == EventType.START:
                self.queue(element, queue, objects)
            elif event == EventType.END:
                obj = self.dequeue(element, queue, objects)

        if not obj:
            raise ParserError(f"Failed to create target class `{clazz.__name__}`")

        return obj

    def add_namespace(self, namespace: Tuple):
        """Add the given namespace in the registry."""
        prefix, uri = namespace
        self.namespaces.add(uri, prefix)

    def queue(self, element: Element, queue: XmlNodes, objects: ParsedObjects):
        """Queue the next xml node for parsing based on the given element
        qualified name."""
        item = queue[-1]
        position = len(objects)
        queue.append(item.next_node(element, position, self.context))

    def dequeue(self, element: Element, queue: XmlNodes, objects: ParsedObjects) -> Any:
        """
        Use the last xml node to parse the given element and bind any child
        objects.

        :return: Any: A dataclass instance or a python primitive value or None
        """
        item = queue.pop()
        result = item.parse_element(element, objects)

        if not isinstance(item, SkipNode):
            objects.append(result)

        return result[1]
