import logging
import platform
import sys
import warnings
from collections.abc import Iterator
from pathlib import Path
from typing import Any

import click
from click_default_group import DefaultGroup

from xsdata import __version__
from xsdata.codegen.transformer import ResourceTransformer
from xsdata.logger import logger
from xsdata.models.config import GeneratorConfig, GeneratorOutput
from xsdata.utils.click import LogFormatter, LogHandler, model_options
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


class DeprecatedDefaultGroup(DefaultGroup):
    """Deprecated default group."""

    def get_command(self, ctx: click.Context, cmd_name: str) -> click.Command:
        """Override to deprecate xsdata <source> shorthand."""
        if cmd_name not in self.commands:
            logger.warning(
                "`xsdata <SOURCE>` is deprecated. "
                "Use `xsdata generate <SOURCE>` instead."
            )
        return super().get_command(ctx, cmd_name)


@click.group(cls=DeprecatedDefaultGroup, default="generate", default_if_no_args=False)
@click.pass_context
@click.version_option(__version__)
def cli(ctx: click.Context, **kwargs: Any) -> None:
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

    def format_warning_restore() -> None:
        warnings.formatwarning = formatwarning_orig

    warnings.formatwarning = format_warning  # type: ignore

    ctx.call_on_close(format_warning_restore)


@cli.command("init-config")
@click.argument("output", type=click.Path(), default=".xsdata.xml")
def init_config(**kwargs: Any) -> None:
    """Create or update a configuration file."""
    file_path = Path(kwargs["output"])
    if file_path.exists():
        config = GeneratorConfig.read(file_path)
        logger.info("Updating configuration file %s", kwargs["output"])
    else:
        logger.info("Initializing configuration file %s", kwargs["output"])
        config = GeneratorConfig.create()

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
def download(source: str, output: str) -> None:
    """Download a schema or a definition locally with all its dependencies."""
    downloader = Downloader(output=Path(output).resolve())
    downloader.wget(source)

    handler.emit_warnings()


_SUPPORTED_EXTENSIONS = ("wsdl", "xsd", "dtd", "xml", "json")


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
@click.option("--cache", is_flag=True, default=False, help="Cache sources loading")
@click.option("--debug", is_flag=True, default=False, help="Show debug messages")
@click.option(
    "--extensions",
    default=",".join(_SUPPORTED_EXTENSIONS),
    help="Comma-separated list of extensions to filter",
)
@model_options(GeneratorOutput)
def generate(**kwargs: Any) -> None:
    """Generate code from xsd, dtd, wsdl, xml and json files.

    The input source can be either a filepath, uri or a directory
    containing xml, json, xsd and wsdl files.
    """
    debug = kwargs.pop("debug")
    if debug:
        logger.setLevel(logging.DEBUG)

    source = kwargs.pop("source")
    cache = kwargs.pop("cache")
    recursive = kwargs.pop("recursive")
    config_file = Path(kwargs.pop("config")).resolve()

    # Parse the comma-separated extensions string into a tuple
    extensions_str = kwargs.pop("extensions")
    extensions = tuple(ext.strip() for ext in extensions_str.split(",") if ext.strip())

    params = {k.replace("__", "."): v for k, v in kwargs.items() if v is not None}
    config = GeneratorConfig.read(config_file)
    config.output.update(**params)

    transformer = ResourceTransformer(config=config)
    uris = sorted(resolve_source(source, recursive=recursive, extensions=extensions))
    transformer.process(uris, cache=cache)

    handler.emit_warnings()


def resolve_source(
    source: str, recursive: bool, extensions: tuple[str, ...] = _SUPPORTED_EXTENSIONS
) -> Iterator[str]:
    """Yields all supported resource URIs."""
    if source.find("://") > -1 and not source.startswith("file://"):
        yield source
    else:
        path = Path(source).resolve()
        match = "**/*" if recursive else "*"
        if path.is_dir():
            for ext in extensions:
                yield from (x.as_uri() for x in path.glob(f"{match}.{ext}"))
        else:  # is a file
            yield path.as_uri()


if __name__ == "__main__":  # pragma: no cover
    cli()
