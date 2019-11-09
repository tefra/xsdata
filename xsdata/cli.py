from pathlib import Path
from typing import List

import click
import click_completion

from xsdata.generator import CodeGenerator
from xsdata.parser import SchemaParser
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
@click.option(
    "--target",
    type=click.Path(exists=False, file_okay=False, resolve_path=True),
    required=True,
    help="Target directory",
)
@click.option("--theme", help="Target theme", default="dataclass")
@click.option("--verbose", is_flag=True, help="Pretty print result")
def generate(file: str, target: str, theme: str, verbose: bool = False):
    process(
        xsd_path=Path(file).resolve(),
        theme=theme,
        target=Path(target).resolve(),
    )


processed: List[Path] = []


def process(xsd_path, theme, target, target_adjusted=False):

    if xsd_path in processed:
        return

    processed.append(xsd_path)

    reader = SchemaParser(path=xsd_path)
    schema = reader.parse()
    module = xsd_path.stem
    if not target_adjusted:
        target = CodeWriter.adjust_target(target, xsd_path, schema)

    imports = schema.imports + schema.includes
    CodeWriter.organize_imports(imports)
    for _import in imports:
        import_xsd_path = xsd_path.parent.joinpath(
            _import.schema_location
        ).resolve()
        import_target_path = target.joinpath(
            _import.schema_location
        ).parent.resolve()
        process(
            import_xsd_path, theme, import_target_path, target_adjusted=True
        )

    classes = CodeGenerator(schema=schema).generate()
    CodeWriter(
        module=module,
        classes=classes,
        imports=imports,
        theme=theme,
        target=target,
    ).write()


if __name__ == "__main__":
    cli()
