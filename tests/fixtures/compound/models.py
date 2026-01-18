from __future__ import annotations

from dataclasses import dataclass, field


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

    alpha_or_bravo_or_charlie: list[Alpha | Bravo | list[str]] = field(
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
                    "type": list[str],
                    "namespace": "",
                    "default_factory": list,
                    "tokens": True,
                },
            ),
        },
    )
