from dataclasses import dataclass
from dataclasses import field
from typing import Any
from typing import Dict
from typing import List
from typing import Tuple
from typing import Type

from lxml.etree import Element
from lxml.etree import QName

from xsdata.exceptions import ModelInspectionError
from xsdata.formats.dataclass.context import ModelContext
from xsdata.formats.dataclass.parsers.utils import ParserUtils
from xsdata.models.inspect import ClassMeta


@dataclass(frozen=True)
class BaseNode:
    index: int
    position: int

    def next_node(self, qname: QName, index: int, position: int, context: ModelContext):
        raise ModelInspectionError(f"Not Implemented {qname}.")

    def parse_element(self, element: Element, objects: List[Any]) -> Tuple:
        raise ModelInspectionError(f"Not Implemented {element.tag}.")


@dataclass(frozen=True)
class ElementNode(BaseNode):
    meta: ClassMeta
    default: Any

    def parse_element(self, element: Element, objects: List[Any]) -> Tuple:
        params: Dict = dict()
        ParserUtils.bind_element_attrs(params, self.meta, element)
        ParserUtils.bind_element_text(params, self.meta, element)
        ParserUtils.bind_element_children(
            params, self.meta, element, self.position, objects
        )
        ParserUtils.bind_element_wild_text(params, self.meta, element)

        qname = QName(element.tag)
        obj = self.meta.clazz(**params)

        return qname, obj

    def next_node(self, qname: QName, index: int, position: int, context: ModelContext):
        var = self.meta.get_var(qname)
        if not var:
            return None
        elif var.dataclass:
            return ElementNode(
                index=index,
                position=position,
                meta=context.class_meta(var.clazz, self.meta.namespace),
                default=var.default,
            )
        elif var.is_any_element:
            return WildcardNode(index=index, position=position, qname=var.qname)
        elif var.types[0] is object:
            return WildcardNode(index=index, position=position, qname=var.qname)
        else:
            return PrimitiveNode(
                index=index, position=position, types=var.types, default=var.default,
            )


@dataclass(frozen=True)
class RootNode(ElementNode):
    def next_node(self, qname: QName, index: int, position: int, context: ModelContext):
        if index == 0:
            return self
        else:
            return super(RootNode, self).next_node(qname, index, position, context)


@dataclass(frozen=True)
class WildcardNode(BaseNode):
    qname: str

    def parse_element(self, element: Element, objects: List[Any]) -> Tuple:
        obj = ParserUtils.parse_any_element(element)
        obj.children = ParserUtils.fetch_any_children(self.position, objects)

        return self.qname, obj

    def next_node(self, qname: QName, index: int, position: int, context: ModelContext):
        return WildcardNode(index=index, position=position, qname=self.qname)


@dataclass(frozen=True)
class SkipNode(BaseNode):
    def parse_element(self, element: Element, objects: List) -> Tuple:
        return None, None

    @classmethod
    def next_node(cls, qname: QName, index: int, position: int, context: ModelContext):
        return SkipNode(index=index, position=position)


@dataclass(frozen=True)
class PrimitiveNode(BaseNode):
    types: List[Type]
    default: Any = field(default=None)

    def parse_element(self, element: Element, objects: List) -> Tuple:
        qname = QName(element.tag)
        value = element.text
        ns_map = element.nsmap
        obj = ParserUtils.parse_value(self.types, value, self.default, ns_map)

        return qname, obj

    def next_node(self, qname: QName, index: int, position: int, context: ModelContext):
        return SkipNode(index=index, position=position)
