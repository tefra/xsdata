import os
from pathlib import Path

from click.testing import CliRunner

from xsdata import cli

os.chdir(Path(__file__).parent.parent.parent)


def test_example2101():
    schema = "tests/fixtures/defxmlschema/chapter21/example2101.xsd"
    package = "tests.fixtures.defxmlschema.chapter21"
    runner = CliRunner()
    result = runner.invoke(cli, [schema, "--package", package])

    if result.exception:
        raise result.exception


def test_example2102():
    schema = "tests/fixtures/defxmlschema/chapter21/example2102.xsd"
    package = "tests.fixtures.defxmlschema.chapter21"
    runner = CliRunner()
    result = runner.invoke(cli, [schema, "--package", package])

    if result.exception:
        raise result.exception


def test_example2103():
    schema = "tests/fixtures/defxmlschema/chapter21/example2103.xsd"
    package = "tests.fixtures.defxmlschema.chapter21"
    runner = CliRunner()
    result = runner.invoke(cli, [schema, "--package", package])

    if result.exception:
        raise result.exception


def test_example2104():
    schema = "tests/fixtures/defxmlschema/chapter21/example2104.xsd"
    package = "tests.fixtures.defxmlschema.chapter21"
    runner = CliRunner()
    result = runner.invoke(cli, [schema, "--package", package])

    if result.exception:
        raise result.exception


def test_example21081():
    schema = "tests/fixtures/defxmlschema/chapter21/example21081.xsd"
    package = "tests.fixtures.defxmlschema.chapter21"
    runner = CliRunner()
    result = runner.invoke(cli, [schema, "--package", package])

    if result.exception:
        raise result.exception


def test_example21082():
    schema = "tests/fixtures/defxmlschema/chapter21/example21082.xsd"
    package = "tests.fixtures.defxmlschema.chapter21"
    runner = CliRunner()
    result = runner.invoke(cli, [schema, "--package", package])

    if result.exception:
        raise result.exception


def test_example21083():
    schema = "tests/fixtures/defxmlschema/chapter21/example21083.xsd"
    package = "tests.fixtures.defxmlschema.chapter21"
    runner = CliRunner()
    result = runner.invoke(cli, [schema, "--package", package])

    if result.exception:
        raise result.exception


def test_example21101():
    schema = "tests/fixtures/defxmlschema/chapter21/example21101.xsd"
    package = "tests.fixtures.defxmlschema.chapter21"
    runner = CliRunner()
    result = runner.invoke(cli, [schema, "--package", package])

    if result.exception:
        raise result.exception


def test_example21102():
    schema = "tests/fixtures/defxmlschema/chapter21/example21102.xsd"
    package = "tests.fixtures.defxmlschema.chapter21"
    runner = CliRunner()
    result = runner.invoke(cli, [schema, "--package", package])

    if result.exception:
        raise result.exception


def test_example21103():
    schema = "tests/fixtures/defxmlschema/chapter21/example21103.xsd"
    package = "tests.fixtures.defxmlschema.chapter21"
    runner = CliRunner()
    result = runner.invoke(cli, [schema, "--package", package])

    if result.exception:
        raise result.exception


def test_example21131():
    schema = "tests/fixtures/defxmlschema/chapter21/example21131.xsd"
    package = "tests.fixtures.defxmlschema.chapter21"
    runner = CliRunner()
    result = runner.invoke(cli, [schema, "--package", package])

    if result.exception:
        raise result.exception


def test_example21132():
    schema = "tests/fixtures/defxmlschema/chapter21/example21132.xsd"
    package = "tests.fixtures.defxmlschema.chapter21"
    runner = CliRunner()
    result = runner.invoke(cli, [schema, "--package", package])

    if result.exception:
        raise result.exception


def test_example21133():
    schema = "tests/fixtures/defxmlschema/chapter21/example21133.xsd"
    package = "tests.fixtures.defxmlschema.chapter21"
    runner = CliRunner()
    result = runner.invoke(cli, [schema, "--package", package])

    if result.exception:
        raise result.exception


def test_example21161():
    schema = "tests/fixtures/defxmlschema/chapter21/example21161.xsd"
    package = "tests.fixtures.defxmlschema.chapter21"
    runner = CliRunner()
    result = runner.invoke(cli, [schema, "--package", package])

    if result.exception:
        raise result.exception


def test_example21162():
    schema = "tests/fixtures/defxmlschema/chapter21/example21162.xsd"
    package = "tests.fixtures.defxmlschema.chapter21"
    runner = CliRunner()
    result = runner.invoke(cli, [schema, "--package", package])

    if result.exception:
        raise result.exception


def test_example2118():
    schema = "tests/fixtures/defxmlschema/chapter21/example2118.xsd"
    package = "tests.fixtures.defxmlschema.chapter21"
    runner = CliRunner()
    result = runner.invoke(cli, [schema, "--package", package])

    if result.exception:
        raise result.exception


def test_example2119():
    schema = "tests/fixtures/defxmlschema/chapter21/example2119.xsd"
    package = "tests.fixtures.defxmlschema.chapter21"
    runner = CliRunner()
    result = runner.invoke(cli, [schema, "--package", package])

    if result.exception:
        raise result.exception


def test_example2120():
    schema = "tests/fixtures/defxmlschema/chapter21/example2120.xsd"
    package = "tests.fixtures.defxmlschema.chapter21"
    runner = CliRunner()
    result = runner.invoke(cli, [schema, "--package", package])

    if result.exception:
        raise result.exception


def test_example2121():
    schema = "tests/fixtures/defxmlschema/chapter21/example2121.xsd"
    package = "tests.fixtures.defxmlschema.chapter21"
    runner = CliRunner()
    result = runner.invoke(cli, [schema, "--package", package])

    if result.exception:
        raise result.exception


def test_example2122():
    schema = "tests/fixtures/defxmlschema/chapter21/example2122.xsd"
    package = "tests.fixtures.defxmlschema.chapter21"
    runner = CliRunner()
    result = runner.invoke(cli, [schema, "--package", package])

    if result.exception:
        raise result.exception
