import sys
from typing import Any
from typing import Dict
from typing import Iterator
from typing import List
from typing import Optional

from xsdata.codegen.models import Attr
from xsdata.codegen.models import AttrType
from xsdata.codegen.models import Class
from xsdata.codegen.models import Extension
from xsdata.codegen.models import Restrictions
from xsdata.models.dtd import Dtd
from xsdata.models.dtd import DtdAttribute
from xsdata.models.dtd import DtdAttributeDefault
from xsdata.models.dtd import DtdAttributeType
from xsdata.models.dtd import DtdContent
from xsdata.models.dtd import DtdContentOccur
from xsdata.models.dtd import DtdContentType
from xsdata.models.dtd import DtdElement
from xsdata.models.dtd import DtdElementType
from xsdata.models.enums import DataType
from xsdata.models.enums import Tag
from xsdata.utils.constants import DEFAULT_ATTR_NAME


class DtdMapper:
    @classmethod
    def map(cls, dtd: Dtd) -> Iterator[Class]:
        for element in dtd.elements:
            yield cls.build_class(element, dtd.location)

    @classmethod
    def build_class(cls, element: DtdElement, location: str) -> Class:
        target = Class(
            qname=element.qname,
            ns_map=element.ns_map,
            tag=Tag.ELEMENT,
            location=location,
        )

        cls.build_attributes(target, element)
        cls.build_elements(target, element)

        return target

    @classmethod
    def build_attributes(cls, target: Class, element: DtdElement):
        for attribute in element.attributes:
            cls.build_attribute(target, attribute)

    @classmethod
    def build_attribute(cls, target: Class, attribute: DtdAttribute):
        attr_type = cls.build_attribute_type(target, attribute)
        attr = Attr(
            name=attribute.name,
            namespace=target.ns_map.get(attribute.prefix),
            tag=Tag.ATTRIBUTE,
            types=[attr_type],
        )

        cls.build_attribute_restrictions(
            attr, attribute.default, attribute.default_value
        )

        attr.index = len(target.attrs)
        target.attrs.append(attr)

    @classmethod
    def build_attribute_restrictions(
        cls, attr: Attr, default: DtdAttributeDefault, default_value: Optional[str]
    ):
        attr.restrictions.max_occurs = 1
        if default == DtdAttributeDefault.REQUIRED:
            attr.restrictions.min_occurs = 1
        elif default == DtdAttributeDefault.IMPLIED:
            attr.restrictions.min_occurs = 0
        elif default == DtdAttributeDefault.FIXED:
            attr.fixed = True
            attr.restrictions.min_occurs = 1
            attr.default = default_value
        elif default_value is not None:
            attr.restrictions.min_occurs = 1
            attr.default = default_value
        else:
            attr.restrictions.min_occurs = 0

    @classmethod
    def build_attribute_type(cls, target: Class, attribute: DtdAttribute) -> AttrType:
        if attribute.type == DtdAttributeType.ENUMERATION:
            cls.build_enumeration(target, attribute.name, attribute.values)
            return AttrType(qname=attribute.name, forward=True)

        return AttrType(qname=str(attribute.data_type), native=True)

    @classmethod
    def build_elements(cls, target: Class, element: DtdElement):
        # "undefined", "empty", "any", "mixed", or "element";
        if element.type == DtdElementType.ELEMENT and element.content:
            cls.build_content(target, element.content)
        elif element.type == DtdElementType.MIXED and element.content:
            cls.build_mixed_content(target, element.content)
        elif element.type == DtdElementType.ANY:
            cls.build_extension(target, DataType.ANY_TYPE)

    @classmethod
    def build_mixed_content(cls, target: Class, content: DtdContent):
        if content.left and content.left.type == DtdContentType.PCDATA:
            target.mixed = True
            content.left = None
        elif content.right and content.right.type == DtdContentType.PCDATA:
            target.mixed = True
            content.right = None

        target.tag = Tag.COMPLEX_TYPE
        cls.build_content(target, content)

    @classmethod
    def build_extension(cls, target: Class, data_type: DataType):
        ext_type = AttrType(qname=str(data_type), native=True)
        extension = Extension(
            tag=Tag.EXTENSION, type=ext_type, restrictions=Restrictions()
        )
        target.extensions.append(extension)

    @classmethod
    def build_content(cls, target: Class, content: DtdContent, **kwargs: Any):
        content_type = content.type
        if content_type == DtdContentType.ELEMENT:
            restrictions = cls.build_restrictions(content.occur, **kwargs)
            cls.build_element(target, content.name, restrictions)
        elif content_type == DtdContentType.SEQ:
            cls.build_content_tree(target, content, **kwargs)
        elif content_type == DtdContentType.OR:
            params = cls.build_occurs(content.occur)
            params.update(
                {
                    "choice": id(content),
                    "min_occurs": 0,
                }
            )
            params.update(**kwargs)
            cls.build_content_tree(target, content, **params)
        else:  # content_type == DtdContentType.PCDATA:
            restrictions = cls.build_restrictions(content.occur, **kwargs)
            cls.build_value(target, restrictions)

    @classmethod
    def build_content_tree(cls, target: Class, content: DtdContent, **kwargs: Any):
        if content.left:
            cls.build_content(target, content.left, **kwargs)

        if content.right:
            cls.build_content(target, content.right, **kwargs)

    @classmethod
    def build_occurs(cls, occur: DtdContentOccur) -> Dict:
        if occur == DtdContentOccur.ONCE:
            min_occurs = 1
            max_occurs = 1
        elif occur == DtdContentOccur.OPT:
            min_occurs = 0
            max_occurs = 1
        elif occur == DtdContentOccur.MULT:
            min_occurs = 0
            max_occurs = sys.maxsize
        else:  # occur == DtdContentOccur.PLUS:
            min_occurs = 1
            max_occurs = sys.maxsize

        return {
            "min_occurs": min_occurs,
            "max_occurs": max_occurs,
        }

    @classmethod
    def build_restrictions(cls, occur: DtdContentOccur, **kwargs: Any) -> Restrictions:
        params = cls.build_occurs(occur)
        params.update(kwargs)

        return Restrictions(**params)

    @classmethod
    def build_element(cls, target: Class, name: str, restrictions: Restrictions):
        types = AttrType(qname=name, native=False)
        attr = Attr(
            name=name, tag=Tag.ELEMENT, types=[types], restrictions=restrictions.clone()
        )
        attr.index = len(target.attrs)
        target.attrs.append(attr)

    @classmethod
    def build_value(cls, target: Class, restrictions: Restrictions):
        types = AttrType(qname=str(DataType.STRING), native=True)
        attr = Attr(
            name=DEFAULT_ATTR_NAME,
            tag=Tag.EXTENSION,
            types=[types],
            restrictions=restrictions.clone(),
        )
        attr.index = len(target.attrs)
        target.attrs.append(attr)

    @classmethod
    def build_enumeration(cls, target: Class, name: str, values: List[str]):
        inner = Class(qname=name, tag=Tag.SIMPLE_TYPE, location=target.location)
        attr_type = AttrType(qname=str(DataType.STRING), native=True)

        for value in values:
            inner.attrs.append(
                Attr(
                    fixed=True,
                    default=value,
                    name=value,
                    tag=Tag.ENUMERATION,
                    types=[attr_type.clone()],
                )
            )

        target.inner.append(inner)
