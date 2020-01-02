from pathlib import Path

import click

from xsdata.tool import ProcessTask
from xsdata.writer import writer


@click.command("generate")
@click.argument("file", type=click.Path(exists=True), required=True)
@click.option(
    "--package", required=True, help="Target Package",
)
@click.option(
    "--renderer",
    type=click.Choice(writer.formats),
    help="Output renderer",
    default="pydata",
)
@click.option("--print", is_flag=True, default=False)
def cli(file: str, package: str, renderer: str, print: bool):
    task = ProcessTask(renderer=renderer, print=print)
    task.process(xsd=Path(file).resolve(), package=package)


if __name__ == "__main__":
    cli()
