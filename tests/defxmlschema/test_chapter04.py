import os
from pathlib import Path

from click.testing import CliRunner

from tests.conftest import load_class
from tests.conftest import validate_bindings
from xsdata import cli

os.chdir(Path(__file__).parent.parent.parent)


def test_integration():

    schema = Path("tests/fixtures/defxmlschema/chapter04/chapter04.xsd")
    package = "tests.fixtures.defxmlschema.chapter04"
    runner = CliRunner()
    result = runner.invoke(cli, [str(schema), "--package", package])

    if result.exception:
        raise result.exception

    clazz = load_class(result.output, "Order")
    validate_bindings(schema, clazz)


def test_example04011():
    schema = "tests/fixtures/defxmlschema/chapter04/example04011.xsd"
    package = "tests.fixtures.defxmlschema.chapter04"
    runner = CliRunner()
    result = runner.invoke(cli, [schema, "--package", package])

    if result.exception:
        raise result.exception


def test_example04012():
    schema = "tests/fixtures/defxmlschema/chapter04/example04012.xsd"
    package = "tests.fixtures.defxmlschema.chapter04"
    runner = CliRunner()
    result = runner.invoke(cli, [schema, "--package", package])

    if result.exception:
        raise result.exception


def test_example04021():
    schema = "tests/fixtures/defxmlschema/chapter04/example04021.xsd"
    package = "tests.fixtures.defxmlschema.chapter04"
    runner = CliRunner()
    result = runner.invoke(cli, [schema, "--package", package])

    if result.exception:
        raise result.exception


def test_example04022():
    schema = "tests/fixtures/defxmlschema/chapter04/example04022.xsd"
    package = "tests.fixtures.defxmlschema.chapter04"
    runner = CliRunner()
    result = runner.invoke(cli, [schema, "--package", package])

    if result.exception:
        raise result.exception


def test_example04031():
    schema = "tests/fixtures/defxmlschema/chapter04/example04031.xsd"
    package = "tests.fixtures.defxmlschema.chapter04"
    runner = CliRunner()
    result = runner.invoke(cli, [schema, "--package", package])

    if result.exception:
        raise result.exception


def test_example04032():
    schema = "tests/fixtures/defxmlschema/chapter04/example04032.xsd"
    package = "tests.fixtures.defxmlschema.chapter04"
    runner = CliRunner()
    result = runner.invoke(cli, [schema, "--package", package])

    if result.exception:
        raise result.exception


def test_example04051():
    schema = "tests/fixtures/defxmlschema/chapter04/example04051.xsd"
    package = "tests.fixtures.defxmlschema.chapter04"
    runner = CliRunner()
    result = runner.invoke(cli, [schema, "--package", package])

    if result.exception:
        raise result.exception


def test_example04052():
    schema = "tests/fixtures/defxmlschema/chapter04/example04052.xsd"
    package = "tests.fixtures.defxmlschema.chapter04"
    runner = CliRunner()
    result = runner.invoke(cli, [schema, "--package", package])

    if result.exception:
        raise result.exception


def test_example04053():
    schema = "tests/fixtures/defxmlschema/chapter04/example04053.xsd"
    package = "tests.fixtures.defxmlschema.chapter04"
    runner = CliRunner()
    result = runner.invoke(cli, [schema, "--package", package])

    if result.exception:
        raise result.exception


def test_example04061():
    schema = "tests/fixtures/defxmlschema/chapter04/example04061.xsd"
    package = "tests.fixtures.defxmlschema.chapter04"
    runner = CliRunner()
    result = runner.invoke(cli, [schema, "--package", package])

    if result.exception:
        raise result.exception


def test_example04062():
    schema = "tests/fixtures/defxmlschema/chapter04/example04062.xsd"
    package = "tests.fixtures.defxmlschema.chapter04"
    runner = CliRunner()
    result = runner.invoke(cli, [schema, "--package", package])

    if result.exception:
        raise result.exception
