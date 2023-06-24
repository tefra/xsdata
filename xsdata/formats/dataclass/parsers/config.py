from typing import Callable
from typing import Dict
from typing import Optional
from typing import Type

from xsdata.formats.bindings import T


def default_class_factory(cls: Type[T], params: Dict) -> T:
    return cls(**params)  # type: ignore


class ParserConfig:
    """
    Parsing configuration options.

    :param base_url: Specify a base URL when parsing from memory, and
        you need support for relative links e.g. xinclude
    :param load_dtd: Enable loading external dtd (lxml only)
    :param process_xinclude: Enable xinclude statements processing
    :param class_factory: Override default object instantiation
    :param fail_on_unknown_properties: Skip unknown properties or fail
        with exception
    :param fail_on_unknown_attributes: Skip unknown XML attributes or
        fail with exception
    :param fail_on_converter_warnings: Turn converter warnings to
        exceptions
    """

    __slots__ = (
        "base_url",
        "load_dtd",
        "process_xinclude",
        "class_factory",
        "fail_on_unknown_properties",
        "fail_on_unknown_attributes",
        "fail_on_converter_warnings",
    )

    def __init__(
        self,
        base_url: Optional[str] = None,
        load_dtd: bool = False,
        process_xinclude: bool = False,
        class_factory: Callable[[Type[T], Dict], T] = default_class_factory,
        fail_on_unknown_properties: bool = True,
        fail_on_unknown_attributes: bool = False,
        fail_on_converter_warnings: bool = False,
    ):
        self.base_url = base_url
        self.load_dtd = load_dtd
        self.process_xinclude = process_xinclude
        self.class_factory = class_factory
        self.fail_on_unknown_properties = fail_on_unknown_properties
        self.fail_on_unknown_attributes = fail_on_unknown_attributes
        self.fail_on_converter_warnings = fail_on_converter_warnings
