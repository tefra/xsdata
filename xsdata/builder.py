import copy
import logging
from dataclasses import dataclass, field
from typing import Any, Dict, Iterator, List, Optional, Union

from lxml import etree

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
from xsdata.models.enums import XSDType

logger = logging.getLogger(__name__)

BaseElement = Union[
    Attribute, AttributeGroup, Element, ComplexType, SimpleType
]
AttributeElement = Union[Attribute, Element, Restriction]


@dataclass
class ClassBuilder:
    common_types: Dict[str, Class] = field(default_factory=dict)

    def build(self, schema: Schema) -> List[Class]:
        """Generate classes from schema elements."""

        self.add_common_types(schema)
        return self.build_classes(schema)

    def add_common_types(self, schema: Schema):
        classes: List[Class] = []
        classes.extend(map(self.build_class, schema.simple_types))
        classes.extend(map(self.build_class, schema.attribute_groups))

        self.common_types.update(
            {
                etree.QName(
                    schema.target_namespace, obj.name
                ).text: self.flatten_common_types(obj, schema.nsmap)
                for obj in classes
            }
        )

    def build_classes(self, schema) -> List[Class]:
        """Go through the global elements of a schema: attributes, attribute
        groups, complex types and elements and build a list of classes."""

        classes: List[Class] = []
        classes.extend(map(self.build_class, schema.attributes))
        classes.extend(map(self.build_class, schema.complex_types))
        classes.extend(map(self.build_class, schema.elements))

        for obj in classes:
            self.flatten_common_types(obj, schema.nsmap)

        return classes

    def find_common_type(
        self, name: str, nsmap: Dict[Any, str]
    ) -> Optional[Class]:
        """Find by namespace reference a common class."""
        prefix = None
        split_name = name.split(":")
        if len(split_name) == 2:
            prefix, name = split_name

        namespace = nsmap.get(prefix)
        qname = etree.QName(namespace, name)
        return self.common_types.get(qname.text)

    def build_class(self, obj: BaseElement) -> Class:
        """Build and return a class instance."""

        item = Class(
            name=obj.real_name,
            extensions=obj.extensions,
            help=obj.display_help,
        )
        for child in self.element_children(obj):
            self.build_class_attribute(item, child)

        if len(item.extensions) == 0 and len(item.attrs) == 0:
            logger.warning(f"Empty class: `{item.name}`")

        return item

    def flatten_common_types(
        self, item: Class, nsmap: Dict[Any, str]
    ) -> Class:
        """Flatten simple types like strings or numbers with restrictions by
        merging the simple types properties into the input class instance."""

        try:
            for inner in item.inner:
                self.flatten_common_types(inner, nsmap)

            for ext in list(item.extensions):
                common = self.find_common_type(ext, nsmap)
                if common is not None:
                    item.attrs = copy.deepcopy(common.attrs) + item.attrs
                    item.extensions.remove(ext)

            for attr in item.attrs:
                common = self.find_common_type(attr.type, nsmap)
                if common is None:
                    continue
                elif len(common.attrs) == 1:
                    value = common.attrs[0]
                    attr.type = value.type
                    attr.restrictions.update(value.restrictions)
                else:
                    # Most likely enumeration
                    logger.debug(f"Missing implementation: {type(common)} ")
                    attr.type = XSDType.STRING.code
        except IndexError:
            logger.warning(f"Failed to flatten types:`{item.name}`")

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


builder = ClassBuilder()
