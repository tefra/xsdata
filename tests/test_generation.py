import os
from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path
from typing import DefaultDict, Dict, List

import pytest
from click.testing import CliRunner
from jinja2 import Template

from xsdata import cli
from xsdata.formats.dataclass.generator import DataclassGenerator
from xsdata.reducer import reducer
from xsdata.writer import writer

runner = CliRunner()

here = Path(__file__).parent
fixtures = here.joinpath("fixtures")

is_travis = "TRAVIS" in os.environ


@dataclass
class Documentation:
    title: str
    source: str
    output: str


docs: Dict[str, List[Documentation]] = defaultdict(list)
schemas = sorted([xsd for xsd in fixtures.glob("defxmlschema/*/*.xsd")])

skipped: DefaultDict[str, int] = defaultdict(int)
passed = 0


@pytest.mark.parametrize("fixture", schemas, ids=lambda x: x.name)
def test_generation(fixture: Path):
    global passed, skipped

    package = ".".join(fixture.relative_to(fixtures).parent.parts)
    source = fixture.read_text()
    should_fail = is_illegal_definition(source)
    skip_message = parse_skip_message(source)

    result = runner.invoke(
        cli, [str(fixture), f"--package=tests.fixtures.{package}"]
    )

    if skip_message:
        skipped[skip_message] += 1
        pytest.skip(skip_message)

    if should_fail:
        if result.exception is None:
            pytest.fail(f"Illegal definition: Should have failed!")
        return

    if result.exception is not None:
        raise result.exception

    expected = fixture.with_suffix(".py")
    output = expected.read_text().strip() if expected.exists() else ""

    if len(output) == 0 and len(fixture.name) > 15:
        pytest.skip("Assisting schema")

    assert len(output.strip()) > 0
    log_output(fixture, expected)
    passed += 1


def is_illegal_definition(source):
    return source.find("llegal") > -1


def parse_skip_message(source):
    skip_message = None
    skip = source.find("<!-- SKIPTEST")
    if skip > -1:
        skipend = source.find("-->", skip)
        msg = source[skip + 14 : skipend].strip()
        skip_message = msg if msg else "Unsupported feature!"
    return skip_message


def log_output(xsd: Path, expected: Path):
    if is_travis:
        return

    source = xsd.read_text()
    source_lines = source.split("\n")
    suite = str(xsd.relative_to(fixtures).parent)
    docs[suite].append(
        Documentation(
            title=source_lines[1]
            .replace("<!--", "")
            .replace("-->", "")
            .strip(),
            source=f"/../tests/{xsd.relative_to(here)}",
            output=f"/../tests/{expected.relative_to(here)}",
        )
    )


def teardown_function():
    reducer.common_types.clear()
    writer.register_generator("pydata", DataclassGenerator())


def teardown_module():

    results = [
        f"- Total tests: **{passed + sum(skipped.values())}**",
        f"- Passed: **{passed}**",
    ]
    for reason, count in skipped.items():
        results.append(f"- {reason}: **{count}**")

    fixtures.joinpath("defxmlschema/results.rst").write_text(
        "\n".join(results)
    )

    for rst in here.parent.joinpath(f"").glob("docs/tests/defxmlschema/*.rst"):
        rst.unlink()

    for suite, items in docs.items():
        template = Template(
            here.joinpath(f"fixtures/{suite}/../output.jinja2").read_text(),
            keep_trailing_newline=True,
        )
        output = template.render(suite=suite, items=items)

        file = here.parent.joinpath(f"docs/tests/{suite}.rst")
        file.parent.mkdir(parents=True, exist_ok=True)
        file.write_text(output)
