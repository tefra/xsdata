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
from xsdata.formats.dataclass.models.elements import XmlMeta
from xsdata.formats.dataclass.parsers.utils import ParserUtils


@dataclass(frozen=True)
class XmlNode:
    index: int
    position: int

    def next_node(
        self, qname: QName, index: int, position: int, context: XmlContext
    ) -> "XmlNode":
        raise NotImplementedError(f"Not Implemented")

    def parse_element(self, element: Element, objects: List[Any]) -> Tuple:
        raise NotImplementedError(f"Not Implemented {element.tag}.")


@dataclass(frozen=True)
class ElementNode(XmlNode):
    meta: XmlMeta
    default: Any

    def parse_element(self, element: Element, objects: List[Any]) -> Tuple:
        params: Dict = dict()
        ParserUtils.bind_element_attrs(params, self.meta, element)
        ParserUtils.bind_element_text(params, self.meta, element)
        ParserUtils.bind_element_children(params, self.meta, self.position, objects)
        ParserUtils.bind_element_wild_text(params, self.meta, element)

        qname = QName(element.tag)
        obj = self.meta.clazz(**params)

        return qname, obj

    def next_node(
        self, qname: QName, index: int, position: int, context: XmlContext
    ) -> XmlNode:
        var = self.meta.find_var(qname)
        if not var:
            raise XmlContextError(
                f"{self.meta.qname} does not support mixed content: {qname}"
            )

        if var.dataclass:
            return ElementNode(
                index=index,
                position=position,
                meta=context.build(var.clazz, self.meta.qname.namespace),
                default=var.default,
            )

        if var.is_any_type:
            return WildcardNode(index=index, position=position, qname=var.qname)

        return PrimitiveNode(
            index=index,
            position=position,
            types=var.types,
            default=var.default,
            tokens=var.is_tokens,
        )


@dataclass(frozen=True)
class RootNode(ElementNode):
    def next_node(
        self, qname: QName, index: int, position: int, context: XmlContext
    ) -> XmlNode:
        if index == 0:
            return self

        return super(RootNode, self).next_node(qname, index, position, context)


@dataclass(frozen=True)
class WildcardNode(XmlNode):
    qname: str

    def parse_element(self, element: Element, objects: List[Any]) -> Tuple:
        obj = ParserUtils.parse_any_element(element)
        obj.children = ParserUtils.fetch_any_children(self.position, objects)

        return self.qname, obj

    def next_node(
        self, qname: QName, index: int, position: int, context: XmlContext
    ) -> XmlNode:
        return WildcardNode(index=index, position=position, qname=self.qname)


@dataclass(frozen=True)
class SkipNode(XmlNode):
    def parse_element(self, element: Element, objects: List) -> Tuple:
        return None, None

    @classmethod
    def next_node(
        cls, qname: QName, index: int, position: int, context: XmlContext
    ) -> XmlNode:
        return SkipNode(index=index, position=position)


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

    def next_node(
        self, qname: QName, index: int, position: int, context: XmlContext
    ) -> XmlNode:
        return SkipNode(index=index, position=position)
