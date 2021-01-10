from decimal import Decimal
from enum import Enum
from pathlib import Path
from typing import Any
from typing import Optional
from xml.etree.ElementTree import QName

from xsdata.models.datatype import XmlDate
from xsdata.models.datatype import XmlDateTime
from xsdata.models.datatype import XmlDuration
from xsdata.models.datatype import XmlPeriod
from xsdata.models.datatype import XmlTime

COMMON_SCHEMA_DIR = Path(__file__).absolute().parent.parent.joinpath("schemas/")


class Namespace(Enum):
    """Common namespaces."""

    XS = ("http://www.w3.org/2001/XMLSchema", "xs")
    XML = ("http://www.w3.org/XML/1998/namespace", "xml")
    XSI = ("http://www.w3.org/2001/XMLSchema-instance", "xsi")
    XLINK = ("http://www.w3.org/1999/xlink", "xlink")
    XHTML = ("http://www.w3.org/1999/xhtml", "xhtml")
    SOAP11 = ("http://schemas.xmlsoap.org/wsdl/soap/", "soap")
    SOAP12 = ("http://schemas.xmlsoap.org/wsdl/soap12/", "soap12")
    SOAP_ENV = ("http://schemas.xmlsoap.org/soap/envelope/", "soap-env")

    def __init__(self, uri: str, prefix: str):
        self.uri = uri
        self.prefix = prefix

    @property
    def location(self) -> Optional[str]:
        local_path = COMMON_SCHEMA_DIR.joinpath(f"{self.prefix}.xsd")
        return local_path.as_uri() if local_path.exists() else None

    @classmethod
    def get_enum(cls, uri: Optional[str]) -> Optional["Namespace"]:
        return __STANDARD_NAMESPACES__.get(uri) if uri else None


__STANDARD_NAMESPACES__ = {ns.uri: ns for ns in Namespace}


class QNames:
    """Common qualified names."""

    XSI_NIL = f"{{{Namespace.XSI.uri}}}nil"
    XSI_TYPE = f"{{{Namespace.XSI.uri}}}type"
    XSI_SCHEMA_LOCATION = f"{{{Namespace.XSI.uri}}}schemaLocation"
    XSI_NO_NAMESPACE_SCHEMA_LOCATION = (
        f"{{{Namespace.XSI.uri}}}noNamespaceSchemaLocation"
    )


class NamespaceType:
    """
    Wildcard elements/attributes namespace types.

    :cvar ANY_NS: elements from any namespace is allowed
    :cvar OTHER_NS: elements from any namespace except the parent element's namespace
    :cvar LOCAL_NS: elements must come from no namespace
    :cvar TARGET_NS: elements from the namespace of the parent element can be present
    """

    ANY_NS = "##any"
    OTHER_NS = "##other"
    LOCAL_NS = "##local"
    TARGET_NS = "##targetNamespace"


class FormType(Enum):
    """Element/Attribute form types."""

    QUALIFIED = "qualified"
    UNQUALIFIED = "unqualified"


class Mode(Enum):
    """OpenContent mode types."""

    NONE = "none"
    SUFFIX = "suffix"
    INTERLEAVE = "interleave"


class DataType(Enum):
    """Xml and Schema data types to native python."""

    ANY_ATOMIC_TYPE = ("anyAtomicType", str)
    ANY_URI = ("anyURI", str)
    ANY_SIMPLE_TYPE = ("anySimpleType", object)
    ANY_TYPE = ("anyType", object)
    BASE = ("base", str)
    BASE64_BINARY = ("base64Binary", bytes)
    BOOLEAN = ("boolean", bool)
    BYTE = ("byte", int)
    DATE = ("date", XmlDate)
    DATE_TIME = ("dateTime", XmlDateTime)
    DATE_TIMESTAMP = ("dateTimeStamp", XmlDateTime)
    DAY_TIME_DURATION = ("dayTimeDuration", XmlDuration)
    YEAR_MONTH_DURATION = ("yearMonthDuration", XmlDuration)
    DECIMAL = ("decimal", Decimal)
    DERIVATION_CONTROL = ("derivationControl", str)
    DOUBLE = ("double", Decimal)
    DURATION = ("duration", XmlDuration)
    ENTITIES = ("ENTITIES", str)
    ENTITY = ("ENTITY", str)
    ERROR = ("error", str)
    FLOAT = ("float", float)
    G_DAY = ("gDay", XmlPeriod)
    G_MONTH = ("gMonth", XmlPeriod)
    G_MONTH_DAY = ("gMonthDay", XmlPeriod)
    G_YEAR = ("gYear", XmlPeriod)
    G_YEAR_MONTH = ("gYearMonth", XmlPeriod)
    HEX_BINARY = ("hexBinary", bytes)
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
    NOTATION = ("NOTATION", QName)
    POSITIVE_INTEGER = ("positiveInteger", int)
    QNAME = ("QName", QName)
    SHORT = ("short", int)
    SIMPLE_DERIVATION_SET = ("simpleDerivationSet", str)
    STRING = ("string", str)
    TIME = ("time", XmlTime)
    TOKEN = ("token", str)
    UNSIGNED_BYTE = ("unsignedByte", int)
    UNSIGNED_INT = ("unsignedInt", int)
    UNSIGNED_LONG = ("unsignedLong", int)
    UNSIGNED_SHORT = ("unsignedShort", int)

    def __init__(self, code: str, python_type: type):
        self.code = code
        self.type = python_type

    def __str__(self) -> str:
        return f"{{{Namespace.XS.uri}}}{self.code}"

    def prefixed(self, prefix: Optional[str] = Namespace.XS.prefix) -> str:
        return f"{prefix}:{self.code}" if prefix else self.code

    @classmethod
    def get_enum(cls, code: str) -> Optional["DataType"]:
        return __DataTypeCodeIndex__.get(code) if code else None

    @classmethod
    def from_value(cls, value: Any) -> "DataType":
        if isinstance(value, bool):
            return DataType.BOOLEAN
        if isinstance(value, int):
            return DataType.INT
        if isinstance(value, float):
            return DataType.FLOAT
        if isinstance(value, Decimal):
            return DataType.DECIMAL
        if isinstance(value, QName):
            return DataType.QNAME

        return DataType.STRING

    @classmethod
    def from_qname(cls, qname: str) -> Optional["DataType"]:
        return __DataTypeQNameIndex__.get(qname)


__DataTypeCodeIndex__ = {dt.code: dt for dt in DataType}
__DataTypeQNameIndex__ = {str(dt): dt for dt in DataType}


class EventType:
    """XmlParsing event types."""

    START = "start"
    START_NS = "start-ns"
    END = "end"


class Tag:
    """Xml Schema tag names."""

    ALL = "All"
    ANNOTATION = "Annotation"
    ANY = "Any"
    ANY_ATTRIBUTE = "AnyAttribute"
    APPINFO = "Appinfo"
    ASSERTION = "Assertion"
    ALTERNATIVE = "Alternative"
    ATTRIBUTE = "Attribute"
    ATTRIBUTE_GROUP = "AttributeGroup"
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
    OVERRIDE = "Override"
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

    # Wsdl
    BINDING_OPERATION = "BindingOperation"
    BINDING_MESSAGE = "BindingMessage"
    MESSAGE = "Message"


class UseType(Enum):
    """Attribute use types."""

    OPTIONAL = "optional"
    PROHIBITED = "prohibited"
    REQUIRED = "required"


class ProcessType(Enum):
    """Wildcard process types."""

    LAX = "lax"
    SKIP = "skip"
    STRICT = "strict"


class BindingStyle(Enum):
    RPC = "rpc"
    DOCUMENT = "document"


class UseChoice(Enum):
    LITERAL = "literal"
    ENCODED = "encoded"
