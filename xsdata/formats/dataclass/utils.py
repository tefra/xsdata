from string import printable
from typing import List
from typing import Set

from lxml import etree

from xsdata.formats.dataclass.serializers import XmlSerializer

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


def safe_snake(string: str) -> str:
    if not string:
        return "empty"

    string = "".join([ch for ch in string if ch in printable])
    if string.lower() in stop_words:
        return f"{string}_value"
    elif string[0].isdigit():
        return f"value_{string}"
    elif string[0] == "-" and string[1].isdigit():
        return f"value_minus_{string[1:]}"
    else:
        return string


def tostring(elements: List):
    root = etree.Element("xsdata")
    namespaces: Set[str] = set()
    XmlSerializer.set_any_children(root, elements, namespaces)
    nsmap = {f"ns{index}": ns for index, ns in enumerate(sorted(namespaces))}
    etree.cleanup_namespaces(root, top_nsmap=nsmap)
    xml = etree.tostring(root, pretty_print=True).decode()
    return xml[xml.find(">") + 1 :].replace("</xsdata>", "").strip()
