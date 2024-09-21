from dataclasses import dataclass, field
from typing import List, Optional


@dataclass(kw_only=True)
class BlogPost:
    """
    A representation of a blog post.
    """

    class Meta:
        name = "blog-post"

    title: str = field(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    content: str = field(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    published_date: Optional[str] = field(
        default=None,
        metadata={
            "name": "publishedDate",
            "type": "Element",
        },
    )
    author: str = field(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    tags: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
