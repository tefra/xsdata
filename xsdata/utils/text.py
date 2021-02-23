import re
import string
from typing import Any
from typing import List
from typing import Match
from typing import Tuple


def prefix(value: str, sep: str = ":") -> str:
    """Return the first part of the string before the separator."""
    return split(value, sep)[0]


def suffix(value: str, sep: str = ":") -> str:
    """Return the last part of the string after the separator."""
    return split(value, sep)[1]


def split(value: str, sep: str = ":") -> Tuple:
    """
    Separate the given string with the given separator and return a tuple of
    the prefix and suffix.

    If the separator isn't present in the string return None as prefix.
    """
    left, _, right = value.partition(sep)
    return (left, right) if right else (None, left)


def capitalize(value: str, **kwargs: Any) -> str:
    """Capitalize the given string."""
    return value[0].upper() + value[1:]


def pascal_case(value: str, **kwargs: Any) -> str:
    """Convert the given string to pascal case."""
    return "".join(map(str.title, split_words(value)))


def camel_case(value: str, **kwargs: Any) -> str:
    """Convert the given string to camel case."""
    result = "".join(map(str.title, split_words(value)))
    return result[0].lower() + result[1:]


def mixed_case(value: str, **kwargs: Any) -> str:
    """Convert the given string to mixed case."""
    return "".join(split_words(value))


def mixed_pascal_case(value: str, **kwargs: Any) -> str:
    """Convert the given string to mixed pascal case."""
    return capitalize(mixed_case(value))


def mixed_snake_case(value: str, **kwargs: Any) -> str:
    """Convert the given string to mixed snake case."""
    return "_".join(split_words(value))


def snake_case(value: str, **kwargs: Any) -> str:
    """Convert the given string to snake case."""
    return "_".join(map(str.lower, split_words(value)))


def screaming_snake_case(value: str, **kwargs: Any) -> str:
    """Convert the given string to screaming snake case."""
    return snake_case(value, **kwargs).upper()


def kebab_case(value: str, **kwargs: Any) -> str:
    """Convert the given string to kebab case."""
    return "-".join(split_words(value))


def split_words(value: str) -> List[str]:
    """Split a string on new capital letters and not alphanumeric
    characters."""
    words: List[str] = []
    buffer: List[str] = []
    previous = None

    def flush():
        if buffer:
            words.append("".join(buffer))
            buffer.clear()

    for char in value:
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


def escape_string(value: str) -> str:
    """
    Escape a string for code generation.

    Source: json.encoder.py_encode_basestring
    """

    def replace(match: Match) -> str:
        return ESCAPE_DCT[match.group(0)]

    return ESCAPE.sub(replace, value)


_punctuation = set(string.punctuation + string.whitespace)


def alnum(value: str) -> str:
    for remove in set(value).intersection(_punctuation):
        value = value.replace(remove, "")

    return value.lower()
