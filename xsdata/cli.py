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
    "--package", required=True, help="Target Package",
)
@click.option(
    "--renderer",
    type=click.Choice(writer.formats),
    help="Output renderer",
    default="pydata",
)
def generate(file: str, package: str, renderer: str):
    process(
        xsd_path=Path(file).resolve(), package=package, renderer=renderer,
    )


processed: List[Path] = []


def process(xsd_path: Path, package: str, renderer: str):
    if xsd_path in processed:
        return
    processed.append(xsd_path)

    schema = SchemaParser.from_file(xsd_path)
    for sub_schema in schema.sub_schemas():
        process(
            xsd_path=xsd_path.parent.joinpath(sub_schema).resolve(),
            package=adjust_package(package, sub_schema),
            renderer=renderer,
        )

    classes = builder.build(schema=schema)
    writer.write(
        schema=schema, classes=classes, package=package, renderer=renderer
    )


def adjust_package(package: str, relative_file_path: str):
    pp = package.split(".")
    for part in Path(relative_file_path).parent.parts:
        if part == "..":
            pp.pop()
        else:
            pp.append(part)
    return ".".join(pp)


if __name__ == "__main__":
    cli()
