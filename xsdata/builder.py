from dataclasses import dataclass, field
from typing import Iterator, List, Optional, Union

from xsdata.logger import logger
from xsdata.models.codegen import Attr, AttrType, Class
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
from xsdata.models.enums import DataType, Namespace, TagType
from xsdata.models.mixins import ElementBase, NamedField
from xsdata.utils import text

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

        attr = self.default_class_attribute(item)
        if attr:
            item.attrs.append(attr)

        item.attrs.sort(key=lambda x: x.index)

    def build_class_extensions(self, obj: ElementBase) -> List[AttrType]:
        """Return a sorted, filtered list of extensions."""
        return sorted(
            list(
                {
                    ext.name: ext for ext in self.element_extensions(obj)
                }.values()
            ),
            key=lambda x: x.name,
        )

    def build_data_type(
        self, name, index: int = 0, forward_ref: bool = False
    ) -> AttrType:
        prefix, suffix = text.split(name)
        native = False

        if prefix and (
            prefix == "xml"
            or self.schema.nsmap.get(prefix) == Namespace.SCHEMA
        ):
            name = suffix
            native = True

        return AttrType(
            name=name, index=index, native=native, forward_ref=forward_ref
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
    ) -> Iterator[AttrType]:
        """
        Recursively find and return all parent Extension classes.

        If the initial given obj has a type attribute include it in
        result.
        """

        if include_current and getattr(obj, "type", None):
            name = getattr(obj, "type")
            yield self.build_data_type(name, index=0)

        for child in obj.children():
            if child.is_attribute:
                continue

            for ext in child.extensions:
                yield self.build_data_type(ext, index=child.index)

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
        types = list(
            map(
                self.build_data_type,
                [name for name in (obj.real_type or "").split(" ") if name],
            )
        )

        if inner_class:
            parent.inner.append(inner_class)
            types.append(AttrType(name=inner_class.name, forward_ref=True))

        if len(types) == 0:
            types.append(AttrType(name=DataType.STRING.code, native=True))
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

        if isinstance(obj, UnionElement) and obj.simple_types:
            # Only the last occurrence will be converted. It doesn't make sense
            # to have a union with two anonymous enumerations.
            for i in range(len(obj.simple_types) - 1, -1, -1):
                if obj.simple_types[i].is_enumeration:
                    simple_type = obj.simple_types.pop(i)
                    simple_type.name = obj.real_name
                    return self.build_class(simple_type)

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
            isinstance(obj, (Attribute, Element))
            and obj.type is None
            and obj.simple_type is not None
            and obj.simple_type.is_enumeration
        )

    @staticmethod
    def default_class_attribute(item: Class) -> Optional[Attr]:
        types = []
        if len(item.extensions) == 0 and len(item.attrs) == 0:
            types.append(AttrType(name=DataType.STRING.code, native=True))
            logger.warning(f"Empty class: `{item.name}`")
        elif not item.is_enumeration:
            for i in range(len(item.extensions) - 1, -1, -1):
                if item.extensions[i].native:
                    types.insert(0, item.extensions.pop(i))

        if types:
            return Attr(
                name="value",
                index=0,
                default=None,
                types=types,
                local_type=TagType.EXTENSION.cname,
            )
        return None
