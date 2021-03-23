from decimal import Decimal
from enum import Enum
from pathlib import Path
from typing import Any
from typing import Callable
from typing import Dict
from typing import Optional
from typing import Type
from xml.etree.ElementTree import QName

from xsdata.models.datatype import XmlBase64Binary
from xsdata.models.datatype import XmlDate
from xsdata.models.datatype import XmlDateTime
from xsdata.models.datatype import XmlDuration
from xsdata.models.datatype import XmlHexBinary
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

    # Primitives
    STRING = ("string", str)
    BOOLEAN = ("boolean", bool)
    DECIMAL = ("decimal", Decimal)
    FLOAT = ("float", float)
    DOUBLE = ("double", float)
    DURATION = ("duration", XmlDuration)
    DATE_TIME = ("dateTime", XmlDateTime)
    TIME = ("time", XmlTime)
    DATE = ("date", XmlDate)
    G_YEAR_MONTH = ("gYearMonth", XmlPeriod)
    G_YEAR = ("gYear", XmlPeriod)
    G_MONTH_DAY = ("gMonthDay", XmlPeriod)
    G_MONTH = ("gMonth", XmlPeriod)
    G_DAY = ("gDay", XmlPeriod)
    HEX_BINARY = ("hexBinary", bytes, "base16", XmlHexBinary)
    BASE64_BINARY = ("base64Binary", bytes, "base64", XmlBase64Binary)
    ANY_URI = ("anyURI", str)
    QNAME = ("QName", QName)
    NOTATION = ("NOTATION", QName)

    # Derived strings
    NORMALIZED_STRING = ("normalizedString", str)
    TOKEN = ("token", str)
    LANGUAGE = ("language", str)
    NMTOKEN = ("NMTOKEN", str)
    NMTOKENS = ("NMTOKENS", str)
    NAME = ("Name", str)
    NCNAME = ("NCName", str)
    ID = ("ID", str)
    IDREF = ("IDREF", str)
    IDREFS = ("IDREFS", str)
    ENTITIES = ("ENTITIES", str)
    ENTITY = ("ENTITY", str)

    # Derived integers
    INTEGER = ("integer", int)
    NON_POSITIVE_INTEGER = ("nonPositiveInteger", int)
    NEGATIVE_INTEGER = ("negativeInteger", int)
    LONG = ("long", int)
    INT = ("int", int)
    SHORT = ("short", int)
    BYTE = ("byte", int)
    NON_NEGATIVE_INTEGER = ("nonNegativeInteger", int)
    UNSIGNED_LONG = ("unsignedLong", int)
    UNSIGNED_INT = ("unsignedInt", int)
    UNSIGNED_SHORT = ("unsignedShort", int)
    UNSIGNED_BYTE = ("unsignedByte", int)
    POSITIVE_INTEGER = ("positiveInteger", int)

    # Derived Date/Time/Duration
    DATE_TIMESTAMP = ("dateTimeStamp", XmlDateTime)
    DAY_TIME_DURATION = ("dayTimeDuration", XmlDuration)
    YEAR_MONTH_DURATION = ("yearMonthDuration", XmlDuration)

    # Extensions
    ANY_TYPE = ("anyType", object)
    ANY_ATOMIC_TYPE = ("anyAtomicType", str)
    ANY_SIMPLE_TYPE = ("anySimpleType", object)
    ERROR = ("error", str)

    def __init__(
        self,
        code: str,
        python_type: type,
        fmt: Optional[str] = None,
        wrapper: Optional[Type] = None,
    ):
        self.code = code
        self.type = python_type
        self.format = fmt
        self.wrapper = wrapper

    def __str__(self) -> str:
        return f"{{{Namespace.XS.uri}}}{self.code}"

    def prefixed(self, prefix: Optional[str] = Namespace.XS.prefix) -> str:
        return f"{prefix}:{self.code}" if prefix else self.code

    @classmethod
    def from_value(cls, value: Any) -> "DataType":
        """Infer the xsd type from the value itself."""
        _type = type(value)
        calculate = __DataTypeInferIndex__.get(_type)
        if calculate:
            return calculate(value)

        return cls.from_type(_type)

    @classmethod
    def from_type(cls, tp: Type) -> "DataType":
        return __DataTypeIndex__.get(tp, DataType.STRING)

    @classmethod
    def from_qname(cls, qname: str) -> Optional["DataType"]:
        return __DataTypeQNameIndex__.get(qname)


def period_datatype(value: XmlPeriod) -> DataType:
    if value.year is not None:
        return DataType.G_YEAR_MONTH if value.month else DataType.G_YEAR
    if value.month:
        return DataType.G_MONTH_DAY if value.day else DataType.G_MONTH
    return DataType.G_DAY


def int_datatype(value: int) -> DataType:
    if -32768 <= value <= 32767:
        return DataType.SHORT
    if -2147483648 <= value <= 2147483647:
        return DataType.INT
    if -9223372036854775808 <= value <= 9223372036854775807:
        return DataType.LONG
    return DataType.INTEGER


def float_datatype(value: float) -> DataType:
    if -1.175494351e-38 <= value <= 3.402823466e38:
        return DataType.FLOAT
    return DataType.DOUBLE


__DataTypeIndex__ = {
    bool: DataType.BOOLEAN,
    int: DataType.INT,
    float: DataType.FLOAT,
    str: DataType.STRING,
    Decimal: DataType.DECIMAL,
    QName: DataType.QNAME,
    XmlDate: DataType.DATE,
    XmlTime: DataType.TIME,
    XmlDateTime: DataType.DATE_TIME,
    XmlDuration: DataType.DURATION,
    XmlPeriod: DataType.G_YEAR_MONTH,
    # bytes: DataType.HEX_BINARY || DataType.BASE64_BINARY, we can't infer formats
    XmlHexBinary: DataType.HEX_BINARY,
    XmlBase64Binary: DataType.BASE64_BINARY,
}
__DataTypeInferIndex__: Dict[Type, Callable] = {
    int: int_datatype,
    float: float_datatype,
    XmlPeriod: period_datatype,
}
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
