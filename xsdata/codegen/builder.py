from dataclasses import dataclass
from typing import Dict
from typing import Iterator
from typing import List
from typing import Optional
from typing import Tuple

from xsdata.codegen.models import Attr
from xsdata.codegen.models import AttrType
from xsdata.codegen.models import Class
from xsdata.codegen.models import Extension
from xsdata.codegen.models import Restrictions
from xsdata.models.enums import DataType
from xsdata.models.enums import Namespace
from xsdata.models.enums import Tag
from xsdata.models.mixins import ElementBase
from xsdata.models.xsd import Attribute
from xsdata.models.xsd import AttributeGroup
from xsdata.models.xsd import ComplexType
from xsdata.models.xsd import Element
from xsdata.models.xsd import Group
from xsdata.models.xsd import Schema
from xsdata.models.xsd import SimpleType
from xsdata.utils import text


@dataclass
class ClassBuilder:
    schema: Schema

    def build(self) -> List[Class]:
        """Generate classes from schema and redefined elements."""
        classes: List[Class] = []

        def is_valid(item: ElementBase) -> bool:
            return isinstance(
                item,
                (SimpleType, ComplexType, Group, AttributeGroup, Element, Attribute),
            )

        for override in self.schema.overrides:
            classes.extend(map(self.build_class, filter(is_valid, override.children())))

        for redefine in self.schema.redefines:
            classes.extend(map(self.build_class, filter(is_valid, redefine.children())))

        classes.extend(map(self.build_class, self.schema.simple_types))
        classes.extend(map(self.build_class, self.schema.attribute_groups))
        classes.extend(map(self.build_class, self.schema.groups))
        classes.extend(map(self.build_class, self.schema.attributes))
        classes.extend(map(self.build_class, self.schema.complex_types))
        classes.extend(map(self.build_class, self.schema.elements))

        return classes

    def build_class(self, obj: ElementBase) -> Class:
        """Build and return a class instance."""
        name = obj.real_name
        namespace = self.element_namespace(obj)
        instance = Class(
            name=name,
            abstract=obj.is_abstract,
            namespace=namespace,
            mixed=obj.is_mixed,
            nillable=obj.is_nillable,
            type=type(obj),
            help=obj.display_help,
            ns_map=obj.ns_map,
            source_namespace=self.schema.target_namespace,
            module=self.schema.module,
            substitutions=obj.substitutions,
        )

        self.build_class_extensions(obj, instance)
        self.build_class_attributes(obj, instance)
        return instance

    def build_class_attributes(self, obj: ElementBase, target: Class):
        """Build the target class attributes from the given ElementBase
        children."""
        for child, restrictions in self.element_children(obj):
            self.build_class_attribute(target, child, restrictions)

        target.attrs.sort(key=lambda x: x.index)

    def build_class_extensions(self, obj: ElementBase, target: Class):
        """Build the item class extensions from the given ElementBase
        children."""
        extensions = {}
        raw_type = obj.raw_type
        if raw_type:
            restrictions = obj.get_restrictions()
            extension = self.build_class_extension(target, raw_type, 0, restrictions)
            extensions[raw_type] = extension

        for extension in self.children_extensions(obj, target):
            extensions[extension.type.name] = extension

        target.extensions = sorted(extensions.values(), key=lambda x: x.type.index)

    def build_data_type(
        self, target: Class, name: str, index: int = 0, forward: bool = False
    ) -> AttrType:
        prefix, suffix = text.split(name)
        native = False
        namespace = target.ns_map.get(prefix)

        if Namespace.get_enum(namespace) and DataType.get_enum(suffix):
            name = suffix
            native = True

        return AttrType(name=name, index=index, native=native, forward=forward,)

    def element_children(
        self, obj: ElementBase, restrictions: Optional[Restrictions] = None
    ) -> Iterator[Tuple[ElementBase, Restrictions]]:
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
            - prefixed elements returns the namespace from schema ns_map
            - qualified elements returns the schema target namespace
            - unqualified elements return an empty string
            - unqualified attributes return None
        """

        raw_namespace = obj.raw_namespace
        if raw_namespace:
            return raw_namespace

        prefix = obj.prefix
        if prefix:
            return obj.ns_map.get(prefix)

        if obj.is_qualified:
            return self.schema.target_namespace

        return "" if isinstance(obj, Element) else None

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
    ) -> Extension:
        return Extension(
            type=self.build_data_type(target, name, index=index),
            restrictions=Restrictions(**restrictions),
        )

    def build_class_attribute(
        self, target: Class, obj: ElementBase, parent_restrictions: Restrictions
    ):
        """Generate and append an attribute target to the target class."""
        types = self.build_class_attribute_types(target, obj)
        restrictions = Restrictions.from_element(obj)

        if obj.class_name in (Tag.ELEMENT, Tag.ANY):
            restrictions.merge(parent_restrictions)

        if restrictions.prohibited:
            return

        name = obj.real_name
        target.ns_map.update(obj.ns_map)

        target.attrs.append(
            Attr(
                index=obj.index,
                name=name,
                local_name=text.suffix(name),
                default=obj.default_value,
                fixed=obj.is_fixed,
                types=types,
                tag=obj.class_name,
                help=obj.display_help,
                namespace=self.element_namespace(obj),
                restrictions=restrictions,
            )
        )

    def build_class_attribute_types(
        self, target: Class, obj: ElementBase
    ) -> List[AttrType]:
        """Convert real type and anonymous inner types to an attribute type
        list."""
        types = [
            self.build_data_type(target, name)
            for name in (obj.real_type or "").split(" ")
            if name
        ]

        for inner in self.build_inner_classes(obj):
            target.inner.append(inner)
            types.append(AttrType(name=inner.name, forward=True))

        if len(types) == 0:
            types.append(AttrType(name=obj.default_type.code, native=True))

        return types

    def build_inner_classes(self, obj: ElementBase) -> Iterator[Class]:
        """Find and convert anonymous types to a class instances."""
        if isinstance(obj, SimpleType) and obj.is_enumeration:
            yield self.build_class(obj)
        else:
            for child in obj.children():
                if isinstance(child, ComplexType) or (
                    isinstance(child, SimpleType) and child.is_enumeration
                ):
                    child.name = obj.real_name
                    yield self.build_class(child)
                else:
                    yield from self.build_inner_classes(child)
