import sys
from collections import defaultdict
from typing import Any
from typing import List
from typing import Optional
from typing import Set

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
    def map(cls, element: AnyElement) -> List[Class]:
        """Map schema children elements to classes."""

        assert element.qname is not None

        target_namespace, module = split_qname(element.qname)
        target = cls.build_class(element, target_namespace)

        return list(ClassUtils.flatten(target, module))

    @classmethod
    def build_class(cls, element: AnyElement, target_namespace: Optional[str]) -> Class:

        assert element.qname is not None

        namespace, name = split_qname(element.qname)
        target = Class(
            qname=build_qname(target_namespace, name),
            namespace=cls.select_namespace(namespace, target_namespace),
            tag=Tag.ELEMENT,
            module="",
        )
        children = [c for c in element.children if isinstance(c, AnyElement)]
        sequential_set = cls.sequential_names(children)

        for key, value in element.attributes.items():
            attr_type = cls.build_attribute_type(key, value)
            cls.build_attribute(target, key, attr_type, target_namespace, Tag.ATTRIBUTE)

        for child in children:

            assert child.qname is not None

            if child.tail:
                target.mixed = True

            if child.attributes or child.children:
                inner = cls.build_class(child, target_namespace)
                attr_type = AttrType(qname=inner.qname, forward=True)
                target.inner.append(inner)
            else:
                attr_type = cls.build_attribute_type(child.qname, child.text)

            cls.build_attribute(
                target,
                child.qname,
                attr_type,
                target_namespace,
                Tag.ELEMENT,
                child.qname in sequential_set,
            )

        if element.text:
            attr_type = cls.build_attribute_type("value", element.text)
            cls.build_attribute(target, "value", attr_type, None, Tag.SIMPLE_TYPE)

        return target

    @classmethod
    def build_attribute_type(cls, qname: str, value: Any) -> AttrType:
        def match_type(val: Any) -> DataType:
            if not isinstance(val, str):
                return DataType.from_value(val)

            for tp in converter.explicit_types():
                if converter.test(val, [tp]):
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
        target_namespace: Optional[str] = None,
        tag: str = Tag.ELEMENT,
        sequential: bool = False,
    ):

        namespace, name = split_qname(qname)
        namespace = cls.select_namespace(namespace, target_namespace, tag)
        index = len(target.attrs)

        attr = Attr(index=index, name=name, tag=tag, namespace=namespace)
        attr.types.append(attr_type)
        attr.restrictions.sequential = sequential or None
        cls.add_attribute(target, attr)

    @classmethod
    def add_attribute(cls, target: Class, attr: Attr):
        existing = collections.first(
            x
            for x in target.attrs
            if x.name == attr.name
            and x.tag == attr.tag
            and x.namespace == attr.namespace
        )

        if existing:
            if attr.restrictions.sequential:
                existing.restrictions.sequential = True

            existing.restrictions.max_occurs = sys.maxsize
            existing.types.extend(attr.types)
        else:
            target.attrs.append(attr)

    @classmethod
    def select_namespace(
        cls,
        namespace: Optional[str],
        target_namespace: Optional[str],
        tag: str = Tag.ELEMENT,
    ) -> Optional[str]:
        if tag == Tag.ATTRIBUTE:
            return namespace

        if namespace is None and target_namespace is not None:
            return ""

        return namespace

    @classmethod
    def sequential_names(cls, children: List[AnyElement]) -> Set[str]:
        mapping = defaultdict(list)
        names = [child.qname for child in children if child.qname]
        indices: Set[int] = set()

        for index, name in enumerate(names):
            mapping[name].append(index)

        for pos in mapping.values():
            total = len(pos)

            if 1 < total < pos[-1] - pos[0] + 1:
                indices.update(range(pos[0], pos[-1] + 1))

        return {names[index] for index in indices}
