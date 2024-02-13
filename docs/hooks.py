from pathlib import Path

from mkdocs.config import Config

docs_dir = Path(__file__).parent


def on_pre_build(config: Config):
    """Mkdocs pre-build entrypoint."""
