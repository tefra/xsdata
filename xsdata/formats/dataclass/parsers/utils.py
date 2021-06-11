from typing import Any
from typing import Dict
from typing import Optional
from typing import Sequence
from typing import Type

from xsdata.formats.converter import converter
from xsdata.formats.converter import QNameConverter
from xsdata.models.enums import QNames
from xsdata.utils import constants
from xsdata.utils import text
from xsdata.utils.namespaces import build_qname


class ParserUtils:
    @classmethod
    def xsi_type(cls, attrs: Dict, ns_map: Dict) -> Optional[str]:
        """Parse the xsi:type attribute if present."""
        xsi_type = attrs.get(QNames.XSI_TYPE)
        if not xsi_type:
            return None

        namespace, name = QNameConverter.resolve(xsi_type, ns_map)
        return build_qname(namespace, name)

    @classmethod
    def is_nillable(cls, attrs: Dict) -> bool:
        """Return whether the element attrs has xsi:nil="false"."""
        return attrs.get(QNames.XSI_NIL) != constants.XML_FALSE

    @classmethod
    def parse_value(
        cls,
        value: Any,
        types: Sequence[Type],
        default: Any = None,
        ns_map: Optional[Dict] = None,
        tokens: bool = False,
        _format: Optional[str] = None,
    ) -> Any:
        """Convert xml string values to s python primitive type."""

        if value is None:

            if callable(default):
                return default() if tokens else None

            return default

        if tokens:
            value = value if isinstance(value, list) else value.split()
            return [
                converter.deserialize(val, types, ns_map=ns_map, format=_format)
                for val in value
            ]

        return converter.deserialize(value, types, ns_map=ns_map, format=_format)

    @classmethod
    def normalize_content(cls, value: Optional[str]) -> Optional[str]:
        """
        Normalize element text or tail content.

        If content is just whitespace return None, otherwise preserve
        the original content.
        """
        if value and value.strip():
            return value

        return None

    @classmethod
    def parse_any_attributes(cls, attrs: Dict, ns_map: Dict) -> Dict:
        return {
            key: cls.parse_any_attribute(value, ns_map) for key, value in attrs.items()
        }

    @classmethod
    def parse_any_attribute(cls, value: str, ns_map: Dict) -> str:
        """Attempt to parse any attribute."""
        prefix, suffix = text.split(value)
        if prefix and prefix in ns_map and not suffix.startswith("//"):
            value = build_qname(ns_map[prefix], suffix)

        return value
