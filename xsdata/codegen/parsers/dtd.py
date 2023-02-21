import io
from typing import Any
from typing import List
from typing import Optional

from xsdata.exceptions import ParserError
from xsdata.models.dtd import Dtd
from xsdata.models.dtd import DtdAttribute
from xsdata.models.dtd import DtdAttributeDefault
from xsdata.models.dtd import DtdAttributeType
from xsdata.models.dtd import DtdContent
from xsdata.models.dtd import DtdContentOccur
from xsdata.models.dtd import DtdContentType
from xsdata.models.dtd import DtdElement
from xsdata.models.dtd import DtdElementType
from xsdata.models.enums import Namespace


class DtdParser:
    @classmethod
    def parse(cls, source: Any, location: str) -> Dtd:
        try:
            from lxml import etree

            dtd = etree.DTD(io.BytesIO(source))
        except ImportError:
            raise ParserError("DtdParser requires lxml to run.")

        elements = list(map(cls.build_element, dtd.iterelements()))
        return Dtd(elements=elements, location=location)

    @classmethod
    def build_element(cls, element: Any) -> DtdElement:
        content = cls.build_content(element.content)
        attributes = list(map(cls.build_attribute, element.iterattributes()))
        ns_map = cls.build_ns_map(element.prefix, attributes)
        return DtdElement(
            name=element.name,
            prefix=element.prefix,
            type=DtdElementType(element.type),
            content=content,
            attributes=attributes,
            ns_map=ns_map,
        )

    @classmethod
    def build_content(cls, content: Any) -> Optional[DtdContent]:
        if not content:
            return None

        return DtdContent(
            name=content.name,
            occur=DtdContentOccur(content.occur),
            type=DtdContentType(content.type),
            left=cls.build_content(content.left),
            right=cls.build_content(content.right),
        )

    @classmethod
    def build_attribute(cls, attribute: Any) -> DtdAttribute:
        return DtdAttribute(
            prefix=attribute.prefix,
            name=attribute.name,
            type=DtdAttributeType(attribute.type),
            default=DtdAttributeDefault(attribute.default),
            default_value=attribute.default_value,
            values=attribute.values(),
        )

    @classmethod
    def build_ns_map(cls, prefix: str, attributes: List[DtdAttribute]) -> dict:
        ns_map = {ns.prefix: ns.uri for ns in Namespace.common()}

        for attribute in list(attributes):
            if not attribute.default_value:
                continue

            if attribute.prefix == "xmlns":
                ns_map[attribute.name] = attribute.default_value
                attributes.remove(attribute)
            elif attribute.name == "xmlns":
                ns_map[prefix] = attribute.default_value
                attributes.remove(attribute)

        return ns_map
