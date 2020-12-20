from dataclasses import dataclass
from dataclasses import field
from dataclasses import is_dataclass
from typing import Any
from typing import Dict
from typing import List
from typing import Optional
from typing import Type

from xsdata.models.enums import NamespaceType
from xsdata.utils.namespaces import split_qname

NoneType = type(None)


@dataclass(frozen=True)
class XmlVar:
    """
    Dataclass field binding metadata.

    :param name: Field name
    :param qname: The namespace qualified local name
    :param init:  Field is present in the constructor parameters
    :param mixed:  Field supports mixed content
    :param tokens: Use a list to map simple values
    :param derived: Use derived elements to bind data
    :param any_type: Support inline declaration
    :param nillable: Allow empty content elements rendering
    :param dataclass: Specify whether the field type is a dataclass
    :param sequential: Switch to sequential rendering with other
        sequential siblings
    :param list_element: Specify whether the field represents a list of
        elements
    :param default: Field default value or factory
    :param types: Field simple types
    :param choices: Field compound element choices
    :param namespaces: Field list of the all the possible namespaces
    """

    name: str
    qname: str
    init: bool = True
    mixed: bool = False
    tokens: bool = False
    derived: bool = False
    any_type: bool = False
    nillable: bool = False
    dataclass: bool = False
    sequential: bool = False
    list_element: bool = False
    default: Any = None
    types: List[Type] = field(default_factory=list)
    choices: List["XmlVar"] = field(default_factory=list)
    namespaces: List[str] = field(default_factory=list)

    @property
    def clazz(self) -> Optional[Type]:
        """Return the first type if field is bound to a dataclass."""
        return self.types[0] if self.dataclass else None

    @property
    def is_any_type(self) -> bool:
        """Return whether the field type is xs:anyType."""
        return False

    @property
    def is_attribute(self) -> bool:
        """Return whether the field is derived from xs:attribute."""
        return False

    @property
    def is_attributes(self) -> bool:
        """Return whether the field is derived from xs:anyAttributes."""
        return False

    @property
    def is_element(self) -> bool:
        """Return whether the field is derived from xs:element."""
        return False

    @property
    def is_elements(self) -> bool:
        """Return whether the field is a compound of other elements."""
        return False

    @property
    def is_list(self) -> bool:
        """Return whether the field is a list of elements."""
        return self.list_element

    @property
    def is_mixed_content(self) -> bool:
        """Return whether the field is a mixed content list of of elements."""
        return False

    @property
    def is_clazz_union(self) -> bool:
        return self.dataclass and len(self.types) > 1

    @property
    def is_text(self) -> bool:
        """Return whether the field is a text element."""
        return False

    @property
    def is_wildcard(self) -> bool:
        """Return whether the field is a text element."""
        return False

    def matches(self, qname: str) -> bool:
        """
        Match the field qualified local name to the given qname.

        Return True automatically if the local name is a wildcard.
        """
        return qname in (self.qname, "*")

    def find_choice(self, qname: str) -> Optional["XmlVar"]:
        """Match and return a choice field by its qualified name."""
        return None

    def find_value_choice(self, value: Any) -> Optional["XmlVar"]:
        """Match and return a choice field that matches the given value."""
        return None


@dataclass(frozen=True)
class XmlElement(XmlVar):
    """Dataclass field binding metadata for xs:element."""

    @property
    def is_element(self) -> bool:
        return True

    @property
    def is_any_type(self) -> bool:
        return self.any_type


@dataclass(frozen=True)
class XmlElements(XmlVar):
    """Dataclass field binding metadata for xs:group elements."""

    @property
    def is_elements(self) -> bool:
        return True

    def matches(self, qname: str) -> bool:
        """Return whether a choice element matches the given qualified name."""

        return self.find_choice(qname) is not None

    def find_choice(self, qname: str) -> Optional[XmlVar]:
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

            if choice.is_any_type or tokens != choice.tokens:
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


@dataclass(frozen=True)
class XmlWildcard(XmlVar):
    """Dataclass field binding metadata for xs:any (wildcard) elements."""

    @property
    def is_mixed_content(self) -> bool:
        return self.mixed

    @property
    def is_wildcard(self) -> bool:
        return True

    def matches(self, qname: str) -> bool:
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


@dataclass(frozen=True)
class XmlAttribute(XmlVar):
    """Dataclass field binding metadata for xs:anyAttributes."""

    @property
    def is_attribute(self) -> bool:
        return True


@dataclass(frozen=True)
class XmlAttributes(XmlVar):
    """Dataclass field bind metadata for xml wildcard attributes."""

    @property
    def is_attributes(self) -> bool:
        return True


@dataclass(frozen=True)
class XmlText(XmlVar):
    """Dataclass field bind metadata for xml text content."""

    @property
    def is_text(self) -> bool:
        return True


class FindMode:
    """Find switches to be used to find a specific var."""

    ALL = 0
    ATTRIBUTE = 1
    ATTRIBUTES = 2
    TEXT = 3
    WILDCARD = 4
    MIXED_CONTENT = 5
    NOT_WILDCARD = 6


find_predicates = {
    FindMode.ALL: lambda x: True,
    FindMode.ATTRIBUTE: lambda x: x.is_attribute,
    FindMode.ATTRIBUTES: lambda x: x.is_attributes,
    FindMode.TEXT: lambda x: x.is_text,
    FindMode.WILDCARD: lambda x: x.is_wildcard,
    FindMode.MIXED_CONTENT: lambda x: x.is_mixed_content,
    FindMode.NOT_WILDCARD: lambda x: not x.is_wildcard,
}


@dataclass(frozen=True)
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
