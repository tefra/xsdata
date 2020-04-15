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
            name="author",
            type="Element",
            namespace="",
            required=True
        )
    )
    title: Optional[str] = field(
        default=None,
        metadata=dict(
            name="title",
            type="Element",
            namespace="",
            required=True
        )
    )
    genre: Optional[str] = field(
        default=None,
        metadata=dict(
            name="genre",
            type="Element",
            namespace="",
            required=True
        )
    )
    price: Optional[float] = field(
        default=None,
        metadata=dict(
            name="price",
            type="Element",
            namespace="",
            required=True
        )
    )
    pub_date: Optional[str] = field(
        default=None,
        metadata=dict(
            name="pub_date",
            type="Element",
            namespace="",
            required=True
        )
    )
    review: Optional[str] = field(
        default=None,
        metadata=dict(
            name="review",
            type="Element",
            namespace="",
            required=True
        )
    )
    id: Optional[str] = field(
        default=None,
        metadata=dict(
            name="id",
            type="Attribute"
        )
    )
    lang: str = field(
        init=False,
        default="en",
        metadata=dict(
            name="lang",
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
            name="book",
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
