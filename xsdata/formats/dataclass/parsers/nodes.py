from dataclasses import dataclass
from typing import Any
from typing import Dict
from typing import List
from typing import Tuple
from typing import Type

from lxml.etree import Element
from lxml.etree import QName

from xsdata.exceptions import XmlContextError
from xsdata.formats.dataclass.context import XmlContext
from xsdata.formats.dataclass.models.elements import FindMode
from xsdata.formats.dataclass.models.elements import XmlMeta
from xsdata.formats.dataclass.parsers.config import ParserConfig
from xsdata.formats.dataclass.parsers.utils import ParserUtils


@dataclass(frozen=True)
class XmlNode:
    position: int

    def next_node(self, element: Element, position: int, ctx: XmlContext) -> "XmlNode":
        raise NotImplementedError("Not Implemented")

    def parse_element(self, element: Element, objects: List[Any]) -> Tuple:
        raise NotImplementedError(f"Not Implemented {element.tag}.")


@dataclass(frozen=True)
class ElementNode(XmlNode):
    meta: XmlMeta
    default: Any
    config: ParserConfig

    def parse_element(self, element: Element, objects: List[Any]) -> Tuple:
        params: Dict = dict()
        ParserUtils.bind_element_attrs(params, self.meta, element)
        ParserUtils.bind_element_text(params, self.meta, element)
        ParserUtils.bind_element_children(params, self.meta, self.position, objects)
        ParserUtils.bind_element_wild_text(params, self.meta, element)

        qname = QName(element.tag)
        obj = self.meta.clazz(**params)

        return qname, obj

    def next_node(self, element: Element, position: int, ctx: XmlContext) -> XmlNode:
        qname = QName(element.tag)
        var = self.meta.find_var(qname, FindMode.NOT_WILDCARD)
        if not var:
            var = self.meta.find_var(qname, FindMode.WILDCARD)

        if not var:
            if self.config.fail_on_unknown_properties:
                raise XmlContextError(
                    f"{self.meta.qname} does not support mixed content: {qname}"
                )
            return SkipNode(position=position)

        if var.clazz:
            xsi_type = ParserUtils.parse_xsi_type(element)
            meta = ctx.fetch(var.clazz, self.meta.qname.namespace, xsi_type)
            return ElementNode(
                position=position, meta=meta, default=var.default, config=self.config
            )

        if var.is_any_type:
            return WildcardNode(position=position, qname=var.qname)

        return PrimitiveNode(
            position=position,
            types=var.types,
            default=var.default,
            tokens=var.is_tokens,
        )


@dataclass(frozen=True)
class RootNode(ElementNode):
    def next_node(self, element: Element, position: int, ctx: XmlContext) -> XmlNode:
        if element.getparent() is None:
            return self
        return super().next_node(element, position, ctx)


@dataclass(frozen=True)
class WildcardNode(XmlNode):
    qname: str

    def parse_element(self, element: Element, objects: List[Any]) -> Tuple:
        obj = ParserUtils.parse_any_element(element)
        obj.children = ParserUtils.fetch_any_children(self.position, objects)

        return self.qname, obj

    def next_node(self, element: Element, position: int, ctx: XmlContext) -> XmlNode:
        return WildcardNode(position=position, qname=self.qname)


@dataclass(frozen=True)
class PrimitiveNode(XmlNode):
    types: List[Type]
    tokens: bool = False
    default: Any = None

    def parse_element(self, element: Element, objects: List) -> Tuple:
        qname = QName(element.tag)
        value = element.text
        ns_map = element.nsmap
        obj = ParserUtils.parse_value(
            self.types, value, self.default, ns_map, self.tokens
        )

        return qname, obj

    def next_node(self, element: Element, position: int, ctx: XmlContext) -> XmlNode:
        raise XmlContextError("Primitive node doesn't support child nodes!")


@dataclass(frozen=True)
class SkipNode(XmlNode):
    def next_node(self, element: Element, position: int, ctx: XmlContext) -> XmlNode:
        return SkipNode(position=position)

    def parse_element(self, element: Element, objects: List[Any]) -> Tuple:
        return None, None
