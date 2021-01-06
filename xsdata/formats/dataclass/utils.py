import re

# python allocated strings

stop_words = [
    "and",
    "except",
    "lambda",
    "with",
    "as",
    "finally",
    "nonlocal",
    "while",
    "assert",
    "false",
    "none",
    "yield",
    "break",
    "for",
    "not",
    "class",
    "from",
    "or",
    "continue",
    "global",
    "pass",
    "def",
    "if",
    "raise",
    "del",
    "import",
    "return",
    "elif",
    "in",
    "true",
    "else",
    "is",
    "try",
    "str",
    "int",
    "bool",
    "float",
    "list",
    "optional",
    "dict",
    "field",
    "decimal",
]


def safe_snake(string: str, default: str = "value") -> str:
    """
    Normalize the given string to make it safe for python source code.

    Return or prepend the default value if after all filters the result
    is invalid.
    """
    if not string:
        return default

    if re.match(r"^-\d*\.?\d+$", string):
        return f"{default}_minus_{string}"

    # Remove invalid characters
    string = re.sub("[^0-9a-zA-Z_-]", " ", string).strip()

    if not string:
        return default

    string = string.strip("_")

    if not string[0].isalpha():
        return f"{default}_{string}"

    if string.lower() in stop_words:
        return f"{string}_{default}"

    return string
