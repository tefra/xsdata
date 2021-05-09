import operator
from dataclasses import is_dataclass
from typing import Any
from typing import Dict
from typing import Iterator
from typing import List
from typing import Mapping
from typing import Optional
from typing import Sequence
from typing import Type

from xsdata.models.enums import NamespaceType
from xsdata.utils import collections
from xsdata.utils.constants import EMPTY_SEQUENCE
from xsdata.utils.namespaces import local_name
from xsdata.utils.namespaces import split_qname
from xsdata.utils.namespaces import target_uri

NoneType = type(None)


class XmlType:
    """Xml node types."""

    TEXT = "Text"
    ELEMENT = "Element"
    ELEMENTS = "Elements"
    WILDCARD = "Wildcard"
    ATTRIBUTE = "Attribute"
    ATTRIBUTES = "Attributes"

    @classmethod
    def all(cls):
        yield XmlType.TEXT
        yield XmlType.ELEMENT
        yield XmlType.ELEMENTS
        yield XmlType.WILDCARD
        yield XmlType.ATTRIBUTE
        yield XmlType.ATTRIBUTES


class MetaMixin:
    def __eq__(self, other: Any) -> bool:
        if isinstance(other, self.__class__):
            return tuple(self) == tuple(other)

        return NotImplemented

    def __iter__(self) -> Iterator:
        for field_name in self.__slots__:
            yield getattr(self, field_name)


class XmlVar(MetaMixin):
    """Class field binding metadata."""

    __slots__ = (
        "name",
        "qname",
        "init",
        "mixed",
        "tokens",
        "format",
        "derived",
        "any_type",
        "nillable",
        "sequential",
        "list_element",
        "default",
        "is_text",
        "is_element",
        "is_elements",
        "is_wildcard",
        "is_attribute",
        "is_attributes",
        "index",
        "types",
        "namespaces",
        "elements",
        "wildcards",
        "namespace_matches",
        "clazz",
        "is_clazz_union",
        "local_name",
    )

    def __init__(
        self,
        *args: Any,
        index: int,
        name: str,
        qname: str,
        types: Sequence[Type],
        init: bool,
        mixed: bool,
        tokens: bool,
        format: Optional[str],
        derived: bool,
        any_type: bool,
        nillable: bool,
        sequential: bool,
        list_element: bool,
        default: Any,
        xml_type: str,
        namespaces: Sequence[str],
        elements: Mapping[str, "XmlVar"],
        wildcards: Sequence["XmlVar"],
    ):
        """
        :param index: Field ordering
        :param name: Field name
        :param qname: Qualified name
        :param types: List of all the supported data types
        :param init:  Include field in the constructor
        :param mixed:  Field supports mixed content type values
        :param tokens: Field is derived from xs:list
        :param format: Value format information
        :param derived: Wrap parsed values with a generic type
        :param any_type: Field supports dynamic value types
        :param nillable: Field supports nillable content
        :param sequential: Render values in sequential mode
        :param list_element: Field is a list of elements
        :param default: Field default value or factory
        :param xml_Type: Field xml type
        :param namespaces: List of the supported namespaces
        :param elements: Mapping of qname-repeatable elements
        :param wildcards: List of repeatable wildcards
        """

        self.index = index
        self.name = name
        self.qname = qname
        self.types = types
        self.init = init
        self.mixed = mixed
        self.tokens = tokens
        self.format = format
        self.derived = derived
        self.any_type = any_type
        self.nillable = nillable
        self.sequential = sequential
        self.list_element = list_element
        self.default = default
        self.namespaces = namespaces
        self.elements = elements
        self.wildcards = wildcards

        self.namespace_matches: Optional[Dict[str, bool]] = None

        self.clazz = collections.first(tp for tp in types if is_dataclass(tp))
        self.is_clazz_union = self.clazz and len(types) > 1
        self.local_name = local_name(qname)

        self.is_text = False
        self.is_element = False
        self.is_elements = False
        self.is_wildcard = False
        self.is_attribute = False
        self.is_attributes = False

        if xml_type == XmlType.ELEMENT or self.clazz:
            self.is_element = True
        elif xml_type == XmlType.ELEMENTS:
            self.is_elements = True
        elif xml_type == XmlType.ATTRIBUTE:
            self.is_attribute = True
        elif xml_type == XmlType.ATTRIBUTES:
            self.is_attributes = True
        elif xml_type == XmlType.WILDCARD:
            self.is_wildcard = True
        else:
            self.is_text = True

    def get_xml_type(self) -> str:
        if self.is_wildcard:
            return XmlType.WILDCARD

        if self.is_attribute:
            return XmlType.ATTRIBUTE

        if self.is_attributes:
            return XmlType.ATTRIBUTES

        if self.is_element:
            return XmlType.ELEMENT

        if self.is_elements:
            return XmlType.ELEMENTS

        return XmlType.TEXT

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

        uri = target_uri(qname)
        if not self.namespaces and uri is None:
            return True

        for check in self.namespaces:
            if (
                (not check and uri is None)
                or check == uri
                or check == NamespaceType.ANY_NS
                or (check and check[0] == "!" and check[1:] != uri)
            ):
                return True

        return False

    def __repr__(self) -> str:
        params = (
            f"index={self.index}, "
            f"name={self.name}, "
            f"qname={self.qname}, "
            f"types={self.types}, "
            f"init={self.init}, "
            f"mixed={self.mixed}, "
            f"tokens={self.tokens}, "
            f"format={self.format}, "
            f"derived={self.derived}, "
            f"any_type={self.any_type}, "
            f"nillable={self.nillable}, "
            f"sequential={self.sequential}, "
            f"list_element={self.list_element}, "
            f"default={self.default}, "
            f"xml_type={self.get_xml_type()}, "
            f"namespaces={self.namespaces}, "
            f"elements={self.elements}, "
            f"wildcards={self.wildcards}"
        )
        return f"{self.__class__.__name__}({params})"


get_index = operator.attrgetter("index")


class XmlMeta(MetaMixin):
    """Class binding metadata."""

    __slots__ = (
        "clazz",
        "qname",
        "source_qname",
        "nillable",
        "text",
        "choices",
        "elements",
        "wildcards",
        "attributes",
        "any_attributes",
        "mixed_content",
    )

    def __init__(
        self,
        *args: Any,
        clazz: Type,
        qname: str,
        source_qname: str,
        nillable: bool,
        text: Optional[XmlVar],
        choices: Sequence[XmlVar],
        elements: Mapping[str, Sequence[XmlVar]],
        wildcards: Sequence[XmlVar],
        attributes: Mapping[str, XmlVar],
        any_attributes: Sequence[XmlVar],
    ):

        """
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

        self.clazz = clazz
        self.qname = qname
        self.source_qname = source_qname
        self.nillable = nillable
        self.text = text
        self.choices = choices
        self.elements = elements
        self.wildcards = wildcards
        self.attributes = attributes
        self.any_attributes = any_attributes
        self.mixed_content = any(wildcard.mixed for wildcard in self.wildcards)

    def get_element_vars(self) -> List[XmlVar]:
        result = list(
            collections.concat(self.wildcards, self.choices, *self.elements.values())
        )
        if self.text:
            result.append(self.text)

        return sorted(result, key=get_index)

    def get_attribute_vars(self) -> List[XmlVar]:
        result = collections.concat(self.any_attributes, self.attributes.values())
        return sorted(result, key=get_index)

    def get_all_vars(self) -> List[XmlVar]:
        result = list(
            collections.concat(
                self.wildcards,
                self.choices,
                self.any_attributes,
                self.attributes.values(),
                *self.elements.values(),
            )
        )
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

    def __repr__(self) -> str:
        params = (
            f"clazz={self.clazz}, "
            f"qname={self.qname}, "
            f"source_qname={self.source_qname}, "
            f"nillable={self.nillable}, "
            f"text={self.text}, "
            f"choices={self.choices}, "
            f"elements={self.elements}, "
            f"wildcards={self.wildcards}, "
            f"attributes={self.attributes}, "
            f"any_attributes={self.any_attributes}"
        )
        return f"{self.__class__.__name__}({params})"


def find_by_namespace(xml_vars: Sequence[XmlVar], qname: str) -> Optional[XmlVar]:
    for xml_var in xml_vars:
        if xml_var.match_namespace(qname):
            return xml_var

    return None
