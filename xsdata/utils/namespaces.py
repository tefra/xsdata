import functools
import re
from typing import Dict
from typing import Optional
from typing import Tuple

from xsdata.models.enums import Namespace
from xsdata.utils import text

__uri_ignore__ = ("www", "xsd", "wsdl")

URI_REGEX = re.compile(
    r"^(([a-zA-Z][0-9a-zA-Z+\\-\\.]*:)?"
    r"/{0,2}[0-9a-zA-Z;/?:@&=+$\\.\\-_!~*'()%]+)?"
    r"(#[0-9a-zA-Z;/?:@&=+$\\.\\-_!~*'()%]+)?$"
)


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


def is_default(uri: str, ns_map: Dict) -> bool:
    """Check if the uri exists and it has no prefix."""
    for prefix, ns in ns_map.items():
        if uri == ns and not prefix:
            return True

    return False


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

    left, right = text.split(namespace)

    if left == "urn":
        namespace = right
    elif left in ("http", "https"):
        namespace = right[2:]

    return "_".join(x for x in namespace.split(".") if x not in __uri_ignore__)


def real_xsi_type(qname: str, target_qname: Optional[str]) -> Optional[str]:
    """Determine if the given target qualified name should be used to define a
    derived type."""
    return target_qname if target_qname != qname else None


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
        left, right = text.split(tag[1:], "}")
        if left:
            return left, right

    return None, tag


def target_uri(tag: str) -> Optional[str]:
    return split_qname(tag)[0]


def local_name(tag: str) -> str:
    return split_qname(tag)[1]


NCNAME_PUNCTUATION = {"\u00B7", "\u0387", ".", "-", "_"}


def is_ncname(name: Optional[str]) -> bool:
    """Verify given string is a valid ncname."""
    if not name:
        return False

    char = name[0]
    if not char.isalpha() and not char == "_":
        return False

    for char in name[1:]:
        if char.isalpha() or char.isdigit() or char in NCNAME_PUNCTUATION:
            continue
        else:
            return False

    return True


def is_uri(uri: Optional[str]) -> bool:
    """Verify given string is a valid uri."""
    return bool(URI_REGEX.search(uri)) if uri else False


@functools.lru_cache(maxsize=50)
def to_package_name(uri: Optional[str]) -> str:
    """Util method to convert a namespace to a dot style package name."""
    if not uri:
        return ""

    # Remove scheme
    domain_sep = "."
    if uri.startswith("http://"):
        uri = uri[7:]
    elif uri.startswith("urn:"):
        uri = uri[4:]
        domain_sep = "-"

        if uri.startswith("xmlns:"):
            uri = uri[6:]

        uri = uri.replace(":", "/")

    # Remote target
    pos = uri.find("#")
    if pos > 0:
        uri = uri[:pos]

    tokens = [token for token in uri.split("/") if token.strip()]

    if not tokens:
        return ""

    # Remove extension
    if len(tokens) > 1:
        last = tokens[-1]
        pos = tokens[-1].rfind(".")
        if pos > 0:
            tokens[-1] = last[:pos]

    # Remove port from domain
    domain = tokens.pop(0)
    pos = domain.find(":")
    if pos > 0:
        domain = domain[:pos]

    # Remove www from domain
    if domain.startswith("www"):
        domain = domain[3:]

    for part in domain.split(domain_sep):
        tokens.insert(0, part)

    return ".".join(token for token in tokens if token)
