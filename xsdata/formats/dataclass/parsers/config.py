from dataclasses import dataclass
from typing import Callable
from typing import Dict
from typing import Optional
from typing import Type
from typing import TypeVar

T = TypeVar("T")


def default_class_factory(cls: Type[T], params: Dict) -> T:
    return cls(**params)  # type: ignore


@dataclass
class ParserConfig:
    """
    Parsing configuration options.

    :param base_url: Specify a base URL when parsing from memory and
        you need support for relative links eg xinclude
    :param process_xinclude: Enable xinclude statements processing
    :param class_factory: Override default object instantiation
    :param fail_on_unknown_properties: Skip unknown properties or
        fail with exception
    :param fail_on_converter_warnings: Turn converter warnings to
        exceptions
    """

    base_url: Optional[str] = None
    process_xinclude: bool = False
    class_factory: Callable[[Type[T], Dict], T] = default_class_factory
    fail_on_unknown_properties: bool = True
    fail_on_converter_warnings: bool = False
