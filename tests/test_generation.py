import os
from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List

import pytest
from click.testing import CliRunner
from jinja2 import Template

from xsdata import cli
from xsdata.reducer import reducer

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


@pytest.mark.parametrize(
    "fixture",
    [
        pytest.param(fixture)
        for fixture in fixtures.glob("defxmlschema/*/*.xsd")
    ],
    ids=lambda x: x.name,
)
def test_generation(fixture: Path):

    reducer.common_types.clear()
    result = runner.invoke(
        cli,
        [str(fixture), "--package=test", "--print"],
        catch_exceptions=False,
    )

    expected = fixture.with_suffix(".py")
    if expected.exists():
        assert result.output == expected.read_text()
        assert len(result.output.strip()) > 0
    else:
        expected.write_text(result.output)

    log_output(fixture, expected)


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


def teardown_module():
    for suite, items in docs.items():
        template = Template(
            here.joinpath(f"fixtures/{suite}/../output.jinja2").read_text()
        )
        output = template.render(suite=suite, items=items)

        file = here.parent.joinpath(f"docs/tests/{suite}.rst")
        file.parent.mkdir(parents=True, exist_ok=True)
        file.write_text(output)
