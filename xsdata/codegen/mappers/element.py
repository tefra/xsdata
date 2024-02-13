from collections import defaultdict
from typing import List, Optional

from xsdata.codegen.mappers.mixins import RawDocumentMapper
from xsdata.codegen.models import AttrType, Class
from xsdata.codegen.utils import ClassUtils
from xsdata.formats.dataclass.models.generics import AnyElement
from xsdata.models.enums import QNames, Tag
from xsdata.utils import collections
from xsdata.utils.namespaces import build_qname, split_qname


class ElementMapper(RawDocumentMapper):
    """Map a generic element to classes.

    This mapper is used to build classes from raw xml documents.
    """

    @classmethod
    def map(cls, element: AnyElement, location: str) -> List[Class]:
        """Map schema children elements to classes.

        Args:
            element: The root element to be mapped
            location: The location of the xml document

        Returns:
            The list of mapped class instances.
        """
        assert element.qname is not None

        uri, name = split_qname(element.qname)
        target = cls.build_class(element, uri)

        return list(ClassUtils.flatten(target, f"{location}/{name}"))

    @classmethod
    def build_class(cls, element: AnyElement, parent_namespace: Optional[str]) -> Class:
        """Build a Class instance for the given generic element.

        Args:
            element: The generic element to be mapped
            parent_namespace: The parent element namespace

        Returns:
            The mapped class instance.
        """
        assert element.qname is not None

        namespace, name = split_qname(element.qname)
        namespace = cls.select_namespace(namespace, parent_namespace)
        target = Class(
            qname=build_qname(namespace, name),
            namespace=namespace,
            tag=Tag.ELEMENT,
            location="",
        )

        cls.build_attributes(target, element, namespace)
        cls.build_elements(target, element, namespace)
        cls.build_text(target, element)

        return target

    @classmethod
    def build_attributes(
        cls,
        target: Class,
        element: AnyElement,
        namespace: Optional[str],
    ):
        """Build attributes for the given Class instance based on AnyElement attributes.

        Args:
            target: The target class instance
            element: The AnyElement containing attributes.
            namespace: The namespace.

        """
        for key, value in element.attributes.items():
            if key == QNames.XSI_NIL:
                target.nillable = value.strip() in ("true", "1")
            else:
                attr_type = cls.build_attr_type(key, value)
                cls.build_attr(target, key, attr_type, namespace, Tag.ATTRIBUTE)

    @classmethod
    def build_elements(
        cls,
        target: Class,
        element: AnyElement,
        namespace: Optional[str],
    ):
        """Build elements for the given Class instance based on AnyElement children.

        Args:
            target: The target class instance
            element: The AnyElement containing children.
            namespace: The namespace.
        """
        sequences = cls.sequential_groups(element)
        for index, child in enumerate(element.children):
            if isinstance(child, AnyElement) and child.qname:
                if child.tail:
                    target.mixed = True

                if child.attributes or child.children:
                    inner = cls.build_class(child, namespace)
                    attr_type = AttrType(qname=inner.qname, forward=True)
                    target.inner.append(inner)
                else:
                    attr_type = cls.build_attr_type(child.qname, child.text)

                sequence = collections.find_connected_component(sequences, index)
                cls.build_attr(
                    target,
                    child.qname,
                    attr_type,
                    namespace,
                    Tag.ELEMENT,
                    sequence + 1,
                )

    @classmethod
    def build_text(cls, target: Class, element: AnyElement):
        """Build a text attr from the generic element text value.

        Args:
            target: The target class instance
            element: The AnyElement containing text content.
        """
        if element.text:
            attr_type = cls.build_attr_type("value", element.text)
            cls.build_attr(target, "value", attr_type, None, Tag.SIMPLE_TYPE)

            if any(attr.tag == Tag.ELEMENT for attr in target.attrs):
                target.mixed = True

    @classmethod
    def sequential_groups(cls, element: AnyElement) -> List[List[int]]:
        """Identify sequential groups of repeating attributes.

        Args:
            element: The generic element instance

        Returns:
            A list of lists of strongly connected children indexes.
        """
        groups = cls.group_repeating_attrs(element)
        return list(collections.connected_components(groups))

    @classmethod
    def group_repeating_attrs(cls, element: AnyElement) -> List[List[int]]:
        """Group repeating children in the given generic element.

        Args:
            element: The generic element instance

        Returns:
            A list of lists of children indexes.
        """
        counters = defaultdict(list)
        for index, child in enumerate(element.children):
            if isinstance(child, AnyElement) and child.qname:
                counters[child.qname].append(index)

        groups = []
        if len(counters) > 1:
            for x in counters.values():
                if len(x) > 1:
                    groups.append(list(range(x[0], x[-1] + 1)))

        return groups
