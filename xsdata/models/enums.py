from enum import Enum
from typing import Optional

from lxml import etree

from xsdata.utils.text import capitalize


class Namespace:
    SCHEMA = "http://www.w3.org/2001/XMLSchema"
    XML = "http://www.w3.org/XML/1998/namespace"


class FormType(Enum):
    QUALIFIED = "qualified"
    UNQUALIFIED = "unqualified"


class DataType(Enum):
    ANY_URI = ("anyURI", str)
    ANY_SIMPLE_TYPE = ("anySimpleType", str)
    BASE = ("base", str)
    BASE64_BINARY = ("base64Binary", str)
    BOOLEAN = ("boolean", bool)
    BYTE = ("byte", int)
    DATE = ("date", str)
    DATE_TIME = ("dateTime", str)
    DECIMAL = ("decimal", float)
    DERIVATION_CONTROL = ("derivationControl", str)
    DOUBLE = ("double", float)
    DURATION = ("duration", str)
    ENTITIES = ("ENTITIES", int)
    ENTITY = ("ENTITY", int)
    FLOAT = ("float", float)
    G_DAY = ("gDay", str)
    G_MONTH = ("gMonth", str)
    G_MONTH_DAY = ("gMonthDay", str)
    G_YEAR = ("gYear", str)
    G_YEAR_MONTH = ("gYearMonth", str)
    HEX_BINARY = ("hexBinary", str)
    ID = ("ID", str)
    IDREF = ("IDREF", str)
    IDREFS = ("IDREFS", str)
    INT = ("int", int)
    INTEGER = ("integer", int)
    LANG = ("lang", str)
    LANGUAGE = ("language", str)
    LONG = ("long", int)
    NAME = ("Name", str)
    NCNAME = ("NCName", str)
    NEGATIVE_INTEGER = ("negativeInteger", int)
    NMTOKEN = ("NMTOKEN", str)
    NMTOKENS = ("NMTOKENS", str)
    NON_NEGATIVE_INTEGER = ("nonNegativeInteger", int)
    NON_POSITIVE_INTEGER = ("nonPositiveInteger", int)
    NORMALIZED_STRING = ("normalizedString", str)
    NOTATION = ("NOTATION", str)
    POSITIVE_INTEGER = ("positiveInteger", int)
    QNAME = ("QName", str)
    SHORT = ("short", int)
    SIMPLE_DERIVATION_SET = ("simpleDerivationSet", str)
    STRING = ("string", str)
    TIME = ("time", str)
    TOKEN = ("token", str)
    UNSIGNED_BYTE = ("unsignedByte", int)
    UNSIGNED_INT = ("unsignedInt", int)
    UNSIGNED_LONG = ("unsignedLong", int)
    UNSIGNED_SHORT = ("unsignedShort", int)

    def __init__(self, code: str, local: type):
        self.code = code
        self.local = local

    @classmethod
    def get_enum(cls, code: str) -> Optional["DataType"]:
        return __XSDType__.get(code) if code else None

    @classmethod
    def get_local(cls, code: str) -> Optional[str]:
        enum = cls.get_enum(code)
        return enum.local.__name__ if enum else None

    @classmethod
    def codes(cls):
        return list(__XSDType__.keys())


__XSDType__ = {xsd.code: xsd for xsd in DataType}


class EventType:
    START = "start"
    END = "end"


class TagType(Enum):
    ALL = "all"
    ANNOTATION = "annotation"
    ANY = "any"
    ANY_ATTRIBUTE = "anyAttribute"
    APPINFO = "appinfo"
    ASSERTION = "assertion"
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
