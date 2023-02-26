from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional


class PostStatus(Enum):
    DRAFT = "draft"
    PUBLISHED = "published"


@dataclass
class Tags:
    tag: List[str] = field(
        default_factory=list,
        metadata={
            "name": "Tag",
            "type": "Element",
        }
    )


@dataclass
class Post:
    status: PostStatus = field(
        default=PostStatus.DRAFT,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    lang: str = field(
        default="en",
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
            "required": True,
        }
    )
    created_at: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    author: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    origin: List[str] = field(
        default_factory=list,
        metadata={
            "name": "Origin",
            "type": "Element",
        }
    )
    source: List[str] = field(
        default_factory=list,
        metadata={
            "name": "Source",
            "type": "Element",
        }
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "name": "Title",
            "type": "Element",
            "required": True,
        }
    )
    body: Optional[str] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
            "required": True,
        }
    )
    tags: Optional[Tags] = field(
        default=None,
        metadata={
            "name": "Tags",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class Blog:
    post: List[Post] = field(
        default_factory=list,
        metadata={
            "name": "Post",
            "type": "Element",
            "min_occurs": 1,
        }
    )
