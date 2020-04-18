import os
from pathlib import Path

from click.testing import CliRunner

from tests.conftest import load_class
from tests.conftest import validate_bindings
from xsdata import cli

os.chdir(Path(__file__).parent.parent.parent)


def test_integration():

    schema = Path("tests/fixtures/defxmlschema/chapter10/chapter10.xsd")
    package = "tests.fixtures.defxmlschema.chapter10"
    runner = CliRunner()
    result = runner.invoke(cli, [str(schema), "--package", package])

    if result.exception:
        raise result.exception

    clazz = load_class(result.output, "Sizes")
    validate_bindings(schema, clazz)


def test_example1001():
    schema = "tests/fixtures/defxmlschema/chapter10/example1001.xsd"
    package = "tests.fixtures.defxmlschema.chapter10"
    runner = CliRunner()
    result = runner.invoke(cli, [schema, "--package", package])

    if result.exception:
        raise result.exception


def test_example1002():
    schema = "tests/fixtures/defxmlschema/chapter10/example1002.xsd"
    package = "tests.fixtures.defxmlschema.chapter10"
    runner = CliRunner()
    result = runner.invoke(cli, [schema, "--package", package])

    if result.exception:
        raise result.exception


def test_example1003():
    schema = "tests/fixtures/defxmlschema/chapter10/example1003.xsd"
    package = "tests.fixtures.defxmlschema.chapter10"
    runner = CliRunner()
    result = runner.invoke(cli, [schema, "--package", package])

    if result.exception:
        raise result.exception


def test_example1004():
    schema = "tests/fixtures/defxmlschema/chapter10/example1004.xsd"
    package = "tests.fixtures.defxmlschema.chapter10"
    runner = CliRunner()
    result = runner.invoke(cli, [schema, "--package", package])

    if result.exception:
        raise result.exception


def test_example1005():
    schema = "tests/fixtures/defxmlschema/chapter10/example1005.xsd"
    package = "tests.fixtures.defxmlschema.chapter10"
    runner = CliRunner()
    result = runner.invoke(cli, [schema, "--package", package])

    if result.exception:
        raise result.exception


def test_example1007():
    schema = "tests/fixtures/defxmlschema/chapter10/example1007.xsd"
    package = "tests.fixtures.defxmlschema.chapter10"
    runner = CliRunner()
    result = runner.invoke(cli, [schema, "--package", package])

    if result.exception:
        raise result.exception


def test_example1009():
    schema = "tests/fixtures/defxmlschema/chapter10/example1009.xsd"
    package = "tests.fixtures.defxmlschema.chapter10"
    runner = CliRunner()
    result = runner.invoke(cli, [schema, "--package", package])

    if result.exception:
        raise result.exception


def test_example1010():
    schema = "tests/fixtures/defxmlschema/chapter10/example1010.xsd"
    package = "tests.fixtures.defxmlschema.chapter10"
    runner = CliRunner()
    result = runner.invoke(cli, [schema, "--package", package])

    if result.exception:
        raise result.exception


def test_example1012():
    schema = "tests/fixtures/defxmlschema/chapter10/example1012.xsd"
    package = "tests.fixtures.defxmlschema.chapter10"
    runner = CliRunner()
    result = runner.invoke(cli, [schema, "--package", package])

    if result.exception:
        raise result.exception


def test_example1013():
    schema = "tests/fixtures/defxmlschema/chapter10/example1013.xsd"
    package = "tests.fixtures.defxmlschema.chapter10"
    runner = CliRunner()
    result = runner.invoke(cli, [schema, "--package", package])

    if result.exception:
        raise result.exception


def test_example1014():
    schema = "tests/fixtures/defxmlschema/chapter10/example1014.xsd"
    package = "tests.fixtures.defxmlschema.chapter10"
    runner = CliRunner()
    result = runner.invoke(cli, [schema, "--package", package])

    if result.exception:
        raise result.exception


def test_example1015():
    schema = "tests/fixtures/defxmlschema/chapter10/example1015.xsd"
    package = "tests.fixtures.defxmlschema.chapter10"
    runner = CliRunner()
    result = runner.invoke(cli, [schema, "--package", package])

    if result.exception:
        raise result.exception


def test_example1016():
    schema = "tests/fixtures/defxmlschema/chapter10/example1016.xsd"
    package = "tests.fixtures.defxmlschema.chapter10"
    runner = CliRunner()
    result = runner.invoke(cli, [schema, "--package", package])

    if result.exception:
        raise result.exception


def test_example1018():
    schema = "tests/fixtures/defxmlschema/chapter10/example1018.xsd"
    package = "tests.fixtures.defxmlschema.chapter10"
    runner = CliRunner()
    result = runner.invoke(cli, [schema, "--package", package])

    if result.exception:
        raise result.exception


def test_example10211():
    schema = "tests/fixtures/defxmlschema/chapter10/example10211.xsd"
    package = "tests.fixtures.defxmlschema.chapter10"
    runner = CliRunner()
    result = runner.invoke(cli, [schema, "--package", package])

    if result.exception:
        raise result.exception
