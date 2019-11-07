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
from xsdata.utils.element import append_documentation
from xsdata.utils.text import pascal_case, safe_snake

logger = logging.getLogger(__name__)

BaseElements = Union[List[Element], List[ComplexType], List[SimpleType]]
BaseElement = Union[Element, ComplexType, SimpleType]
AttributeElement = Union[Attribute, Element, Restriction]


@dataclass
class CodeGenerator:
    INNER_COMPLEX_TYPE_GENERATED = "Inner ComplexType name auto generated"
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
            card = self.generate_element(obj)
            self.deck.append(card)

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
        display_type = obj.display_type
        if not display_type and isinstance(obj, Element) and obj.complex_type:
            self.recover_complex_type(obj)
            return self.generate_class_field(obj)

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
        )

    def recover_complex_type(self, obj: Element):
        assert obj.complex_type is not None
        self.recovered += 1
        obj.type = "{}Type{}".format(pascal_case(obj.name), self.recovered)
        obj.complex_type.name = obj.type
        append_documentation(
            obj.complex_type, self.INNER_COMPLEX_TYPE_GENERATED
        )
        self.queue.insert(0, obj.complex_type)
        obj.complex_type = None
