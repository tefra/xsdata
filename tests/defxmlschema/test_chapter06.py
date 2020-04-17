import os
from pathlib import Path

from click.testing import CliRunner

from xsdata import cli

os.chdir(Path(__file__).parent.parent.parent)


def test_example0601():
    schema = "tests/fixtures/defxmlschema/chapter06/example0601.xsd"
    package = "tests.fixtures.defxmlschema.chapter06"
    runner = CliRunner()
    result = runner.invoke(cli, [schema, "--package", package])

    if result.exception:
        raise result.exception


def test_example0603():
    schema = "tests/fixtures/defxmlschema/chapter06/example0603.xsd"
    package = "tests.fixtures.defxmlschema.chapter06"
    runner = CliRunner()
    result = runner.invoke(cli, [schema, "--package", package])

    if result.exception:
        raise result.exception


def test_example0607():
    schema = "tests/fixtures/defxmlschema/chapter06/example0607.xsd"
    package = "tests.fixtures.defxmlschema.chapter06"
    runner = CliRunner()
    result = runner.invoke(cli, [schema, "--package", package])

    if result.exception:
        raise result.exception


def test_example0608():
    schema = "tests/fixtures/defxmlschema/chapter06/example0608.xsd"
    package = "tests.fixtures.defxmlschema.chapter06"
    runner = CliRunner()
    result = runner.invoke(cli, [schema, "--package", package])

    if result.exception:
        raise result.exception


def test_example0611():
    schema = "tests/fixtures/defxmlschema/chapter06/example0611.xsd"
    package = "tests.fixtures.defxmlschema.chapter06"
    runner = CliRunner()
    result = runner.invoke(cli, [schema, "--package", package])

    if result.exception:
        raise result.exception


def test_example0615():
    schema = "tests/fixtures/defxmlschema/chapter06/example0615.xsd"
    package = "tests.fixtures.defxmlschema.chapter06"
    runner = CliRunner()
    result = runner.invoke(cli, [schema, "--package", package])

    if result.exception:
        raise result.exception
