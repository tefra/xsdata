import re
import string
from re import Match
from typing import Any

stop_words = {
    "",
    "Any",
    "Decimal",
    "Enum",
    "False",
    "Meta",
    "None",
    "Optional",
    "QName",
    "True",
    "Union",
    "and",
    "as",
    "assert",
    "async",
    "bool",
    "break",
    "class",
    "continue",
    "def",
    "del",
    "dict",
    "elif",
    "else",
    "except",
    "field",
    "Field",
    "finally",
    "float",
    "for",
    "from",
    "global",
    "if",
    "import",
    "in",
    "int",
    "is",
    "lambda",
    "list",
    "nonlocal",
    "not",
    "object",
    "or",
    "pass",
    "raise",
    "return",
    "self",
    "str",
    "try",
    "type",
    "validate",
    "while",
    "with",
    "yield",
}

is_reserved = stop_words.__contains__


def prefix(value: str, sep: str = ":") -> str:
    """Return the first part of the string before the separator."""
    return split(value, sep)[0]


def suffix(value: str, sep: str = ":") -> str:
    """Return the last part of the string after the separator."""
    return split(value, sep)[1]


def split(value: str, sep: str = ":") -> tuple:
    """Split the given value with the given separator once."""
    left, _, right = value.partition(sep)
    return (left, right) if right else (None, left)


def capitalize(value: str, **kwargs: Any) -> str:
    """Capitalize the given string."""
    return value[0].upper() + value[1:]


def original_case(value: str, **kwargs: Any) -> str:
    """Return the input string but ensure it's a valid Python variable."""
    # Strip out all characters that are not alphanumeric or underscores
    value = re.sub(r"\W", "", value)
    # Then strip out leading digit and underscore characters
    return re.sub(r"^[^a-zA-Z_]+", "", value)


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


def split_words(value: str) -> list[str]:
    """Split a string on capital letters and not alphanumeric characters."""
    words: list[str] = []
    buffer: list[str] = []
    previous = None

    def flush() -> None:
        if buffer:
            words.append("".join(buffer))
            buffer.clear()

    for char in value:
        tp = classify(char)
        if tp == CharType.OTHER:
            flush()
        elif not previous or tp == previous:
            buffer.append(char)
        elif tp == CharType.UPPER and previous != CharType.UPPER:
            flush()
            buffer.append(char)
        else:
            buffer.append(char)

        previous = tp

    flush()
    return words


class CharType:
    """Character types."""

    UPPER = 1
    LOWER = 2
    NUMERIC = 3
    OTHER = 4


def classify(character: str) -> int:
    """String classifier."""
    code_point = ord(character)
    if 64 < code_point < 91:
        return CharType.UPPER

    if 96 < code_point < 123:
        return CharType.LOWER

    if 47 < code_point < 58:
        return CharType.NUMERIC

    return CharType.OTHER


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
    """Escape a string for code generation."""

    def replace(match: Match) -> str:
        return ESCAPE_DCT[match.group(0)]

    return ESCAPE.sub(replace, value)


__alnum_ascii__ = set(string.digits + string.ascii_letters)


def alnum(value: str) -> str:
    """Return the ascii alphanumerical characters in lower case."""
    return "".join(filter(__alnum_ascii__.__contains__, value)).lower()
