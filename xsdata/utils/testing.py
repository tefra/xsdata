import importlib
from pathlib import Path
from typing import TypeVar

from lxml.etree import iterparse
from lxml.etree import XMLSyntaxError

from xsdata.formats.dataclass import utils
from xsdata.models.enums import EventType
from xsdata.utils import text
from xsdata.utils.namespaces import split_qname

T = TypeVar("T")


def load_class(output: str, clazz_name: str) -> T:
    search = "Generating package: "
    start = len(search)
    packages = [line[start:] for line in output.split("\n") if line.startswith(search)]

    for package in reversed(packages):
        try:
            module = importlib.import_module(package)
            return getattr(module, clazz_name)
        except (ModuleNotFoundError, AttributeError):
            pass

    raise ModuleNotFoundError(f"Class `{clazz_name}` not found.")


def read_root_name(path: Path) -> str:
    try:
        context = iterparse(str(path), events=(EventType.START,), recover=True)
        _, root = next(context)
        _, local_name = split_qname(root.tag)
        return text.pascal_case(utils.safe_snake(local_name, "Type"))
    except XMLSyntaxError:
        return ""
    except OSError:
        return ""
