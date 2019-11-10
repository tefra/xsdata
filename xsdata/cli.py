from pathlib import Path
from typing import List

import click
import click_completion

from xsdata.builder import builder
from xsdata.parser import SchemaParser
from xsdata.version import version
from xsdata.writer import writer

click_completion.init(complete_options=True)


@click.group()
@click.version_option(version=version)
@click.pass_context
def cli(ctx: click.Context):
    pass


@cli.command()
@click.argument("file", type=click.Path(exists=True), required=True)
@click.option(
    "--target",
    type=click.Path(exists=False, file_okay=False, resolve_path=True),
    required=True,
    help="Target directory",
)
@click.option(
    "--renderer",
    type=click.Choice(writer.formats),
    help="Output renderer",
    default="pydata",
)
def generate(file: str, target: str, renderer: str):
    process(
        xsd_path=Path(file).resolve(),
        target=Path(target).resolve(),
        renderer=renderer,
    )


processed: List[Path] = []


def process(
    xsd_path: Path, target: Path, renderer: str, target_adjusted=False
):

    if xsd_path in processed:
        return

    processed.append(xsd_path)

    schema = SchemaParser(path=xsd_path).parse()
    if not target_adjusted:
        target = writer.adjust_target(target, xsd_path, schema)

    for sub_schema in schema.sub_schemas():
        process(
            xsd_path=xsd_path.parent.joinpath(sub_schema).resolve(),
            target=target.joinpath(sub_schema).parent.resolve(),
            renderer=renderer,
            target_adjusted=True,
        )

    classes = builder.build(schema=schema)
    writer.write(
        schema=schema, classes=classes, target=target, renderer=renderer
    )


if __name__ == "__main__":
    cli()
