from typing import List
from typing import Optional
from typing import Tuple


def strip_prefix(string: str, prefix: Optional[str]):
    return (
        string[len(prefix) + 1 :]
        if prefix and string.startswith(f"{prefix}:", 0)
        else string
    )


def prefix(string: Optional[str], sep: str = ":"):
    return split(string, sep)[0] if string else string


def suffix(string: Optional[str], sep: str = ":"):
    return split(string, sep)[1] if string else string


def split(string: str, sep: str = ":") -> Tuple:
    index = string.find(sep)
    if index == -1:
        return None, string
    else:
        return string[:index], string[index + len(sep) :]


def collapse_whitespace(string: str):
    return " ".join([part for part in string.split(" ") if part.strip()])


def capitalize(string: str) -> str:
    return string[0].upper() + string[1:]


def pascal_case(string: str) -> str:
    return "".join([capitalize(part) for part in snake_case(string).split("_") if part])


def camel_case(string: str) -> str:
    string = pascal_case(string)
    return string[0].lower() + string[1:]


def snake_case(string: str) -> str:
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
