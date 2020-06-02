from dataclasses import dataclass


@dataclass
class ParserConfig:
    """
    Parsing configuration.

    :param fail_on_unknown_properties: Skip unknown properties or fail with exception.
    """

    fail_on_unknown_properties: bool = True
