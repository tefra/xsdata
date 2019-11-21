import logging
from dataclasses import dataclass
from typing import Iterator, List, Union

from xsdata.models.codegen import Attr, Class
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

logger = logging.getLogger(__name__)

BaseElement = Union[
    Attribute, AttributeGroup, Element, ComplexType, SimpleType
]
AttributeElement = Union[Attribute, Element, Restriction]


@dataclass
class ClassBuilder:
    schema: Schema

    def build(self) -> List[Class]:
        """Generate classes from schema elements."""
        classes: List[Class] = []
        classes.extend(map(self.build_class, self.schema.simple_types))
        classes.extend(map(self.build_class, self.schema.attribute_groups))
        classes.extend(map(self.build_class, self.schema.attributes))
        classes.extend(map(self.build_class, self.schema.complex_types))
        classes.extend(map(self.build_class, self.schema.elements))
        return classes

    def build_class(self, obj: BaseElement) -> Class:
        """Build and return a class instance."""

        item = Class(
            name=obj.real_name,
            type=type(obj),
            extensions=obj.extensions,
            help=obj.display_help,
        )
        for child in self.element_children(obj):
            self.build_class_attribute(item, child)

        if len(item.extensions) == 0 and len(item.attrs) == 0:
            logger.warning(f"Empty class: `{item.name}`")

        return item

    def element_children(self, obj: ElementBase) -> Iterator[AttributeElement]:
        """Recursively find and return all child elements that can be used to
        codegen class attributes."""

        for child in obj.children():
            if isinstance(child, (Attribute, Element, Restriction)):
                yield child
            elif isinstance(child, ElementBase):
                yield from self.element_children(child)

    def build_class_attribute(self, parent: Class, obj: AttributeElement):
        """
        Generate and append an attribute instance to the parent class.

        Skip if no real type could be detected because of an invalid
        schema or missing implementation.
        """
        forward_ref = False
        if self.has_inner_type(obj):
            forward_ref = True
            self.build_inner_class(parent, obj)

        if not obj.real_type:
            logger.warning(
                f"Failed to detect type for element: {obj.real_name}"
            )
            return None

        parent.attrs.append(
            Attr(
                name=obj.real_name,
                default=getattr(obj, "default", None),
                type=obj.real_type,
                local_type=type(obj).__name__,
                help=obj.display_help,
                forward_ref=forward_ref,
                namespace=obj.namespace,
                restrictions=obj.get_restrictions(),
            )
        )

    def build_inner_class(self, parent: Class, obj: AttributeElement):
        """
        Build a class from an Element complex type and append it to the parent
        inner class list.

        Assign the element name to the complex type name and to the
        element type.
        """
        if isinstance(obj, Element) and obj.complex_type:
            obj.complex_type.name = obj.type = obj.name
            parent.inner.append(self.build_class(obj.complex_type))

    @staticmethod
    def has_inner_type(obj: AttributeElement) -> bool:
        """
        Detect and return if an element instance has inner reference to a
        complex type.

        Generate and append the inner class to the parent class.
        """
        return (
            isinstance(obj, Element)
            and obj.real_type is None
            and obj.complex_type is not None
        )
