import os

from click.testing import CliRunner

from tests import fixtures_dir
from tests import root
from xsdata.cli import cli
from xsdata.utils.testing import load_class

os.chdir(root)


def test_dtd_documents():
    runner = CliRunner()
    result = runner.invoke(
        cli,
        [
            str(fixtures_dir.joinpath("dtd/complete_example.dtd")),
            "--package",
            "tests.fixtures.dtd.models",
        ],
    )

    if result.exception:
        raise result.exception

    clazz = load_class(result.output, "Post")

    assert clazz is not None
