import copy
import warnings
from dataclasses import dataclass
from dataclasses import field
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
from xsdata.formats.converter import converter
from xsdata.formats.dataclass.context import XmlContext
from xsdata.formats.dataclass.models.elements import XmlMeta
from xsdata.formats.dataclass.models.elements import XmlVar
from xsdata.formats.dataclass.parsers.config import ParserConfig
from xsdata.formats.dataclass.parsers.mixins import EventsHandler
from xsdata.formats.dataclass.parsers.mixins import PushParser
from xsdata.formats.dataclass.parsers.mixins import XmlHandler
from xsdata.formats.dataclass.parsers.mixins import XmlNode
from xsdata.formats.dataclass.parsers.utils import ParserUtils
from xsdata.logger import logger
from xsdata.models.enums import DataType
from xsdata.models.enums import EventType
from xsdata.utils.namespaces import target_uri

Parsed = Tuple[Optional[str], Any]
NoneStr = Optional[str]


class ElementNode(XmlNode):
    """
    XmlNode for complex elements and dataclasses.

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

    __slots__ = (
        "meta",
        "attrs",
        "ns_map",
        "config",
        "context",
        "position",
        "mixed",
        "derived_factory",
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
        derived_factory: Optional[Type] = None,
        xsi_type: Optional[str] = None,
    ):
        self.meta = meta
        self.attrs = attrs
        self.ns_map = ns_map
        self.config = config
        self.context = context
        self.position = position
        self.mixed = mixed
        self.derived_factory = derived_factory
        self.xsi_type = xsi_type
        self.assigned: Set[int] = set()

    def bind(self, qname: str, text: NoneStr, tail: NoneStr, objects: List) -> bool:
        params: Dict = {}
        self.bind_attrs(params)

        wild_var = self.meta.find_any_wildcard()
        if wild_var and wild_var.mixed:
            self.bind_mixed_objects(params, wild_var, objects)
            bind_text = False
        else:
            self.bind_objects(params, objects)
            bind_text = self.bind_content(params, text)

        if not bind_text and wild_var:
            self.bind_wild_content(params, wild_var, text, tail)

        obj = self.meta.clazz(**params)
        if self.derived_factory:
            obj = self.derived_factory(qname=qname, value=obj, type=self.xsi_type)

        objects.append((qname, obj))

        if self.mixed and not wild_var:
            tail = ParserUtils.normalize_content(tail)
            if tail:
                objects.append((None, tail))

        return True

    def bind_attrs(self, params: Dict):
        """Parse the given element's attributes and any text content and return
        a dictionary of field names and values based on the given class
        metadata."""

        if not self.attrs:
            return

        for qname, value in self.attrs.items():
            var = self.meta.find_attribute(qname)
            if var and var.name not in params:
                self.bind_attr(params, var, value)
            else:
                var = self.meta.find_any_attributes(qname)
                if var:
                    self.bind_any_attr(params, var, qname, value)

    def bind_attr(self, params: Dict, var: XmlVar, value: Any):
        if var.init:
            params[var.name] = ParserUtils.parse_value(
                value,
                var.types,
                var.default,
                self.ns_map,
                var.tokens,
                var.format,
            )

    def bind_any_attr(self, params: Dict, var: XmlVar, qname: str, value: Any):
        if var.name not in params:
            params[var.name] = {}

        params[var.name][qname] = ParserUtils.parse_any_attribute(value, self.ns_map)

    def bind_objects(self, params: Dict, objects: List):
        """Return a dictionary of qualified object names and their values for
        the given queue item."""

        position = self.position
        for qname, value in objects[position:]:
            if not self.bind_object(params, qname, value):
                logger.warning("Unassigned parsed object %s", qname)

        del objects[position:]

    def bind_object(self, params: Dict, qname: str, value: Any) -> bool:
        for var in self.meta.find_children(qname):
            if var.is_wildcard:
                return self.bind_wild_var(params, var, qname, value)

            if self.bind_var(params, var, value):
                return True

        return False

    @classmethod
    def bind_var(cls, params: Dict, var: XmlVar, value: Any) -> bool:
        """
        Add the given value to the params dictionary with the var name as key.

        Wrap the value to a list if var is a list. If the var name already exists it
        means we have a name conflict and the parser needs to lookup for any available
        wildcard fields.

        :return: Whether the binding process was successful or not.
        """
        if var.init:
            if var.list_element:
                items = params.get(var.name)
                if items is None:
                    params[var.name] = [value]
                else:
                    items.append(value)
            elif var.name not in params:
                params[var.name] = value
            else:
                return False

        return True

    def bind_wild_var(self, params: Dict, var: XmlVar, qname: str, value: Any) -> bool:
        """
        Add the given value to the params dictionary with the wildcard var name
        as key.

        If the key is already present wrap the previous value into a
        generic AnyElement instance. If the previous value is already a
        generic instance add the current value as a child object.
        """

        value = self.prepare_generic_value(qname, value)

        if var.list_element:
            items = params.get(var.name)
            if items is None:
                params[var.name] = [value]
            else:
                items.append(value)
        elif var.name in params:
            previous = params[var.name]
            if previous.qname:
                factory = self.context.compat.any_element
                params[var.name] = factory(children=[previous])

            params[var.name].children.append(value)
        else:
            params[var.name] = value

        return True

    def bind_mixed_objects(self, params: Dict, var: XmlVar, objects: List):
        """Return a dictionary of qualified object names and their values for
        the given mixed content xml var."""

        pos = self.position
        params[var.name] = [
            self.prepare_generic_value(qname, value) for qname, value in objects[pos:]
        ]
        del objects[pos:]

    def prepare_generic_value(self, qname: Optional[str], value: Any) -> Any:
        """Prepare parsed value before binding to a wildcard field."""

        if qname:
            any_factory = self.context.compat.any_element
            derived_factory = self.context.compat.derived_element

            if not self.context.compat.is_model(value):

                value = any_factory(qname=qname, text=converter.serialize(value))
            elif not isinstance(value, (any_factory, derived_factory)):
                value = derived_factory(qname=qname, value=value)

        return value

    def bind_content(self, params: Dict, txt: Optional[str]) -> bool:
        """
        Add the given element's text content if any to the params dictionary
        with the text var name as key.

        Return if any data was bound.
        """

        if txt is not None:
            var = self.meta.text
            if var and var.init:
                params[var.name] = ParserUtils.parse_value(
                    txt, var.types, var.default, self.ns_map, var.tokens, var.format
                )
                return True

        return False

    def bind_wild_content(
        self, params: Dict, var: XmlVar, txt: Optional[str], tail: Optional[str]
    ) -> bool:
        """
        Extract the text and tail content and bind it accordingly in the params
        dictionary. Return if any data was bound.

        - var is a list prepend the text and append the tail.
        - var is present in the params assign the text and tail to the generic object.
        - Otherwise bind the given element to a new generic object.
        """

        txt = ParserUtils.normalize_content(txt)
        tail = ParserUtils.normalize_content(tail)
        if txt is None and tail is None:
            return False

        if var.list_element:
            items = params.get(var.name)
            if items is None:
                params[var.name] = items = []

            if txt:
                items.insert(0, txt)
            if tail:
                items.append(tail)
        else:
            previous = params.get(var.name, None)
            factory = self.context.compat.any_element
            generic = factory(
                text=txt,
                tail=tail,
                attributes=ParserUtils.parse_any_attributes(self.attrs, self.ns_map),
            )
            if previous:
                generic.children.append(previous)

            params[var.name] = generic

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
        derived_factory = self.context.compat.derived_element

        if var.clazz:
            return self.build_element_node(
                var.clazz,
                attrs,
                ns_map,
                position,
                derived_factory if var.derived else None,
                xsi_type,
            )

        if not var.any_type and not var.is_wildcard:
            return PrimitiveNode(var, ns_map, derived_factory)

        datatype = DataType.from_qname(xsi_type) if xsi_type else None
        derived = var.derived or var.is_wildcard
        if datatype:
            return StandardNode(
                datatype, ns_map, var.nillable, derived_factory if derived else None
            )

        node = None
        clazz = None
        if xsi_type:
            clazz = self.context.find_type(xsi_type)

        if clazz:
            node = self.build_element_node(
                clazz,
                attrs,
                ns_map,
                position,
                derived_factory if derived else None,
                xsi_type,
            )

        if node:
            return node

        return WildcardNode(
            var=var,
            attrs=attrs,
            ns_map=ns_map,
            position=position,
            factory=self.context.compat.any_element,
        )

    def build_element_node(
        self,
        clazz: Type,
        attrs: Dict,
        ns_map: Dict,
        position: int,
        derived_factory: Optional[Type] = None,
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
            derived_factory=derived_factory,
            xsi_type=xsi_type,
            mixed=self.meta.mixed_content,
        )


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

    __slots__ = "var", "attrs", "ns_map", "position", "factory"

    def __init__(
        self, var: XmlVar, attrs: Dict, ns_map: Dict, position: int, factory: Type
    ):
        self.var = var
        self.attrs = attrs
        self.ns_map = ns_map
        self.position = position
        self.factory = factory

    def bind(self, qname: str, text: NoneStr, tail: NoneStr, objects: List) -> bool:
        children = self.fetch_any_children(self.position, objects)
        attributes = ParserUtils.parse_any_attributes(self.attrs, self.ns_map)
        derived = self.var.derived or qname != self.var.qname
        text = ParserUtils.normalize_content(text) if children else text
        text = "" if text is None and not self.var.nillable else text
        tail = ParserUtils.normalize_content(tail)

        if tail or attributes or children or self.var.is_wildcard or derived:
            obj = self.factory(
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

    @classmethod
    def fetch_any_children(cls, position: int, objects: List) -> List:
        """Fetch the children of a wildcard node."""
        children = [value for _, value in objects[position:]]

        del objects[position:]

        return children

    def child(self, qname: str, attrs: Dict, ns_map: Dict, position: int) -> XmlNode:
        return WildcardNode(
            position=position,
            var=self.var,
            attrs=attrs,
            ns_map=ns_map,
            factory=self.factory,
        )


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
    :param context: Model context provider
    """

    __slots__ = "var", "attrs", "ns_map", "position", "context", "level", "events"

    def __init__(
        self, var: XmlVar, attrs: Dict, ns_map: Dict, position: int, context: XmlContext
    ):
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

            if self.context.compat.is_model(clazz):
                self.context.build(clazz, parent_ns=parent_namespace)
                candidate = self.parse_class(clazz)
            else:
                candidate = self.parse_value(text, [clazz])

            score = self.context.compat.score_object(candidate)
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
    """
    XmlNode for text elements with primitive values like str, int, float.

    :param var: Class field xml var instance
    :param ns_map: Namespace prefix-URI map
    """

    __slots__ = ("var", "ns_map", "derived_factory")

    def __init__(self, var: XmlVar, ns_map: Dict, derived_factory: Type):
        self.var = var
        self.ns_map = ns_map
        self.derived_factory = derived_factory

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
            obj = self.derived_factory(qname=qname, value=obj)

        objects.append((qname, obj))
        return True

    def child(self, qname: str, attrs: Dict, ns_map: Dict, position: int) -> XmlNode:
        raise XmlContextError("Primitive node doesn't support child nodes!")


class StandardNode(XmlNode):
    """
    XmlNode for any type elements with a standard xsi:type.

    :param datatype: Standard xsi data type
    :param ns_map: Namespace prefix-URI map
    :param derived: Specify whether the value needs to be wrapped with
        :class:`~xsdata.formats.dataclass.models.generics.DerivedElement`
    :param nillable: Specify whether the node supports nillable content
    """

    __slots__ = ("datatype", "ns_map", "nillable", "derived_factory")

    def __init__(
        self,
        datatype: DataType,
        ns_map: Dict,
        nillable: bool,
        derived_factory: Optional[Type],
    ):
        self.datatype = datatype
        self.ns_map = ns_map
        self.nillable = nillable
        self.derived_factory = derived_factory

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

        if self.derived_factory:
            obj = self.derived_factory(qname=qname, value=obj)

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

        with warnings.catch_warnings():
            if self.config.fail_on_converter_warnings:
                warnings.filterwarnings("error", category=ConverterWarning)

            try:
                result = handler.parse(source)
            except ConverterWarning as e:
                raise ParserError(e)

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
            if xsi_type is None or meta.qname == qname:
                derived_factory = None
            else:
                derived_factory = self.context.compat.derived_element

            child = ElementNode(
                position=0,
                meta=meta,
                config=self.config,
                attrs=attrs,
                ns_map=ns_map,
                context=self.context,
                derived_factory=derived_factory,
                xsi_type=xsi_type if derived_factory else None,
            )

        queue.append(child)

    def end(
        self,
        queue: List[XmlNode],
        objects: List[Parsed],
        qname: str,
        text: NoneStr,
        tail: NoneStr,
    ) -> bool:
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
        item = queue.pop()
        return item.bind(qname, text, tail, objects)


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
