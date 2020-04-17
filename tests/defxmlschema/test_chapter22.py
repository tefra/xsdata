import os
from pathlib import Path

from click.testing import CliRunner

from xsdata import cli

os.chdir(Path(__file__).parent.parent.parent)


def test_example2207():
    schema = "tests/fixtures/defxmlschema/chapter22/example2207.xsd"
    package = "tests.fixtures.defxmlschema.chapter22"
    runner = CliRunner()
    result = runner.invoke(cli, [schema, "--package", package])

    if result.exception:
        raise result.exception
