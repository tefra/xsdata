import copy
from dataclasses import dataclass
from dataclasses import field
from dataclasses import fields
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
    Element type node is equivalent to xml elements and is used to bind user
    defined dataclasses.

    :param meta: Model xml metadata
    :param attrs: Key-value attribute mapping
    :param ns_map: Prefix-URI Namespace mapping
    :param config: Parser configuration
    :param context: Model xml metadata builder
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
        """
        Parse the given element attributes/text, find all child objects and
        mixed content and initialize a new dataclass instance.

        :return: A tuple of the object's qualified name and the new object.
        """
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
        """
        Initialize the next node to be queued for the given starting element.

        Search by the given element tag for a matching variable and create the next
        node by the variable type.

        :return: The next node to be queued.
        :raises: ParserError if the element is unknown and parser config is strict.
        """

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
                ns_map=self.ns_map,
                attributes=ParserUtils.parse_any_attributes(self.attrs, self.ns_map),
                children=ParserUtils.fetch_any_children(self.position, objects),
            )
            objects.append((self.var.qname, obj))
        else:
            var = self.var
            ns_map = self.ns_map
            datatype = ParserUtils.data_type(self.attrs, self.ns_map)
            obj = ParserUtils.parse_value(text, [datatype.local], var.default, ns_map)

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
    Wildcard nodes are used for extensible elements that can hold any attribute
    and content and don't have a specific dataclass or primitive type.

    Notes:
        In the future this node should check all known user defined models in the
        target namespace and use that instead of the generic.

    :param var: Class field xml var instance
    :param attrs: Key-value attribute mapping
    :param ns_map: Prefix-URI Namespace mapping
    :param position: The node position of objects cache
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
            text=ParserUtils.normalize_content(text),
            tail=ParserUtils.normalize_content(tail),
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

    :param var: Class field xml var instance
    :param attrs: Key-value attribute mapping
    :param ns_map: Prefix-URI Namespace mapping
    :param position: The node position of objects cache
    :param context: Model xml context cache
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
        """Skip all child nodes as we are going to parse the complete element
        tree."""

        self.level += 1
        self.events.append(("start", qname, copy.deepcopy(attrs), ns_map))
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

        self.events.insert(0, ("start", qname, copy.deepcopy(self.attrs), self.ns_map))

        obj = None
        max_score = -1.0
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
            parser = NodeParser(context=self.context)
            return parser.parse(self.events, clazz)
        except Exception:
            return None

    @classmethod
    def score_object(cls, obj: Any) -> float:
        """
        Score a dataclass instance by the field values types.

        Weights:
            1. None: 0
            2. str: 1
            3. *: 1.5
        """

        if not obj:
            return -1.0

        score = 0.0
        for var in fields(obj):
            val = getattr(obj, var.name)
            if isinstance(val, str):
                score += 1.0
            elif val is not None:
                score += 1.5

        return score


@dataclass
class PrimitiveNode(XmlNode):
    """
    XmlNode for text elements with primitive values eg str, int, float.

    :param var: Class field xml var instance
    :param ns_map: Prefix-URI Namespace mapping
    """

    var: XmlVar
    ns_map: Dict

    def bind(self, qname: str, text: NoneStr, tail: NoneStr, objects: List) -> bool:
        """
        Parse the given element text according to the node possible types.

        :return: A tuple of the object's qualified name and the new object.
        """
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
    """The skip node should be used when we want to skip parsing child
    elements."""

    def child(self, qname: str, attrs: Dict, ns_map: Dict, position: int) -> XmlNode:
        """Skip the current child."""
        return self

    def bind(self, qname: str, text: NoneStr, tail: NoneStr, objects: List) -> bool:
        """Skip parsing the current element."""
        return False


@dataclass
class NodeParser(PushParser):
    """
    Bind xml nodes to dataclasses.

    :param config: Parser configuration
    :param context: Model metadata builder
    :param handler: Override default XmlHandler
    :param ms_map: Namespace registry for prefix-URI mappings
    """

    config: ParserConfig = field(default_factory=ParserConfig)
    context: XmlContext = field(default_factory=XmlContext)
    handler: Type[XmlHandler] = field(default=EventsHandler)
    ns_map: Dict = field(init=False, default_factory=dict)

    def parse(self, source: Any, clazz: Type[T]) -> T:
        """Parse the XML input stream and return the resulting object tree."""
        handler = self.handler(clazz=clazz, parser=self)
        result = handler.parse(source)

        if result is not None:
            return result

        raise ParserError(f"Failed to create target class `{clazz.__name__}`")

    def start(
        self,
        clazz: Type,
        queue: List[XmlNode],
        objects: List[Parsed],
        qname: str,
        attrs: Dict,
        ns_map: Dict,
    ):
        """Queue the next xml node for parsing."""
        try:
            item = queue[-1]
            child = item.child(qname, attrs, ns_map, len(objects))
        except IndexError:
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
        Parse the last xml node and bind any intermediate objects.

        :return: The result of the binding process.
        """
        obj = None
        item = queue.pop()
        if item.bind(qname, text, tail, objects):
            obj = objects[-1][1]

        return obj

    def start_prefix_mapping(self, prefix: NoneStr, uri: str):
        """Add the given prefix-URI namespaces mapping if the prefix is new."""
        prefix = prefix or None
        if prefix not in self.ns_map:
            self.ns_map[prefix] = uri


@dataclass
class RecordParser(NodeParser):
    """
    Bind xml nodes to dataclasses with an events recorder.

    :param events: List of pushed events
    """

    events: List = field(default_factory=list)

    def start(
        self,
        clazz: Type,
        queue: List[XmlNode],
        objects: List[Parsed],
        qname: str,
        attrs: Dict,
        ns_map: Dict,
    ):
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
        self.events.append((EventType.END, qname, text, tail))
        return super().end(queue, objects, qname, text, tail)

    def start_prefix_mapping(self, prefix: NoneStr, uri: str):
        self.events.append((EventType.START_NS, prefix, uri))
        super().start_prefix_mapping(prefix, uri)
