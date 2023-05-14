import logging
import platform
import sys
import warnings
from pathlib import Path
from typing import Any
from typing import Iterator

import click
from click_default_group import DefaultGroup

from xsdata import __version__
from xsdata.codegen.transformer import SchemaTransformer
from xsdata.logger import logger
from xsdata.models.config import GeneratorConfig
from xsdata.models.config import GeneratorOutput
from xsdata.utils.click import LogFormatter
from xsdata.utils.click import LogHandler
from xsdata.utils.click import model_options
from xsdata.utils.downloader import Downloader
from xsdata.utils.hooks import load_entry_points

# Load cli plugins
load_entry_points("xsdata.plugins.cli")

# Setup xsdata logger to print records to stdout/stderr
handler = LogHandler()
handler.formatter = LogFormatter()

logger.handlers = [handler]
logger.propagate = False

# Attach the cli handler to the python warnings logger
py_warnings = logging.getLogger("py.warnings")
py_warnings.handlers = [handler]
py_warnings.propagate = False

# Log warnings as well
logging.captureWarnings(True)


@click.group(cls=DefaultGroup, default="generate", default_if_no_args=False)
@click.pass_context
@click.version_option(__version__)
def cli(ctx: click.Context, **kwargs: Any):
    """Xsdata command line interface."""
    logger.setLevel(logging.INFO)
    formatwarning_orig = warnings.formatwarning
    logger.info(
        "========= xsdata v%s / Python %s / Platform %s =========\n",
        __version__,
        platform.python_version(),
        sys.platform,
    )

    def format_warning(message: Any, category: Any, *args: Any) -> str:
        return (
            f"{category.__name__}: {message}" if category else message
        )  # pragma: no cover

    def format_warning_restore():
        warnings.formatwarning = formatwarning_orig

    warnings.formatwarning = format_warning  # type: ignore

    ctx.call_on_close(format_warning_restore)


@cli.command("init-config")
@click.argument("output", type=click.Path(), default=".xsdata.xml")
@click.option("-pp", "--print", is_flag=True, default=False, help="Print output")
def init_config(**kwargs: Any):
    """Create or update a configuration file."""
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

    handler.emit_warnings()


@cli.command("download")
@click.argument("source", required=True)
@click.option(
    "-o",
    "--output",
    type=click.Path(),
    default="./",
    help="Output directory, default cwd",
)
def download(source: str, output: str):
    """Download a schema or a definition locally with all its dependencies."""
    downloader = Downloader(output=Path(output).resolve())
    downloader.wget(source)

    handler.emit_warnings()


@cli.command("generate")
@click.argument("source", required=True)
@click.option(
    "-r",
    "--recursive",
    is_flag=True,
    default=False,
    help="Search files recursively in the source directory",
)
@click.option("-c", "--config", default=".xsdata.xml", help="Project configuration")
@click.option("-pp", "--print", is_flag=True, default=False, help="Print output")
@click.option("--cache", is_flag=True, default=False, help="Cache sources loading")
@click.option("--debug", is_flag=True, default=False, help="Show debug messages")
@model_options(GeneratorOutput)
def generate(**kwargs: Any):
    """
    Generate code from xml schemas, webservice definitions and any xml or json
    document.

    The input source can be either a filepath, uri or a directory
    containing xml, json, xsd and wsdl files.
    """

    debug = kwargs.pop("debug")
    if debug:
        logger.setLevel(logging.DEBUG)

    source = kwargs.pop("source")
    stdout = kwargs.pop("print")
    cache = kwargs.pop("cache")
    recursive = kwargs.pop("recursive")
    config_file = Path(kwargs.pop("config")).resolve()

    params = {k.replace("__", "."): v for k, v in kwargs.items() if v is not None}
    config = GeneratorConfig.read(config_file)
    config.output.update(**params)

    transformer = SchemaTransformer(config=config, print=stdout)
    uris = sorted(resolve_source(source, recursive=recursive))
    transformer.process(uris, cache=cache)

    handler.emit_warnings()


def resolve_source(source: str, recursive: bool) -> Iterator[str]:
    if source.find("://") > -1 and not source.startswith("file://"):
        yield source
    else:
        path = Path(source).resolve()
        match = "**/*" if recursive else "*"
        if path.is_dir():
            for ext in ["wsdl", "xsd", "dtd", "xml", "json"]:
                yield from (x.as_uri() for x in path.glob(f"{match}.{ext}"))
        else:  # is file
            yield path.as_uri()


if __name__ == "__main__":  # pragma: no cover
    cli()
