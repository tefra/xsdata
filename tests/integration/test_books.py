import os

from click.testing import CliRunner

from tests import fixtures_dir, root
from xsdata.cli import cli
from xsdata.utils.testing import load_class

os.chdir(root)


def test_books_schema() -> None:
    schema = fixtures_dir.joinpath("books/schema.xsd")
    package = "tests.fixtures.books"
    runner = CliRunner()
    result = runner.invoke(
        cli,
        [
            "generate",
            str(schema),
            "--package",
            package,
            "--structure-style=namespaces",
            "--docstring-style=Google",
        ],
        catch_exceptions=False,
    )

    if result.exception:
        raise result.exception

    clazz = load_class(result.output, "Books")
    assert clazz.Meta.name == "books"
    assert clazz.Meta.namespace == "urn:books"
