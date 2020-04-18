import os
from pathlib import Path

from click.testing import CliRunner

from tests.conftest import load_class
from tests.conftest import validate_bindings
from xsdata import cli

os.chdir(Path(__file__).parent.parent.parent)


def test_integration():

    schema = Path("tests/fixtures/defxmlschema/chapter08/chapter08.xsd")
    package = "tests.fixtures.defxmlschema.chapter08"
    runner = CliRunner()
    result = runner.invoke(cli, [str(schema), "--package", package])

    if result.exception:
        raise result.exception

    clazz = load_class(result.output, "Sizes")
    validate_bindings(schema, clazz)


def test_example0801():
    schema = "tests/fixtures/defxmlschema/chapter08/example0801.xsd"
    package = "tests.fixtures.defxmlschema.chapter08"
    runner = CliRunner()
    result = runner.invoke(cli, [schema, "--package", package])

    if result.exception:
        raise result.exception


def test_example0802():
    schema = "tests/fixtures/defxmlschema/chapter08/example0802.xsd"
    package = "tests.fixtures.defxmlschema.chapter08"
    runner = CliRunner()
    result = runner.invoke(cli, [schema, "--package", package])

    if result.exception:
        raise result.exception


def test_example0803():
    schema = "tests/fixtures/defxmlschema/chapter08/example0803.xsd"
    package = "tests.fixtures.defxmlschema.chapter08"
    runner = CliRunner()
    result = runner.invoke(cli, [schema, "--package", package])

    if result.exception:
        raise result.exception


def test_example0804():
    schema = "tests/fixtures/defxmlschema/chapter08/example0804.xsd"
    package = "tests.fixtures.defxmlschema.chapter08"
    runner = CliRunner()
    result = runner.invoke(cli, [schema, "--package", package])

    if result.exception:
        raise result.exception


def test_example0805():
    schema = "tests/fixtures/defxmlschema/chapter08/example0805.xsd"
    package = "tests.fixtures.defxmlschema.chapter08"
    runner = CliRunner()
    result = runner.invoke(cli, [schema, "--package", package])

    if result.exception:
        raise result.exception


def test_example0807():
    schema = "tests/fixtures/defxmlschema/chapter08/example0807.xsd"
    package = "tests.fixtures.defxmlschema.chapter08"
    runner = CliRunner()
    result = runner.invoke(cli, [schema, "--package", package])

    if result.exception:
        raise result.exception


def test_example0808():
    schema = "tests/fixtures/defxmlschema/chapter08/example0808.xsd"
    package = "tests.fixtures.defxmlschema.chapter08"
    runner = CliRunner()
    result = runner.invoke(cli, [schema, "--package", package])

    if result.exception:
        raise result.exception


def test_example0809():
    schema = "tests/fixtures/defxmlschema/chapter08/example0809.xsd"
    package = "tests.fixtures.defxmlschema.chapter08"
    runner = CliRunner()
    result = runner.invoke(cli, [schema, "--package", package])

    if result.exception:
        raise result.exception


def test_example0810():
    schema = "tests/fixtures/defxmlschema/chapter08/example0810.xsd"
    package = "tests.fixtures.defxmlschema.chapter08"
    runner = CliRunner()
    result = runner.invoke(cli, [schema, "--package", package])

    if result.exception:
        raise result.exception


def test_example0812():
    schema = "tests/fixtures/defxmlschema/chapter08/example0812.xsd"
    package = "tests.fixtures.defxmlschema.chapter08"
    runner = CliRunner()
    result = runner.invoke(cli, [schema, "--package", package])

    if result.exception:
        raise result.exception


def test_example08131():
    schema = "tests/fixtures/defxmlschema/chapter08/example08131.xsd"
    package = "tests.fixtures.defxmlschema.chapter08"
    runner = CliRunner()
    result = runner.invoke(cli, [schema, "--package", package])

    if result.exception:
        raise result.exception


def test_example0814():
    schema = "tests/fixtures/defxmlschema/chapter08/example0814.xsd"
    package = "tests.fixtures.defxmlschema.chapter08"
    runner = CliRunner()
    result = runner.invoke(cli, [schema, "--package", package])

    if result.exception:
        raise result.exception


def test_example0815():
    schema = "tests/fixtures/defxmlschema/chapter08/example0815.xsd"
    package = "tests.fixtures.defxmlschema.chapter08"
    runner = CliRunner()
    result = runner.invoke(cli, [schema, "--package", package])

    if result.exception:
        raise result.exception


def test_example0817():
    schema = "tests/fixtures/defxmlschema/chapter08/example0817.xsd"
    package = "tests.fixtures.defxmlschema.chapter08"
    runner = CliRunner()
    result = runner.invoke(cli, [schema, "--package", package])

    if result.exception:
        raise result.exception


def test_example0818():
    schema = "tests/fixtures/defxmlschema/chapter08/example0818.xsd"
    package = "tests.fixtures.defxmlschema.chapter08"
    runner = CliRunner()
    result = runner.invoke(cli, [schema, "--package", package])

    if result.exception:
        raise result.exception


def test_example0821():
    schema = "tests/fixtures/defxmlschema/chapter08/example0821.xsd"
    package = "tests.fixtures.defxmlschema.chapter08"
    runner = CliRunner()
    result = runner.invoke(cli, [schema, "--package", package])

    if result.exception:
        raise result.exception


def test_example0823():
    schema = "tests/fixtures/defxmlschema/chapter08/example0823.xsd"
    package = "tests.fixtures.defxmlschema.chapter08"
    runner = CliRunner()
    result = runner.invoke(cli, [schema, "--package", package])

    if result.exception:
        raise result.exception
