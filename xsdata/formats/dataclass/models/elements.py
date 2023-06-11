import itertools
import operator
import sys
from typing import Any
from typing import Callable
from typing import Dict
from typing import Iterator
from typing import List
from typing import Mapping
from typing import Optional
from typing import Sequence
from typing import Set
from typing import Tuple
from typing import Type

from xsdata.formats.converter import converter
from xsdata.models.enums import NamespaceType
from xsdata.utils import collections
from xsdata.utils.namespaces import local_name
from xsdata.utils.namespaces import target_uri

NoneType = type(None)


class XmlType:
    """Xml node types."""

    TEXT = sys.intern("Text")
    ELEMENT = sys.intern("Element")
    ELEMENTS = sys.intern("Elements")
    WILDCARD = sys.intern("Wildcard")
    ATTRIBUTE = sys.intern("Attribute")
    ATTRIBUTES = sys.intern("Attributes")
    IGNORE = sys.intern("Ignore")


class MetaMixin:
    """Use this mixin for unit tests only!!!"""

    __slots__: Tuple[str, ...] = ()

    def __eq__(self, other: Any) -> bool:
        return tuple(self) == tuple(other)

    def __iter__(self) -> Iterator:
        for name in self.__slots__:
            yield getattr(self, name)

    def __repr__(self) -> str:
        params = (f"{name}={getattr(self, name)!r}" for name in self.__slots__)
        return f"{self.__class__.__qualname__}({', '.join(params)})"


class XmlVar(MetaMixin):
    """
    Class field binding metadata.

    :param index: Field ordering
    :param name: Field name
    :param qname: Qualified name
    :param types: List of all the supported data types
    :param init: Include field in the constructor
    :param mixed: Field supports mixed content type values
    :param tokens: Field is derived from xs:list
    :param format: Value format information
    :param derived: Wrap parsed values with a generic type
    :param any_type: Field supports dynamic value types
    :param required: Field is mandatory
    :param nillable: Field supports nillable content
    :param sequence: Render values in sequential mode
    :param list_element: Field is a list of elements
    :param default: Field default value or factory
    :param xml_Type: Field xml type
    :param namespaces: List of the supported namespaces
    :param elements: Mapping of qname-repeatable elements
    :param wildcards: List of repeatable wildcards
    :param wrapper: A name for the wrapper. Applies for list types only.
    """

    __slots__ = (
        "index",
        "name",
        "qname",
        "types",
        "clazz",
        "init",
        "mixed",
        "factory",
        "tokens_factory",
        "format",
        "derived",
        "any_type",
        "required",
        "nillable",
        "sequence",
        "default",
        "namespaces",
        "elements",
        "wildcards",
        "wrapper",
        # Calculated
        "tokens",
        "list_element",
        "is_text",
        "is_element",
        "is_elements",
        "is_wildcard",
        "is_attribute",
        "is_attributes",
        "namespace_matches",
        "is_clazz_union",
        "local_name",
    )

    def __init__(
        self,
        index: int,
        name: str,
        qname: str,
        types: Sequence[Type],
        clazz: Optional[Type],
        init: bool,
        mixed: bool,
        factory: Optional[Callable],
        tokens_factory: Optional[Callable],
        format: Optional[str],
        derived: bool,
        any_type: bool,
        required: bool,
        nillable: bool,
        sequence: Optional[int],
        default: Any,
        xml_type: str,
        namespaces: Sequence[str],
        elements: Mapping[str, "XmlVar"],
        wildcards: Sequence["XmlVar"],
        wrapper: Optional[str] = None,
        **kwargs: Any,
    ):
        self.index = index
        self.name = name
        self.qname = qname
        self.types = types
        self.clazz = clazz
        self.init = init
        self.mixed = mixed
        self.tokens = tokens_factory is not None
        self.format = format
        self.derived = derived
        self.any_type = any_type
        self.required = required
        self.nillable = nillable
        self.sequence = sequence
        self.list_element = factory in (list, tuple)
        self.default = default
        self.namespaces = namespaces
        self.elements = elements
        self.wildcards = wildcards
        self.wrapper = wrapper

        self.factory = factory
        self.tokens_factory = tokens_factory

        self.namespace_matches: Optional[Dict[str, bool]] = None

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

    @property
    def element_types(self) -> Set[Type]:
        return {tp for element in self.elements.values() for tp in element.types}

    def find_choice(self, qname: str) -> Optional["XmlVar"]:
        """Match and return a choice field by its qualified name."""
        match = self.elements.get(qname)
        return match or find_by_namespace(self.wildcards, qname)

    def find_value_choice(self, value: Any, is_class: bool) -> Optional["XmlVar"]:
        """
        Match and return a choice field that matches the given value.

        Cases:
            - value is none or empty tokens list: look for a nillable choice
            - value is a dataclass: look for exact type or a subclass
            - value is primitive: test value against the converter
        """
        is_tokens = collections.is_array(value)
        if value is None or (not value and is_tokens):
            return self.find_nillable_choice(is_tokens)

        if is_class:
            return self.find_clazz_choice(type(value))

        return self.find_primitive_choice(value, is_tokens)

    def find_nillable_choice(self, is_tokens: bool) -> Optional["XmlVar"]:
        return collections.first(
            element
            for element in self.elements.values()
            if element.nillable and is_tokens == element.tokens
        )

    def find_clazz_choice(self, tp: Type) -> Optional["XmlVar"]:
        derived = None
        for element in self.elements.values():
            if element.clazz:
                if tp in element.types:
                    return element

                if derived is None and any(issubclass(tp, t) for t in element.types):
                    derived = element

        return derived

    def find_primitive_choice(self, value: Any, is_tokens: bool) -> Optional["XmlVar"]:
        tp = type(value) if not is_tokens else type(value[0])
        for element in self.elements.values():
            if (element.any_type or element.clazz) or element.tokens != is_tokens:
                continue

            if tp in element.types:
                return element

            if is_tokens and all(converter.test(val, element.types) for val in value):
                return element

            if converter.test(value, element.types):
                return element

        return None

    def is_optional(self, value: Any) -> bool:
        """Return whether this var instance is not required and the given value
        matches the default one."""
        if self.required:
            return False

        if callable(self.default):
            return self.default() == value
        return self.default == value

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


get_index = operator.attrgetter("index")


class XmlMeta(MetaMixin):
    """
    Class binding metadata.

    :param clazz: The dataclass type
    :param qname: The namespace qualified name.
    :param target_qname: The target namespace qualified name.
    :param nillable: Specifies whether an explicit empty value can be
        assigned.
    :param mixed_content: Has a wildcard with mixed flag enabled
    :param text: Text var
    :param choices: List of compound vars
    :param elements: Mapping of qname-element vars
    :param wildcards: List of wildcard vars
    :param attributes: Mapping of qname-attribute vars
    :param any_attributes: List of wildcard attributes vars
    """

    __slots__ = (
        "clazz",
        "qname",
        "target_qname",
        "nillable",
        "text",
        "choices",
        "elements",
        "wildcards",
        "attributes",
        "any_attributes",
        "wrappers",
        # Calculated
        "namespace",
        "mixed_content",
    )

    def __init__(
        self,
        clazz: Type,
        qname: str,
        target_qname: Optional[str],
        nillable: bool,
        text: Optional[XmlVar],
        choices: Sequence[XmlVar],
        elements: Mapping[str, Sequence[XmlVar]],
        wildcards: Sequence[XmlVar],
        attributes: Mapping[str, XmlVar],
        any_attributes: Sequence[XmlVar],
        wrappers: Mapping[str, Sequence[XmlVar]],
        **kwargs: Any,
    ):
        self.clazz = clazz
        self.qname = qname
        self.namespace = target_uri(qname)
        self.target_qname = target_qname
        self.nillable = nillable
        self.text = text
        self.choices = choices
        self.elements = elements
        self.wildcards = wildcards
        self.attributes = attributes
        self.any_attributes = any_attributes
        self.mixed_content = any(wildcard.mixed for wildcard in self.wildcards)
        self.wrappers = wrappers

    @property
    def element_types(self) -> Set[Type]:
        return {
            tp
            for elements in self.elements.values()
            for element in elements
            for tp in element.types
        }

    def get_element_vars(self) -> List[XmlVar]:
        result = list(
            itertools.chain(self.wildcards, self.choices, *self.elements.values())
        )
        if self.text:
            result.append(self.text)

        return sorted(result, key=get_index)

    def get_attribute_vars(self) -> List[XmlVar]:
        result = itertools.chain(self.any_attributes, self.attributes.values())
        return sorted(result, key=get_index)

    def get_all_vars(self) -> List[XmlVar]:
        result = list(
            itertools.chain(
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

    def find_attribute(self, qname: str) -> Optional[XmlVar]:
        return self.attributes.get(qname)

    def find_any_attributes(self, qname: str) -> Optional[XmlVar]:
        return find_by_namespace(self.any_attributes, qname)

    def find_wildcard(self, qname: str) -> Optional[XmlVar]:
        """Match the given qualified name to a wildcard and optionally to one
        of its choice elements."""
        wildcard = find_by_namespace(self.wildcards, qname)

        if wildcard and wildcard.elements:
            choice = wildcard.find_choice(qname)
            if choice:
                return choice

        return wildcard

    def find_any_wildcard(self) -> Optional[XmlVar]:
        if self.wildcards:
            return self.wildcards[0]

        return None

    def find_children(self, qname: str) -> Iterator[XmlVar]:
        elements = self.elements.get(qname)
        if elements:
            yield from elements

        for choice in self.choices:
            match = choice.find_choice(qname)
            if match:
                yield match

        chd = self.find_wildcard(qname)
        if chd:
            yield chd


def find_by_namespace(xml_vars: Sequence[XmlVar], qname: str) -> Optional[XmlVar]:
    for xml_var in xml_vars:
        if xml_var.match_namespace(qname):
            return xml_var

    return None
