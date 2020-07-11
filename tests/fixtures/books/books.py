from dataclasses import dataclass, field
from typing import List, Optional

__NAMESPACE__ = "urn:books"


@dataclass
class BookForm:
    """
    :ivar author:
    :ivar title:
    :ivar genre:
    :ivar price:
    :ivar pub_date:
    :ivar review:
    :ivar id:
    :ivar lang:
    """
    author: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="",
            required=True
        )
    )
    title: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="",
            required=True
        )
    )
    genre: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="",
            required=True
        )
    )
    price: Optional[float] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="",
            required=True
        )
    )
    pub_date: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="",
            required=True
        )
    )
    review: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="",
            required=True
        )
    )
    id: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
    lang: str = field(
        init=False,
        default="en",
        metadata=dict(
            type="Attribute"
        )
    )


@dataclass
class BooksForm:
    """
    :ivar book:
    """
    book: List[BookForm] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )


@dataclass
class Books(BooksForm):
    class Meta:
        name = "books"
        namespace = "urn:books"
