from dataclasses import dataclass, field
from typing import Iterator, List, Optional, Union

from xsdata.logger import logger
from xsdata.models.codegen import Attr, Class, Extension
from xsdata.models.elements import (
    Attribute,
    AttributeGroup,
    ComplexType,
    Element,
    Enumeration,
    Group,
)
from xsdata.models.elements import List as ListElement
from xsdata.models.elements import Restriction, Schema, SimpleType
from xsdata.models.elements import Union as UnionElement
from xsdata.models.enums import TagType, XSDType
from xsdata.models.mixins import ElementBase

BaseElement = Union[
    Attribute, AttributeGroup, Element, ComplexType, SimpleType, Group
]
AttributeElement = Union[
    Attribute, Element, Restriction, Enumeration, UnionElement, ListElement
]


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
        classes.extend(map(self.build_class, self.schema.complex_types))
        classes.extend(map(self.build_class, self.schema.elements))
        return classes

    def build_class(self, obj: BaseElement, inner=False) -> Class:
        """Build and return a class instance."""
        item = Class(
            name=obj.real_name,
            is_abstract=obj.is_abstract,
            namespace=obj.namespace,
            type=type(obj),
            extensions=self.build_class_extensions(obj),
            help=obj.display_help,
        )

        prefix = "Inner" if inner else "Root"
        logger.info(f"{prefix } candidate: `{item.name}`")

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
            name = getattr(obj, "type")
            type_name = type(obj).__name__
            yield Extension(name=name, index=0, type=type_name)

        for child in obj.children():
            if child.is_attribute:
                continue

            for ext in child.extensions:
                type_name = type(child).__name__
                yield Extension(name=ext, index=child.index, type=type_name)

            yield from self.element_extensions(child, include_current=False)

    def build_class_attribute(self, parent: Class, obj: AttributeElement):
        """
        Generate and append an attribute instance to the parent class.

        Skip if no real type could be detected because of an invalid
        schema or missing implementation.
        """
        forward_ref = False
        if self.has_anonymous_class(obj):
            forward_ref = True
            self.build_inner_class(parent, obj)
        elif self.has_anonymous_enumeration(obj):
            forward_ref = True
            self.build_inner_enumeration(parent, obj)

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
        """Build a class from an anonymous complex type inside an element."""
        if isinstance(obj, Element) and obj.complex_type:
            obj.complex_type.name = obj.type = obj.name
            parent.inner.append(self.build_class(obj.complex_type, inner=True))

    def build_inner_enumeration(self, parent: Class, obj: AttributeElement):
        """Build an enumeration class from an anonymous restriction with
        enumeration facet."""
        if (
            isinstance(obj, (Element, Attribute, ListElement))
            and obj.simple_type
        ):
            obj.simple_type.name = obj.real_name
            parent.inner.append(self.build_class(obj.simple_type, inner=True))

            obj.type = obj.simple_type.name
            obj.simple_type = None

    @staticmethod
    def has_anonymous_class(obj: AttributeElement) -> bool:
        """Check if the attribute element contains anonymous complex type."""
        return (
            isinstance(obj, Element)
            and obj.real_type is None
            and obj.complex_type is not None
        )

    @staticmethod
    def has_anonymous_enumeration(obj: AttributeElement) -> bool:
        """Check if the attribute element contains anonymous restriction with
        enumeration facet."""
        return (
            isinstance(obj, (Attribute, Element, ListElement))
            and obj.type is None
            and obj.simple_type is not None
            and obj.simple_type.restriction is not None
            and len(obj.simple_type.restriction.enumerations) > 0
        )

    @staticmethod
    def default_value_type(item: Class) -> Optional[str]:
        value_type = None
        if len(item.extensions) == 0 and len(item.attrs) == 0:
            value_type = XSDType.STRING.code
            logger.warning(f"Empty class: `{item.name}`")
        elif not item.is_enumeration:
            tmp = []
            for i in range(len(item.extensions) - 1, -1, -1):
                extension = item.extensions[i]
                if XSDType.get_enum(extension.name):
                    tmp.append(extension.name)
                    item.extensions.pop(i)
            if tmp:
                value_type = " ".join(reversed(tmp))

        return value_type
