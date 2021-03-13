from dataclasses import dataclass
from dataclasses import field
from dataclasses import InitVar
from dataclasses import is_dataclass
from typing import Any
from typing import Dict
from typing import List
from typing import Optional
from typing import Type

from xsdata.exceptions import XmlContextError
from xsdata.models.enums import NamespaceType
from xsdata.utils.namespaces import split_qname

NoneType = type(None)


@dataclass
class XmlVar:
    """
    Dataclass field binding metadata.

    :param name: Field name
    :param qname: Qualified name
    :param init:  Include field in the constructor
    :param mixed:  Field supports mixed content type values
    :param tokens: Field is derived from xs:list
    :param format: Value format information
    :param derived: Wrap parsed values with
        :class:`~xsdata.formats.dataclass.models.generics.DerivedElement`
    :param any_type: Field supports dynamic value types
    :param nillable: Field supports nillable content
    :param dataclass: Field value is bound to a dataclass
    :param sequential: Render values in sequential mode
    :param list_element: Field is a list of elements
    :param default: Field default value or factory
    :param text: Field is derived from xs:simpleType
    :param element: Field is derived from xs:element
    :param elements: Field is derived from xs:choice
    :param wildcard: Field is derived from xs:anyType
    :param attribute: Field is derived from xs:attribute
    :param attributes: Field is derived from xs:attributes
    :param types: List of all the supported data types
    :param choices: List of repeatable choice elements
    :param namespaces: List of the supported namespaces
    """

    name: str
    qname: str
    init: bool = True
    mixed: bool = False
    tokens: bool = False
    format: Optional[str] = None
    derived: bool = False
    any_type: bool = False
    nillable: bool = False
    dataclass: bool = False
    sequential: bool = False
    list_element: bool = False
    default: Any = None
    text: bool = False
    element: bool = False
    elements: bool = False
    wildcard: bool = False
    attribute: bool = False
    attributes: bool = False
    types: List[Type] = field(default_factory=list)
    choices: List["XmlVar"] = field(default_factory=list)
    namespaces: List[str] = field(default_factory=list)

    xml_type: InitVar[Optional[str]] = None

    def __post_init__(self, xml_type: Optional[str]):
        if xml_type == XmlType.ELEMENT:
            self.element = True
        elif xml_type == XmlType.ELEMENTS:
            self.elements = True
        elif xml_type == XmlType.ATTRIBUTE:
            self.attribute = True
            self.any_type = False
        elif xml_type == XmlType.ATTRIBUTES:
            self.attributes = True
            self.any_type = False
        elif xml_type == XmlType.WILDCARD:
            self.wildcard = True
            self.any_type = False
        elif xml_type == XmlType.TEXT:
            self.text = True
            self.any_type = False
        elif xml_type:
            raise XmlContextError(f"Unknown xml type `{xml_type}`")

    @property
    def lname(self) -> str:
        """Local name."""
        _, name = split_qname(self.qname)
        return name

    @property
    def clazz(self) -> Optional[Type]:
        """Return the first type if field is bound to a dataclass."""
        return self.types[0] if self.dataclass else None

    @property
    def is_clazz_union(self) -> bool:
        return self.dataclass and len(self.types) > 1

    def matches(self, qname: str) -> bool:
        """
        Match the field qualified local name to the given qname.

        Return True automatically if the local name is a wildcard.
        """
        if self.elements:
            return self.matches_choice(qname)

        if self.wildcard:
            return self.matches_wildcard(qname)

        return qname in (self.qname, "*")

    def matches_choice(self, qname: str) -> bool:
        """Return whether a choice element matches the given qualified name."""
        return self.find_choice(qname) is not None

    def find_choice(self, qname: str) -> Optional["XmlVar"]:
        """Match and return a choice field by its qualified name."""
        for choice in self.choices:
            if choice.matches(qname):
                return choice

        return None

    def find_value_choice(self, value: Any) -> Optional["XmlVar"]:
        """Match and return a choice field that matches the given value
        type."""

        if isinstance(value, list):
            tp = type(None) if not value else type(value[0])
            tokens = True
            check_subclass = False
        else:
            tp = type(value)
            tokens = False
            check_subclass = is_dataclass(value)

        return self.find_type_choice(tp, tokens, check_subclass)

    def find_type_choice(
        self, tp: Type, tokens: bool, check_subclass: bool
    ) -> Optional["XmlVar"]:
        """Match and return a choice field that matches the given type."""

        for choice in self.choices:

            if choice.any_type or tokens != choice.tokens:
                continue

            if tp is NoneType:
                if choice.nillable:
                    return choice
            elif self.match_type(tp, choice.types, check_subclass):
                return choice

        return None

    @classmethod
    def match_type(cls, tp: Type, types: List[Type], check_subclass: bool) -> bool:
        for candidate in types:
            if tp == candidate or (check_subclass and issubclass(tp, candidate)):
                return True

        return False

    def matches_wildcard(self, qname: str) -> bool:
        """Match the given qname to the wildcard allowed namespaces."""

        if qname == "*":
            return True

        namespace, tag = split_qname(qname)
        if not self.namespaces and namespace is None:
            return True

        return any(self.match_namespace(ns, namespace) for ns in self.namespaces)

    @staticmethod
    def match_namespace(source: Optional[str], cmp: Optional[str]) -> bool:
        if not source and cmp is None:
            return True
        if source == cmp:
            return True
        if source == NamespaceType.ANY_NS:
            return True
        if source and source[0] == "!" and source[1:] != cmp:
            return True

        return False


class FindMode:
    """Find switches to be used to find a specific var."""

    ALL = 0
    ATTRIBUTE = 1
    ATTRIBUTES = 2
    TEXT = 3
    WILDCARD = 4
    MIXED_CONTENT = 5
    ELEMENT = 6


find_predicates = {
    FindMode.ALL: lambda x: True,
    FindMode.ATTRIBUTE: lambda x: x.attribute,
    FindMode.ATTRIBUTES: lambda x: x.attributes,
    FindMode.TEXT: lambda x: x.text,
    FindMode.WILDCARD: lambda x: x.wildcard,
    FindMode.MIXED_CONTENT: lambda x: x.mixed,
    FindMode.ELEMENT: lambda x: x.element or x.elements,
}


@dataclass
class XmlMeta:
    """
    Dataclass binding metadata.

    :param clazz: The dataclass type
    :param qname: The namespace qualified name.
    :param source_qname: The source namespace qualified name.
    :param nillable: Specifies whether an explicit empty value can be assigned.
    :param vars: The list of field metadata
    """

    clazz: Type
    qname: str
    source_qname: str
    nillable: bool
    vars: List[XmlVar] = field(default_factory=list)
    cache: Dict = field(default_factory=dict, init=False)

    @property
    def namespace(self) -> Optional[str]:
        return split_qname(self.qname)[0]

    def has_var(self, qname: str = "*", mode: int = FindMode.ALL) -> bool:
        return self.find_var(qname, mode) is not None

    def find_var(self, qname: str = "*", mode: int = FindMode.ALL) -> Optional[XmlVar]:
        """Find and cache a field by it's qualified name and the specified
        mode."""
        key = (qname, mode)
        index = self.cache.get(key)
        if index is None:
            self.cache[key] = index = self._find_var(qname, mode)

        return None if index < 0 else self.vars[index]

    def _find_var(self, qname: str, mode: int) -> int:
        predicate = find_predicates[mode]
        for index, var in enumerate(self.vars):
            if predicate(var) and var.matches(qname):
                return index

        return -1


class XmlType:
    """Xml node types."""

    TEXT = "Text"
    ELEMENT = "Element"
    ELEMENTS = "Elements"
    WILDCARD = "Wildcard"
    ATTRIBUTE = "Attribute"
    ATTRIBUTES = "Attributes"
