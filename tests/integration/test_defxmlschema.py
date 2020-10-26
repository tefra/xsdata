import os
from pathlib import Path

from click.testing import CliRunner

from tests import root
from tests.conftest import validate_bindings
from xsdata.cli import cli
from xsdata.utils.testing import load_class

os.chdir(root)


def test_definitive_xml_schema_chapter_01():
    schema = Path("tests/fixtures/defxmlschema/chapter01.xsd")
    package = "tests.fixtures.defxmlschema"
    runner = CliRunner()
    result = runner.invoke(cli, [str(schema), "--package", package])

    if result.exception:
        raise result.exception

    clazz = load_class(result.output, "Product")
    validate_bindings(schema, clazz)


def test_definitive_xml_schema_chapter_03():
    schema = Path("tests/fixtures/defxmlschema/chapter03.xsd")
    package = "tests.fixtures.defxmlschema"
    runner = CliRunner()
    result = runner.invoke(cli, [str(schema), "--package", package])

    if result.exception:
        raise result.exception

    clazz = load_class(result.output, "Envelope")
    validate_bindings(schema, clazz)


def test_definitive_xml_schema_chapter_04():
    schema = Path("tests/fixtures/defxmlschema/chapter04.xsd")
    package = "tests.fixtures.defxmlschema"
    runner = CliRunner()
    result = runner.invoke(cli, [str(schema), "--package", package])

    if result.exception:
        raise result.exception

    clazz = load_class(result.output, "Order")
    validate_bindings(schema, clazz)


def test_definitive_xml_schema_chapter_05():
    schema = Path("tests/fixtures/defxmlschema/chapter05.xsd")
    package = "tests.fixtures.defxmlschema"
    runner = CliRunner()
    result = runner.invoke(cli, [str(schema), "--package", package])

    if result.exception:
        raise result.exception

    clazz = load_class(result.output, "Order")
    validate_bindings(schema, clazz)


def test_definitive_xml_schema_chapter_08():
    schema = Path("tests/fixtures/defxmlschema/chapter08.xsd")
    package = "tests.fixtures.defxmlschema"
    runner = CliRunner()
    result = runner.invoke(cli, [str(schema), "--package", package])

    if result.exception:
        raise result.exception

    clazz = load_class(result.output, "Sizes")
    validate_bindings(schema, clazz)


def test_definitive_xml_schema_chapter_10():
    schema = Path("tests/fixtures/defxmlschema/chapter10.xsd")
    package = "tests.fixtures.defxmlschema"
    runner = CliRunner()
    result = runner.invoke(cli, [str(schema), "--package", package])

    if result.exception:
        raise result.exception

    clazz = load_class(result.output, "Sizes")
    validate_bindings(schema, clazz)


def test_definitive_xml_schema_chapter_12():
    schema = Path("tests/fixtures/defxmlschema/chapter12.xsd")
    package = "tests.fixtures.defxmlschema"
    runner = CliRunner()
    result = runner.invoke(
        cli, [str(schema), "--package", package, "--compound-fields", "yes"]
    )

    if result.exception:
        raise result.exception

    clazz = load_class(result.output, "Items")
    validate_bindings(schema, clazz)


def test_definitive_xml_schema_chapter_13():
    schema = Path("tests/fixtures/defxmlschema/chapter13.xsd")
    package = "tests.fixtures.defxmlschema"
    runner = CliRunner()
    result = runner.invoke(cli, [str(schema), "--package", package])

    if result.exception:
        raise result.exception

    clazz = load_class(result.output, "Items")
    validate_bindings(schema, clazz)


def test_definitive_xml_schema_chapter_15():
    schema = Path("tests/fixtures/defxmlschema/chapter15.xsd")
    package = "tests.fixtures.defxmlschema"
    runner = CliRunner()
    result = runner.invoke(cli, [str(schema), "--package", package])

    if result.exception:
        raise result.exception

    clazz = load_class(result.output, "Shirt")
    validate_bindings(schema, clazz)


def test_definitive_xml_schema_chapter_16():
    schema = Path("tests/fixtures/defxmlschema/chapter16.xsd")
    package = "tests.fixtures.defxmlschema"
    runner = CliRunner()
    result = runner.invoke(cli, [str(schema), "--package", package])

    if result.exception:
        raise result.exception

    clazz = load_class(result.output, "Items")
    validate_bindings(schema, clazz)


def test_definitive_xml_schema_chapter_17():
    schema = Path("tests/fixtures/defxmlschema/chapter17.xsd")
    package = "tests.fixtures.defxmlschema"
    runner = CliRunner()
    result = runner.invoke(
        cli, [str(schema), "--package", package, "--compound-fields", "yes"]
    )

    if result.exception:
        raise result.exception

    clazz = load_class(result.output, "Order")
    validate_bindings(schema, clazz)
