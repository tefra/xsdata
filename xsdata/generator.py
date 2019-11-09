import copy
import logging
from dataclasses import dataclass, field
from typing import List, Optional, Union

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
        self.generate_elements(self.schema.simple_types)
        self.generate_elements(self.schema.complex_types)
        self.generate_elements(self.schema.elements)

        return self.deck

    def generate_elements(self, items: BaseElements):
        """Clone and the list of elements and start processing it, use a queue
        because the list can grow for inner types without a standard
        reference."""
        self.queue = copy.deepcopy(list(items))
        while len(self.queue):
            obj = self.queue.pop()
            item = self.generate_element(obj)

            if getattr(obj, "inner", False):
                self.deck[-1].inner.append(item)
            else:
                self.deck.append(item)

    def generate_element(self, obj: BaseElement) -> Class:
        return Class(
            name=obj.pascal_name,
            extends=obj.extends,
            attrs=self.generate_class_fields(obj, container=True),
            help=obj.display_help,
        )

    def generate_class_fields(
        self, obj: ElementBase, container=False
    ) -> List[Attr]:
        result = []
        if not container and (
            isinstance(obj, Attribute)
            or isinstance(obj, Element)
            or isinstance(obj, Restriction)
        ):
            result.append(self.generate_class_field(obj))
        else:
            for child in obj.children():
                result.extend(self.generate_class_fields(child))

        return list(filter(None, result))

    def generate_class_field(self, obj: AttributeElement) -> Optional[Attr]:
        queued = self.queue_inner_element(obj)
        display_type = obj.display_type
        if not display_type:
            logger.warning("Failed to detect type for element: {}".format(obj))
            return None

        name = obj.raw_name
        metadata = obj.get_restrictions()
        metadata.update(
            dict(name=name, type=type(obj).__name__, help=obj.display_help)
        )

        return Attr(
            name=safe_snake(name),
            default=getattr(obj, "default", None),
            metadata=metadata,
            type=display_type,
            forward_ref=queued,
        )

    def queue_inner_element(self, obj: AttributeElement):
        if isinstance(obj, Element):
            if not obj.raw_type and obj.complex_type:
                obj.complex_type.name = obj.type = obj.name
                setattr(obj.complex_type, "inner", True)
                self.queue.append(obj.complex_type)
                return True
