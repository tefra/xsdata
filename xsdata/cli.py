import json
from dataclasses import asdict

import click
import click_completion

from xsdata.models.elements import Schema
from xsdata.schema import SchemaReader
from xsdata.version import version
from xsdata.writer import SchemaWriter

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
    schema = reader.parse()
    if verbose:
        click.echo(json.dumps(asdict(schema), indent=4))
    else:
        assert isinstance(schema, Schema)
        writer = SchemaWriter(schema, "dataclass")
        writer.write()


if __name__ == "__main__":
    cli()
