from dataclasses import dataclass, field
from typing import Any, Callable, Dict, Optional, Type

from xsdata.formats.bindings import T


def default_class_factory(cls: Type[T], params: Dict[str, Any]) -> T:
    """The default class factory.

    To be used as a hook for plugins.

    Args:
        cls: The target class type to instantiate
        params: The class keyword arguments

    Returns:
        A new class instance with the given params.
    """
    return cls(**params)  # type: ignore


@dataclass
class ParserConfig:
    """Parsing configuration options.

    Not all options are applicable for both xml and json documents.

    Args:
        base_url: Specify a base URL when parsing from memory, and
            you need support for relative links e.g. xinclude
        load_dtd: Enable loading external dtd (lxml only)
        process_xinclude: Enable xinclude statements processing
        class_factory: Override default object instantiation
        fail_on_unknown_properties: Skip unknown properties or fail with exception
        fail_on_unknown_attributes: Skip unknown XML attributes or fail with exception
        fail_on_converter_warnings: Turn converter warnings to exceptions
    """

    base_url: Optional[str] = None
    load_dtd: bool = False
    process_xinclude: bool = False
    class_factory: Callable[[Type[T], Dict[str, Any]], T] = field(
        default=default_class_factory
    )
    fail_on_unknown_properties: bool = True
    fail_on_unknown_attributes: bool = False
    fail_on_converter_warnings: bool = False
