import itertools
import operator
import sys
from typing import (
    Any,
    Callable,
    Dict,
    Iterator,
    List,
    Mapping,
    Optional,
    Sequence,
    Set,
    Tuple,
    Type,
)

from xsdata.formats.converter import converter
from xsdata.models.enums import NamespaceType
from xsdata.utils import collections
from xsdata.utils.namespaces import local_name, target_uri

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
        """Implement equality operator."""
        return tuple(self) == tuple(other)

    def __iter__(self) -> Iterator:
        """Implement iteration."""
        for name in self.__slots__:
            yield getattr(self, name)

    def __repr__(self) -> str:
        """Implement representation."""
        params = (f"{name}={getattr(self, name)!r}" for name in self.__slots__)
        return f"{self.__class__.__qualname__}({', '.join(params)})"


class XmlVar(MetaMixin):
    """Class field binding metadata.

    Args:
        index: Position index of the variable
        name: Name of the variable
        qname: Namespace-qualified name of the variable
        types: Supported types for the variable
        clazz: Target class type
        init: Indicates if the field should be included in the constructor
        mixed: Indicates if the field supports mixed content type values.
        factory: Callable factory for lists
        tokens_factory: Callable factory for tokens
        format: Information about the value format
        any_type: Indicates if the field supports dynamic value types
        process_contents: Information about processing contents
        required: Indicates if the field is mandatory
        nillable: Indicates if the field supports nillable content
        sequence: Specifies rendering values in sequential mode
        default: Default value or factory for the field
        xml_type: Type of the XML field (element, attribute, etc.)
        namespaces: List of supported namespaces
        elements: Mapping of qualified name-repeatable elements
        wildcards: List of repeatable wildcards
        wrapper: Name for the wrapper (applies for list types only)

    Attributes:
        tokens: Indicates if the field has associated tokens
        list_element: Indicates if the field is a list or tuple element
        namespace_matches: Matching namespaces information
        is_clazz_union: Indicates if the field is a union of multiple types
        local_name: Local name extracted from the qualified name
        is_text: Indicates if the field represents text content
        is_element: Indicates if the field represents an XML element
        is_elements: Indicates if the field represents a sequence of XML elements
        is_wildcard: Indicates if the field represents a wildcard
        is_attribute: Indicates if the field represents an XML attribute
        is_attributes: Indicates if the field represents a sequence of XML attributes
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
        "any_type",
        "process_contents",
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
        any_type: bool,
        process_contents: str,
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
        self.any_type = any_type
        self.process_contents = process_contents
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

        if xml_type == XmlType.ELEMENTS:
            self.is_elements = True
        elif xml_type == XmlType.ELEMENT or self.clazz:
            self.is_element = True
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
        """Return the unique element types."""
        return {tp for element in self.elements.values() for tp in element.types}

    def find_choice(self, qname: str) -> Optional["XmlVar"]:
        """Match and return a choice field by its qualified name.

        Args:
            qname: The qualified name to lookup

        Returns:
            The choice xml var instance or None if there are no matches.
        """
        match = self.elements.get(qname)
        return match or find_by_namespace(self.wildcards, qname)

    def find_value_choice(self, value: Any, is_class: bool) -> Optional["XmlVar"]:
        """Match and return a choice field that matches the given value.

        Cases:
            - value is none or empty tokens list: look for a nillable choice
            - value is a dataclass: look for exact type or a subclass
            - value is primitive: test value against the converter

        Args:
            value: The value to match its type to one of the choices
            is_class: Whether the value is a binding class

        Returns:
            The choice xml var instance or None if there are no matches.
        """
        is_tokens = collections.is_array(value)
        if value is None or (not value and is_tokens):
            return self.find_nillable_choice(is_tokens)

        if is_class:
            return self.find_clazz_choice(type(value))

        return self.find_primitive_choice(value, is_tokens)

    def find_nillable_choice(self, is_tokens: bool) -> Optional["XmlVar"]:
        """Find the first nillable choice.

        Args:
            is_tokens: Specify if the choice must support token values

        Returns:
            The choice xml var instance or None if there are no matches.
        """
        return collections.first(
            element
            for element in self.elements.values()
            if element.nillable and is_tokens == element.tokens
        )

    def find_clazz_choice(self, clazz: Type) -> Optional["XmlVar"]:
        """Find the best matching choice for the given class.

        Best Matches:
            1. The class is explicitly defined in a choice types
            2. The class is a subclass of one of the choice types

        Args:
            clazz: The class type to match

        Returns:
            The choice xml var instance or None if there are no matches.
        """
        derived = None
        for element in self.elements.values():
            if not element.clazz:
                continue

            if clazz in element.types:
                return element

            if derived is None and any(issubclass(clazz, t) for t in element.types):
                derived = element

        return derived

    def find_primitive_choice(self, value: Any, is_tokens: bool) -> Optional["XmlVar"]:
        """Match and return a choice field that matches the given primitive value.

        Args:
            value: A primitive value, e.g. str, int, float, enum
            is_tokens: Specify whether it's a tokens value

        Returns:
            The choice xml var instance or None if there are no matches.
        """
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
        """Verify this var is optional and the value matches the default one.

        Args:
            value: The value to compare against the default one

        Returns:
            The bool result.
        """
        if self.required:
            return False

        if callable(self.default):
            return self.default() == value
        return self.default == value

    def match_namespace(self, qname: str) -> bool:
        """Match the given qname to the wildcard allowed namespaces.

        Args:
            qname: The namespace qualified name of an element

        Returns:
            The bool result.
        """
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
    """Class binding metadata.

    Args:
        clazz: The binding model
        qname: The namespace-qualified name
        target_qname: The target namespace-qualified name
        nillable: Specifies whether this class supports nillable content
        text: A text variable
        choices: A list of compound variables
        elements: A mapping of qualified name to sequence of element variables
        wildcards: A list of wildcard variables
        attributes: A mapping of qualified name to attribute variable
        any_attributes: A list of wildcard variables
        wrappers: a mapping of wrapper names to sequences of wrapped variables

    Attributes:
        namespace: The target namespace extracted from the qualified name
        mixed_content: Specifies if the class supports mixed content
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
        """Return a unique list of all elements types."""
        return {
            tp
            for elements in self.elements.values()
            for element in elements
            for tp in element.types
        }

    def get_element_vars(self) -> List[XmlVar]:
        """Return a sorted list of the class element variables."""
        result = list(
            itertools.chain(self.wildcards, self.choices, *self.elements.values())
        )
        if self.text:
            result.append(self.text)

        return sorted(result, key=get_index)

    def get_attribute_vars(self) -> List[XmlVar]:
        """Return a sorted list of the class attribute variables."""
        result = itertools.chain(self.any_attributes, self.attributes.values())
        return sorted(result, key=get_index)

    def get_all_vars(self) -> List[XmlVar]:
        """Return a sorted list of all the class variables."""
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
        """Find an attribute var with the given qname.

        Args:
            qname: The namespace qualified name

        Returns:
            The xml var instance or None if there is no match.
        """
        return self.attributes.get(qname)

    def find_any_attributes(self, qname: str) -> Optional[XmlVar]:
        """Find a wildcard attribute var that matches the given qname.

        Args:
            qname: The namespace qualified name

        Returns:
            The xml var instance or None if there is no match.
        """
        return find_by_namespace(self.any_attributes, qname)

    def find_wildcard(self, qname: str) -> Optional[XmlVar]:
        """Find a wildcard var that matches the given qname.

        If the wildcard has choices, attempt to match and return
        one of them as well.

        Args:
            qname: The namespace qualified name

        Returns:
            The xml var instance or None if there is no match.
        """
        wildcard = find_by_namespace(self.wildcards, qname)

        if wildcard and wildcard.elements:
            choice = wildcard.find_choice(qname)
            if choice:
                return choice

        return wildcard

    def find_any_wildcard(self) -> Optional[XmlVar]:
        """Return the first declared wildcard var.

        Returns:
            The xml var instance or None if there are no wildcard vars.
        """
        return self.wildcards[0] if self.wildcards else None

    def find_children(self, qname: str) -> Iterator[XmlVar]:
        """Find all class vars that match the given qname.

        Go through the elements, choices and wildcards. Sometimes
        a class might contain more than one var with the same
        qualified name. The binding process has to check all
        of them and see which one to use.

        Args:
            qname: The namespace qualified name

        Yields:
            An iterator of all the class vars that match the given qname.
        """
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


def find_by_namespace(vars: Sequence[XmlVar], qname: str) -> Optional[XmlVar]:
    """Match the given qname to one of the given vars.

    Args:
        vars: The list of vars to match
        qname: The namespace qualified name to lookup

    Returns:
        The first matching xml var instance or None if there are no matches.
    """
    for xml_var in vars:
        if xml_var.match_namespace(qname):
            return xml_var

    return None
