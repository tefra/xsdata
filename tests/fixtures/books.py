from dataclasses import dataclass, field
from typing import List, Optional


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
    """

    author: Optional[str] = field(
        default=None,
        metadata=dict(name="author", type="Element", required=True),
    )
    title: Optional[str] = field(
        default=None,
        metadata=dict(name="title", type="Element", required=True),
    )
    genre: Optional[str] = field(
        default=None,
        metadata=dict(name="genre", type="Element", required=True),
    )
    price: Optional[float] = field(
        default=None,
        metadata=dict(name="price", type="Element", required=True),
    )
    pub_date: Optional[str] = field(
        default=None,
        metadata=dict(name="pub_date", type="Element", required=True),
    )
    review: Optional[str] = field(
        default=None,
        metadata=dict(name="review", type="Element", required=True),
    )
    id: Optional[str] = field(
        default=None, metadata=dict(name="id", type="Attribute")
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
            min_occurs=0,
            max_occurs=9223372036854775807,
        ),
    )


@dataclass
class Books(BooksForm):
    class Meta:
        name = "books"
