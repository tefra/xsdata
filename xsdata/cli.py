import logging
import sys
from pathlib import Path
from typing import Any
from typing import Iterator

import click
import click_log
from click_default_group import DefaultGroup
from pkg_resources import get_distribution

from xsdata.codegen.transformer import SchemaTransformer
from xsdata.codegen.writer import CodeWriter
from xsdata.logger import logger
from xsdata.models.config import DocstringStyle
from xsdata.models.config import GeneratorConfig
from xsdata.models.config import OutputStructure
from xsdata.utils.downloader import Downloader
from xsdata.utils.hooks import load_entry_points

load_entry_points("xsdata.plugins.cli")

outputs = click.Choice(CodeWriter.generators.keys())
docstring_styles = click.Choice([x.value for x in DocstringStyle])
click_log.basic_config(logger)


@click.group(cls=DefaultGroup, default="generate", default_if_no_args=False)
@click.version_option(get_distribution("xsdata").version)
@click_log.simple_verbosity_option(logger)
def cli():
    """xsdata command line interface."""


@cli.command("init-config")
@click.argument("output", type=click.Path(), default=".xsdata.xml")
@click.option("-pp", "--print", is_flag=True, default=False, help="Print output")
def init_config(**kwargs: Any):
    """Create or update a configuration file."""

    if kwargs["print"]:
        logger.setLevel(logging.ERROR)

    file_path = Path(kwargs["output"])
    if file_path.exists():
        config = GeneratorConfig.read(file_path)
        logger.info("Updating configuration file %s", kwargs["output"])
    else:
        logger.info("Initializing configuration file %s", kwargs["output"])
        config = GeneratorConfig.create()

    if kwargs["print"]:
        config.write(sys.stdout, config)
    else:
        with file_path.open("w") as fp:
            config.write(fp, config)


@cli.command("download")
@click.argument("source", required=True)
@click.option(
    "-o",
    "--output",
    type=click.Path(resolve_path=True),
    default="./",
    help="Output directory, default cwd",
)
def download(source: str, output: str):
    """Download a schema or a definition locally with all its dependencies."""
    downloader = Downloader(output=Path(output).resolve())
    downloader.wget(source)


@cli.command("generate")
@click.argument("source", required=True)
@click.option(
    "-c",
    "--config",
    default=".xsdata.xml",
    help="Specify a configuration file with advanced options.",
)
@click.option(
    "-p",
    "--package",
    required=False,
    help=(
        "Specify the target package to be created inside the current working directory "
        "Default: generated"
        "\n\n"
        "The generated module structure relies on the common input source path"
        "\n\n"
        "Use the --ns-struct option for a more flat structure and to avoid circular "
        "import errors."
    ),
    default="generated",
)
@click.option(
    "-o",
    "--output",
    type=outputs,
    help=(
        "Specify the output format from the builtin code generator and any third "
        "party installed plugins. Default: dataclasses"
    ),
    default="dataclasses",
)
@click.option(
    "-ds",
    "--docstring-style",
    type=docstring_styles,
    help=(
        "Specify the docstring style for the default output format. "
        "Default: reStructuredText"
    ),
    default="reStructuredText",
)
@click.option(
    "-ns",
    "--ns-struct",
    is_flag=True,
    default=False,
    help=(
        "Use namespaces to group classes in modules. "
        "Useful against circular import errors."
    ),
)
@click.option(
    "-cf",
    "--compound-fields",
    is_flag=True,
    default=False,
    help=(
        "Use compound fields for repeating choices in order to maintain elements "
        "ordering between data binding operations."
    ),
)
@click.option(
    "-pp",
    "--print",
    is_flag=True,
    default=False,
    help="Print to console instead of writing the generated output to files",
)
def generate(**kwargs: Any):
    """
    Generate code from xml schemas, webservice definitions and any xml
    document.

    The input source can be either a filepath, uri or a directory
    containing xml, xsd, wsdl files.
    """
    if kwargs["print"]:
        logger.setLevel(logging.ERROR)

    config_file = Path(kwargs["config"])
    if config_file.exists():
        config = GeneratorConfig.read(config_file)
        if kwargs["package"] != "generated":
            config.output.package = kwargs["package"]
    else:
        config = GeneratorConfig()
        config.output.format = kwargs["output"]
        config.output.package = kwargs["package"]
        config.output.compound_fields = kwargs["compound_fields"]
        config.output.docstring_style = DocstringStyle(kwargs["docstring_style"])

        if kwargs["ns_struct"]:
            config.output.structure = OutputStructure.NAMESPACES

    uris = resolve_source(kwargs["source"])
    transformer = SchemaTransformer(config=config, print=kwargs["print"])
    transformer.process(list(uris))


def resolve_source(source: str) -> Iterator[str]:
    if source.find("://") > -1 and not source.startswith("file://"):
        yield source
    else:
        path = Path(source).resolve()
        if path.is_dir():
            sources = [x.as_uri() for x in path.glob("*.wsdl")]
            sources.extend([x.as_uri() for x in path.glob("*.xsd")])
            sources.extend([x.as_uri() for x in path.glob("*.xml")])
            yield from sources
        else:  # is file
            yield path.as_uri()


if __name__ == "__main__":  # pragma: no cover
    cli()
