import functools
from typing import Dict
from typing import Optional
from typing import Tuple

from xsdata.models.enums import Namespace
from xsdata.utils.text import split


__uri_ignore__ = ("www", "xsd", "wsdl")


def load_prefix(uri: str, ns_map: Dict) -> Optional[str]:
    """Get or create a prefix for the given uri in the prefix-URI namespace
    mapping."""
    for prefix, ns in ns_map.items():
        if ns == uri:
            return prefix

    return generate_prefix(uri, ns_map)


def generate_prefix(uri: str, ns_map: Dict) -> str:
    """Generate and add a prefix for the given uri in the prefix-URI namespace
    mapping."""
    namespace = Namespace.get_enum(uri)
    if namespace:
        prefix = namespace.prefix
    else:
        number = len(ns_map)
        prefix = f"ns{number}"

    ns_map[prefix] = uri

    return prefix


def prefix_exists(uri: str, ns_map: Dict) -> bool:
    """Check if the uri exists in the prefix-URI namespace mapping."""
    return uri in ns_map.values()


def clean_prefixes(ns_map: Dict) -> Dict:
    """Remove default namespace if it's also assigned to a prefix."""
    result = {}
    for prefix, ns in ns_map.items():
        if ns:
            prefix = prefix or None
            if prefix not in result:
                result[prefix] = ns

    default_ns = result.get(None)
    if default_ns and any(prefix and ns == default_ns for prefix, ns in result.items()):
        result.pop(None)

    return result


def clean_uri(namespace: str) -> str:
    """Remove common prefixes and suffixes from a uri string."""
    if namespace[:2] == "##":
        namespace = namespace[2:]

    left, right = split(namespace)

    if left == "urn":
        namespace = right
    elif left in ("http", "https"):
        namespace = right[2:]

    return "_".join(x for x in namespace.split(".") if x not in __uri_ignore__)


@functools.lru_cache(maxsize=50)
def build_qname(tag_or_uri: Optional[str], tag: Optional[str] = None) -> str:
    """Create namespace qualified strings."""

    if not tag_or_uri:
        if not tag:
            raise ValueError("Invalid input both uri and tag are empty.")

        return tag

    return f"{{{tag_or_uri}}}{tag}" if tag else tag_or_uri


@functools.lru_cache(maxsize=50)
def split_qname(tag: str) -> Tuple:
    """Split namespace qualified strings."""
    if tag[0] == "{":
        left, right = split(tag[1:], "}")
        if left:
            return left, right

    return None, tag
