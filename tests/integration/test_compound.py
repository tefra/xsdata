import os

from click.testing import CliRunner

from tests import fixtures_dir
from tests import root
from tests.conftest import validate_bindings
from xsdata.cli import cli
from xsdata.utils.testing import load_class

os.chdir(root)


def test_xml_documents():
    schema = fixtures_dir.joinpath("compound/schema.xsd")
    package = "tests.fixtures.compound.models"
    runner = CliRunner()
    result = runner.invoke(
        cli, [str(schema), "-p", package, "-ss", "single-package", "--compound-fields"]
    )

    if result.exception:
        raise result.exception

    clazz = load_class(result.output, "Root")
    validate_bindings(schema, clazz)
