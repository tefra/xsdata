import logging
from typing import Iterator, List, Union

from xsdata.models.elements import (
    Attribute,
    AttributeGroup,
    ComplexType,
    Element,
    ElementBase,
    Restriction,
    Schema,
    SimpleType,
)
from xsdata.models.render import Attr, Class

logger = logging.getLogger(__name__)

BaseElement = Union[
    Attribute, AttributeGroup, Element, ComplexType, SimpleType
]
AttributeElement = Union[Attribute, Element, Restriction]


class ClassBuilder:
    def build(self, schema: Schema) -> List[Class]:
        """Generate classes from schema elements."""
        classes: List[Class] = []
        classes.extend(map(self.build_class, schema.attributes))
        classes.extend(map(self.build_class, schema.attribute_groups))
        classes.extend(map(self.build_class, schema.simple_types))
        classes.extend(map(self.build_class, schema.complex_types))
        classes.extend(map(self.build_class, schema.elements))
        return classes

    def build_class(self, obj: BaseElement) -> Class:
        item = Class(
            name=obj.real_name,
            extensions=obj.extensions,
            help=obj.display_help,
        )
        for child in self.element_children(obj):
            self.build_class_attribute(item, child)

        if len(item.extensions) == 0 and len(item.attrs) == 0:
            logger.warning(
                f"Generating class without base and no fields `{item.name}`"
            )

        return item

    def element_children(self, obj: ElementBase) -> Iterator[AttributeElement]:
        for child in obj.children():
            if isinstance(child, (Attribute, Element, Restriction)):
                yield child
            elif isinstance(child, ElementBase):
                yield from self.element_children(child)

    def build_class_attribute(self, parent: Class, obj: AttributeElement):
        inner_type = self.has_inner_type(parent, obj)
        if not obj.real_type:
            logger.warning("Failed to detect type for element: {}".format(obj))
            return None

        parent.attrs.append(
            Attr(
                name=obj.real_name,
                default=getattr(obj, "default", None),
                type=obj.real_type,
                local_type=type(obj).__name__,
                help=obj.display_help,
                forward_ref=inner_type,
                restrictions=obj.get_restrictions(),
            )
        )

    def has_inner_type(self, parent: Class, obj: AttributeElement) -> bool:
        if isinstance(obj, Element):
            if not obj.real_type and obj.complex_type:
                obj.complex_type.name = obj.type = obj.name
                parent.inner.append(self.build_class(obj.complex_type))
                return True
        return False


builder = ClassBuilder()
