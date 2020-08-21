from typing import List
from typing import Optional
from typing import Tuple


def prefix(string: str, sep: str = ":") -> str:
    """Return the first part of the string before the separator."""
    return split(string, sep)[0]


def suffix(string: str, sep: str = ":") -> str:
    """Return the last part of the string after the separator."""
    return split(string, sep)[1]


def split(string: str, sep: str = ":") -> Tuple:
    """
    Separate the given string with the given separator and return a tuple of
    the prefix and suffix.

    If the separator isn't present in the string return None as prefix.
    """
    left, _, right = string.partition(sep)
    return (left, right) if right else (None, left)


def capitalize(string: str) -> str:
    """Capitalize the given string."""
    return string[0].upper() + string[1:]


def pascal_case(string: str) -> str:
    """Convert the given string to pascal case."""
    return "".join([capitalize(part) for part in snake_case(string).split("_") if part])


def snake_case(string: str) -> str:
    """Convert the given string to snake case."""
    result: List[str] = []
    was_upper = False
    for char in string:

        if char.isalnum():
            if char.isupper():
                if not was_upper and result and result[-1] != "_":
                    result.append("_")
                was_upper = True
            else:
                was_upper = False
            result.append(char.lower())
        else:
            was_upper = False
            if result and result[-1] != "_":
                result.append("_")
    return "".join(result).strip("_")


def clean_uri(namespace: str) -> str:
    """Remove common prefixes and suffixes from a uri string."""
    if namespace[:2] == "##":
        namespace = namespace[2:]

    left, right = split(namespace)

    if left == "urn":
        namespace = right
    elif left in ("http", "https"):
        namespace = right[2:]

    return "_".join(
        [part for part in namespace.split(".") if part not in ("www", "xsd", "wsdl")]
    )


def qname(tag_or_uri: Optional[str], tag: Optional[str] = None) -> str:
    """Create namespace qualified strings."""

    if not tag_or_uri:
        if not tag:
            raise ValueError("Invalid input both uri and tag are empty.")

        return tag

    return f"{{{tag_or_uri}}}{tag}" if tag else tag_or_uri


def split_qname(tag: str) -> Tuple:
    """Split namespace qualified strings."""
    if tag[0] == "{":
        return tuple(tag[1:].split("}", 1))
    else:
        return None, tag
