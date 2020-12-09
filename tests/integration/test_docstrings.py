import os

from click.testing import CliRunner

from tests import fixtures_dir
from tests import root
from xsdata.cli import cli
from xsdata.utils.testing import load_class

os.chdir(root)


def test_generate_restructured_docstrings():
    schema = fixtures_dir.joinpath("docstrings/schema.xsd")
    package = "tests.fixtures.docstrings.rst"
    runner = CliRunner()
    result = runner.invoke(
        cli,
        [
            str(schema),
            "--package",
            package,
            "--docstring-style",
            "reStructuredText",
        ],
        catch_exceptions=False,
    )

    assert result.exception is None


def test_generate_numpy_docstrings():
    schema = fixtures_dir.joinpath("docstrings/schema.xsd")
    package = "tests.fixtures.docstrings.numpy"
    runner = CliRunner()
    result = runner.invoke(
        cli,
        [
            str(schema),
            "--package",
            package,
            "--docstring-style",
            "NumPy",
        ],
    )

    assert result.exception is None


def test_generate_google_docstrings():
    schema = fixtures_dir.joinpath("docstrings/schema.xsd")
    package = "tests.fixtures.docstrings.google"
    runner = CliRunner()
    result = runner.invoke(
        cli,
        [
            str(schema),
            "--package",
            package,
            "--docstring-style",
            "Google",
        ],
    )

    assert result.exception is None


def test_generate_accessible_docstrings():
    schema = fixtures_dir.joinpath("docstrings/schema.xsd")
    package = "tests.fixtures.docstrings.accessible"
    runner = CliRunner()
    result = runner.invoke(
        cli,
        [
            str(schema),
            "--package",
            package,
            "--docstring-style",
            "Accessible",
        ],
    )

    assert result.exception is None
