import re
from typing import Any
from typing import List
from typing import Match
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


def capitalize(string: str, **kwargs: Any) -> str:
    """Capitalize the given string."""
    return string[0].upper() + string[1:]


def pascal_case(string: str, **kwargs: Any) -> str:
    """Convert the given string to pascal case."""
    return "".join(map(str.title, split_words(string)))


def camel_case(string: str, **kwargs: Any) -> str:
    """Convert the given string to camel case."""
    result = "".join(map(str.title, split_words(string)))
    return result[0].lower() + result[1:]


def mixed_case(string: str, **kwargs: Any) -> str:
    """Convert the given string to mixed case."""
    return "".join(split_words(string))


def mixed_pascal_case(string: str, **kwargs: Any) -> str:
    """Convert the given string to mixed pascal case."""
    return capitalize(mixed_case(string))


def mixed_snake_case(string: str, **kwargs: Any) -> str:
    """Convert the given string to mixed snake case."""
    return "_".join(split_words(string))


def snake_case(string: str, **kwargs: Any) -> str:
    """Convert the given string to snake case."""
    return "_".join(map(str.lower, split_words(string)))


def kebab_case(string: str, **kwargs: Any) -> str:
    """Convert the given string to kebab case."""
    return "-".join(split_words(string))


def split_words(string: str) -> List[str]:
    """Split a string on new capital letters and not alphanumeric
    characters."""
    words: List[str] = []
    buffer: List[str] = []
    previous = None

    def flush():
        if buffer:
            words.append("".join(buffer))
            buffer.clear()

    for char in string:
        tp = classify(char)
        if tp == StringType.OTHER:
            flush()
        elif not previous or tp == previous:
            buffer.append(char)
        elif tp == StringType.UPPER and previous != StringType.UPPER:
            flush()
            buffer.append(char)
        else:
            buffer.append(char)

        previous = tp

    flush()
    return words


class StringType:
    UPPER = 1
    LOWER = 2
    NUMERIC = 3
    OTHER = 4


def classify(character: str) -> int:
    """String classifier."""
    if character.isupper():
        return StringType.UPPER
    if character.islower():
        return StringType.LOWER
    if character.isnumeric():
        return StringType.NUMERIC

    return StringType.OTHER


ESCAPE = re.compile(r'[\x00-\x1f\\"\b\f\n\r\t]')
ESCAPE_DCT = {
    "\\": "\\\\",
    '"': '\\"',
    "\b": "\\b",
    "\f": "\\f",
    "\n": "\\n",
    "\r": "\\r",
    "\t": "\\t",
}
for i in range(0x20):
    ESCAPE_DCT.setdefault(chr(i), f"\\u{i:04x}")


def escape_string(string: str) -> str:
    """
    Escape a string for code generation.

    Source: json.encoder.py_encode_basestring
    """

    def replace(match: Match) -> str:
        return ESCAPE_DCT[match.group(0)]

    return ESCAPE.sub(replace, string)
