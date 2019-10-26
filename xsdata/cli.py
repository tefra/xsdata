import json
from dataclasses import asdict

import click
import click_completion

from xsdata.schema import SchemaReader
from xsdata.version import version

click_completion.init(complete_options=True)


@click.group()
@click.version_option(version=version)
@click.pass_context
def cli(ctx: click.Context):
    pass


@cli.command()
@click.argument("file", type=click.Path(exists=True), required=True)
@click.option("--verbose", is_flag=True, help="Pretty print result")
def generate(file: str, verbose: bool = False):

    reader = SchemaReader(file)
    result = reader.parse()
    if verbose:
        click.echo(json.dumps(asdict(result), indent=4))
    else:
        click.echo("I can't write yet :)")


if __name__ == "__main__":
    cli()
