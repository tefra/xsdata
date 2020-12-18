from dataclasses import dataclass
from typing import Optional


@dataclass
class ParserConfig:
    """
    Parsing configuration options.

    :param base_url: Optionally provide a base URL for the parser, if you are
        parsing from memory and you want support for relative links eg xinclude
    :param process_xinclude: Process xinclude statements.
    :param fail_on_unknown_properties: Skip unknown properties or fail with exception.
    """

    base_url: Optional[str] = None
    process_xinclude: bool = False
    fail_on_unknown_properties: bool = True
