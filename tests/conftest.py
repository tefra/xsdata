from pathlib import Path
from typing import Type

from lxml import etree

from xsdata.formats.dataclass.context import XmlContext
from xsdata.formats.dataclass.parsers import JsonParser, XmlParser
from xsdata.formats.dataclass.serializers import (
    JsonSerializer,
    PycodeSerializer,
    XmlSerializer,
)
from xsdata.formats.dataclass.serializers.config import SerializerConfig


def validate_bindings(schema: Path, clazz: Type):
    __tracebackhide__ = True

    sample = schema.parent.joinpath("sample.xml")
    context = XmlContext()

    config = SerializerConfig(indent="  ")
    xml_parser = XmlParser(context=context)
    xml_serializer = XmlSerializer(context=context, config=config)
    json_serializer = JsonSerializer(context=context, config=config)
    pycode_serializer = PycodeSerializer(context=context)

    obj = xml_parser.from_path(sample, clazz)

    code = pycode_serializer.render(obj)
    sample.with_suffix(".py").write_text(code)

    actual = json_serializer.render(obj)

    expected = sample.with_suffix(".json")
    if expected.exists():
        assert expected.read_text() == actual
        assert obj == JsonParser().from_string(actual, clazz)
    else:
        expected.write_text(actual, encoding="utf-8")

    xml = xml_serializer.render(obj)

    expected.with_suffix(".xsdata.xml").write_text(xml, encoding="utf-8")

    validator = etree.XMLSchema(etree.parse(str(schema)))
    assert validator.validate(etree.fromstring(xml.encode())), validator.error_log
