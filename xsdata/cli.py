import logging
from pathlib import Path
from typing import List

import click
import click_log

from xsdata.logger import logger
from xsdata.transformer import SchemaTransformer
from xsdata.writer import writer


@click.command("generate")
@click.argument("sources", required=True, nargs=-1)
@click.option("--package", required=True, help="Target Package")
@click.option(
    "--output",
    type=click.Choice(writer.formats),
    help="Output Format",
    default="pydata",
)
@click.option(
    "--print", is_flag=True, default=False, help="Preview the resulting classes."
)
@click_log.simple_verbosity_option(logger)
def cli(sources: List, package: str, output: str, print: bool):
    """
    Convert schema definitions to code.

    SOURCES can be one or more files or directories or urls.
    """
    if print:
        logger.setLevel(logging.ERROR)

    urls = process_sources(sources)
    transformer = SchemaTransformer(output=output, print=print)
    transformer.process(urls, package)


def process_sources(sources: List[str]) -> List[str]:
    result: List[str] = list()
    for source in sources:
        path = Path(source).resolve()
        if path.is_dir():
            result.extend(x.as_uri() for x in path.glob("*.xsd"))
        elif path.is_file():
            result.append(path.as_uri())
        else:
            result.append(source)
    return result


if __name__ == "__main__":
    cli()
