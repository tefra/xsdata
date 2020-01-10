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
]


def safe_snake(input: str) -> str:
    if input.lower() in stop_words:
        return f"{input}_value"
    if input[0].isdigit():
        return f"value_{input}"
    return input
