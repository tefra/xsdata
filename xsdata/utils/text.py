from typing import List, Tuple


def strip_prefix(string: str, sep: str = ":") -> str:
    prefix, string = split_prefix(string, sep)
    return string


def split_prefix(string: str, sep: str = ":") -> Tuple:
    index = string.find(sep)
    if index == -1:
        return None, string
    else:
        return string[:index], string[index + len(sep) :]


def capitalize(string: str) -> str:
    return string[0].upper() + string[1:]


def pascal_case(string: str) -> str:
    return "".join(
        [capitalize(part) for part in snake_case(string).split("_") if part]
    )


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
