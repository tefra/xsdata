from dataclasses import dataclass, field
from typing import Iterator, List, Optional, Union

from xsdata.logger import logger
from xsdata.models.codegen import Attr, AttrType, Class, Extension
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
from xsdata.models.mixins import ElementBase, NamedField

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

    def build_class(self, obj: BaseElement) -> Class:
        """Build and return a class instance."""

        if obj.real_name == "travelFlightInfo":
            pass

        item = Class(
            name=obj.real_name,
            is_abstract=obj.is_abstract,
            namespace=self.element_namespace(obj),
            type=type(obj),
            extensions=self.build_class_extensions(obj),
            help=obj.display_help,
        )

        self.build_class_attributes(obj, item)
        return item

    def build_class_attributes(self, obj: ElementBase, item: Class):
        """
        Build the target item class attributes from the given obj child
        elements.

        If exists append default value attribute.
        """
        for child in self.element_children(obj):
            self.build_class_attribute(item, child)

        default_value_type = self.default_value_type(item)
        if default_value_type is not None:
            value_attr = Attr(
                index=0,
                name="value",
                default=None,
                types=[AttrType(name=default_value_type)],
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

    def element_namespace(self, obj: NamedField) -> Optional[str]:
        """
        Returns an element's namespace by its prefix and form.

        Examples:
            - prefixed elements returns the namespace from schema nsmap
            - qualified elements returns the schema target namespace
            - unqualified elements return an empty string
            - unqualified attributes return None
        """

        prefix = obj.prefix
        if prefix:
            return self.schema.nsmap.get(prefix)
        elif obj.is_qualified:
            return self.schema.target_namespace
        elif isinstance(obj, Element):
            return ""

        return None

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

        :raise ValueError:  if types list is empty
        """
        types = self.build_class_attribute_types(parent, obj)
        parent.attrs.append(
            Attr(
                index=obj.index,
                name=obj.real_name,
                default=getattr(obj, "default", None),
                types=types,
                local_type=type(obj).__name__,
                help=obj.display_help,
                namespace=self.element_namespace(obj),
                **obj.get_restrictions(),
            )
        )

    def build_class_attribute_types(
        self, parent: Class, obj: AttributeElement
    ) -> List[AttrType]:
        """Convert real type and anonymous inner elements to an attribute type
        list."""
        inner_class = self.build_inner_class(obj)
        types = [
            AttrType(name=name)
            for name in (obj.real_type or "").split(" ")
            if name
        ]

        if inner_class:
            parent.inner.append(inner_class)
            types.append(AttrType(name=inner_class.name, forward_ref=True))

        if len(types) == 0:
            types.append(AttrType(name=XSDType.STRING.code))
            logger.warning(
                "Default type string for attribute %s.%s",
                parent.name,
                obj.real_name,
            )

        return types

    def build_inner_class(self, obj: AttributeElement) -> Optional[Class]:
        """Convert anonymous type to class to be appended in the parent inner
        class list."""
        if self.has_anonymous_class(obj):
            complex_type = obj.complex_type  # type: ignore
            complex_type.name = obj.name  # type: ignore
            obj.complex_type = None  # type: ignore
            return self.build_class(complex_type)  # type: ignore

        if self.has_anonymous_enumeration(obj):
            simple_type = obj.simple_type  # type: ignore
            simple_type.name = obj.real_name  # type: ignore
            obj.type = None  # type: ignore
            obj.simple_type = None  # type: ignore

            return self.build_class(simple_type)  # type: ignore

        return None

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
