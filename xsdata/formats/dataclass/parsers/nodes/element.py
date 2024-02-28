from typing import Any, Dict, List, Optional, Set, Type

from xsdata.exceptions import ParserError
from xsdata.formats.converter import converter
from xsdata.formats.dataclass.context import XmlContext
from xsdata.formats.dataclass.models.elements import XmlMeta, XmlVar
from xsdata.formats.dataclass.parsers import nodes
from xsdata.formats.dataclass.parsers.config import ParserConfig
from xsdata.formats.dataclass.parsers.mixins import XmlNode
from xsdata.formats.dataclass.parsers.utils import ParserUtils, PendingCollection
from xsdata.logger import logger
from xsdata.models.enums import DataType, Namespace
from xsdata.utils.namespaces import target_uri


class ElementNode(XmlNode):
    """XmlNode for complex elements.

    Args:
        meta: The class binding metadata instance
        attrs: The element attributes
        ns_map: The element namespace prefix-URI map
        config: The parser config instance
        context: The models context instance
        position: The current objects length, everything after
            this position are considered children of this node.
        mixed: Specifies whether this node supports mixed content.
        derived_factory: Derived element factory
        xsi_type: The xml type substitution
        xsi_nil: Specifies whether element has the xsi:nil attribute

    Attributes:
        assigned: A set to store the processed sub-nodes
        tail_processed: Whether the tail process is consumed
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
        "xsi_nil",
        "assigned",
        "tail_processed",
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
        xsi_nil: Optional[bool] = None,
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
        self.xsi_nil = xsi_nil
        self.assigned: Set[int] = set()
        self.tail_processed: bool = False

    def bind(
        self,
        qname: str,
        text: Optional[str],
        tail: Optional[str],
        objects: List[Any],
    ) -> bool:
        """Bind the parsed data into an object for the ending element.

        This entry point is called when a xml element ends and is
        responsible to parse the current element attributes/text, bind
        any children objects and initialize new object.

        Args:
            qname: The element qualified name
            text: The element text content
            tail: The element tail content
            objects: The list of intermediate parsed objects

        Returns:
            Whether the binding process was successful or not.
        """
        obj: Any = None
        if not self.xsi_nil or self.meta.nillable:
            params: Dict = {}
            self.bind_attrs(params)
            self.bind_content(params, text, tail, objects)
            obj = self.config.class_factory(self.meta.clazz, params)

        if self.derived_factory:
            obj = self.derived_factory(qname=qname, value=obj, type=self.xsi_type)

        objects.append((qname, obj))

        if self.mixed and not self.tail_processed:
            tail = ParserUtils.normalize_content(tail)
            if tail:
                objects.append((None, tail))

        return True

    def bind_content(
        self,
        params: Dict,
        text: Optional[str],
        tail: Optional[str],
        objects: List[Any],
    ):
        """Parse the text and tail content.

        Args:
            params: The class parameters
            text: The element text content
            tail: The element tail content
            objects: The list of intermediate parsed objects
        """
        wild_var = self.meta.find_any_wildcard()
        if wild_var and wild_var.mixed:
            self.bind_mixed_objects(params, wild_var, objects)
            bind_text = False
        else:
            self.bind_objects(params, objects)
            bind_text = self.bind_text(params, text)

        if not bind_text and wild_var:
            self.bind_wild_text(params, wild_var, text, tail)
            self.tail_processed = True

        for key in params:
            if isinstance(params[key], PendingCollection):
                params[key] = params[key].evaluate()

    def bind_attrs(self, params: Dict[str, Any]):
        """Parse the element attributes.

        Scenarios:
            - Each attribute matches a class field
            - Class has a wildcard field that sucks everything else

        Args:
            params: The class parameters

        Raises:
            ParserError: If the document contains an unknown attribute
                and the configuration is strict.
        """
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
                else:
                    if (
                        self.config.fail_on_unknown_attributes
                        and target_uri(qname) != Namespace.XSI.uri
                    ):
                        raise ParserError(
                            f"Unknown attribute {self.meta.qname}:{qname}"
                        )

    def bind_attr(self, params: Dict, var: XmlVar, value: Any):
        """Parse an element attribute.

        Ignores fields with init==false!

        Args:
            params: The class parameters
            var: The xml var instance
            value: The attribute value
        """
        if var.init:
            params[var.name] = ParserUtils.parse_value(
                value=value,
                types=var.types,
                default=var.default,
                ns_map=self.ns_map,
                tokens_factory=var.tokens_factory,
                format=var.format,
            )

    def bind_any_attr(self, params: Dict, var: XmlVar, qname: str, value: Any):
        """Parse an element attribute to a wildcard field.

        Args:
            params: The class parameters
            var: The xml var instance
            qname:  The attribute namespace qualified name
            value: The attribute value
        """
        if var.name not in params:
            params[var.name] = {}

        params[var.name][qname] = ParserUtils.parse_any_attribute(value, self.ns_map)

    def bind_objects(self, params: Dict, objects: List):
        """Bind children objects.

        Emit a warning if an object doesn't fit in any
        class parameters.

        Args:
            params: The class parameters
            objects: The list of intermediate parsed objects
        """
        position = self.position
        for qname, obj in objects[position:]:
            if not self.bind_object(params, qname, obj):
                logger.warning("Unassigned parsed object %s", qname)

        del objects[position:]

    def bind_object(self, params: Dict, qname: str, value: Any) -> bool:
        """Bind a child object.

        Args:
            params: The class parameters
            qname: The qualified name of the element
            value: The parsed object

        Returns:
            Whether the parsed object can fit in one of class
            parameters or not.
        """
        for var in self.meta.find_children(qname):
            if var.is_wildcard:
                return self.bind_wild_var(params, var, qname, value)

            if self.bind_var(params, var, value):
                return True

        return False

    @classmethod
    def bind_var(cls, params: Dict, var: XmlVar, value: Any) -> bool:
        """Bind a child object to an element field.

        Args:
            params: The class parameters
            var: The matched xml var instance
            value: The parsed object

        Returns:
            Whether the parsed object can fit in one of class
            parameters or not.
        """
        if var.init:
            if var.list_element:
                items = params.get(var.name)
                if items is None:
                    params[var.name] = PendingCollection([value], var.factory)
                else:
                    items.append(value)
            elif var.name not in params:
                params[var.name] = value
            else:
                return False

        return True

    def bind_wild_var(self, params: Dict, var: XmlVar, qname: str, value: Any) -> bool:
        """Bind a child object to a wildcard field.

        The wildcard might support one or more values. If it
        supports only one the values are nested under a parent
        generic element instance.

        Args:
            params: The class parameters
            var: The wildcard var instance
            qname: The qualified name of the element
            value: The parsed value

        Returns:
            Always true, since wildcard fields can absorb any value.
        """
        value = self.prepare_generic_value(qname, value)

        if var.list_element:
            items = params.get(var.name)
            if items is None:
                params[var.name] = PendingCollection([value], var.factory)
            else:
                items.append(value)
        elif var.name in params:
            previous = params[var.name]
            factory = self.context.class_type.any_element

            if not isinstance(previous, factory) or previous.qname:
                params[var.name] = factory(children=[previous])

            params[var.name].children.append(value)
        else:
            params[var.name] = value

        return True

    def bind_mixed_objects(self, params: Dict, var: XmlVar, objects: List):
        """Bind children objects to a mixed content wildcard field.

        Args:
            params: The class parameters
            var: The wildcard var instance
            objects: The list of intermediate parsed objects
        """
        pos = self.position
        params[var.name] = [
            self.prepare_generic_value(qname, value) for qname, value in objects[pos:]
        ]
        del objects[pos:]

    def prepare_generic_value(self, qname: Optional[str], value: Any) -> Any:
        """Wrap primitive text nodes in a generic element.

        Args:
            qname: The qualified name of the element
            value: The parsed object

        Returns:
            The original parsed value if it's a data class, or
            the wrapped primitive value in a generic element.
        """
        if qname and not self.context.class_type.is_model(value):
            any_factory = self.context.class_type.any_element
            value = any_factory(qname=qname, text=converter.serialize(value))

        return value

    def bind_text(self, params: Dict, text: Optional[str]) -> bool:
        """Bind the element text content.

        Args:
            params: The class parameters
            text: The element text content

        Returns:
            Whether the text content can fit in one of class
            parameters or not.
        """
        var = self.meta.text

        if not var or (text is None and not self.xsi_nil):
            return False

        if var.init:
            if self.xsi_nil and not text:
                params[var.name] = None
            else:
                params[var.name] = ParserUtils.parse_value(
                    value=text,
                    types=var.types,
                    default=var.default,
                    ns_map=self.ns_map,
                    tokens_factory=var.tokens_factory,
                    format=var.format,
                )
        return True

    def bind_wild_text(
        self,
        params: Dict,
        var: XmlVar,
        text: Optional[str],
        tail: Optional[str],
    ) -> bool:
        """Bind the element text and tail content to a wildcard field.

        If the field is a list, prepend the text and append the tail content.
        Otherwise, build a generic element with the text/tail content
        and any attributes. If the field is already occupied, then this
        means the current node is a child, and we need to nested them.

        Args:
            params: The class parameters
            var: The wildcard var instance
            text: The element text content
            tail: The element text content

        Returns:
            Whether the text content can fit in one of class
            parameters or not.
        """
        text = ParserUtils.normalize_content(text)
        tail = ParserUtils.normalize_content(tail)
        if text is None and tail is None:
            return False

        if var.list_element:
            items = params.get(var.name)
            if items is None:
                params[var.name] = items = PendingCollection(None, var.factory)

            items.insert(0, text)
            if tail:
                items.append(tail)

        else:
            previous = params.get(var.name, None)
            factory = self.context.class_type.any_element
            generic = factory(
                text=text,
                tail=tail,
                attributes=ParserUtils.parse_any_attributes(self.attrs, self.ns_map),
            )
            if previous:
                generic.children.append(previous)

            params[var.name] = generic

        return True

    def child(self, qname: str, attrs: Dict, ns_map: Dict, position: int) -> XmlNode:
        """Initialize the next child node to be queued, when an element starts.

        This entry point is responsible to create the next node type
        with all the necessary information on how to bind the incoming
        input data.

        Args:
            qname: The element qualified name
            attrs: The element attributes
            ns_map: The element namespace prefix-URI map
            position: The current length of the intermediate objects

        Raises:
            ParserError: If the child element is unknown
        """
        for var in self.meta.find_children(qname):
            unique = 0 if not var.is_element or var.list_element else var.index
            if not unique or unique not in self.assigned:
                node = self.build_node(qname, var, attrs, ns_map, position)

                if node:
                    if unique:
                        self.assigned.add(unique)

                    return node

        if self.config.fail_on_unknown_properties:
            raise ParserError(f"Unknown property {self.meta.qname}:{qname}")

        return nodes.SkipNode()

    def build_node(
        self,
        qname: str,
        var: XmlVar,
        attrs: Dict,
        ns_map: Dict,
        position: int,
    ) -> Optional[XmlNode]:
        """Build the next child node based on the xml var instance.

        Args:
            qname: The element qualified name
            var: The xml var instance
            attrs: The element attributes
            ns_map: The element namespace prefix-URI map
            position: The current length of the intermediate objects

        Returns:
            The next child node instance, or None if nothing matched
            the starting element.
        """
        if var.is_clazz_union:
            return nodes.UnionNode(
                var=var,
                attrs=attrs,
                ns_map=ns_map,
                config=self.config,
                context=self.context,
                position=position,
            )

        xsi_type = ParserUtils.xsi_type(attrs, ns_map)
        xsi_nil = ParserUtils.xsi_nil(attrs)
        derived_factory = self.context.class_type.derived_element

        if var.clazz:
            return self.build_element_node(
                var.clazz,
                False,
                var.nillable,
                attrs,
                ns_map,
                position,
                derived_factory,
                xsi_type,
                xsi_nil,
            )

        if not var.any_type and not var.is_wildcard:
            return nodes.PrimitiveNode(var, ns_map, self.meta.mixed_content)

        datatype = DataType.from_qname(xsi_type) if xsi_type else None
        derived = var.is_wildcard
        if datatype:
            return nodes.StandardNode(
                datatype,
                ns_map,
                var.nillable,
                derived_factory if derived else None,
            )

        node = None
        clazz = None
        if xsi_type:
            clazz = self.context.find_type(xsi_type)

        if clazz:
            node = self.build_element_node(
                clazz,
                derived,
                var.nillable,
                attrs,
                ns_map,
                position,
                derived_factory,
                xsi_type,
                xsi_nil,
            )

        if node:
            return node

        if var.process_contents != "skip":
            clazz = self.context.find_type(qname)

        if clazz:
            node = self.build_element_node(
                clazz,
                False,
                var.nillable,
                attrs,
                ns_map,
                position,
                None,
                xsi_type,
                xsi_nil,
            )

        if node:
            return node

        return nodes.WildcardNode(
            var=var,
            attrs=attrs,
            ns_map=ns_map,
            position=position,
            factory=self.context.class_type.any_element,
        )

    def build_element_node(
        self,
        clazz: Type,
        derived: bool,
        nillable: bool,
        attrs: Dict,
        ns_map: Dict,
        position: int,
        derived_factory: Type,
        xsi_type: Optional[str] = None,
        xsi_nil: Optional[bool] = None,
    ) -> Optional["ElementNode"]:
        """Build the next element child node.

        Args:
            clazz: The target class
            derived: Whether derived elements should wrap the parsed object
            nillable: Specifies whether nil content is allowed
            attrs: The element attributes
            ns_map: The element namespace prefix-URI map
            position: The current length of the intermediate objects
            derived_factory: The derived factory
            xsi_type: The xml type substitution
            xsi_nil: Specifies whether the node supports nillable content

        Returns:
            The next child element node instance, or None if the
            clazz doesn't match the starting element.
        """
        meta = self.context.fetch(clazz, self.meta.namespace, xsi_type)
        nillable = nillable or meta.nillable

        if not meta or (xsi_nil is not None and nillable != xsi_nil):
            return None

        if xsi_type and not derived and not issubclass(meta.clazz, clazz):
            derived = True

        return ElementNode(
            meta=meta,
            config=self.config,
            attrs=attrs,
            ns_map=ns_map,
            context=self.context,
            position=position,
            derived_factory=derived_factory if derived else None,
            xsi_type=xsi_type,
            xsi_nil=xsi_nil,
            mixed=self.meta.mixed_content,
        )
