import sys
from typing import Any, Optional

from xsdata.codegen.models import Attr, AttrType, Class
from xsdata.formats.converter import converter
from xsdata.models.enums import DataType, QNames, Tag
from xsdata.utils import collections
from xsdata.utils.namespaces import split_qname


class RawDocumentMapper:
    """Mixin class for raw json/xml documents."""

    @classmethod
    def build_attr(
        cls,
        target: Class,
        qname: str,
        attr_type: AttrType,
        parent_namespace: Optional[str] = None,
        tag: str = Tag.ELEMENT,
        sequence: int = 0,
    ):
        """Build an attr for the given class instance.

        Args:
            target: The target class instance
            qname: The attr qualified name
            attr_type: The attr type instance
            parent_namespace: The parent namespace
            tag: The attr tag
            sequence: The attr sequence number
        """
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
    def build_attr_type(cls, qname: str, value: Any) -> AttrType:
        """Build an attribute type for the given attribute name and value.

        Args:
            qname: The attr qualified name
            value: The attr value

        Returns:
           The new attr type instance.
        """

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
    def select_namespace(
        cls,
        namespace: Optional[str],
        parent_namespace: Optional[str],
        tag: str = Tag.ELEMENT,
    ) -> Optional[str]:
        """Select the namespace based on the tag and namespace.

        Args:
            namespace: The current namespace
            parent_namespace: The parent namespace
            tag: The tag name

        Returns:
            Optional[str]: The selected namespace.
        """
        if tag == Tag.ATTRIBUTE:
            return namespace

        if namespace is None and parent_namespace is not None:
            return ""

        return namespace

    @classmethod
    def add_attribute(cls, target: Class, attr: Attr):
        """Add an attr to the target class instance.

        Args:
            target: The target class instance
            attr (Attr): The attribute to be added.
        """
        pos = collections.find(target.attrs, attr)

        if pos > -1:
            existing = target.attrs[pos]
            existing.restrictions.max_occurs = sys.maxsize
            existing.types.extend(attr.types)
            existing.types = collections.unique_sequence(existing.types, key="qname")
        else:
            target.attrs.append(attr)
