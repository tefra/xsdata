from enum import Enum

from lxml import etree

from xsdata import XMLSchema


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
    MINLENGTH = "minLength"
    MAXLENGTH = "maxLength"
    PATTERN = "pattern"

    @property
    def qname(self):
        return etree.QName(XMLSchema, self.value)

    @classmethod
    def element_parents(cls):
        return [Tag.SCHEMA, Tag.CHOICE, Tag.ALL, Tag.SEQUENCE, Tag.GROUP]
