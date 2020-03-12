from pathlib import Path

import click
import click_log

from xsdata.logger import logger
from xsdata.transformer import SchemaTransformer
from xsdata.writer import writer


@click.command("generate")
@click.argument("XSD-Path", type=click.Path(exists=True), required=True)
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
def cli(xsd_path: str, package: str, output: str, print: bool):
    if print:
        logger.setLevel("ERROR")

    transformer = SchemaTransformer(output=output, print=print)
    transformer.process(Path(xsd_path).resolve(), package)


if __name__ == "__main__":
    cli()
