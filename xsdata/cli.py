from pathlib import Path

import click
import click_log

from xsdata.logger import logger
from xsdata.tool import ProcessTask
from xsdata.writer import writer


@click.command("generate")
@click.argument("XSD-Path", type=click.Path(exists=True), required=True)
@click.option(
    "--package", required=True, help="Target Package",
)
@click.option(
    "--renderer",
    type=click.Choice(writer.formats),
    help="Output renderer",
    default="pydata",
)
@click.option(
    "--print",
    is_flag=True,
    default=False,
    help="Preview the resulting classes.",
)
@click_log.simple_verbosity_option(logger)
def cli(xsd_path: str, package: str, renderer: str, print: bool):
    if print:
        logger.setLevel("ERROR")

    task = ProcessTask(renderer=renderer, print=print)
    task.process(xsd=Path(xsd_path).resolve(), package=package)


if __name__ == "__main__":
    cli()
