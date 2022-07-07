import enum
from dataclasses import dataclass
from typing import Dict
from typing import List
from typing import Optional

from xsdata.models.enums import DataType
from xsdata.utils.namespaces import build_qname


class DtdElementType(enum.Enum):
    UNDEFINED = "undefined"
    EMPTY = "empty"
    ANY = "any"
    MIXED = "mixed"
    ELEMENT = "element"


class DtdAttributeDefault(enum.Enum):
    REQUIRED = "required"
    IMPLIED = "implied"
    FIXED = "fixed"
    NONE = "none"


class DtdAttributeType(enum.Enum):
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
    PCDATA = "pcdata"
    ELEMENT = "element"
    SEQ = "seq"
    OR = "or"


class DtdContentOccur(enum.Enum):
    ONCE = "once"
    OPT = "opt"
    MULT = "mult"
    PLUS = "plus"


@dataclass
class DtdAttribute:
    name: str
    prefix: Optional[str]
    type: DtdAttributeType
    default: DtdAttributeDefault
    default_value: Optional[str]
    values: List[str]

    @property
    def data_type(self) -> DataType:
        return DataType.from_code(self.type.value.lower())


@dataclass
class DtdContent:
    name: str
    type: DtdContentType
    occur: DtdContentOccur
    left: Optional["DtdContent"]
    right: Optional["DtdContent"]


@dataclass
class DtdElement:
    name: str
    type: DtdElementType
    prefix: Optional[str]
    content: Optional[DtdContent]
    attributes: List[DtdAttribute]
    ns_map: Dict

    @property
    def qname(self) -> str:
        namespace = self.ns_map.get(self.prefix)
        return build_qname(namespace, self.name)


@dataclass
class Dtd:
    location: str
    elements: List[DtdElement]
