from dataclasses import dataclass


@dataclass
class ParserConfig:
    fail_on_unknown_properties: bool = True
