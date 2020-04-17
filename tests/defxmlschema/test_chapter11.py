import os
from pathlib import Path

from click.testing import CliRunner

from xsdata import cli

os.chdir(Path(__file__).parent.parent.parent)


def test_example1101():
    schema = "tests/fixtures/defxmlschema/chapter11/example1101.xsd"
    package = "tests.fixtures.defxmlschema.chapter11"
    runner = CliRunner()
    result = runner.invoke(cli, [schema, "--package", package])

    if result.exception:
        raise result.exception


def test_example11051():
    schema = "tests/fixtures/defxmlschema/chapter11/example11051.xsd"
    package = "tests.fixtures.defxmlschema.chapter11"
    runner = CliRunner()
    result = runner.invoke(cli, [schema, "--package", package])

    if result.exception:
        raise result.exception


def test_example11061():
    schema = "tests/fixtures/defxmlschema/chapter11/example11061.xsd"
    package = "tests.fixtures.defxmlschema.chapter11"
    runner = CliRunner()
    result = runner.invoke(cli, [schema, "--package", package])

    if result.exception:
        raise result.exception


def test_example11071():
    schema = "tests/fixtures/defxmlschema/chapter11/example11071.xsd"
    package = "tests.fixtures.defxmlschema.chapter11"
    runner = CliRunner()
    result = runner.invoke(cli, [schema, "--package", package])

    if result.exception:
        raise result.exception


def test_example11081():
    schema = "tests/fixtures/defxmlschema/chapter11/example11081.xsd"
    package = "tests.fixtures.defxmlschema.chapter11"
    runner = CliRunner()
    result = runner.invoke(cli, [schema, "--package", package])

    if result.exception:
        raise result.exception
