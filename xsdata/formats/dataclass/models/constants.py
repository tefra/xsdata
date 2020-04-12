from xsdata.formats.dataclass.models.elements import XmlAttribute
from xsdata.formats.dataclass.models.elements import XmlAttributes
from xsdata.formats.dataclass.models.elements import XmlElement
from xsdata.formats.dataclass.models.elements import XmlText
from xsdata.formats.dataclass.models.elements import XmlWildcard


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
