import os
from pathlib import Path

from click.testing import CliRunner

from tests.conftest import load_class
from tests.conftest import validate_bindings
from xsdata import cli

os.chdir(Path(__file__).parent.parent.parent)


def test_integration():

    schema = Path("tests/fixtures/defxmlschema/chapter13/chapter13.xsd")
    package = "tests.fixtures.defxmlschema.chapter13"
    runner = CliRunner()
    result = runner.invoke(cli, [str(schema), "--package", package])

    if result.exception:
        raise result.exception

    clazz = load_class(result.output, "Items")
    validate_bindings(schema, clazz)


def test_example13011():
    schema = "tests/fixtures/defxmlschema/chapter13/example13011.xsd"
    package = "tests.fixtures.defxmlschema.chapter13"
    runner = CliRunner()
    result = runner.invoke(cli, [schema, "--package", package])

    if result.exception:
        raise result.exception


def test_example1302():
    schema = "tests/fixtures/defxmlschema/chapter13/example1302.xsd"
    package = "tests.fixtures.defxmlschema.chapter13"
    runner = CliRunner()
    result = runner.invoke(cli, [schema, "--package", package])

    if result.exception:
        raise result.exception


def test_example1303():
    schema = "tests/fixtures/defxmlschema/chapter13/example1303.xsd"
    package = "tests.fixtures.defxmlschema.chapter13"
    runner = CliRunner()
    result = runner.invoke(cli, [schema, "--package", package])

    if result.exception:
        raise result.exception


def test_example1304():
    schema = "tests/fixtures/defxmlschema/chapter13/example1304.xsd"
    package = "tests.fixtures.defxmlschema.chapter13"
    runner = CliRunner()
    result = runner.invoke(cli, [schema, "--package", package])

    if result.exception:
        raise result.exception


def test_example1305():
    schema = "tests/fixtures/defxmlschema/chapter13/example1305.xsd"
    package = "tests.fixtures.defxmlschema.chapter13"
    runner = CliRunner()
    result = runner.invoke(cli, [schema, "--package", package])

    if result.exception:
        raise result.exception


def test_example1306():
    schema = "tests/fixtures/defxmlschema/chapter13/example1306.xsd"
    package = "tests.fixtures.defxmlschema.chapter13"
    runner = CliRunner()
    result = runner.invoke(cli, [schema, "--package", package])

    if result.exception:
        raise result.exception


def test_example1307():
    schema = "tests/fixtures/defxmlschema/chapter13/example1307.xsd"
    package = "tests.fixtures.defxmlschema.chapter13"
    runner = CliRunner()
    result = runner.invoke(cli, [schema, "--package", package])

    if result.exception:
        raise result.exception


def test_example1308():
    schema = "tests/fixtures/defxmlschema/chapter13/example1308.xsd"
    package = "tests.fixtures.defxmlschema.chapter13"
    runner = CliRunner()
    result = runner.invoke(cli, [schema, "--package", package])

    if result.exception:
        raise result.exception


def test_example1309():
    schema = "tests/fixtures/defxmlschema/chapter13/example1309.xsd"
    package = "tests.fixtures.defxmlschema.chapter13"
    runner = CliRunner()
    result = runner.invoke(cli, [schema, "--package", package])

    if result.exception:
        raise result.exception


def test_example13101():
    schema = "tests/fixtures/defxmlschema/chapter13/example13101.xsd"
    package = "tests.fixtures.defxmlschema.chapter13"
    runner = CliRunner()
    result = runner.invoke(cli, [schema, "--package", package])

    if result.exception:
        raise result.exception


def test_example1311():
    schema = "tests/fixtures/defxmlschema/chapter13/example1311.xsd"
    package = "tests.fixtures.defxmlschema.chapter13"
    runner = CliRunner()
    result = runner.invoke(cli, [schema, "--package", package])

    if result.exception:
        raise result.exception


def test_example1312():
    schema = "tests/fixtures/defxmlschema/chapter13/example1312.xsd"
    package = "tests.fixtures.defxmlschema.chapter13"
    runner = CliRunner()
    result = runner.invoke(cli, [schema, "--package", package])

    if result.exception:
        raise result.exception


def test_example1313():
    schema = "tests/fixtures/defxmlschema/chapter13/example1313.xsd"
    package = "tests.fixtures.defxmlschema.chapter13"
    runner = CliRunner()
    result = runner.invoke(cli, [schema, "--package", package])

    if result.exception:
        raise result.exception


def test_example1314():
    schema = "tests/fixtures/defxmlschema/chapter13/example1314.xsd"
    package = "tests.fixtures.defxmlschema.chapter13"
    runner = CliRunner()
    result = runner.invoke(cli, [schema, "--package", package])

    if result.exception:
        raise result.exception


def test_example13261():
    schema = "tests/fixtures/defxmlschema/chapter13/example13261.xsd"
    package = "tests.fixtures.defxmlschema.chapter13"
    runner = CliRunner()
    result = runner.invoke(cli, [schema, "--package", package])

    if result.exception:
        raise result.exception


def test_example13262():
    schema = "tests/fixtures/defxmlschema/chapter13/example13262.xsd"
    package = "tests.fixtures.defxmlschema.chapter13"
    runner = CliRunner()
    result = runner.invoke(cli, [schema, "--package", package])

    if result.exception:
        raise result.exception


def test_example13263():
    schema = "tests/fixtures/defxmlschema/chapter13/example13263.xsd"
    package = "tests.fixtures.defxmlschema.chapter13"
    runner = CliRunner()
    result = runner.invoke(cli, [schema, "--package", package])

    if result.exception:
        raise result.exception


def test_example1327():
    schema = "tests/fixtures/defxmlschema/chapter13/example1327.xsd"
    package = "tests.fixtures.defxmlschema.chapter13"
    runner = CliRunner()
    result = runner.invoke(cli, [schema, "--package", package])

    if result.exception:
        raise result.exception


def test_example1328():
    schema = "tests/fixtures/defxmlschema/chapter13/example1328.xsd"
    package = "tests.fixtures.defxmlschema.chapter13"
    runner = CliRunner()
    result = runner.invoke(cli, [schema, "--package", package])

    if result.exception:
        raise result.exception


def test_example1329():
    schema = "tests/fixtures/defxmlschema/chapter13/example1329.xsd"
    package = "tests.fixtures.defxmlschema.chapter13"
    runner = CliRunner()
    result = runner.invoke(cli, [schema, "--package", package])

    if result.exception:
        raise result.exception


def test_example1330():
    schema = "tests/fixtures/defxmlschema/chapter13/example1330.xsd"
    package = "tests.fixtures.defxmlschema.chapter13"
    runner = CliRunner()
    result = runner.invoke(cli, [schema, "--package", package])

    if result.exception:
        raise result.exception


def test_example1332():
    schema = "tests/fixtures/defxmlschema/chapter13/example1332.xsd"
    package = "tests.fixtures.defxmlschema.chapter13"
    runner = CliRunner()
    result = runner.invoke(cli, [schema, "--package", package])

    if result.exception:
        raise result.exception


def test_example1333():
    schema = "tests/fixtures/defxmlschema/chapter13/example1333.xsd"
    package = "tests.fixtures.defxmlschema.chapter13"
    runner = CliRunner()
    result = runner.invoke(cli, [schema, "--package", package])

    if result.exception:
        raise result.exception


def test_example13341():
    schema = "tests/fixtures/defxmlschema/chapter13/example13341.xsd"
    package = "tests.fixtures.defxmlschema.chapter13"
    runner = CliRunner()
    result = runner.invoke(cli, [schema, "--package", package])

    if result.exception:
        raise result.exception


def test_example13342():
    schema = "tests/fixtures/defxmlschema/chapter13/example13342.xsd"
    package = "tests.fixtures.defxmlschema.chapter13"
    runner = CliRunner()
    result = runner.invoke(cli, [schema, "--package", package])

    if result.exception:
        raise result.exception


def test_example13351():
    schema = "tests/fixtures/defxmlschema/chapter13/example13351.xsd"
    package = "tests.fixtures.defxmlschema.chapter13"
    runner = CliRunner()
    result = runner.invoke(cli, [schema, "--package", package])

    if result.exception:
        raise result.exception


def test_example13352():
    schema = "tests/fixtures/defxmlschema/chapter13/example13352.xsd"
    package = "tests.fixtures.defxmlschema.chapter13"
    runner = CliRunner()
    result = runner.invoke(cli, [schema, "--package", package])

    if result.exception:
        raise result.exception


def test_example1336():
    schema = "tests/fixtures/defxmlschema/chapter13/example1336.xsd"
    package = "tests.fixtures.defxmlschema.chapter13"
    runner = CliRunner()
    result = runner.invoke(cli, [schema, "--package", package])

    if result.exception:
        raise result.exception


def test_example1338():
    schema = "tests/fixtures/defxmlschema/chapter13/example1338.xsd"
    package = "tests.fixtures.defxmlschema.chapter13"
    runner = CliRunner()
    result = runner.invoke(cli, [schema, "--package", package])

    if result.exception:
        raise result.exception


def test_example1339():
    schema = "tests/fixtures/defxmlschema/chapter13/example1339.xsd"
    package = "tests.fixtures.defxmlschema.chapter13"
    runner = CliRunner()
    result = runner.invoke(cli, [schema, "--package", package])

    if result.exception:
        raise result.exception


def test_example1341():
    schema = "tests/fixtures/defxmlschema/chapter13/example1341.xsd"
    package = "tests.fixtures.defxmlschema.chapter13"
    runner = CliRunner()
    result = runner.invoke(cli, [schema, "--package", package])

    if result.exception:
        raise result.exception
