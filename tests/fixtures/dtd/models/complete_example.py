from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum


@dataclass(kw_only=True)
class Body:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
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


@dataclass(kw_only=True)
class Source:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class Tag:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class Title:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class Tags:
    tag: list[Tag] = field(
        default_factory=list,
        metadata={
            "name": "Tag",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
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
    created_at: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    author: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
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
    title: Title = field(
        metadata={
            "name": "Title",
            "type": "Element",
            "required": True,
        }
    )
    body: Body = field(
        metadata={
            "name": "Body",
            "type": "Element",
            "required": True,
        }
    )
    tags: Tags = field(
        metadata={
            "name": "Tags",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class Blog:
    post: list[Post] = field(
        default_factory=list,
        metadata={
            "name": "Post",
            "type": "Element",
            "min_occurs": 1,
        },
    )
