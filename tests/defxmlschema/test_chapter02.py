import os
from pathlib import Path

from click.testing import CliRunner

from xsdata import cli

os.chdir(Path(__file__).parent.parent.parent)


def test_example0202():
    schema = "tests/fixtures/defxmlschema/chapter02/example0202.xsd"
    package = "tests.fixtures.defxmlschema.chapter02"
    runner = CliRunner()
    result = runner.invoke(cli, [schema, "--package", package])

    if result.exception:
        raise result.exception


def test_example0206():
    schema = "tests/fixtures/defxmlschema/chapter02/example0206.xsd"
    package = "tests.fixtures.defxmlschema.chapter02"
    runner = CliRunner()
    result = runner.invoke(cli, [schema, "--package", package])

    if result.exception:
        raise result.exception


def test_example0208():
    schema = "tests/fixtures/defxmlschema/chapter02/example0208.xsd"
    package = "tests.fixtures.defxmlschema.chapter02"
    runner = CliRunner()
    result = runner.invoke(cli, [schema, "--package", package])

    if result.exception:
        raise result.exception


def test_example0209():
    schema = "tests/fixtures/defxmlschema/chapter02/example0209.xsd"
    package = "tests.fixtures.defxmlschema.chapter02"
    runner = CliRunner()
    result = runner.invoke(cli, [schema, "--package", package])

    if result.exception:
        raise result.exception


def test_example0210():
    schema = "tests/fixtures/defxmlschema/chapter02/example0210.xsd"
    package = "tests.fixtures.defxmlschema.chapter02"
    runner = CliRunner()
    result = runner.invoke(cli, [schema, "--package", package])

    if result.exception:
        raise result.exception


def test_example0214():
    schema = "tests/fixtures/defxmlschema/chapter02/example0214.xsd"
    package = "tests.fixtures.defxmlschema.chapter02"
    runner = CliRunner()
    result = runner.invoke(cli, [schema, "--package", package])

    if result.exception:
        raise result.exception
