import logging
from dataclasses import dataclass, field
from typing import Iterator, List, Optional, Union

from xsdata.models.codegen import Attr, Class, Extension
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
from xsdata.models.enums import TagType, XSDType
from xsdata.models.mixins import ElementBase

logger = logging.getLogger(__name__)

BaseElement = Union[
    Attribute, AttributeGroup, Element, ComplexType, SimpleType, Group
]
AttributeElement = Union[Attribute, Element, Restriction, Enumeration]


@dataclass
class ClassBuilder:
    schema: Schema
    target_prefix: Optional[str] = field(init=False)

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
            is_abstract=obj.is_abstract,
            namespace=obj.namespace,
            type=type(obj),
            extensions=self.build_class_extensions(obj),
            help=obj.display_help,
        )

        self.build_class_attributes(obj, item)

        return item

    def build_class_attributes(self, obj: ElementBase, item: Class):
        for child in self.element_children(obj):
            self.build_class_attribute(item, child)

        default_value_type = self.default_value_type(item)
        if default_value_type is not None:
            value_attr = Attr(
                index=0,
                name="value",
                default=None,
                type=default_value_type,
                local_type=TagType.EXTENSION.cname,
            )
            item.attrs.append(value_attr)

        item.attrs.sort(key=lambda x: x.index)

    def build_class_extensions(self, obj: ElementBase) -> List[Extension]:
        """Return a sorted, filtered list of extensions."""
        return sorted(
            list(
                {
                    ext.name: ext for ext in self.element_extensions(obj)
                }.values()
            ),
            key=lambda x: x.name,
        )

    def element_children(self, obj: ElementBase) -> Iterator[AttributeElement]:
        """Recursively find and return all child elements that are qualified to
        be class attributes."""
        for child in obj.children():
            if child.is_attribute:
                yield child
            else:
                yield from self.element_children(child)

    def element_extensions(
        self, obj: ElementBase, include_current=True
    ) -> Iterator[Extension]:
        """
        Recursively find and return all parent Extension classes.

        If the initial given obj has a type attribute include it in
        result.
        """

        if include_current and getattr(obj, "type", None):
            yield Extension(name=getattr(obj, "type"), index=0)

        for child in obj.children():
            if child.is_attribute:
                continue

            if child.extends is not None:
                yield Extension(name=child.extends, index=child.index)

            yield from self.element_extensions(child, include_current=False)

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
                index=obj.index,
                name=obj.real_name,
                default=getattr(obj, "default", None),
                type=obj.real_type,
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

    @staticmethod
    def default_value_type(item: Class):
        value_type = None
        if len(item.extensions) == 0 and len(item.attrs) == 0:
            value_type = XSDType.STRING.code
            logger.warning(f"Empty class: `{item.name}`")
        elif not item.is_enumeration:
            extension = next(
                (ext for ext in item.extensions if XSDType.get_enum(ext.name)),
                None,
            )
            if extension:
                item.extensions.remove(extension)
                value_type = extension.name

        return value_type
