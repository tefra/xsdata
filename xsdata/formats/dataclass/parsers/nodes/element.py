from typing import Any
from typing import Dict
from typing import List
from typing import Optional
from typing import Set
from typing import Type

from xsdata.exceptions import ParserError
from xsdata.formats.converter import converter
from xsdata.formats.dataclass.context import XmlContext
from xsdata.formats.dataclass.models.elements import XmlMeta
from xsdata.formats.dataclass.models.elements import XmlVar
from xsdata.formats.dataclass.parsers import nodes
from xsdata.formats.dataclass.parsers.config import ParserConfig
from xsdata.formats.dataclass.parsers.mixins import XmlNode
from xsdata.formats.dataclass.parsers.utils import ParserUtils
from xsdata.formats.dataclass.parsers.utils import PendingCollection
from xsdata.logger import logger
from xsdata.models.enums import DataType
from xsdata.utils import namespaces


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
    :param derived_factory: Derived element factory
    :param xsi_type: The xml type substitution
    :param xsi_nil: The xml type substitution
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
        self, qname: str, text: Optional[str], tail: Optional[str], objects: List
    ) -> bool:
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
        self, params: Dict, text: Optional[str], tail: Optional[str], objects: List[Any]
    ):
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

        for key in params.keys():
            if isinstance(params[key], PendingCollection):
                params[key] = params[key].evaluate()

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
                else:
                    if self.config.fail_on_unknown_attributes:
                        raise ParserError(
                            f"Unknown attribute {self.meta.qname}:{qname}"
                        )

    def bind_attr(self, params: Dict, var: XmlVar, value: Any):
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

        Wrap the value to a list if var is a list. If the var name
        already exists it means we have a name conflict and the parser
        needs to lookup for any available wildcard fields.

        :return: Whether the binding process was successful or not.
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
        """
        Add the given value to the params dictionary with the wildcard var name
        as key.

        If the key is already present wrap the previous value into a
        generic AnyElement instance. If the previous value is already a
        generic instance add the current value as a child object.
        """
        value = self.prepare_generic_value(qname, value, var)

        if var.list_element:
            items = params.get(var.name)
            if items is None:
                params[var.name] = PendingCollection([value], var.factory)
            else:
                items.append(value)
        elif var.name in params:
            previous = params[var.name]
            if previous.qname:
                factory = self.context.class_type.any_element
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
            self.prepare_generic_value(qname, value, var)
            for qname, value in objects[pos:]
        ]
        del objects[pos:]

    def prepare_generic_value(
        self, qname: Optional[str], value: Any, var: XmlVar
    ) -> Any:
        """Prepare parsed value before binding to a wildcard field."""

        if qname:
            any_factory = self.context.class_type.any_element
            derived_factory = self.context.class_type.derived_element

            if not self.context.class_type.is_model(value):
                value = any_factory(qname=qname, text=converter.serialize(value))
            elif not isinstance(
                value, (any_factory, derived_factory)
            ) and not var.find_choice(qname):
                meta = self.context.fetch(type(value))
                xsi_type = namespaces.real_xsi_type(qname, meta.target_qname)
                value = derived_factory(qname=qname, value=value, type=xsi_type)

        return value

    def bind_text(self, params: Dict, text: Optional[str]) -> bool:
        """
        Add the given element's text content if any to the params dictionary
        with the text var name as key.

        Return if any data was bound.
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
                params[var.name] = items = PendingCollection(None, var.factory)

            if txt:
                items.insert(0, txt)
            if tail:
                items.append(tail)
        else:
            previous = params.get(var.name, None)
            factory = self.context.class_type.any_element
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

        return nodes.SkipNode()

    def build_node(
        self, var: XmlVar, attrs: Dict, ns_map: Dict, position: int
    ) -> Optional[XmlNode]:
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
                var.derived,
                attrs,
                ns_map,
                position,
                derived_factory,
                xsi_type,
                xsi_nil,
            )

        if not var.any_type and not var.is_wildcard:
            return nodes.PrimitiveNode(
                var, ns_map, self.meta.mixed_content, derived_factory
            )

        datatype = DataType.from_qname(xsi_type) if xsi_type else None
        derived = var.derived or var.is_wildcard
        if datatype:
            return nodes.StandardNode(
                datatype, ns_map, var.nillable, derived_factory if derived else None
            )

        node = None
        clazz = None
        if xsi_type:
            clazz = self.context.find_type(xsi_type)

        if clazz:
            node = self.build_element_node(
                clazz,
                derived,
                attrs,
                ns_map,
                position,
                derived_factory,
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
        attrs: Dict,
        ns_map: Dict,
        position: int,
        derived_factory: Type,
        xsi_type: Optional[str] = None,
        xsi_nil: Optional[bool] = None,
    ) -> Optional[XmlNode]:
        meta = self.context.fetch(clazz, self.meta.namespace, xsi_type)

        if not meta or (meta.nillable and xsi_nil is False):
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
