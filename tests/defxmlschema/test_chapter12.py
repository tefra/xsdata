import os
from pathlib import Path

from click.testing import CliRunner

from tests.conftest import load_class
from tests.conftest import validate_bindings
from xsdata import cli

os.chdir(Path(__file__).parent.parent.parent)


def test_integration():

    schema = Path("tests/fixtures/defxmlschema/chapter12/chapter12.xsd")
    package = "tests.fixtures.defxmlschema.chapter12"
    runner = CliRunner()
    result = runner.invoke(cli, [str(schema), "--package", package])

    if result.exception:
        raise result.exception

    clazz = load_class(result.output, "Items")
    validate_bindings(schema, clazz)


def test_example1202():
    schema = "tests/fixtures/defxmlschema/chapter12/example1202.xsd"
    package = "tests.fixtures.defxmlschema.chapter12"
    runner = CliRunner()
    result = runner.invoke(cli, [schema, "--package", package])

    if result.exception:
        raise result.exception


def test_example1203():
    schema = "tests/fixtures/defxmlschema/chapter12/example1203.xsd"
    package = "tests.fixtures.defxmlschema.chapter12"
    runner = CliRunner()
    result = runner.invoke(cli, [schema, "--package", package])

    if result.exception:
        raise result.exception


def test_example1205():
    schema = "tests/fixtures/defxmlschema/chapter12/example1205.xsd"
    package = "tests.fixtures.defxmlschema.chapter12"
    runner = CliRunner()
    result = runner.invoke(cli, [schema, "--package", package])

    if result.exception:
        raise result.exception


def test_example1207():
    schema = "tests/fixtures/defxmlschema/chapter12/example1207.xsd"
    package = "tests.fixtures.defxmlschema.chapter12"
    runner = CliRunner()
    result = runner.invoke(cli, [schema, "--package", package])

    if result.exception:
        raise result.exception


def test_example1209():
    schema = "tests/fixtures/defxmlschema/chapter12/example1209.xsd"
    package = "tests.fixtures.defxmlschema.chapter12"
    runner = CliRunner()
    result = runner.invoke(cli, [schema, "--package", package])

    if result.exception:
        raise result.exception


def test_example1211():
    schema = "tests/fixtures/defxmlschema/chapter12/example1211.xsd"
    package = "tests.fixtures.defxmlschema.chapter12"
    runner = CliRunner()
    result = runner.invoke(cli, [schema, "--package", package])

    if result.exception:
        raise result.exception


def test_example1212():
    schema = "tests/fixtures/defxmlschema/chapter12/example1212.xsd"
    package = "tests.fixtures.defxmlschema.chapter12"
    runner = CliRunner()
    result = runner.invoke(cli, [schema, "--package", package])

    if result.exception:
        raise result.exception


def test_example1213():
    schema = "tests/fixtures/defxmlschema/chapter12/example1213.xsd"
    package = "tests.fixtures.defxmlschema.chapter12"
    runner = CliRunner()
    result = runner.invoke(cli, [schema, "--package", package])

    if result.exception:
        raise result.exception


def test_example1215():
    schema = "tests/fixtures/defxmlschema/chapter12/example1215.xsd"
    package = "tests.fixtures.defxmlschema.chapter12"
    runner = CliRunner()
    result = runner.invoke(cli, [schema, "--package", package])

    if result.exception:
        raise result.exception


def test_example1218():
    schema = "tests/fixtures/defxmlschema/chapter12/example1218.xsd"
    package = "tests.fixtures.defxmlschema.chapter12"
    runner = CliRunner()
    result = runner.invoke(cli, [schema, "--package", package])

    if result.exception:
        raise result.exception


def test_example1219():
    schema = "tests/fixtures/defxmlschema/chapter12/example1219.xsd"
    package = "tests.fixtures.defxmlschema.chapter12"
    runner = CliRunner()
    result = runner.invoke(cli, [schema, "--package", package])

    if result.exception:
        raise result.exception


def test_example1221():
    schema = "tests/fixtures/defxmlschema/chapter12/example1221.xsd"
    package = "tests.fixtures.defxmlschema.chapter12"
    runner = CliRunner()
    result = runner.invoke(cli, [schema, "--package", package])

    if result.exception:
        raise result.exception


def test_example1223():
    schema = "tests/fixtures/defxmlschema/chapter12/example1223.xsd"
    package = "tests.fixtures.defxmlschema.chapter12"
    runner = CliRunner()
    result = runner.invoke(cli, [schema, "--package", package])

    if result.exception:
        raise result.exception


def test_example1224():
    schema = "tests/fixtures/defxmlschema/chapter12/example1224.xsd"
    package = "tests.fixtures.defxmlschema.chapter12"
    runner = CliRunner()
    result = runner.invoke(cli, [schema, "--package", package])

    if result.exception:
        raise result.exception


def test_example1227():
    schema = "tests/fixtures/defxmlschema/chapter12/example1227.xsd"
    package = "tests.fixtures.defxmlschema.chapter12"
    runner = CliRunner()
    result = runner.invoke(cli, [schema, "--package", package])

    if result.exception:
        raise result.exception


def test_example1229():
    schema = "tests/fixtures/defxmlschema/chapter12/example1229.xsd"
    package = "tests.fixtures.defxmlschema.chapter12"
    runner = CliRunner()
    result = runner.invoke(cli, [schema, "--package", package])

    if result.exception:
        raise result.exception


def test_example1230():
    schema = "tests/fixtures/defxmlschema/chapter12/example1230.xsd"
    package = "tests.fixtures.defxmlschema.chapter12"
    runner = CliRunner()
    result = runner.invoke(cli, [schema, "--package", package])

    if result.exception:
        raise result.exception


def test_example1231():
    schema = "tests/fixtures/defxmlschema/chapter12/example1231.xsd"
    package = "tests.fixtures.defxmlschema.chapter12"
    runner = CliRunner()
    result = runner.invoke(cli, [schema, "--package", package])

    if result.exception:
        raise result.exception


def test_example1232():
    schema = "tests/fixtures/defxmlschema/chapter12/example1232.xsd"
    package = "tests.fixtures.defxmlschema.chapter12"
    runner = CliRunner()
    result = runner.invoke(cli, [schema, "--package", package])

    if result.exception:
        raise result.exception


def test_example1233():
    schema = "tests/fixtures/defxmlschema/chapter12/example1233.xsd"
    package = "tests.fixtures.defxmlschema.chapter12"
    runner = CliRunner()
    result = runner.invoke(cli, [schema, "--package", package])

    if result.exception:
        raise result.exception


def test_example1235():
    schema = "tests/fixtures/defxmlschema/chapter12/example1235.xsd"
    package = "tests.fixtures.defxmlschema.chapter12"
    runner = CliRunner()
    result = runner.invoke(cli, [schema, "--package", package])

    if result.exception:
        raise result.exception


def test_example1237():
    schema = "tests/fixtures/defxmlschema/chapter12/example1237.xsd"
    package = "tests.fixtures.defxmlschema.chapter12"
    runner = CliRunner()
    result = runner.invoke(cli, [schema, "--package", package])

    if result.exception:
        raise result.exception


def test_example1240():
    schema = "tests/fixtures/defxmlschema/chapter12/example1240.xsd"
    package = "tests.fixtures.defxmlschema.chapter12"
    runner = CliRunner()
    result = runner.invoke(cli, [schema, "--package", package])

    if result.exception:
        raise result.exception


def test_example1242():
    schema = "tests/fixtures/defxmlschema/chapter12/example1242.xsd"
    package = "tests.fixtures.defxmlschema.chapter12"
    runner = CliRunner()
    result = runner.invoke(cli, [schema, "--package", package])

    if result.exception:
        raise result.exception


def test_example1244():
    schema = "tests/fixtures/defxmlschema/chapter12/example1244.xsd"
    package = "tests.fixtures.defxmlschema.chapter12"
    runner = CliRunner()
    result = runner.invoke(cli, [schema, "--package", package])

    if result.exception:
        raise result.exception


def test_example1246():
    schema = "tests/fixtures/defxmlschema/chapter12/example1246.xsd"
    package = "tests.fixtures.defxmlschema.chapter12"
    runner = CliRunner()
    result = runner.invoke(cli, [schema, "--package", package])

    if result.exception:
        raise result.exception


def test_example1247():
    schema = "tests/fixtures/defxmlschema/chapter12/example1247.xsd"
    package = "tests.fixtures.defxmlschema.chapter12"
    runner = CliRunner()
    result = runner.invoke(cli, [schema, "--package", package])

    if result.exception:
        raise result.exception
