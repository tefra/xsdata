import sys
from typing import Any, Dict, List

from xsdata.codegen.mappers.mixins import RawDocumentMapper
from xsdata.codegen.models import AttrType, Class
from xsdata.codegen.utils import ClassUtils
from xsdata.models.enums import Tag


class DictMapper(RawDocumentMapper):
    """Map a dictionary to classes.

    This mapper is used to build classes from raw json documents.
    """

    @classmethod
    def map(cls, data: Dict, name: str, location: str) -> List[Class]:
        """Map a dictionary to classes.

        Args:
            data: The json resource data
            name: The main resource name
            location: The resource location

        Returns:
            The list of classes.
        """
        target = cls.build_class(data, name)
        return list(ClassUtils.flatten(target, f"{location}/{name}"))

    @classmethod
    def build_class(cls, data: Dict, name: str) -> Class:
        """Build a class from a data dictionary.

        Args:
            data: The json resource data
            name: The main resource name

        Returns:
            The list of classes.
        """
        target = Class(qname=name, tag=Tag.ELEMENT, location="")

        for key, value in data.items():
            cls.build_class_attribute(target, key, value)

        return target

    @classmethod
    def build_class_attribute(cls, target: Class, name: str, value: Any):
        """Build a class attr.

        Args:
            target: The target class instance
            name: The attr name
            value: The data value to extract types and restrictions.
        """
        if isinstance(value, list):
            if not value:
                cls.build_class_attribute(target, name, None)
                target.attrs[-1].restrictions.max_occurs = sys.maxsize
            else:
                for val in value:
                    cls.build_class_attribute(target, name, val)
                    target.attrs[-1].restrictions.max_occurs = sys.maxsize
        else:
            if isinstance(value, dict):
                inner = cls.build_class(value, name)
                attr_type = AttrType(qname=inner.qname, forward=True)
                target.inner.append(inner)
            else:
                attr_type = cls.build_attr_type(name, value)

            cls.build_attr(target, name, attr_type)
