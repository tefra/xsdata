from typing import Dict, Iterator, List, Optional, Tuple

from xsdata.codegen.models import Attr, AttrType, Class, Extension, Restrictions
from xsdata.models.enums import DataType, Tag
from xsdata.models.mixins import ElementBase
from xsdata.models.xsd import (
    Attribute,
    AttributeGroup,
    ComplexType,
    Element,
    Group,
    Schema,
    SimpleType,
)
from xsdata.utils import collections, text
from xsdata.utils.namespaces import build_qname, is_default, prefix_exists

ROOT_CLASSES = (SimpleType, ComplexType, Group, AttributeGroup, Element, Attribute)


class SchemaMapper:
    """Map a schema instance to classes.

    This mapper is used to build classes from xsd documents.
    """

    @classmethod
    def map(cls, schema: Schema) -> List[Class]:
        """Map schema children elements to classes.

        Args:
            schema: The schema instance

        Returns:
            A list of classes.
        """
        assert schema.location is not None

        location = schema.location
        target_namespace = schema.target_namespace

        return [
            cls.build_class(element, container, location, target_namespace)
            for container, element in cls.root_elements(schema)
        ]

    @classmethod
    def root_elements(cls, schema: Schema) -> Iterator[Tuple[str, ElementBase]]:
        """Return the schema root elements.

        Qualified Elements:
            - SimpleType
            - ComplexType
            - Group
            - AttributeGroup
            - Element
            - Attribute

        Args:
            schema: The schema instance

        Yields:
            An iterator of element base instances.
        """

        def condition(item: ElementBase) -> bool:
            return isinstance(item, ROOT_CLASSES)

        for override in schema.overrides:
            for child in override.children(condition=condition):
                yield Tag.OVERRIDE, child

        for redefine in schema.redefines:
            for child in redefine.children(condition=condition):
                yield Tag.REDEFINE, child

        for child in schema.children(condition=condition):
            yield Tag.SCHEMA, child

    @classmethod
    def build_class(
        cls,
        obj: ElementBase,
        container: str,
        location: str,
        target_namespace: Optional[str],
    ) -> Class:
        """Build and return a class instance.

        Args:
            obj: The element base instance
            container: The container name
            location: The schema location
            target_namespace: The schema target namespace

        Returns:
            The new class instance.
        """
        instance = Class(
            qname=build_qname(target_namespace, obj.real_name),
            abstract=obj.is_abstract,
            namespace=cls.element_namespace(obj, target_namespace),
            mixed=obj.is_mixed,
            nillable=obj.is_nillable,
            tag=obj.class_name,
            container=container,
            help=obj.display_help,
            ns_map=obj.ns_map,
            location=location,
            default=obj.default_value,
            fixed=obj.is_fixed,
            substitutions=cls.build_substitutions(obj, target_namespace),
        )

        cls.build_class_extensions(obj, instance)
        cls.build_class_attributes(obj, instance)
        return instance

    @classmethod
    def build_substitutions(
        cls,
        obj: ElementBase,
        target_namespace: Optional[str],
    ) -> List[str]:
        """Builds a list of qualified substitution group names.

        Args:
            obj: The element base instance
            target_namespace: The schema target namespace

        Returns:
            A list of qualified substitution group names.
        """
        return [
            build_qname(obj.ns_map.get(prefix, target_namespace), suffix)
            for prefix, suffix in map(text.split, obj.substitutions)
        ]

    @classmethod
    def build_class_attributes(cls, obj: ElementBase, target: Class):
        """Build the target class attrs from the element children.

        Args:
            obj: The element base instance
            target: The target class instance
        """
        base_restrictions = Restrictions.from_element(obj)
        for child, restrictions in cls.element_children(obj, base_restrictions):
            cls.build_class_attribute(target, child, restrictions)

        target.attrs.sort(key=lambda x: x.index)

    @classmethod
    def build_class_extensions(cls, obj: ElementBase, target: Class):
        """Build the target class extensions from the element children.

        Args:
            obj: The element base instance
            target: The target class instance
        """
        restrictions = obj.get_restrictions()
        extensions = [
            cls.build_class_extension(obj.class_name, target, base, restrictions)
            for base in obj.bases
        ]
        extensions.extend(cls.children_extensions(obj, target))
        target.extensions = collections.unique_sequence(extensions)

    @classmethod
    def build_attr_type(
        cls,
        target: Class,
        name: str,
        forward: bool = False,
    ) -> AttrType:
        """Create a reference attr type for the target class.

        Args:
            target: The target class instance
            name: the qualified name of the attr
            forward: Whether the reference is for an inner class

        Returns:
            The new attr type instance.
        """
        prefix, suffix = text.split(name)
        namespace = target.ns_map.get(prefix, target.target_namespace)
        qname = build_qname(namespace, suffix)
        datatype = DataType.from_qname(qname)

        return AttrType(
            qname=qname,
            native=datatype is not None,
            forward=forward,
        )

    @classmethod
    def element_children(
        cls,
        obj: ElementBase,
        parent_restrictions: Restrictions,
    ) -> Iterator[Tuple[ElementBase, Restrictions]]:
        """Recursively find and return all child elements.

        Args:
            obj: The element base instance.
            parent_restrictions: The parent element restrictions instance

        Yields:
            An iterator of elements and their parent restrictions.
        """
        for child in obj.children():
            if child.is_property:
                yield child, parent_restrictions
            else:
                restrictions = Restrictions.from_element(child)
                restrictions.merge(parent_restrictions)
                yield from cls.element_children(child, restrictions)

    @classmethod
    def element_namespace(
        cls,
        obj: ElementBase,
        target_namespace: Optional[str],
    ) -> Optional[str]:
        """Return the target namespace for the given schema element.

        Rules:
            - elements/attributes with specific target namespace
            - prefixed elements returns the namespace from schema ns_map
            - qualified elements returns the schema target namespace
            - unqualified elements return an empty string
            - unqualified attributes return None

        Args:
            obj: The element base instance
            target_namespace: The schema target namespace

        Returns:
            The element real namespace or None if no namespace
        """
        raw_namespace = obj.raw_namespace
        if raw_namespace:
            return raw_namespace

        prefix = obj.prefix
        if prefix:
            return obj.ns_map.get(prefix)

        if obj.is_qualified and (
            not obj.is_ref
            or not target_namespace
            or not prefix_exists(target_namespace, obj.ns_map)
            or is_default(target_namespace, obj.ns_map)
        ):
            return target_namespace

        return "" if isinstance(obj, Element) else None

    @classmethod
    def children_extensions(
        cls,
        obj: ElementBase,
        target: Class,
    ) -> Iterator[Extension]:
        """Recursively find and return all target's extension instances.

        Args:
            obj: The element base instance
            target: The target class instance

        Yields:
            An iterator of extension instances.
        """
        for child in obj.children():
            if child.is_property:
                continue

            for ext in child.bases:
                yield cls.build_class_extension(
                    child.class_name, target, ext, child.get_restrictions()
                )

            yield from cls.children_extensions(child, target)

    @classmethod
    def build_class_extension(
        cls,
        tag: str,
        target: Class,
        name: str,
        restrictions: Dict,
    ) -> Extension:
        """Create a reference extension for the target class.

        Args:
            tag: The tag name
            target: The target class instance
            name: The qualified name of the extension
            restrictions: A key-value restrictions mapping

        Returns:
            The new extension instance.
        """
        return Extension(
            type=cls.build_attr_type(target, name),
            tag=tag,
            restrictions=Restrictions(**restrictions),
        )

    @classmethod
    def build_class_attribute(
        cls,
        target: Class,
        obj: ElementBase,
        parent_restrictions: Restrictions,
    ):
        """Build and append a new attr to the target class.

        Args:
            target: The target class instance
            obj: The element base instance to map to an attr
            parent_restrictions: The parent element restrictions
        """
        target.ns_map.update(obj.ns_map)
        types = cls.build_attr_types(target, obj)
        restrictions = Restrictions.from_element(obj)

        if obj.class_name in (Tag.ELEMENT, Tag.ANY, Tag.GROUP):
            restrictions.merge(parent_restrictions)

        name = obj.real_name
        target.attrs.append(
            Attr(
                index=obj.index,
                name=name,
                default=obj.default_value,
                fixed=obj.is_fixed,
                types=types,
                tag=obj.class_name,
                help=obj.display_help,
                namespace=cls.element_namespace(obj, target.target_namespace),
                restrictions=restrictions,
            )
        )

    @classmethod
    def build_attr_types(cls, target: Class, obj: ElementBase) -> List[AttrType]:
        """Convert the element types and inner types to an attr types.

        Args:
            target: The target class instance
            obj: The element base instance to extract the types from

        Returns:
            A list of attr type instances.
        """
        types = [cls.build_attr_type(target, tp) for tp in obj.attr_types]

        location = target.location
        namespace = target.target_namespace
        for inner in cls.build_inner_classes(obj, location, namespace):
            target.inner.append(inner)
            types.append(AttrType(qname=inner.qname, forward=True))

        if len(types) == 0:
            types.append(cls.build_attr_type(target, name=obj.default_type))

        return collections.unique_sequence(types)

    @classmethod
    def build_inner_classes(
        cls,
        obj: ElementBase,
        location: str,
        namespace: Optional[str],
    ) -> Iterator[Class]:
        """Find and convert anonymous types to a class instances.

        Args:
            obj: The element base instance
            location: The schema location
            namespace: The parent element namespace

        Yields:
            An iterator of class instances.
        """
        if isinstance(obj, SimpleType) and obj.is_enumeration:
            yield cls.build_class(obj, obj.class_name, location, namespace)
        else:
            for child in obj.children():
                if isinstance(child, ComplexType) or (
                    isinstance(child, SimpleType) and child.is_enumeration
                ):
                    child.name = obj.real_name
                    yield cls.build_class(child, obj.class_name, location, namespace)
                else:
                    yield from cls.build_inner_classes(child, location, namespace)
