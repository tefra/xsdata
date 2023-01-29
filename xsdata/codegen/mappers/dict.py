import sys
from typing import Any
from typing import Dict
from typing import List

from xsdata.codegen.mappers.element import ElementMapper
from xsdata.codegen.models import AttrType
from xsdata.codegen.models import Class
from xsdata.codegen.utils import ClassUtils
from xsdata.models.enums import Tag


class DictMapper:
    """Map a dictionary to classes, extensions and attributes."""

    @classmethod
    def map(cls, data: Dict, name: str, location: str) -> List[Class]:
        """Convert a dictionary to a list of codegen classes."""
        target = cls.build_class(data, name)
        return list(ClassUtils.flatten(target, f"{location}/{name}"))

    @classmethod
    def build_class(cls, data: Dict, name: str) -> Class:
        target = Class(qname=name, tag=Tag.ELEMENT, location="")

        for key, value in data.items():
            cls.build_class_attribute(target, key, value)

        return target

    @classmethod
    def build_class_attribute(cls, target: Class, name: str, value: Any):
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
                attr_type = ElementMapper.build_attribute_type(name, value)

            ElementMapper.build_attribute(target, name, attr_type)
