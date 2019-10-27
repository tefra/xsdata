from typing import List, Optional


def capitalize(string: Optional[str]) -> str:
    if string is None:
        return ""

    return string[0].upper() + string[1:]


def pascal_case(string: Optional[str]) -> str:
    if string is None:
        return ""

    return "".join(
        [
            capitalize(part)
            for part in snake_case(string).split("_")
            if part is not None
        ]
    )


def snake_case(string: Optional[str]) -> str:
    if string is None:
        return ""

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
    return "".join(result)
