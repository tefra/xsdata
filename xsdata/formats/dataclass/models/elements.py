from __future__ import annotations

import itertools
import operator
import sys
from collections.abc import Callable, Iterator, Mapping, Sequence
from typing import Any

from xsdata.formats.converter import converter
from xsdata.models.enums import NamespaceType
from xsdata.utils import collections
from xsdata.utils.namespaces import build_qname, target_uri

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

    __slots__: tuple[str, ...] = ()

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


def default_namespace(namespaces: Sequence[str]) -> str | None:
    """Return the first valid namespace uri or None.

    Args:
        namespaces: A list of namespace options which may include
            valid uri(s) or a placeholder e.g. ##any, ##other,
            ##targetNamespace, ##local

    Returns:
        A namespace uri or None if there isn't any.
    """
    for namespace in namespaces:
        if namespace and not namespace.startswith("#"):
            return namespace

    return None


class XmlVar(MetaMixin):
    """Class field binding metadata.

    Args:
        index: Position index of the variable
        name: Name of the variable
        local_name: Local name of the variable
        wrapper: The element wrapper name
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

    Attributes:
        qname: Namespace-qualified name of the variable
        wrapper_qname: Namespace-qualified name of the variable wrapper
        tokens: Indicates if the field has associated tokens
        list_element: Indicates if the field is a list or tuple element
        namespace_matches: Matching namespaces information
        is_clazz_union: Indicates if the field is a union of multiple types
        is_text: Indicates if the field represents text content
        is_element: Indicates if the field represents an XML element
        is_elements: Indicates if the field represents a sequence of XML elements
        is_wildcard: Indicates if the field represents a wildcard
        is_attribute: Indicates if the field represents an XML attribute
        is_attributes: Indicates if the field represents a sequence of XML attributes
    """

    __slots__ = (
        "any_type",
        "clazz",
        "default",
        "elements",
        "factory",
        "format",
        "index",
        "init",
        "is_attribute",
        "is_attributes",
        "is_clazz_union",
        "is_element",
        "is_elements",
        "is_text",
        "is_wildcard",
        "list_element",
        "local_name",
        "mixed",
        "name",
        "namespace_matches",
        "namespaces",
        "nillable",
        "process_contents",
        # Calculated
        "qname",
        "required",
        "sequence",
        "tokens",
        "tokens_factory",
        "types",
        "wildcards",
        "wrapper",
        "wrapper_qname",
    )

    def __init__(
        self,
        index: int,
        name: str,
        local_name: str,
        wrapper: str | None,
        types: Sequence[type],
        clazz: type | None,
        init: bool,
        mixed: bool,
        factory: Callable | None,
        tokens_factory: Callable | None,
        format: str | None,
        any_type: bool,
        process_contents: str,
        required: bool,
        nillable: bool,
        sequence: int | None,
        default: Any,
        xml_type: str,
        namespaces: Sequence[str],
        elements: Mapping[str, XmlVar],
        wildcards: Sequence[XmlVar],
        **kwargs: Any,
    ):
        """Initialize the xml var."""
        self.index = index
        self.name = name
        self.local_name = local_name
        self.wrapper = wrapper
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

        self.namespace_matches: dict[str, bool] | None = None
        self.is_clazz_union = self.clazz and len(types) > 1

        namespace = default_namespace(namespaces)

        self.qname = build_qname(namespace, local_name)
        self.wrapper_qname = None
        if wrapper:
            self.wrapper_qname = build_qname(namespace, wrapper)

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
    def element_types(self) -> set[type]:
        """Return the unique element types."""
        return {tp for element in self.elements.values() for tp in element.types}

    def find_choice(self, qname: str) -> XmlVar | None:
        """Match and return a choice field by its qualified name.

        Args:
            qname: The qualified name to lookup

        Returns:
            The choice xml var instance or None if there are no matches.
        """
        match = self.elements.get(qname)
        return match or find_by_namespace(self.wildcards, qname)

    def find_value_choice(self, value: Any, is_class: bool) -> XmlVar | None:
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

    def find_nillable_choice(self, is_tokens: bool) -> XmlVar | None:
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

    def find_clazz_choice(self, clazz: type) -> XmlVar | None:
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

    def find_primitive_choice(self, value: Any, is_tokens: bool) -> XmlVar | None:
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
                or check in (uri, NamespaceType.ANY_NS)
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
        "any_attributes",
        "attributes",
        "choices",
        "clazz",
        "elements",
        "mixed_content",
        # Calculated
        "namespace",
        "nillable",
        "qname",
        "target_qname",
        "text",
        "wildcards",
        "wrappers",
    )

    def __init__(
        self,
        clazz: type,
        qname: str,
        target_qname: str | None,
        nillable: bool,
        text: XmlVar | None,
        choices: Sequence[XmlVar],
        elements: Mapping[str, Sequence[XmlVar]],
        wildcards: Sequence[XmlVar],
        attributes: Mapping[str, XmlVar],
        any_attributes: Sequence[XmlVar],
        wrappers: Mapping[str, str],
        **kwargs: Any,
    ):
        """Initialize the xml meta."""
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
    def element_types(self) -> set[type]:
        """Return a unique list of all elements types."""
        return {
            tp
            for elements in self.elements.values()
            for element in elements
            for tp in element.types
        }

    def get_element_vars(self) -> list[XmlVar]:
        """Return a sorted list of the class element variables."""
        result = list(
            itertools.chain(self.wildcards, self.choices, *self.elements.values())
        )
        if self.text:
            result.append(self.text)

        return sorted(result, key=get_index)

    def get_attribute_vars(self) -> list[XmlVar]:
        """Return a sorted list of the class attribute variables."""
        result = itertools.chain(self.any_attributes, self.attributes.values())
        return sorted(result, key=get_index)

    def get_all_vars(self) -> list[XmlVar]:
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

    def find_attribute(self, qname: str) -> XmlVar | None:
        """Find an attribute var with the given qname.

        Args:
            qname: The namespace qualified name

        Returns:
            The xml var instance or None if there is no match.
        """
        return self.attributes.get(qname)

    def find_any_attributes(self, qname: str) -> XmlVar | None:
        """Find a wildcard attribute var that matches the given qname.

        Args:
            qname: The namespace qualified name

        Returns:
            The xml var instance or None if there is no match.
        """
        return find_by_namespace(self.any_attributes, qname)

    def find_wildcard(self, qname: str) -> XmlVar | None:
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

    def find_any_wildcard(self) -> XmlVar | None:
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


def find_by_namespace(vars: Sequence[XmlVar], qname: str) -> XmlVar | None:
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
