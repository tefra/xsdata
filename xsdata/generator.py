import logging
from dataclasses import dataclass, field
from typing import Iterator, List, Union

from xsdata.models.elements import (
    Attribute,
    ComplexType,
    Element,
    ElementBase,
    Restriction,
    Schema,
    SimpleType,
)
from xsdata.models.templates import Attr, Class
from xsdata.utils.text import safe_snake

logger = logging.getLogger(__name__)

BaseElements = Union[List[Element], List[ComplexType], List[SimpleType]]
BaseElement = Union[Element, ComplexType, SimpleType]
AttributeElement = Union[Attribute, Element, Restriction]


@dataclass
class CodeGenerator:
    schema: Schema
    recovered: int = field(default=0, init=False)
    queue: List[BaseElement] = field(default_factory=list, init=False)
    deck: List[Class] = field(default_factory=list, init=False)

    def generate(self) -> List[Class]:
        """Generate class properties from schema elements and simple/complex
        types."""
        classes: List[Class] = []
        classes.extend(map(self.generate_element, self.schema.simple_types))
        classes.extend(map(self.generate_element, self.schema.complex_types))
        classes.extend(map(self.generate_element, self.schema.elements))
        return classes

    def generate_element(self, obj: BaseElement) -> Class:
        item = Class(
            name=obj.pascal_name,
            extends=obj.display_base,
            help=obj.display_help,
        )
        for child in self.field_children(obj):
            self.generate_class_field(item, child)

        return item

    def field_children(self, obj: ElementBase) -> Iterator[AttributeElement]:
        for child in obj.children():
            if isinstance(child, (Attribute, Element, Restriction)):
                yield child
            elif isinstance(child, ElementBase):
                yield from self.field_children(child)

    def generate_class_field(self, item: Class, obj: AttributeElement):
        queued = self.queue_inner_element(item, obj)
        display_type = obj.display_type
        if not display_type:
            logger.warning("Failed to detect type for element: {}".format(obj))
            return None

        name = obj.raw_name
        metadata = obj.get_restrictions()
        metadata.update(
            dict(name=name, type=type(obj).__name__, help=obj.display_help)
        )

        item.attrs.append(
            Attr(
                name=safe_snake(name),
                default=getattr(obj, "default", None),
                metadata=metadata,
                type=display_type,
                forward_ref=queued,
            )
        )

    def queue_inner_element(self, item: Class, obj: AttributeElement):
        if isinstance(obj, Element):
            if not obj.raw_type and obj.complex_type:
                obj.complex_type.name = obj.type = obj.name
                item.inner.append(self.generate_element(obj.complex_type))
                return True
