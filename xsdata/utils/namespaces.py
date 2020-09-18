from typing import Dict
from typing import Optional

from xsdata.models.enums import Namespace


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
    return any(val == uri for val in ns_map.values())


def clean_prefixes(ns_map: Dict) -> Dict:
    """Remove default namespace if it's also assigned to a prefix."""
    result = {}
    for prefix, uri in ns_map.items():
        if uri:
            prefix = prefix or None
            if prefix not in result:
                result[prefix] = uri

    default_prefix = result.get(None)
    if default_prefix and any(
        True for prefix, uri in result.items() if prefix and uri == default_prefix
    ):
        result.pop(None)

    return result
