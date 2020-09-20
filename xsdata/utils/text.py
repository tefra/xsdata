from typing import List
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
