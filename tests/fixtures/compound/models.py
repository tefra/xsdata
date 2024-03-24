from dataclasses import dataclass, field
from typing import List, Union


@dataclass
class Alpha:
    class Meta:
        name = "alpha"

    a: bool = field(
        init=False,
        default=True,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class Bravo:
    class Meta:
        name = "bravo"

    b: bool = field(
        init=False,
        default=True,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class Root:
    class Meta:
        name = "root"

    alpha_or_bravo_or_charlie: List[Union[Alpha, Bravo, List[str]]] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "alpha",
                    "type": Alpha,
                },
                {
                    "name": "bravo",
                    "type": Bravo,
                },
                {
                    "name": "charlie",
                    "type": List[str],
                    "namespace": "",
                    "default_factory": list,
                    "tokens": True,
                },
            ),
        },
    )
