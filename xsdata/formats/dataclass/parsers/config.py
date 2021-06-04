from dataclasses import dataclass
from typing import Optional


@dataclass
class ParserConfig:
    """
    Parsing configuration options.

    :param base_url: Specify a base URL when parsing from memory and
        you need support for relative links eg xinclude
    :param process_xinclude: Enable xinclude statements processing
    :param fail_on_unknown_properties: Skip unknown properties or
        fail with exception
    :param fail_on_converter_warnings: Turn converter warnings to
        exceptions
    """

    base_url: Optional[str] = None
    process_xinclude: bool = False
    fail_on_unknown_properties: bool = True
    fail_on_converter_warnings: bool = False
