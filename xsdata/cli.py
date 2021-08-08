import logging
import sys
from pathlib import Path
from typing import Any
from typing import Iterator

import click
import click_log
from click_default_group import DefaultGroup

from xsdata import __version__
from xsdata.codegen.transformer import SchemaTransformer
from xsdata.codegen.writer import CodeWriter
from xsdata.logger import logger
from xsdata.models.config import DocstringStyle
from xsdata.models.config import GeneratorConfig
from xsdata.models.config import GeneratorOutput
from xsdata.models.config import StructureStyle
from xsdata.utils.click import model_options
from xsdata.utils.downloader import Downloader
from xsdata.utils.hooks import load_entry_points

load_entry_points("xsdata.plugins.cli")

outputs = click.Choice(CodeWriter.generators.keys())
docstring_styles = click.Choice([x.value for x in DocstringStyle])
structure_styles = click.Choice([x.value for x in StructureStyle])
click_log.basic_config(logger)


@click.group(cls=DefaultGroup, default="generate", default_if_no_args=False)
@click.version_option(__version__)
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
@click.option("-c", "--config", default=".xsdata.xml", help="Project configuration")
@click.option("-pp", "--print", is_flag=True, default=False, help="Print output")
@model_options(GeneratorOutput)
def generate(**kwargs: Any):
    """
    Generate code from xml schemas, webservice definitions and any xml or json
    document.

    The input source can be either a filepath, uri or a directory
    containing xml, json, xsd and wsdl files.
    """
    source = kwargs.pop("source")
    stdout = kwargs.pop("print")
    config_file = Path(kwargs.pop("config")).resolve()

    if stdout:
        logger.setLevel(logging.ERROR)

    params = {k.replace("__", "."): v for k, v in kwargs.items() if v is not None}
    config = GeneratorConfig.read(config_file)
    config.output.update(**params)

    transformer = SchemaTransformer(config=config, print=stdout)
    transformer.process(list(resolve_source(source)))


def resolve_source(source: str) -> Iterator[str]:
    if source.find("://") > -1 and not source.startswith("file://"):
        yield source
    else:
        path = Path(source).resolve()
        if path.is_dir():
            yield from (x.as_uri() for x in path.glob("*.wsdl"))
            yield from (x.as_uri() for x in path.glob("*.xsd"))
            yield from (x.as_uri() for x in path.glob("*.xml"))
            yield from (x.as_uri() for x in path.glob("*.json"))
        else:  # is file
            yield path.as_uri()


if __name__ == "__main__":  # pragma: no cover
    cli()
