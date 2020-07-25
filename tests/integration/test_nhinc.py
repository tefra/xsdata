import os
from pathlib import Path

from click.testing import CliRunner

from tests import root
from xsdata import cli

os.chdir(root)


def test_schema_hl7():
    source = Path("tests/fixtures/common/nhinc/hl7").resolve()
    package = "tests.fixtures.common.models"
    runner = CliRunner()
    result = runner.invoke(cli, [str(source), "--package", package])

    if result.exception:
        raise result.exception
