from dataclasses import dataclass, field
from typing import Optional

from xsdata.models.datatype import XmlDate

__NAMESPACE__ = "urn:books"


@dataclass
class BookForm:
    """
    Book Definition.

    Attributes:
        author: Writer's name
        title: Book Title
        genre: Book Genre
        price: Amount in USD
        pub_date: Publication date
        review: Sticky Review
        id: International Standard Book Number
        lang: Language ISO Code
    """

    author: str | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
    title: str | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
    genre: str | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
    price: float | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
    pub_date: XmlDate | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
    review: str | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
    id: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    lang: str = field(
        init=False,
        default="en",
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class BooksForm:
    book: list[BookForm] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class Books(BooksForm):
    """
    Το βιβλίο.
    """

    class Meta:
        name = "books"
        namespace = "urn:books"
