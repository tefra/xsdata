import os
from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path
from typing import DefaultDict
from typing import Dict
from typing import List

import pytest
from click.testing import CliRunner
from jinja2 import Template

from xsdata import cli

here = Path(__file__).parent
fixtures = here.joinpath("fixtures")

is_travis = "TRAVIS" in os.environ


@dataclass
class Documentation:
    title: str
    skip_message: str
    source: str
    target: str


schemas = sorted([xsd for xsd in fixtures.glob("defxmlschema/*/example*.xsd")])
skipped: DefaultDict[str, int] = defaultdict(int)
passed = 0
titles = {
    "01": "Chapter 01: Schemas: An introduction",
    "02": "Chapter 02: A quick tour of XML Schema",
    "03": "Chapter 03: Namespaces",
    "04": "Chapter 04: Schema composition",
    "05": "Chapter 05: Instances and schemas",
    "06": "Chapter 06: Element declarations",
    "07": "Chapter 07: Attribute declarations",
    "08": "Chapter 08: Simple types",
    "09": "Chapter 09: Regular expressions",
    "10": "Chapter 10: Union and list types",
    "11": "Chapter 11: Built-in simple types",
    "12": "Chapter 12: Complex types",
    "13": "Chapter 13: Deriving complex types",
    "14": "Chapter 14: Assertions",
    "15": "Chapter 15: Named groups",
    "16": "Chapter 16: Substitution groups",
    "17": "Chapter 17: Identity constraints",
    "18": "Chapter 18: Redefining and overriding schema components",
    "19": "Chapter 19: Topics for DTD users",
    "20": "Chapter 20: XML information modeling",
    "21": "Chapter 21: Schema design and documentation",
    "22": "Chapter 22: Extensibility and reuse",
    "23": "Chapter 23: Versioning",
}


@pytest.mark.parametrize("fixture", schemas, ids=lambda x: x.name)
def test_generation(fixture: Path):
    global passed, skipped

    package = ".".join(fixture.relative_to(fixtures).parent.parts)
    runner = CliRunner()
    result = runner.invoke(cli, [str(fixture), f"--package=tests.fixtures.{package}"])

    if result.exception is not None:
        raise result.exception

    passed += 1


def parse_skip_message(source):
    skip_message = None
    skip = source.find("<!-- SKIPTEST")
    if skip > -1:
        skipend = source.find("-->", skip)
        msg = source[skip + 14 : skipend].strip()
        skip_message = msg if msg else "Unsupported feature!"
    return skip_message


def parse_title(source):
    pos = source.find("<!-- Example ")
    if pos > -1:
        end = source.find("-->", pos)
        return source[pos + 5 : end].strip()
    return ""


def teardown_module():

    results = [
        f"- Total tests: **{passed + sum(skipped.values())}**",
        f"- Passed: **{passed}**",
    ]
    for reason, count in skipped.items():
        results.append(f"- {reason}: **{count}**")

    fixtures.joinpath("defxmlschema/generation.results.rst").write_text(
        "\n".join(results)
    )

    if passed > 1:
        for rst in here.parent.joinpath(f"").glob("docs/tests/defxmlschema/*.rst"):
            rst.unlink()

    docs: Dict[str, List[Documentation]] = defaultdict(list)
    sections = defaultdict(int)
    for schema in schemas:
        source = schema.read_text()
        target = schema.with_suffix(".py")

        if "chapter" in schema.name:
            section_title = "full example"
            rename = False
        else:
            section_title = parse_title(source)
            rename = section_title in sections
            sections[section_title] += 1

        if rename:
            parts = section_title.split(" ")
            for i in range(len(parts)):
                if parts[i][0].isdigit():
                    parts[i] += f".{sections[section_title]}"
            section_title = " ".join(parts)

        docs[schema.parent.name].append(
            Documentation(
                title=section_title,
                skip_message=None,
                source=f"/../tests/{schema.relative_to(here)}",
                target=f"/../tests/{target.relative_to(here)}"
                if target.exists()
                else None,
            )
        )

    for suite, items in docs.items():
        number = suite.replace("chapter", "")
        template = Template(
            here.joinpath(
                f"fixtures/defxmlschema/generation.output.jinja2"
            ).read_text(),
            keep_trailing_newline=True,
        )
        output = template.render(suite=titles[number], items=items)

        file = here.parent.joinpath(f"docs/tests/generation/{suite}.rst")
        file.parent.mkdir(parents=True, exist_ok=True)
        file.write_text(output)
