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

    SOURCES can be one or more files or directories.
    """
    if print:
        logger.setLevel(logging.ERROR)

    schemas: List[Path] = list()
    for source in sources:
        src_path = Path(source).resolve()

        if src_path.is_dir():
            schemas.extend(src_path.glob("*.xsd"))
        else:
            schemas.append(src_path)

    transformer = SchemaTransformer(output=output, print=print)
    transformer.process(schemas, package)


if __name__ == "__main__":
    cli()
