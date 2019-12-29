from enum import Enum
from typing import Optional

from lxml import etree

from xsdata.utils.text import capitalize, split


class Namespace:
    SCHEMA = "http://www.w3.org/2001/XMLSchema"
    XML = "http://www.w3.org/XML/1998/namespace"


class FormType(Enum):
    QUALIFIED = "qualified"
    UNQUALIFIED = "unqualified"


class XSDType(Enum):
    ANY_URI = ("xs:anyURI", str)
    ANY_SIMPLE_TYPE = ("xs:anySimpleType", str)
    BASE64_BINARY = ("xs:base64Binary", str)
    BOOLEAN = ("xs:boolean", bool)
    BYTE = ("xs:byte", int)
    DATE = ("xs:date", str)
    DATE_TIME = ("xs:dateTime", str)
    DECIMAL = ("xs:decimal", float)
    DERIVATION_CONTROL = ("xs:derivationControl", str)
    DOUBLE = ("xs:double", float)
    DURATION = ("xs:duration", str)
    ENTITIES = ("xs:ENTITIES", int)
    ENTITY = ("xs:ENTITY", int)
    FLOAT = ("xs:float", float)
    G_DAY = ("xs:gDay", str)
    G_MONTH = ("xs:gMonth", str)
    G_MONTH_DAY = ("xs:gMonthDay", str)
    G_YEAR = ("xs:gYear", str)
    G_YEAR_MONTH = ("xs:gYearMonth", str)
    HEX_BINARY = ("xs:hexBinary", str)
    ID = ("xs:ID", str)
    IDREF = ("xs:IDREF", str)
    IDREFS = ("xs:IDREFS", str)
    INT = ("xs:int", int)
    INTEGER = ("xs:integer", int)
    LANGUAGE = ("xs:language", str)
    LONG = ("xs:long", int)
    NAME = ("xs:Name", str)
    NCNAME = ("xs:NCName", str)
    NEGATIVE_INTEGER = ("xs:negativeInteger", int)
    NMTOKEN = ("xs:NMTOKEN", str)
    NMTOKENS = ("xs:NMTOKENS", str)
    NON_NEGATIVE_INTEGER = ("xs:nonNegativeInteger", int)
    NON_POSITIVE_INTEGER = ("xs:nonPositiveInteger", int)
    NORMALIZED_STRING = ("xs:normalizedString", str)
    NOTATION = ("xs:NOTATION", str)
    POSITIVE_INTEGER = ("xs:positiveInteger", int)
    QNAME = ("xs:QName", str)
    SHORT = ("xs:short", int)
    SIMPLE_DERIVATION_SET = ("xs:simpleDerivationSet", str)
    STRING = ("xs:string", str)
    TIME = ("xs:time", str)
    TOKEN = ("xs:token", str)
    UNSIGNED_BYTE = ("xs:unsignedByte", int)
    UNSIGNED_INT = ("xs:unsignedInt", int)
    UNSIGNED_LONG = ("xs:unsignedLong", int)
    UNSIGNED_SHORT = ("xs:unsignedShort", int)

    def __init__(self, code: str, local: type):
        self.code = code
        self.local = local

    @classmethod
    def get_enum(cls, code: str) -> Optional["XSDType"]:
        prefix, suffix = split(code)
        return __XSDType__.get("xs:" + suffix) if prefix else None

    @classmethod
    def get_local(cls, code: str) -> Optional[str]:
        enum = cls.get_enum(code)
        return enum.local.__name__ if enum else None

    @classmethod
    def codes(cls):
        return list(__XSDType__.keys())


__XSDType__ = {xsd.code: xsd for xsd in XSDType}


class EventType:
    START = "start"
    END = "end"


class TagType(Enum):
    ALL = "all"
    ANNOTATION = "annotation"
    ANY = "any"
    ANY_ATTRIBUTE = "anyAttribute"
    APPINFO = "appinfo"
    ATTRIBUTE = "attribute"
    ATTRIBUTEGROUP = "attributeGroup"
    CHOICE = "choice"
    COMPLEX_CONTENT = "complexContent"
    COMPLEX_TYPE = "complexType"
    DOCUMENTATION = "documentation"
    ELEMENT = "element"
    EXTENSION = "extension"
    FIELD = "field"
    GROUP = "group"
    IMPORT = "import"
    INCLUDE = "include"
    KEY = "key"
    KEYREF = "keyref"
    LIST = "list"
    NOTATION = "notation"
    REDEFINE = "redefine"
    RESTRICTION = "restriction"
    SCHEMA = "schema"
    SELECTOR = "selector"
    SEQUENCE = "sequence"
    SIMPLE_CONTENT = "simpleContent"
    SIMPLE_TYPE = "simpleType"
    UNION = "union"
    UNIQUE = "unique"

    # Restrictions
    ENUMERATION = "enumeration"
    FRACTION_DIGITS = "fractionDigits"
    LENGTH = "length"
    MAX_EXCLUSIVE = "maxExclusive"
    MAX_INCLUSIVE = "maxInclusive"
    MAX_LENGTH = "maxLength"
    MIN_EXCLUSIVE = "minExclusive"
    MIN_INCLUSIVE = "minInclusive"
    MIN_LENGTH = "minLength"
    PATTERN = "pattern"
    TOTAL_DIGITS = "totalDigits"
    WHITE_SPACE = "whiteSpace"

    @property
    def qname(self):
        """Qualified name: {namespace}tag."""
        return etree.QName(Namespace.SCHEMA, self.value)

    @property
    def cname(self):
        """Class name."""
        return capitalize(self.value)

    @classmethod
    def qnames(cls):
        """All types indexed by their qname."""
        return {tag.qname: tag for tag in TagType}


class UseType(Enum):
    OPTIONAL = "optional"
    PROHIBITED = "prohibited"
    REQUIRED = "required"


class ProcessType(Enum):
    LAX = "lax"
    SKIP = "skip"
    STRICT = "strict"
