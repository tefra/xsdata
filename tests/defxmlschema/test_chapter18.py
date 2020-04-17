import os
from pathlib import Path

from click.testing import CliRunner

from xsdata import cli

os.chdir(Path(__file__).parent.parent.parent)


def test_example18011():
    schema = "tests/fixtures/defxmlschema/chapter18/example18011.xsd"
    package = "tests.fixtures.defxmlschema.chapter18"
    runner = CliRunner()
    result = runner.invoke(cli, [schema, "--package", package])

    if result.exception:
        raise result.exception


def test_example18012():
    schema = "tests/fixtures/defxmlschema/chapter18/example18012.xsd"
    package = "tests.fixtures.defxmlschema.chapter18"
    runner = CliRunner()
    result = runner.invoke(cli, [schema, "--package", package])

    if result.exception:
        raise result.exception


def test_example18021():
    schema = "tests/fixtures/defxmlschema/chapter18/example18021.xsd"
    package = "tests.fixtures.defxmlschema.chapter18"
    runner = CliRunner()
    result = runner.invoke(cli, [schema, "--package", package])

    if result.exception:
        raise result.exception


def test_example18022():
    schema = "tests/fixtures/defxmlschema/chapter18/example18022.xsd"
    package = "tests.fixtures.defxmlschema.chapter18"
    runner = CliRunner()
    result = runner.invoke(cli, [schema, "--package", package])

    if result.exception:
        raise result.exception


def test_example18031():
    schema = "tests/fixtures/defxmlschema/chapter18/example18031.xsd"
    package = "tests.fixtures.defxmlschema.chapter18"
    runner = CliRunner()
    result = runner.invoke(cli, [schema, "--package", package])

    if result.exception:
        raise result.exception


def test_example18032():
    schema = "tests/fixtures/defxmlschema/chapter18/example18032.xsd"
    package = "tests.fixtures.defxmlschema.chapter18"
    runner = CliRunner()
    result = runner.invoke(cli, [schema, "--package", package])

    if result.exception:
        raise result.exception


def test_example18041():
    schema = "tests/fixtures/defxmlschema/chapter18/example18041.xsd"
    package = "tests.fixtures.defxmlschema.chapter18"
    runner = CliRunner()
    result = runner.invoke(cli, [schema, "--package", package])

    if result.exception:
        raise result.exception


def test_example18042():
    schema = "tests/fixtures/defxmlschema/chapter18/example18042.xsd"
    package = "tests.fixtures.defxmlschema.chapter18"
    runner = CliRunner()
    result = runner.invoke(cli, [schema, "--package", package])

    if result.exception:
        raise result.exception


def test_example18051():
    schema = "tests/fixtures/defxmlschema/chapter18/example18051.xsd"
    package = "tests.fixtures.defxmlschema.chapter18"
    runner = CliRunner()
    result = runner.invoke(cli, [schema, "--package", package])

    if result.exception:
        raise result.exception


def test_example18052():
    schema = "tests/fixtures/defxmlschema/chapter18/example18052.xsd"
    package = "tests.fixtures.defxmlschema.chapter18"
    runner = CliRunner()
    result = runner.invoke(cli, [schema, "--package", package])

    if result.exception:
        raise result.exception


def test_example18061():
    schema = "tests/fixtures/defxmlschema/chapter18/example18061.xsd"
    package = "tests.fixtures.defxmlschema.chapter18"
    runner = CliRunner()
    result = runner.invoke(cli, [schema, "--package", package])

    if result.exception:
        raise result.exception


def test_example18062():
    schema = "tests/fixtures/defxmlschema/chapter18/example18062.xsd"
    package = "tests.fixtures.defxmlschema.chapter18"
    runner = CliRunner()
    result = runner.invoke(cli, [schema, "--package", package])

    if result.exception:
        raise result.exception


def test_example18071():
    schema = "tests/fixtures/defxmlschema/chapter18/example18071.xsd"
    package = "tests.fixtures.defxmlschema.chapter18"
    runner = CliRunner()
    result = runner.invoke(cli, [schema, "--package", package])

    if result.exception:
        raise result.exception


def test_example18072():
    schema = "tests/fixtures/defxmlschema/chapter18/example18072.xsd"
    package = "tests.fixtures.defxmlschema.chapter18"
    runner = CliRunner()
    result = runner.invoke(cli, [schema, "--package", package])

    if result.exception:
        raise result.exception


def test_example18081():
    schema = "tests/fixtures/defxmlschema/chapter18/example18081.xsd"
    package = "tests.fixtures.defxmlschema.chapter18"
    runner = CliRunner()
    result = runner.invoke(cli, [schema, "--package", package])

    if result.exception:
        raise result.exception


def test_example18082():
    schema = "tests/fixtures/defxmlschema/chapter18/example18082.xsd"
    package = "tests.fixtures.defxmlschema.chapter18"
    runner = CliRunner()
    result = runner.invoke(cli, [schema, "--package", package])

    if result.exception:
        raise result.exception


def test_example18091():
    schema = "tests/fixtures/defxmlschema/chapter18/example18091.xsd"
    package = "tests.fixtures.defxmlschema.chapter18"
    runner = CliRunner()
    result = runner.invoke(cli, [schema, "--package", package])

    if result.exception:
        raise result.exception


def test_example18092():
    schema = "tests/fixtures/defxmlschema/chapter18/example18092.xsd"
    package = "tests.fixtures.defxmlschema.chapter18"
    runner = CliRunner()
    result = runner.invoke(cli, [schema, "--package", package])

    if result.exception:
        raise result.exception


def test_example18101():
    schema = "tests/fixtures/defxmlschema/chapter18/example18101.xsd"
    package = "tests.fixtures.defxmlschema.chapter18"
    runner = CliRunner()
    result = runner.invoke(cli, [schema, "--package", package])

    if result.exception:
        raise result.exception


def test_example18102():
    schema = "tests/fixtures/defxmlschema/chapter18/example18102.xsd"
    package = "tests.fixtures.defxmlschema.chapter18"
    runner = CliRunner()
    result = runner.invoke(cli, [schema, "--package", package])

    if result.exception:
        raise result.exception


def test_example18111():
    schema = "tests/fixtures/defxmlschema/chapter18/example18111.xsd"
    package = "tests.fixtures.defxmlschema.chapter18"
    runner = CliRunner()
    result = runner.invoke(cli, [schema, "--package", package])

    if result.exception:
        raise result.exception


def test_example18112():
    schema = "tests/fixtures/defxmlschema/chapter18/example18112.xsd"
    package = "tests.fixtures.defxmlschema.chapter18"
    runner = CliRunner()
    result = runner.invoke(cli, [schema, "--package", package])

    if result.exception:
        raise result.exception


def test_example18121():
    schema = "tests/fixtures/defxmlschema/chapter18/example18121.xsd"
    package = "tests.fixtures.defxmlschema.chapter18"
    runner = CliRunner()
    result = runner.invoke(cli, [schema, "--package", package])

    if result.exception:
        raise result.exception


def test_example18122():
    schema = "tests/fixtures/defxmlschema/chapter18/example18122.xsd"
    package = "tests.fixtures.defxmlschema.chapter18"
    runner = CliRunner()
    result = runner.invoke(cli, [schema, "--package", package])

    if result.exception:
        raise result.exception


def test_example18131():
    schema = "tests/fixtures/defxmlschema/chapter18/example18131.xsd"
    package = "tests.fixtures.defxmlschema.chapter18"
    runner = CliRunner()
    result = runner.invoke(cli, [schema, "--package", package])

    if result.exception:
        raise result.exception


def test_example18132():
    schema = "tests/fixtures/defxmlschema/chapter18/example18132.xsd"
    package = "tests.fixtures.defxmlschema.chapter18"
    runner = CliRunner()
    result = runner.invoke(cli, [schema, "--package", package])

    if result.exception:
        raise result.exception
