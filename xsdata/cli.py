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
from xsdata.exceptions import CodeGenerationError
from xsdata.logger import logger
from xsdata.models.config import GeneratorConfig
from xsdata.models.config import OutputFormat
from xsdata.models.config import OutputStructure
from xsdata.utils.downloader import Downloader

outputs = click.Choice([x.value for x in OutputFormat])


@click.group(cls=DefaultGroup, default="generate", default_if_no_args=False)
@click.version_option(get_distribution("xsdata").version)
@click_log.simple_verbosity_option(logger)
def cli():
    """xsdata command line interface."""


@cli.command("init-config")
@click.argument("output", type=click.Path(), default=".xsdata.xml")
@click.option("--print", is_flag=True, default=False, help="Print output")
def init_config(*args: Any, **kwargs: Any):
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
@click.option("--config", default=".xsdata.xml", help="Configuration file")
@click.option("--package", required=False, help="Target Package", default="generated")
@click.option("--output", type=outputs, help="Output Format", default="pydata")
@click.option(
    "--compound-fields",
    type=click.BOOL,
    default=False,
    help=(
        "Use compound fields for repeating choices. "
        "Enable if elements ordering matters for your case."
    ),
)
@click.option("--wsdl", is_flag=True, default=False, help="WSDL Mode (experimental)")
@click.option("--print", is_flag=True, default=False, help="Print output")
@click.option(
    "--ns-struct",
    is_flag=True,
    default=False,
    help=(
        "Use namespaces to group classes in the same module. "
        "Useful against circular import errors."
    ),
)
def generate(*args: Any, **kwargs: Any):
    """
    Convert schema definitions to code.

    SOURCE can be either a filepath, directory or url
    """
    if kwargs["print"]:
        logger.setLevel(logging.ERROR)

    config_file = Path(kwargs["config"])
    if config_file.exists():
        config = GeneratorConfig.read(config_file)
    else:
        config = GeneratorConfig()
        config.output.format = OutputFormat(kwargs["output"])
        config.output.package = kwargs["package"]
        config.output.wsdl = kwargs["wsdl"]
        config.output.compound_fields = kwargs["compound_fields"]

        if kwargs["ns_struct"]:
            config.output.structure = OutputStructure.NAMESPACES

    uris = resolve_source(kwargs["source"], wsdl=config.output.wsdl)
    transformer = SchemaTransformer(config=config, print=kwargs["print"])

    if config.output.wsdl:
        transformer.process_definitions(next(uris))
    else:
        transformer.process_schemas(list(uris))


def resolve_source(source: str, wsdl: bool) -> Iterator[str]:
    if source.find("://") > -1 and not source.startswith("file://"):
        yield source
    else:
        path = Path(source).resolve()
        if path.is_dir():

            if wsdl:
                raise CodeGenerationError(
                    "WSDL mode doesn't support scanning directories."
                )

            yield from (x.as_uri() for x in path.glob("*.xsd"))
        else:  # is file
            yield path.as_uri()


if __name__ == "__main__":  # pragma: no cover
    cli()
