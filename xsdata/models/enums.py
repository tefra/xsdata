from enum import Enum
from typing import Optional

from lxml import etree

XMLSchema = "http://www.w3.org/2001/XMLSchema"


class XSDType(Enum):
    STRING = ("xs:string", str)
    DECIMAL = ("xs:decimal", float)
    INTEGER = ("xs:integer", int)
    BOOLEAN = ("xs:boolean", bool)
    DATE = ("xs:date", str)
    TIME = ("xs:time", str)

    def __init__(self, xsd_type, py_type):
        self.xsd_type = xsd_type
        self.py_type = py_type

    @property
    def py_name(self):
        return self.py_type.__name__

    @classmethod
    def find(cls, xsd_type: str) -> Optional["XSDType"]:
        for value in XSDType:
            if value.xsd_type == xsd_type:
                return value
        return None


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
