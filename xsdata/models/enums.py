from enum import Enum

from lxml import etree

XMLSchema = "http://www.w3.org/2001/XMLSchema"


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
