from enum import Enum
from typing import Optional

from lxml import etree

XMLSchema = "http://www.w3.org/2001/XMLSchema"


class XSDType(Enum):
    ANY_URI = ("xs:anyURI", str)
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
        pos = code.find(":")
        if pos == -1:
            return None

        return __XSDType__.get("xs:" + code[pos + 1:])

    @classmethod
    def get_local(cls, code: str) -> Optional[str]:
        enum = cls.get_enum(code)
        return enum.local.__name__ if enum else None


__XSDType__ = {xsd.code: xsd for xsd in XSDType}


class Event:
    START = "start"
    END = "end"


class Tag(Enum):
    ALL = "all"
    ANNOTATION = "annotation"
    ANY = "any"
    ANYATTRIBUTE = "anyAttribute"
    APPINFO = "appinfo"
    ATTRIBUTE = "attribute"
    ATTRIBUTEGROUP = "attributeGroup"
    CHOICE = "choice"
    COMPLEXCONTENT = "complexContent"
    COMPLEXTYPE = "complexType"
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
    SIMPLECONTENT = "simpleContent"
    SIMPLETYPE = "simpleType"
    UNION = "union"
    UNIQUE = "unique"

    # Restrictions
    ENUMERATION = "enumeration"
    FRACTIONDIGITS = "fractionDigits"
    LENGTH = "length"
    MAXEXCLUSIVE = "maxExclusive"
    MAXINCLUSIVE = "maxInclusive"
    MAXLENGTH = "maxLength"
    MINEXCLUSIVE = "minExclusive"
    MININCLUSIVE = "minInclusive"
    MINLENGTH = "minLength"
    PATTERN = "pattern"
    TOTALDIGITS = "totalDigits"
    WHITESPACE = "whiteSpace"

    @property
    def qname(self):
        return etree.QName(XMLSchema, self.value)
