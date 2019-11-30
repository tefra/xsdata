import logging
from dataclasses import dataclass, field
from typing import Iterator, List, Optional, Union

from xsdata.models.codegen import Attr, Class
from xsdata.models.elements import (
    Attribute,
    AttributeGroup,
    ComplexType,
    Element,
    Enumeration,
    Group,
    Restriction,
    Schema,
    SimpleType,
)
from xsdata.models.mixins import ElementBase
from xsdata.utils import text

logger = logging.getLogger(__name__)

BaseElement = Union[
    Attribute, AttributeGroup, Element, ComplexType, SimpleType, Group
]
AttributeElement = Union[Attribute, Element, Restriction, Enumeration]


@dataclass
class ClassBuilder:
    schema: Schema
    target_prefix: Optional[str] = field(init=False)

    def __post_init__(self) -> None:
        """Find and set the target prefix for local types."""
        self.target_prefix = None
        for prefix, namespace in self.schema.nsmap.items():
            if namespace == self.schema.target_namespace:
                self.target_prefix = f"{prefix}:"

    def build(self) -> List[Class]:
        """Generate classes from schema elements."""
        classes: List[Class] = []
        classes.extend(map(self.build_class, self.schema.simple_types))
        classes.extend(map(self.build_class, self.schema.attribute_groups))
        classes.extend(map(self.build_class, self.schema.groups))
        classes.extend(map(self.build_class, self.schema.attributes))
        classes.extend(map(self.build_root_class, self.schema.complex_types))
        classes.extend(map(self.build_root_class, self.schema.elements))
        return classes

    def build_root_class(self, obj: BaseElement):
        return self.build_class(obj, is_root=True)

    def build_class(self, obj: BaseElement, is_root=False) -> Class:
        """Build and return a class instance."""

        item = Class(
            name=obj.real_name,
            is_root=is_root,
            type=type(obj),
            extensions=list(map(self.strip_target_namespace, obj.extensions)),
            help=obj.display_help,
        )
        for child in self.element_children(obj):
            self.build_class_attribute(item, child)

        if len(item.extensions) == 0 and len(item.attrs) == 0:
            logger.warning(f"Empty class: `{item.name}`")

        return item

    def element_children(self, obj: ElementBase) -> Iterator[AttributeElement]:
        """Recursively find and return all child elements that are qualified to
        be class attributes."""
        for child in obj.children():
            if child.is_attribute:
                yield child
            else:
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
            raise ValueError(f"Failed to detect type for element: {obj}")

        parent.attrs.append(
            Attr(
                name=obj.real_name,
                default=getattr(obj, "default", None),
                type=self.strip_target_namespace(obj.real_type),
                local_type=type(obj).__name__,
                help=obj.display_help,
                forward_ref=forward_ref,
                namespace=obj.namespace,
                **obj.get_restrictions(),
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

    def strip_target_namespace(self, value: str) -> str:
        """
        Strip prefixes when they match the target namespace.

        Example: targetNamespace="urn:books" xmlns:bks="urn:books"
        strip prefix bks from type="bks:BookForm" or base="bks:BookForm"
        """
        if self.target_prefix is None:
            return value

        return text.strip_prefix(value, self.target_prefix)

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
