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
        return __mapped_xml_type_vars__.get(name, XmlText)


__mapped_xml_type_vars__ = {
    XmlType.ELEMENT: XmlElement,
    XmlType.WILDCARD: XmlWildcard,
    XmlType.ATTRIBUTE: XmlAttribute,
    XmlType.ATTRIBUTES: XmlAttributes,
}
