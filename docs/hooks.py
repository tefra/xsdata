from pathlib import Path

from mkdocs.config import Config

docs_dir = Path(__file__).parent


def on_pre_build(config: Config) -> None:
    """Mkdocs pre-build entrypoint."""
