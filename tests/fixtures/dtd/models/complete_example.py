from dataclasses import dataclass, field
from enum import Enum
from typing import Optional


@dataclass
class Body:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass
class Origin:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


class PostStatus(Enum):
    DRAFT = "draft"
    PUBLISHED = "published"


@dataclass
class Source:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass
class Tag:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass
class Title:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass
class Tags:
    tag: list[Tag] = field(
        default_factory=list,
        metadata={
            "name": "Tag",
            "type": "Element",
        },
    )


@dataclass
class Post:
    status: PostStatus = field(
        default=PostStatus.DRAFT,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    lang: str = field(
        default="en",
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
            "required": True,
        },
    )
    created_at: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    author: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    origin: list[Origin] = field(
        default_factory=list,
        metadata={
            "name": "Origin",
            "type": "Element",
        },
    )
    source: list[Source] = field(
        default_factory=list,
        metadata={
            "name": "Source",
            "type": "Element",
        },
    )
    title: Optional[Title] = field(
        default=None,
        metadata={
            "name": "Title",
            "type": "Element",
            "required": True,
        },
    )
    body: Optional[Body] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
            "required": True,
        },
    )
    tags: Optional[Tags] = field(
        default=None,
        metadata={
            "name": "Tags",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class Blog:
    post: list[Post] = field(
        default_factory=list,
        metadata={
            "name": "Post",
            "type": "Element",
            "min_occurs": 1,
        },
    )
