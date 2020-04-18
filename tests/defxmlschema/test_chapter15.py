import os
from pathlib import Path

from click.testing import CliRunner

from tests.conftest import load_class
from tests.conftest import validate_bindings
from xsdata import cli

os.chdir(Path(__file__).parent.parent.parent)


def test_integration():

    schema = Path("tests/fixtures/defxmlschema/chapter15/chapter15.xsd")
    package = "tests.fixtures.defxmlschema.chapter15"
    runner = CliRunner()
    result = runner.invoke(cli, [str(schema), "--package", package])

    if result.exception:
        raise result.exception

    clazz = load_class(result.output, "Shirt")
    validate_bindings(schema, clazz)


def test_example1501():
    schema = "tests/fixtures/defxmlschema/chapter15/example1501.xsd"
    package = "tests.fixtures.defxmlschema.chapter15"
    runner = CliRunner()
    result = runner.invoke(cli, [schema, "--package", package])

    if result.exception:
        raise result.exception


def test_example1502():
    schema = "tests/fixtures/defxmlschema/chapter15/example1502.xsd"
    package = "tests.fixtures.defxmlschema.chapter15"
    runner = CliRunner()
    result = runner.invoke(cli, [schema, "--package", package])

    if result.exception:
        raise result.exception


def test_example1504():
    schema = "tests/fixtures/defxmlschema/chapter15/example1504.xsd"
    package = "tests.fixtures.defxmlschema.chapter15"
    runner = CliRunner()
    result = runner.invoke(cli, [schema, "--package", package])

    if result.exception:
        raise result.exception


def test_example1505():
    schema = "tests/fixtures/defxmlschema/chapter15/example1505.xsd"
    package = "tests.fixtures.defxmlschema.chapter15"
    runner = CliRunner()
    result = runner.invoke(cli, [schema, "--package", package])

    if result.exception:
        raise result.exception


def test_example1506():
    schema = "tests/fixtures/defxmlschema/chapter15/example1506.xsd"
    package = "tests.fixtures.defxmlschema.chapter15"
    runner = CliRunner()
    result = runner.invoke(cli, [schema, "--package", package])

    if result.exception:
        raise result.exception


def test_example1507():
    schema = "tests/fixtures/defxmlschema/chapter15/example1507.xsd"
    package = "tests.fixtures.defxmlschema.chapter15"
    runner = CliRunner()
    result = runner.invoke(cli, [schema, "--package", package])

    if result.exception:
        raise result.exception


def test_example1508():
    schema = "tests/fixtures/defxmlschema/chapter15/example1508.xsd"
    package = "tests.fixtures.defxmlschema.chapter15"
    runner = CliRunner()
    result = runner.invoke(cli, [schema, "--package", package])

    if result.exception:
        raise result.exception


def test_example1509():
    schema = "tests/fixtures/defxmlschema/chapter15/example1509.xsd"
    package = "tests.fixtures.defxmlschema.chapter15"
    runner = CliRunner()
    result = runner.invoke(cli, [schema, "--package", package])

    if result.exception:
        raise result.exception


def test_example1510():
    schema = "tests/fixtures/defxmlschema/chapter15/example1510.xsd"
    package = "tests.fixtures.defxmlschema.chapter15"
    runner = CliRunner()
    result = runner.invoke(cli, [schema, "--package", package])

    if result.exception:
        raise result.exception


def test_example1511():
    schema = "tests/fixtures/defxmlschema/chapter15/example1511.xsd"
    package = "tests.fixtures.defxmlschema.chapter15"
    runner = CliRunner()
    result = runner.invoke(cli, [schema, "--package", package])

    if result.exception:
        raise result.exception


def test_example1512():
    schema = "tests/fixtures/defxmlschema/chapter15/example1512.xsd"
    package = "tests.fixtures.defxmlschema.chapter15"
    runner = CliRunner()
    result = runner.invoke(cli, [schema, "--package", package])

    if result.exception:
        raise result.exception


def test_example1514():
    schema = "tests/fixtures/defxmlschema/chapter15/example1514.xsd"
    package = "tests.fixtures.defxmlschema.chapter15"
    runner = CliRunner()
    result = runner.invoke(cli, [schema, "--package", package])

    if result.exception:
        raise result.exception


def test_example1515():
    schema = "tests/fixtures/defxmlschema/chapter15/example1515.xsd"
    package = "tests.fixtures.defxmlschema.chapter15"
    runner = CliRunner()
    result = runner.invoke(cli, [schema, "--package", package])

    if result.exception:
        raise result.exception


def test_example1516():
    schema = "tests/fixtures/defxmlschema/chapter15/example1516.xsd"
    package = "tests.fixtures.defxmlschema.chapter15"
    runner = CliRunner()
    result = runner.invoke(cli, [schema, "--package", package])

    if result.exception:
        raise result.exception


def test_example15171():
    schema = "tests/fixtures/defxmlschema/chapter15/example15171.xsd"
    package = "tests.fixtures.defxmlschema.chapter15"
    runner = CliRunner()
    result = runner.invoke(cli, [schema, "--package", package])

    if result.exception:
        raise result.exception


def test_example15172():
    schema = "tests/fixtures/defxmlschema/chapter15/example15172.xsd"
    package = "tests.fixtures.defxmlschema.chapter15"
    runner = CliRunner()
    result = runner.invoke(cli, [schema, "--package", package])

    if result.exception:
        raise result.exception


def test_example1518():
    schema = "tests/fixtures/defxmlschema/chapter15/example1518.xsd"
    package = "tests.fixtures.defxmlschema.chapter15"
    runner = CliRunner()
    result = runner.invoke(cli, [schema, "--package", package])

    if result.exception:
        raise result.exception
