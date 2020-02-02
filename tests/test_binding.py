import importlib
import os
from dataclasses import dataclass
from pathlib import Path

import pytest
from click.testing import CliRunner
from jinja2 import Template
from lxml import etree

from tests.test_generation import titles
from xsdata import cli
from xsdata.formats.dataclass.generator import DataclassGenerator
from xsdata.formats.dataclass.parsers import XmlParser
from xsdata.formats.dataclass.serializers import JsonSerializer
from xsdata.formats.dataclass.serializers import XmlSerializer
from xsdata.reducer import reducer
from xsdata.writer import writer

runner = CliRunner()

here = Path(__file__).parent
fixtures = here.joinpath("fixtures")

is_travis = "TRAVIS" in os.environ


@dataclass
class Documentation:
    title: str
    skip_message: str
    source: str
    target: str


xml_parser = XmlParser()
xml_serializer = XmlSerializer(pretty_print=True)
json_serializer = JsonSerializer(indent=4)

xmls = sorted(
    [
        xsd
        for xsd in fixtures.glob("defxmlschema/*/chapter*.xml")
        if not str(xsd).endswith("xsdata.xml")
    ]
)

total = 0
skipped = 0


@pytest.mark.parametrize("fixture", xmls, ids=lambda x: x.name)
def test_binding(fixture: Path):
    global total, skipped
    total += 1
    source = fixture.read_text()
    clazz = import_clazz(source)

    if not clazz:
        skipped += 1
        pytest.skip("no clazz set")

    obj = xml_parser.from_string(source, clazz)
    actual = json_serializer.render(obj)

    expected = fixture.with_suffix(".json")
    if expected.exists():
        assert expected.read_text() == actual
    else:
        expected.write_text(actual)

    xml = xml_serializer.render(obj)

    schema = etree.XMLSchema(etree.parse(str(fixture.with_suffix(".xsd"))))
    assert schema.validate(etree.fromstring(xml.encode())), schema.error_log

    expected.with_suffix(".xsdata.xml").write_text(xml)


def import_clazz(source):
    pos = source.find("<!-- model: ")
    if pos > -1:
        end = source.find("-->", pos)
        chapter, file, name = source[pos + 12 : end].strip().split(".")
        module = importlib.import_module(
            f"tests.fixtures.defxmlschema.{chapter}.{file}"
        )
        return getattr(module, name)
    return None


def setup_module(module):
    for xsd in fixtures.glob("defxmlschema/*/chapter*.xsd"):
        reducer.common_types.clear()
        writer.register_generator("pydata", DataclassGenerator())

        package = ".".join(xsd.relative_to(fixtures).parent.parts)
        result = runner.invoke(cli, [str(xsd), f"--package=tests.fixtures.{package}"])
        if result.exception:
            raise result.exception


def teardown_module():
    results = [
        f"- Total tests: **{total}**",
        f"- Passed: **{total - skipped}**",
        f"- Skipped: **{skipped}**",
    ]

    fixtures.joinpath("defxmlschema/binding.results.rst").write_text("\n".join(results))

    for rst in here.parent.joinpath(f"").glob("docs/tests/binding/*.rst"):
        rst.unlink()

    for xml in xmls:
        json = xml.with_suffix(".json")
        xsdata_xml = xml.with_suffix(".xsdata.xml")
        if not json.exists():
            continue

        schema = xml.with_suffix(".xsd")
        template = Template(
            here.joinpath(f"fixtures/defxmlschema/binding.output.jinja2").read_text(),
            keep_trailing_newline=True,
        )

        number = xml.name.replace("chapter", "").replace(".xml", "")
        output = template.render(
            suite=titles[number],
            schema=f"/../tests/{schema.relative_to(here)}",
            source=f"/../tests/{xml.relative_to(here)}",
            xsdata_json=f"/../tests/{json.relative_to(here)}",
            xsdata_xml=f"/../tests/{xsdata_xml.relative_to(here)}",
        )

        file = here.parent.joinpath(f"docs/tests/binding/{xml.name}.rst")
        file.parent.mkdir(parents=True, exist_ok=True)
        file.write_text(output)
