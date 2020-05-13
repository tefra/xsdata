import importlib
from pathlib import Path
from typing import Type

from lxml import etree

from xsdata.formats.dataclass.filters import class_name
from xsdata.formats.dataclass.parsers import JsonParser
from xsdata.formats.dataclass.parsers import XmlParser
from xsdata.formats.dataclass.serializers import JsonSerializer
from xsdata.formats.dataclass.serializers import XmlSerializer


def load_class(output, clazz_name):
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
        recovering_parser = etree.XMLParser(recover=True)
        tree = etree.parse(str(path), parser=recovering_parser)
        root = tree.getroot()
        return class_name(etree.QName(root.tag).localname)
    except etree.XMLSyntaxError:
        return ""
    except OSError:
        return ""


def validate_bindings(schema: Path, clazz: Type):
    __tracebackhide__ = True

    obj = XmlParser().from_path(schema.with_suffix(".xml"), clazz)
    actual = JsonSerializer(indent=4).render(obj)

    expected = schema.with_suffix(".json")
    if expected.exists():
        assert expected.read_text() == actual
        assert obj == JsonParser().from_string(actual, clazz)
    else:
        expected.write_text(actual)

    xml = XmlSerializer(pretty_print=True).render(obj)

    validator = etree.XMLSchema(etree.parse(str(schema)))
    assert validator.validate(etree.fromstring(xml.encode())), validator.error_log

    expected.with_suffix(".xsdata.xml").write_text(xml)
