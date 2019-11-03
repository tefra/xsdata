import json
from dataclasses import asdict
from pathlib import Path

import click
import click_completion

from xsdata.generator import CodeGenerator
from xsdata.schema import SchemaReader
from xsdata.utils.text import snake_case
from xsdata.version import version
from xsdata.writer import CodeWriter

click_completion.init(complete_options=True)


@click.group()
@click.version_option(version=version)
@click.pass_context
def cli(ctx: click.Context):
    pass


@cli.command()
@click.argument("file", type=click.Path(exists=True), required=True)
@click.option("--module", help="Module name")
@click.option(
    "--target",
    type=click.Path(exists=True, file_okay=False, resolve_path=True),
    required=True,
    help="Target directory",
)
@click.option("--theme", help="Target theme", default="dataclass")
@click.option("--verbose", is_flag=True, help="Pretty print result")
def generate(
    file: str, module: str, target: str, theme: str, verbose: bool = False
):

    reader = SchemaReader(file)
    schema = reader.parse()
    if verbose:
        click.echo(json.dumps(asdict(schema), indent=4))
    else:
        properties = CodeGenerator(schema=schema).generate()
        CodeWriter(
            module=module or snake_case(Path(file).stem),
            properties=properties,
            theme=theme,
            target=target,
        ).write()


if __name__ == "__main__":
    cli()
