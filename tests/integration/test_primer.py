import os

from click.testing import CliRunner

from tests import fixtures_dir
from tests import root
from tests.conftest import validate_bindings
from xsdata.cli import cli
from xsdata.utils.testing import load_class

os.chdir(root)


def test_primer_schema():
    schema = fixtures_dir.joinpath("primer/order.xsd")
    package = "tests.fixtures.primer"
    runner = CliRunner()
    result = runner.invoke(
        cli, [str(schema), "--package", package, "--docstring-style", "NumPy"]
    )

    if result.exception:
        raise result.exception

    clazz = load_class(result.output, "PurchaseOrder")
    assert "purchaseOrder" == clazz.Meta.name

    validate_bindings(schema, clazz)
