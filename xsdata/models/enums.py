from enum import Enum
from typing import Optional

from lxml import etree

XMLSchema = "http://www.w3.org/2001/XMLSchema"


class XSDType:
    MAP = {
        "anyURI": "str",
        "base64Binary": "str",
        "boolean": "bool",
        "byte": "int",
        "date": "str",
        "dateTime": "str",
        "decimal": "float",
        "derivationControl": "str",
        "double": "float",
        "duration": "str",
        "ENTITIES": "int",
        "ENTITY": "int",
        "float": "float",
        "gDay": "str",
        "gMonth": "str",
        "gMonthDay": "str",
        "gYear": "str",
        "gYearMonth": "str",
        "hexBinary": "str",
        "ID": "str",
        "IDREF": "str",
        "IDREFS": "str",
        "int": "int",
        "integer": "int",
        "language": "str",
        "long": "int",
        "Name": "str",
        "NCName": "str",
        "negativeInteger": "int",
        "NMTOKEN": "str",
        "NMTOKENS": "str",
        "nonNegativeInteger": "int",
        "nonPositiveInteger": "int",
        "normalizedString": "str",
        "NOTATION": "str",
        "positiveInteger": "int",
        "QName": "str",
        "short": "int",
        "simpleDerivationSet": "str",
        "string": "str",
        "time": "str",
        "token": "str",
        "unsignedByte": "int",
        "unsignedInt": "int",
        "unsignedLong": "int",
        "unsignedShort": "int",
    }

    @classmethod
    def map(cls, xsd_type: str) -> Optional[str]:
        pos = xsd_type.find(":")
        if pos == -1:
            return None

        return cls.MAP.get(xsd_type[pos + 1 :])


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
