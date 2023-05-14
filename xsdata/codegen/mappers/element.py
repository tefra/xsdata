import sys
from collections import defaultdict
from typing import Any
from typing import List
from typing import Optional

from xsdata.codegen.models import Attr
from xsdata.codegen.models import AttrType
from xsdata.codegen.models import Class
from xsdata.codegen.utils import ClassUtils
from xsdata.formats.converter import converter
from xsdata.formats.dataclass.models.generics import AnyElement
from xsdata.models.enums import DataType
from xsdata.models.enums import QNames
from xsdata.models.enums import Tag
from xsdata.utils import collections
from xsdata.utils.namespaces import build_qname
from xsdata.utils.namespaces import split_qname


class ElementMapper:
    """Map a schema instance to classes, extensions and attributes."""

    @classmethod
    def map(cls, element: AnyElement, location: str) -> List[Class]:
        """Map schema children elements to classes."""
        assert element.qname is not None

        uri, name = split_qname(element.qname)
        target = cls.build_class(element, uri)

        return list(ClassUtils.flatten(target, f"{location}/{name}"))

    @classmethod
    def build_class(cls, element: AnyElement, parent_namespace: Optional[str]) -> Class:
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
        cls, target: Class, element: AnyElement, namespace: Optional[str]
    ):
        for key, value in element.attributes.items():
            if key == QNames.XSI_NIL:
                target.nillable = value.strip() in ("true", "1")
            else:
                attr_type = cls.build_attribute_type(key, value)
                cls.build_attribute(target, key, attr_type, namespace, Tag.ATTRIBUTE)

    @classmethod
    def build_elements(
        cls, target: Class, element: AnyElement, namespace: Optional[str]
    ):
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
                    attr_type = cls.build_attribute_type(child.qname, child.text)

                sequence = collections.find_connected_component(sequences, index)
                cls.build_attribute(
                    target,
                    child.qname,
                    attr_type,
                    namespace,
                    Tag.ELEMENT,
                    sequence + 1,
                )

    @classmethod
    def build_text(cls, target: Class, element: AnyElement):
        if element.text:
            attr_type = cls.build_attribute_type("value", element.text)
            cls.build_attribute(target, "value", attr_type, None, Tag.SIMPLE_TYPE)

            if any(attr.tag == Tag.ELEMENT for attr in target.attrs):
                target.mixed = True

    @classmethod
    def build_attribute_type(cls, qname: str, value: Any) -> AttrType:
        def match_type(val: Any) -> DataType:
            if not isinstance(val, str):
                return DataType.from_value(val)

            for tp in converter.explicit_types():
                if converter.test(val, [tp], strict=True):
                    return DataType.from_type(tp)

            return DataType.STRING

        if qname == QNames.XSI_TYPE:
            data_type = DataType.QNAME
        elif value is None or value == "":
            data_type = DataType.ANY_SIMPLE_TYPE
        else:
            data_type = match_type(value)

        return AttrType(qname=str(data_type), native=True)

    @classmethod
    def build_attribute(
        cls,
        target: Class,
        qname: str,
        attr_type: AttrType,
        parent_namespace: Optional[str] = None,
        tag: str = Tag.ELEMENT,
        sequence: int = 0,
    ):
        namespace, name = split_qname(qname)
        namespace = cls.select_namespace(namespace, parent_namespace, tag)
        index = len(target.attrs)

        attr = Attr(index=index, name=name, tag=tag, namespace=namespace)
        attr.types.append(attr_type)

        if sequence:
            attr.restrictions.path.append(("s", sequence, 1, sys.maxsize))

        attr.restrictions.min_occurs = 1
        attr.restrictions.max_occurs = 1
        cls.add_attribute(target, attr)

    @classmethod
    def add_attribute(cls, target: Class, attr: Attr):
        pos = collections.find(target.attrs, attr)

        if pos > -1:
            existing = target.attrs[pos]
            existing.restrictions.max_occurs = sys.maxsize
            existing.types.extend(attr.types)
            existing.types = collections.unique_sequence(existing.types, key="qname")
        else:
            target.attrs.append(attr)

    @classmethod
    def select_namespace(
        cls,
        namespace: Optional[str],
        parent_namespace: Optional[str],
        tag: str = Tag.ELEMENT,
    ) -> Optional[str]:
        if tag == Tag.ATTRIBUTE:
            return namespace

        if namespace is None and parent_namespace is not None:
            return ""

        return namespace

    @classmethod
    def sequential_groups(cls, element: AnyElement) -> List[List[int]]:
        groups = cls.group_repeating_attrs(element)
        return list(collections.connected_components(groups))

    @classmethod
    def group_repeating_attrs(cls, element: AnyElement) -> List[List[int]]:
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
