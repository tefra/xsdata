from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(kw_only=True)
class Member:
    class Meta:
        name = "member"
        namespace = "urn:relations"
        abstract = True
        key = ["name", "surname"]

    name: str = field(
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    surname: str = field(
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )

@dataclass(kw_only=True)
class Child(Member):
    class Meta:
        name = "child"

    age: int = field(
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )

@dataclass(kw_only=True)
class Parent(Member):
    class Meta:
        name = "parent"

    children: list[Child] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "wrapper": "children",
            "name": "child",
            "idref": True,
        }
    )

@dataclass(kw_only=True)
class Family:
    class Meta:
        name = "family"
        namespace = "urn:relations"

    member: list[Member] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "wrapper": "members",
        }  )
    favorite: Member = field(
        metadata={
            "type": "Element",
            "idref": True,
        })