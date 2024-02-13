import io
from typing import Any, Dict, List, Optional

from xsdata.exceptions import ParserError
from xsdata.models.dtd import (
    Dtd,
    DtdAttribute,
    DtdAttributeDefault,
    DtdAttributeType,
    DtdContent,
    DtdContentOccur,
    DtdContentType,
    DtdElement,
    DtdElementType,
)
from xsdata.models.enums import Namespace


class DtdParser:
    """Document type definition parser.

    The parser requires lxml package to be installed.
    """

    @classmethod
    def parse(cls, source: bytes, location: str) -> Dtd:
        """Parse the input source bytes object into a dtd instance.

        Args:
            source: The source bytes object to parse
            location: The source location uri

        Returns:
            A dtd instance representing the parsed content.
        """
        try:
            from lxml import etree

            dtd = etree.DTD(io.BytesIO(source))
        except ImportError:
            raise ParserError("DtdParser requires lxml to run.")

        elements = list(map(cls.build_element, dtd.iterelements()))
        return Dtd(elements=elements, location=location)

    @classmethod
    def build_element(cls, element: Any) -> DtdElement:
        """Build a dtd element from the lxml element.

        Args:
            element: The lxml dtd element instance

        Returns:
            The converted xsdata dtd element instance.
        """
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
        """Build a dtd content instance from the lxml content.

        Args:
            content: The lxml content instance

        Returns:
            The converted xsdata dtd content instance, or None if the content is empty.
        """
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
        """Build a dtd attribute instance from the lxml instance.

        Args:
            attribute: The lxml attribute instance

        Returns:
            The converted xsdata dtd attribute instance.
        """
        return DtdAttribute(
            prefix=attribute.prefix,
            name=attribute.name,
            type=DtdAttributeType(attribute.type),
            default=DtdAttributeDefault(attribute.default),
            default_value=attribute.default_value,
            values=attribute.values(),
        )

    @classmethod
    def build_ns_map(cls, prefix: str, attributes: List[DtdAttribute]) -> Dict:
        """Build the dtd element namespace prefix-URI map.

        It also adds common namespaces like xs, xsi, xlink and xml.

        Args:
            prefix: The element namespace prefix
            attributes: Element attributes, to extract any xmlns keys

        Returns:
            The element namespace prefix-URI map.
        """
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
