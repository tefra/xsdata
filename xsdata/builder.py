from dataclasses import dataclass
from typing import Dict
from typing import Iterator
from typing import List
from typing import Optional
from typing import Tuple
from typing import Union

from xsdata.models.codegen import Attr
from xsdata.models.codegen import AttrType
from xsdata.models.codegen import Class
from xsdata.models.codegen import Extension
from xsdata.models.codegen import Restrictions
from xsdata.models.elements import Attribute
from xsdata.models.elements import AttributeGroup
from xsdata.models.elements import ComplexType
from xsdata.models.elements import Element
from xsdata.models.elements import Enumeration
from xsdata.models.elements import Group
from xsdata.models.elements import List as ListElement
from xsdata.models.elements import Restriction
from xsdata.models.elements import Schema
from xsdata.models.elements import SimpleType
from xsdata.models.elements import Union as UnionElement
from xsdata.models.enums import DataType
from xsdata.models.enums import Namespace
from xsdata.models.enums import TagType
from xsdata.models.mixins import ElementBase
from xsdata.utils import text

BaseElement = Union[Attribute, AttributeGroup, Element, ComplexType, SimpleType, Group]
AttributeElement = Union[
    Attribute, Element, Restriction, Enumeration, UnionElement, ListElement, SimpleType
]


@dataclass
class ClassBuilder:
    schema: Schema
    package: str

    def build(self) -> List[Class]:
        """Generate classes from schema and redefined elements."""
        classes: List[Class] = []

        for override in self.schema.overrides:
            classes.extend(map(self.build_class, override.children()))

        for redefine in self.schema.redefines:
            classes.extend(map(self.build_class, redefine.children()))

        classes.extend(map(self.build_class, self.schema.simple_types))
        classes.extend(map(self.build_class, self.schema.attribute_groups))
        classes.extend(map(self.build_class, self.schema.groups))
        classes.extend(map(self.build_class, self.schema.attributes))
        classes.extend(map(self.build_class, self.schema.complex_types))
        classes.extend(map(self.build_class, self.schema.elements))

        return classes

    def build_class(self, obj: BaseElement) -> Class:
        """Build and return a class instance."""
        namespace = self.element_namespace(obj)
        instance = Class(
            name=obj.real_name,
            abstract=obj.is_abstract,
            namespace=namespace,
            mixed=obj.is_mixed,
            nillable=obj.is_nillable,
            type=type(obj),
            help=obj.display_help,
            nsmap=obj.nsmap,
            source_namespace=self.schema.target_namespace,
            module=self.schema.module,
            package=self.package,
            substitutions=obj.substitutions,
        )

        self.build_class_extensions(obj, instance)
        self.build_class_attributes(obj, instance)
        return instance

    def build_class_attributes(self, obj: BaseElement, target: Class):
        """Build the target class attributes from the given ElementBase
        children."""
        for child, restrictions in self.element_children(obj):
            self.build_class_attribute(target, child, restrictions)

        target.attrs.sort(key=lambda x: x.index)

    def build_class_extensions(self, obj: BaseElement, target: Class):
        """Build the item class extensions from the given ElementBase
        children."""
        extensions = dict()
        raw_type = obj.raw_type
        if raw_type:
            restrictions = obj.get_restrictions()
            extension = self.build_class_extension(target, raw_type, 0, restrictions)
            extensions[raw_type] = extension

        for extension in self.children_extensions(obj, target):
            extension.forward_ref = False
            extensions[extension.type.name] = extension

        target.extensions = sorted(extensions.values(), key=lambda x: x.type.index)

    def build_data_type(
        self, target: Class, name: str, index: int = 0, forward_ref: bool = False
    ) -> AttrType:
        prefix, suffix = text.split(name)
        native = False
        self_ref = False
        namespace = target.nsmap.get(prefix)

        if Namespace.get_enum(namespace) and DataType.get_enum(suffix):
            name = suffix
            native = True
        elif namespace == self.schema.target_namespace and suffix == target.name:
            self_ref = True

        return AttrType(
            name=name,
            index=index,
            native=native,
            forward_ref=forward_ref,
            self_ref=self_ref,
        )

    def element_children(
        self, obj: ElementBase, restrictions: Optional[Restrictions] = None
    ) -> Iterator[Tuple[AttributeElement, Restrictions]]:
        """Recursively find and return all child elements that are qualified to
        be class attributes."""

        for child in obj.children():
            if child.is_attribute:
                yield child, restrictions or Restrictions()
            else:
                yield from self.element_children(
                    child, restrictions=Restrictions.from_element(child)
                )

    def element_namespace(self, obj: ElementBase) -> Optional[str]:
        """
        Return the target namespace for the given schema element.

        In order:
            - elements/attributes with specific target namespace
            - prefixed elements returns the namespace from schema nsmap
            - qualified elements returns the schema target namespace
            - unqualified elements return an empty string
            - unqualified attributes return None
        """

        raw_namespace = obj.raw_namespace
        if raw_namespace:
            return raw_namespace

        prefix = obj.prefix
        if prefix:
            return obj.nsmap.get(prefix)

        if obj.is_qualified:
            return self.schema.target_namespace
        elif isinstance(obj, Element):
            return ""

        return None

    def children_extensions(
        self, obj: ElementBase, target: Class
    ) -> Iterator[Extension]:
        """
        Recursively find and return all target's Extension classes.

        If the initial given obj has a type attribute include it in
        result.
        """
        for child in obj.children():
            if child.is_attribute:
                continue

            for ext in child.extensions:
                yield self.build_class_extension(
                    target, ext, child.index, child.get_restrictions()
                )

            yield from self.children_extensions(child, target)

    def build_class_extension(
        self, target: Class, name: str, index: int, restrictions: Dict
    ):
        return Extension(
            type=self.build_data_type(target, name, index=index),
            restrictions=Restrictions(**restrictions),
        )

    def build_class_attribute(
        self, target: Class, obj: AttributeElement, parent_restrictions: Restrictions
    ):
        """Generate and append an attribute target to the target class."""
        types = self.build_class_attribute_types(target, obj)
        restrictions = Restrictions.from_element(obj)

        if obj.class_name in (TagType.ELEMENT, TagType.ANY):
            restrictions.merge(parent_restrictions)

        if restrictions.prohibited:
            return

        name = obj.real_name
        target.nsmap.update(obj.nsmap)

        target.attrs.append(
            Attr(
                index=obj.index,
                name=name,
                local_name=name,
                default=obj.default_value,
                fixed=obj.is_fixed,
                wildcard=obj.is_wildcard,
                types=types,
                local_type=obj.class_name,
                help=obj.display_help,
                namespace=self.element_namespace(obj),
                restrictions=restrictions,
            )
        )

    def build_class_attribute_types(
        self, target: Class, obj: AttributeElement
    ) -> List[AttrType]:
        """Convert real type and anonymous inner elements to an attribute type
        list."""
        inner_class = self.build_inner_class(obj)

        types = [
            self.build_data_type(target, name)
            for name in (obj.real_type or "").split(" ")
            if name
        ]

        if inner_class:
            target.inner.append(inner_class)
            types.append(AttrType(name=inner_class.name, forward_ref=True))

        if len(types) == 0:
            types.append(AttrType(name=DataType.STRING.code, native=True))

        return types

    def build_inner_class(self, obj: AttributeElement) -> Optional[Class]:
        """Find and convert anonymous types to a class instance."""
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

        if isinstance(obj, SimpleType) and obj.is_enumeration:
            obj.name = "type"
            inner = self.build_class(obj)
            obj.name = "value"
            obj.restriction = None
            return inner

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
