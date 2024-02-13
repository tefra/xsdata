import enum
from dataclasses import dataclass
from typing import Dict, List, Optional

from xsdata.models.enums import DataType
from xsdata.utils.namespaces import build_qname


class DtdElementType(enum.Enum):
    """DTD Element type enumeration."""

    UNDEFINED = "undefined"
    EMPTY = "empty"
    ANY = "any"
    MIXED = "mixed"
    ELEMENT = "element"


class DtdAttributeDefault(enum.Enum):
    """DTD Attribute default enumeration."""

    REQUIRED = "required"
    IMPLIED = "implied"
    FIXED = "fixed"
    NONE = "none"


class DtdAttributeType(enum.Enum):
    """DTD Attribute type enumeration."""

    CDATA = "cdata"
    ID = "id"
    IDREF = "idref"
    IDREFS = "idrefs"
    ENTITY = "entity"
    ENTITIES = "entities"
    NMTOKEN = "nmtoken"
    NMTOKENS = "nmtokens"
    ENUMERATION = "enumeration"
    NOTATION = "notation"


class DtdContentType(enum.Enum):
    """DTD Content type enumeration."""

    PCDATA = "pcdata"
    ELEMENT = "element"
    SEQ = "seq"
    OR = "or"


class DtdContentOccur(enum.Enum):
    """DTD Content occur enumeration."""

    ONCE = "once"
    OPT = "opt"
    MULT = "mult"
    PLUS = "plus"


@dataclass
class DtdAttribute:
    """DTD Attribute model representation.

    Args:
        name: The attribute name
        prefix: The attribute namespace prefix
        type: The attribute type
        default: The attribute default type
        default_value: The attribute default value
        values: The available choices as value
    """

    name: str
    prefix: Optional[str]
    type: DtdAttributeType
    default: DtdAttributeDefault
    default_value: Optional[str]
    values: List[str]

    @property
    def data_type(self) -> DataType:
        """Return the data type instance from the attribute type."""
        return DataType.from_code(self.type.value.lower())


@dataclass
class DtdContent:
    """DTD Content model representation.

    Args:
        name: The content name
        type: The content type
        occur: The content occur type
        left: The parent content
        right: The child content
    """

    name: str
    type: DtdContentType
    occur: DtdContentOccur
    left: Optional["DtdContent"]
    right: Optional["DtdContent"]


@dataclass
class DtdElement:
    """DTD Element model representation.

    Args:
        name: The element name
        type: The element type
        prefix: The element namespace prefix
        content: The element content
        attributes: The element attribute list
        ns_map: The namespace prefix-URI map
    """

    name: str
    type: DtdElementType
    prefix: Optional[str]
    content: Optional[DtdContent]
    attributes: List[DtdAttribute]
    ns_map: Dict

    @property
    def qname(self) -> str:
        """Return the element qualified name."""
        namespace = self.ns_map.get(self.prefix)
        return build_qname(namespace, self.name)


@dataclass
class Dtd:
    """The DTD Document model representation.

    Args:
        location: The source location URI
        elements: The list of included elements
    """

    location: str
    elements: List[DtdElement]
