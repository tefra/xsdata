import os
from pathlib import Path

from click.testing import CliRunner

from xsdata import cli

os.chdir(Path(__file__).parent.parent.parent)


def test_example0701():
    schema = "tests/fixtures/defxmlschema/chapter07/example0701.xsd"
    package = "tests.fixtures.defxmlschema.chapter07"
    runner = CliRunner()
    result = runner.invoke(cli, [schema, "--package", package])

    if result.exception:
        raise result.exception


def test_example0702():
    schema = "tests/fixtures/defxmlschema/chapter07/example0702.xsd"
    package = "tests.fixtures.defxmlschema.chapter07"
    runner = CliRunner()
    result = runner.invoke(cli, [schema, "--package", package])

    if result.exception:
        raise result.exception


def test_example0703():
    schema = "tests/fixtures/defxmlschema/chapter07/example0703.xsd"
    package = "tests.fixtures.defxmlschema.chapter07"
    runner = CliRunner()
    result = runner.invoke(cli, [schema, "--package", package])

    if result.exception:
        raise result.exception


def test_example07041():
    schema = "tests/fixtures/defxmlschema/chapter07/example07041.xsd"
    package = "tests.fixtures.defxmlschema.chapter07"
    runner = CliRunner()
    result = runner.invoke(cli, [schema, "--package", package])

    if result.exception:
        raise result.exception


def test_example0705():
    schema = "tests/fixtures/defxmlschema/chapter07/example0705.xsd"
    package = "tests.fixtures.defxmlschema.chapter07"
    runner = CliRunner()
    result = runner.invoke(cli, [schema, "--package", package])

    if result.exception:
        raise result.exception


def test_example0707():
    schema = "tests/fixtures/defxmlschema/chapter07/example0707.xsd"
    package = "tests.fixtures.defxmlschema.chapter07"
    runner = CliRunner()
    result = runner.invoke(cli, [schema, "--package", package])

    if result.exception:
        raise result.exception
