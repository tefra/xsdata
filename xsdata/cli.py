import logging
from pathlib import Path
from typing import Iterator

import click
import click_log
from pkg_resources import get_distribution

from xsdata.codegen.transformer import SchemaTransformer
from xsdata.codegen.writer import writer
from xsdata.logger import logger

outputs = click.Choice(writer.formats)


@click.command("generate")
@click.argument("source", required=True)
@click.option("--package", required=True, help="Target Package")
@click.option("--output", type=outputs, help="Output Format", default="pydata")
@click.option("--print", is_flag=True, default=False, help="Print output")
@click.version_option(get_distribution("xsdata").version)
@click_log.simple_verbosity_option(logger)
def cli(source: str, package: str, output: str, print: bool):
    """
    Convert schema definitions to code.

    SOURCE can be either a filepath, directory or url
    """
    if print:
        logger.setLevel(logging.ERROR)

    uris = resolve_source(source)
    transformer = SchemaTransformer(output=output, print=print)
    transformer.process(list(uris), package)


def resolve_source(source: str) -> Iterator[str]:
    path = Path(source).resolve()
    if path.is_dir():
        yield from (x.as_uri() for x in path.glob("*.xsd"))
    elif path.is_file():
        yield path.as_uri()
    else:
        yield source


if __name__ == "__main__":  # pragma: no cover
    cli()
