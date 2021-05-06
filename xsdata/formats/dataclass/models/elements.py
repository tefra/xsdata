import operator
from dataclasses import dataclass
from dataclasses import field
from dataclasses import is_dataclass
from typing import Any
from typing import Dict
from typing import Iterator
from typing import List
from typing import Optional
from typing import Sequence
from typing import Tuple
from typing import Type

from xsdata.models.enums import NamespaceType
from xsdata.utils import collections
from xsdata.utils.constants import EMPTY_SEQUENCE
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
    :param is_text: Field is derived from xs:simpleType
    :param is_element: Field is derived from xs:element
    :param is_elements: Field is derived from xs:choice
    :param is_wildcard: Field is derived from xs:anyType
    :param is_attribute: Field is derived from xs:attribute
    :param is_attributes: Field is derived from xs:attributes
    :param index: Field ordering
    :param types: List of all the supported data types
    :param namespaces: List of the supported namespaces
    :param elements: Mapping of qname-repeatable elements
    :param wildcards: List of repeatable wildcards
    :ivar namespace_matches: Matching cache for the repeatable wildcards
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
    is_text: bool = False
    is_element: bool = False
    is_elements: bool = False
    is_wildcard: bool = False
    is_attribute: bool = False
    is_attributes: bool = False
    index: int = field(default_factory=int)
    types: Tuple[Type, ...] = field(default_factory=tuple)
    namespaces: Tuple[str, ...] = field(default_factory=tuple)
    elements: Dict[str, "XmlVar"] = field(default_factory=dict)
    wildcards: List["XmlVar"] = field(default_factory=list)
    namespace_matches: Optional[Dict[str, bool]] = field(init=False, default=None)

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

    def find_choice(self, qname: str) -> Optional["XmlVar"]:
        """Match and return a choice field by its qualified name."""
        match = self.elements.get(qname)
        return match or find_by_namespace(self.wildcards, qname)

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

        for element in self.elements.values():

            if element.any_type or tokens != element.tokens:
                continue

            if tp is NoneType:
                if element.nillable:
                    return element
            elif self.match_type(tp, element.types, check_subclass):
                return element

        return None

    @classmethod
    def match_type(cls, tp: Type, types: Sequence[Type], check_subclass: bool) -> bool:
        for candidate in types:
            if tp == candidate or (check_subclass and issubclass(tp, candidate)):
                return True

        return False

    def match_namespace(self, qname: str) -> bool:
        """Match the given qname to the wildcard allowed namespaces."""

        if self.namespace_matches is None:
            self.namespace_matches = {}

        matches = self.namespace_matches.get(qname)
        if matches is None:
            matches = self._match_namespace(qname)
            self.namespace_matches[qname] = matches

        return matches

    def _match_namespace(self, qname: str) -> bool:
        if qname == "*":
            return True

        namespace, tag = split_qname(qname)
        if not self.namespaces and namespace is None:
            return True

        for check in self.namespaces:
            if (
                (not check and namespace is None)
                or check == namespace
                or check == NamespaceType.ANY_NS
                or (check and check[0] == "!" and check[1:] != namespace)
            ):
                return True

        return False


get_index = operator.attrgetter("index")


@dataclass
class XmlMeta:
    """
    Dataclass binding metadata.

    :param clazz: The dataclass type
    :param qname: The namespace qualified name.
    :param source_qname: The source namespace qualified name.
    :param nillable: Specifies whether an explicit empty value can be assigned.
    :param mixed_content: Has a wildcard with mixed flag enabled
    :param text: Text var
    :param choices: List of compound vars
    :param elements: Mapping of qname-element vars
    :param wildcards: List of wildcard vars
    :param attributes: Mapping of qname-attribute vars
    :param any_attributes: List of wildcard attributes vars
    """

    clazz: Type
    qname: str
    source_qname: str
    nillable: bool
    mixed_content: bool = field(default=False)
    text: Optional[XmlVar] = field(default=None)
    choices: List[XmlVar] = field(default_factory=list)
    elements: Dict[str, List[XmlVar]] = field(default_factory=dict)
    wildcards: List[XmlVar] = field(default_factory=list)
    attributes: Dict[str, XmlVar] = field(default_factory=dict)
    any_attributes: List[XmlVar] = field(default_factory=list)

    def __post_init__(self):
        self.mixed_content = any(wildcard.mixed for wildcard in self.wildcards)

    def get_element_vars(self) -> List[XmlVar]:
        result = self.wildcards + self.choices

        for elements in self.elements.values():
            result.extend(elements)

        if self.text:
            result.append(self.text)

        return sorted(result, key=get_index)

    def get_attribute_vars(self) -> List[XmlVar]:
        result = collections.concat(self.any_attributes, self.attributes.values())
        return sorted(result, key=get_index)

    def get_all_vars(self) -> List[XmlVar]:
        result = self.wildcards + self.choices + self.any_attributes
        result.extend(self.attributes.values())
        for elements in self.elements.values():
            result.extend(elements)

        if self.text:
            result.append(self.text)

        return sorted(result, key=get_index)

    @property
    def namespace(self) -> Optional[str]:
        return split_qname(self.qname)[0]

    def find_attribute(self, qname: str) -> Optional[XmlVar]:
        return self.attributes.get(qname)

    def find_elements(self, qname: str) -> Sequence[XmlVar]:
        return self.elements.get(qname, EMPTY_SEQUENCE)

    def find_choice(self, qname: str) -> Optional[XmlVar]:
        for choice in self.choices:
            match = choice.find_choice(qname)
            if match:
                return match

        return None

    def find_any_attributes(self, qname: str) -> Optional[XmlVar]:
        return find_by_namespace(self.any_attributes, qname)

    def find_wildcard(self, qname: str) -> Optional[XmlVar]:
        return find_by_namespace(self.wildcards, qname)

    def find_children(self, qname: str) -> Iterator[XmlVar]:

        yield from self.find_elements(qname)

        chd = self.find_choice(qname)
        if chd:
            yield chd

        chd = self.find_wildcard(qname)
        if chd:
            yield chd


class XmlType:
    """Xml node types."""

    TEXT = "Text"
    ELEMENT = "Element"
    ELEMENTS = "Elements"
    WILDCARD = "Wildcard"
    ATTRIBUTE = "Attribute"
    ATTRIBUTES = "Attributes"


def find_by_namespace(xml_vars: List[XmlVar], qname: str) -> Optional[XmlVar]:
    for xml_var in xml_vars:
        if xml_var.match_namespace(qname):
            return xml_var

    return None
