import importlib
from pathlib import Path
from typing import TypeVar

from lxml import etree

from xsdata.formats.dataclass import utils
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
        recovering_parser = etree.XMLParser(
            recover=True, resolve_entities=False, no_network=True
        )
        tree = etree.parse(str(path), parser=recovering_parser)  # nosec
        _, local_name = split_qname(tree.getroot().tag)
        return text.pascal_case(utils.safe_snake(local_name, "Type"))
    except Exception:
        return ""
