import os

from click.testing import CliRunner

from tests import fixtures_dir
from tests import root
from xsdata.cli import cli
from xsdata.utils.testing import load_class

os.chdir(root)


def test_books_schema():
    schema = fixtures_dir.joinpath("books/schema.xsd")
    package = "tests.fixtures.books"
    runner = CliRunner()
    result = runner.invoke(cli, [str(schema), "--package", package, "--ns-struct"])

    if result.exception:
        raise result.exception

    clazz = load_class(result.output, "Books")
    assert "books" == clazz.Meta.name
    assert "urn:books" == clazz.Meta.namespace
