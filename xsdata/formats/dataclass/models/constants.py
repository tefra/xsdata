from xsdata.formats.dataclass.models.context import XmlAttribute
from xsdata.formats.dataclass.models.context import XmlAttributes
from xsdata.formats.dataclass.models.context import XmlElement
from xsdata.formats.dataclass.models.context import XmlText
from xsdata.formats.dataclass.models.context import XmlWildcard


class XmlType:
    TEXT = "Text"
    ELEMENT = "Element"
    WILDCARD = "Wildcard"
    ATTRIBUTE = "Attribute"
    ATTRIBUTES = "Attributes"

    @classmethod
    def to_xml_class(cls, name):
        if name == XmlType.ELEMENT:
            return XmlElement
        elif name == XmlType.WILDCARD:
            return XmlWildcard
        elif name == XmlType.ATTRIBUTE:
            return XmlAttribute
        elif name == XmlType.ATTRIBUTES:
            return XmlAttributes
        else:
            return XmlText
