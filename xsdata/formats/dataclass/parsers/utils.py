from collections import UserList
from typing import Any, Callable, Dict, Iterable, Optional, Sequence, Type

from xsdata.formats.converter import QNameConverter, converter
from xsdata.models.enums import QNames
from xsdata.utils import collections, constants, text
from xsdata.utils.namespaces import build_qname


class PendingCollection(UserList):
    """An iterable implementation of parsed values.

    The values are parsed individually in the end we
    need to convert it to a tuple or a list based on
    the mutability setting of the data class.

    Args:
        initlist: An initial list of values or None
        factory: A callable factory for the values
            when the node parse has finished.

    """

    def __init__(self, initlist: Optional[Iterable], factory: Optional[Callable]):
        super().__init__(initlist)
        self.factory = factory or list

    def evaluate(self) -> Iterable[Any]:
        """Evaluate the values factory and return the result.

        Returns:
            A list or tuple or set of values
        """
        return self.factory(self.data)


class ParserUtils:
    """Random parser util functions."""

    @classmethod
    def xsi_type(cls, attrs: Dict, ns_map: Dict) -> Optional[str]:
        """Parse the xsi:type attribute value if present.

        Args:
            attrs: The element attributes
            ns_map: The element namespace prefix-URI map

        Returns:
            The xsi:type attribute value or None
        """
        xsi_type = attrs.get(QNames.XSI_TYPE)
        if not xsi_type:
            return None

        namespace, name = QNameConverter.resolve(xsi_type, ns_map)
        return build_qname(namespace, name)

    @classmethod
    def xsi_nil(cls, attrs: Dict) -> Optional[bool]:
        """Return whether xsi:nil attribute value.

        Args:
            attrs: The element attributes

        Returns:
            The bool value or None if it doesn't exist.
        """
        xsi_nil = attrs.get(QNames.XSI_NIL)
        return xsi_nil == constants.XML_TRUE if xsi_nil else None

    @classmethod
    def parse_value(
        cls,
        value: Any,
        types: Sequence[Type],
        default: Optional[Any] = None,
        ns_map: Optional[Dict] = None,
        tokens_factory: Optional[Callable] = None,
        format: Optional[str] = None,
    ) -> Any:
        """Convert a value to a python primitive type.

        Args:
            value: A primitive value or a list of primitive values
            types: An iterable of types to try to convert the value
            default: The default value/factory if the given is None
            ns_map: The element namespace prefix-URI map
            tokens_factory: A callable factory for the converted values
                if the element is derived from xs:NMTOKENS
            format: The format argument for base64/hex values or dates.

        Returns:
            The converted value or values.
        """
        if value is None:
            if callable(default):
                return default() if tokens_factory else None

            return default

        if tokens_factory:
            value = value if collections.is_array(value) else value.split()
            return tokens_factory(
                converter.deserialize(val, types, ns_map=ns_map, format=format)
                for val in value
            )

        return converter.deserialize(value, types, ns_map=ns_map, format=format)

    @classmethod
    def normalize_content(cls, value: Optional[str]) -> Optional[str]:
        """Normalize element text or tail content.

        If content is just whitespace return None, otherwise preserve
        the original content.

        Args:
            value: The element content

        Returns:
            The normalized content
        """
        if value and value.strip():
            return value

        return None

    @classmethod
    def parse_any_attributes(
        cls, attrs: Dict[str, str], ns_map: Dict[Optional[str], str]
    ) -> Dict[str, str]:
        """Parse attributes with qname support.

        Example:
            {"foo": "bar", "xsi:type": "my:type"} ->
            {"foo": "bar", "xsi:type" "{http://someuri.com}type"}

        Args:
            attrs: The element attributes
            ns_map: The element namespace prefix-URI map

        Returns:
            The parsed attributes with expanded namespace prefixes
        """
        return {
            key: cls.parse_any_attribute(value, ns_map) for key, value in attrs.items()
        }

    @classmethod
    def parse_any_attribute(cls, value: str, ns_map: Dict) -> str:
        """Expand the value with the full namespace if it has a prefix.

        Args:
            value: The attr value
            ns_map: The element namespace prefix-URI map

        Returns:
            The expanded value.
        """
        prefix, suffix = text.split(value)
        if prefix and prefix in ns_map and not suffix.startswith("//"):
            value = build_qname(ns_map[prefix], suffix)

        return value
