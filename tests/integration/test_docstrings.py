import os

from click.testing import CliRunner

from tests import fixtures_dir, root
from xsdata.cli import cli

os.chdir(root)
schema = fixtures_dir.joinpath("docstrings/schema.xsd")


def test_generate_restructured_docstrings() -> None:
    package = "tests.fixtures.docstrings.rst"
    runner = CliRunner()
    runner.invoke(
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


def test_generate_numpy_docstrings() -> None:
    package = "tests.fixtures.docstrings.numpy"
    runner = CliRunner()
    runner.invoke(
        cli,
        [
            str(schema),
            "--package",
            package,
            "--docstring-style",
            "NumPy",
        ],
        catch_exceptions=False,
    )


def test_generate_google_docstrings() -> None:
    package = "tests.fixtures.docstrings.google"
    runner = CliRunner()
    runner.invoke(
        cli,
        [
            str(schema),
            "--package",
            package,
            "--docstring-style",
            "Google",
        ],
        catch_exceptions=False,
    )


def test_generate_accessible_docstrings() -> None:
    package = "tests.fixtures.docstrings.accessible"
    runner = CliRunner()
    runner.invoke(
        cli,
        [
            str(schema),
            "--package",
            package,
            "--docstring-style",
            "Accessible",
        ],
        catch_exceptions=False,
    )


def test_generate_blank_docstrings() -> None:
    package = "tests.fixtures.docstrings.blank"
    runner = CliRunner()
    runner.invoke(
        cli,
        [
            str(schema),
            "--package",
            package,
            "--docstring-style",
            "Blank",
        ],
        catch_exceptions=False,
    )
