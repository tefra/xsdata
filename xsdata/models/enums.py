from decimal import Decimal
from enum import Enum
from typing import Iterable
from typing import Optional

from lxml.etree import QName


class Namespace(Enum):
    SCHEMA = "http://www.w3.org/2001/XMLSchema"
    XML = "http://www.w3.org/XML/1998/namespace"
    INSTANCE = "http://www.w3.org/2001/XMLSchema-instance"
    XLINK = "http://www.w3.org/1999/xlink"

    @property
    def uri(self):
        return self.value

    @property
    def prefix(self):
        return self.name.lower()


class FormType(Enum):
    QUALIFIED = "qualified"
    UNQUALIFIED = "unqualified"


class DataType(Enum):
    # xsdata custom any type
    QMAP = ("qmap", (QName, str))
    OBJECT = ("object", object)

    # xsd and xml data types
    ANY_URI = ("anyURI", str)
    ANY_SIMPLE_TYPE = ("anySimpleType", str)
    BASE = ("base", str)
    BASE64_BINARY = ("base64Binary", str)
    BOOLEAN = ("boolean", bool)
    BYTE = ("byte", int)
    DATE = ("date", str)
    DATE_TIME = ("dateTime", str)
    DATE_TIMESTAMP = ("dateTimeStamp", str)
    DAY_TIME_DURATION = ("dayTimeDuration", str)
    YEAR_MONTH_DURATION = ("yearMonthDuration", str)
    DECIMAL = ("decimal", Decimal)
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

    @property
    def xml_prefixed(self):
        return f"xml:{self.code}"

    @property
    def local_name(self) -> str:
        if isinstance(self.local, Iterable):
            return ", ".join([local.__name__ for local in self.local])
        else:
            return self.local.__name__

    @classmethod
    def get_enum(cls, code: str) -> Optional["DataType"]:
        return __XSDType__.get(code) if code else None


__XSDType__ = {xsd.code: xsd for xsd in DataType}


class EventType:
    START = "start"
    END = "end"


class TagType:
    ALL = "All"
    ANNOTATION = "Annotation"
    ANY = "Any"
    ANY_ATTRIBUTE = "AnyAttribute"
    APPINFO = "Appinfo"
    ASSERTION = "Assertion"
    ATTRIBUTE = "Attribute"
    ATTRIBUTEGROUP = "AttributeGroup"
    CHOICE = "Choice"
    COMPLEX_CONTENT = "ComplexContent"
    COMPLEX_TYPE = "ComplexType"
    DOCUMENTATION = "Documentation"
    ELEMENT = "Element"
    EXTENSION = "Extension"
    FIELD = "Field"
    GROUP = "Group"
    IMPORT = "Import"
    INCLUDE = "Include"
    KEY = "Key"
    KEYREF = "Keyref"
    LIST = "List"
    NOTATION = "Notation"
    REDEFINE = "Redefine"
    RESTRICTION = "Restriction"
    SCHEMA = "Schema"
    SELECTOR = "Selector"
    SEQUENCE = "Sequence"
    SIMPLE_CONTENT = "SimpleContent"
    SIMPLE_TYPE = "SimpleType"
    UNION = "Union"
    UNIQUE = "Unique"

    # Restrictions
    ENUMERATION = "Enumeration"
    FRACTION_DIGITS = "FractionDigits"
    LENGTH = "Length"
    MAX_EXCLUSIVE = "MaxExclusive"
    MAX_INCLUSIVE = "MaxInclusive"
    MAX_LENGTH = "MaxLength"
    MIN_EXCLUSIVE = "MinExclusive"
    MIN_INCLUSIVE = "MinInclusive"
    MIN_LENGTH = "MinLength"
    PATTERN = "Pattern"
    TOTAL_DIGITS = "TotalDigits"
    WHITE_SPACE = "WhiteSpace"


class UseType(Enum):
    OPTIONAL = "optional"
    PROHIBITED = "prohibited"
    REQUIRED = "required"


class ProcessType(Enum):
    LAX = "lax"
    SKIP = "skip"
    STRICT = "strict"
