import copy
import logging
from dataclasses import dataclass, field
from typing import Dict, Iterator, List, Union

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
from xsdata.models.render import Attr, Class
from xsdata.utils.text import strip_prefix

logger = logging.getLogger(__name__)

BaseElement = Union[
    Attribute, AttributeGroup, Element, ComplexType, SimpleType
]
AttributeElement = Union[Attribute, Element, Restriction]


@dataclass
class ClassBuilder:
    simple_types: Dict[str, Class] = field(default_factory=dict)

    def build(self, schema: Schema) -> List[Class]:
        """Generate classes from schema elements."""
        self.register_simple_types(schema.simple_types)
        return self.build_classes(schema)

    def register_simple_types(self, simple_types: List[SimpleType]):
        """Take global simple types build them and add them to the internal
        storage for later usage when we attempt to replace class extensions and
        attributes with the simple type restrictions and value fields."""
        for simple_type in simple_types:
            obj = self.build_class(simple_type)
            if obj.name not in self.simple_types:
                self.simple_types[obj.name] = obj
            else:
                # If you encounter this warning then it's time to implement
                # qname lookup {namespace}{name}
                logger.warning(f"Name Collision for simple type: {obj.name}")

    def build_classes(self, schema):
        classes: List[Class] = []
        classes.extend(map(self.build_class, schema.attributes))
        classes.extend(map(self.build_class, schema.attribute_groups))
        classes.extend(map(self.build_class, schema.complex_types))
        classes.extend(map(self.build_class, schema.elements))
        return classes

    def find_simple_type(self, name: str):
        """String namespace prefix and look just for the name."""
        name = strip_prefix(name)
        return self.simple_types.get(name)

    def build_class(self, obj: BaseElement) -> Class:
        item = Class(
            name=obj.real_name,
            extensions=obj.extensions,
            help=obj.display_help,
        )
        for child in self.element_children(obj):
            self.build_class_attribute(item, child)

        if len(item.extensions) == 0 and len(item.attrs) == 0:
            logger.warning(f"Empty class: `{item.name}`")
        else:
            self.replace_simple_types(item)
        return item

    def replace_simple_types(self, item: Class):
        try:
            for inner in item.inner:
                self.replace_simple_types(inner)

            for i in range(len(item.extensions)):
                ext = item.extensions[i]
                simple = self.find_simple_type(ext)
                if simple:
                    item.attrs.insert(0, copy.deepcopy(simple.attrs[0]))
                    item.extensions.pop(i)

            for attr in item.attrs:
                simple = self.find_simple_type(attr.type)
                if simple and len(simple.attrs) == 1:
                    value = simple.attrs[0]
                    attr.type = value.type
                    attr.restrictions.update(value.restrictions)
                else:
                    # Most likely enumeration
                    logger.debug(f"Missing implementation: {type(simple)} ")
                    attr.type = XSDType.STRING.code
        except IndexError:
            logger.warning(f"Failed to flatten types:`{item.name}`")

    def element_children(self, obj: ElementBase) -> Iterator[AttributeElement]:
        for child in obj.children():
            if isinstance(child, (Attribute, Element, Restriction)):
                yield child
            elif isinstance(child, ElementBase):
                yield from self.element_children(child)

    def build_class_attribute(self, parent: Class, obj: AttributeElement):
        inner_type = self.has_inner_type(parent, obj)
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
