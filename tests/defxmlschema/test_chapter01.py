import os
from pathlib import Path

from click.testing import CliRunner

from tests.conftest import load_class
from tests.conftest import validate_bindings
from xsdata import cli

os.chdir(Path(__file__).parent.parent.parent)


def test_integration():

    schema = Path("tests/fixtures/defxmlschema/chapter01/chapter01.xsd")
    package = "tests.fixtures.defxmlschema.chapter01"
    runner = CliRunner()
    result = runner.invoke(cli, [str(schema), "--package", package])

    if result.exception:
        raise result.exception

    clazz = load_class(result.output, "Product")
    validate_bindings(schema, clazz)


def test_example0102():
    schema = "tests/fixtures/defxmlschema/chapter01/example0102.xsd"
    package = "tests.fixtures.defxmlschema.chapter01"
    runner = CliRunner()
    result = runner.invoke(cli, [schema, "--package", package])

    if result.exception:
        raise result.exception
