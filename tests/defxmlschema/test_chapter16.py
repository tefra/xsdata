import os
from pathlib import Path

from click.testing import CliRunner

from tests.conftest import load_class
from tests.conftest import validate_bindings
from xsdata import cli

os.chdir(Path(__file__).parent.parent.parent)


def test_integration():

    schema = Path("tests/fixtures/defxmlschema/chapter16/chapter16.xsd")
    package = "tests.fixtures.defxmlschema.chapter16"
    runner = CliRunner()
    result = runner.invoke(cli, [str(schema), "--package", package])

    if result.exception:
        raise result.exception

    clazz = load_class(result.output, "Items")
    validate_bindings(schema, clazz)


def test_example1601():
    schema = "tests/fixtures/defxmlschema/chapter16/example1601.xsd"
    package = "tests.fixtures.defxmlschema.chapter16"
    runner = CliRunner()
    result = runner.invoke(cli, [schema, "--package", package])

    if result.exception:
        raise result.exception


def test_example1602():
    schema = "tests/fixtures/defxmlschema/chapter16/example1602.xsd"
    package = "tests.fixtures.defxmlschema.chapter16"
    runner = CliRunner()
    result = runner.invoke(cli, [schema, "--package", package])

    if result.exception:
        raise result.exception


def test_example1604():
    schema = "tests/fixtures/defxmlschema/chapter16/example1604.xsd"
    package = "tests.fixtures.defxmlschema.chapter16"
    runner = CliRunner()
    result = runner.invoke(cli, [schema, "--package", package])

    if result.exception:
        raise result.exception


def test_example1605():
    schema = "tests/fixtures/defxmlschema/chapter16/example1605.xsd"
    package = "tests.fixtures.defxmlschema.chapter16"
    runner = CliRunner()
    result = runner.invoke(cli, [schema, "--package", package])

    if result.exception:
        raise result.exception


def test_example1606():
    schema = "tests/fixtures/defxmlschema/chapter16/example1606.xsd"
    package = "tests.fixtures.defxmlschema.chapter16"
    runner = CliRunner()
    result = runner.invoke(cli, [schema, "--package", package])

    if result.exception:
        raise result.exception


def test_example1607():
    schema = "tests/fixtures/defxmlschema/chapter16/example1607.xsd"
    package = "tests.fixtures.defxmlschema.chapter16"
    runner = CliRunner()
    result = runner.invoke(cli, [schema, "--package", package])

    if result.exception:
        raise result.exception


def test_example1609():
    schema = "tests/fixtures/defxmlschema/chapter16/example1609.xsd"
    package = "tests.fixtures.defxmlschema.chapter16"
    runner = CliRunner()
    result = runner.invoke(cli, [schema, "--package", package])

    if result.exception:
        raise result.exception


def test_example1610():
    schema = "tests/fixtures/defxmlschema/chapter16/example1610.xsd"
    package = "tests.fixtures.defxmlschema.chapter16"
    runner = CliRunner()
    result = runner.invoke(cli, [schema, "--package", package])

    if result.exception:
        raise result.exception
