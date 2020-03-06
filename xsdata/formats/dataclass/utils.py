import re
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
    "str",
    "int",
    "bool",
    "float",
    "list",
    "optional",
    "dict",
]


def safe_snake(string: str, default: str = "value") -> str:
    if not string:
        return default

    # Remove invalid characters
    string = re.sub("[^0-9a-zA-Z_-]", " ", string).strip()

    if not string:
        return default
    elif re.match(r"^-\d*\.?\d+$", string):
        return f"{default}_minus_{string}"
    elif not string[0].isalpha():
        return f"{default}_{string}"
    elif string.lower() in stop_words:
        return f"{string}_{default}"
    else:
        return string.strip("_")


def tostring(elements: List):
    root = etree.Element("xsdata")
    namespaces: Set[str] = set()
    XmlSerializer.set_any_children(root, elements, namespaces)
    nsmap = {f"ns{index}": ns for index, ns in enumerate(sorted(namespaces))}
    etree.cleanup_namespaces(root, top_nsmap=nsmap)
    xml = etree.tostring(root, pretty_print=True).decode()
    return xml[xml.find(">") + 1 :].replace("</xsdata>", "").strip()
