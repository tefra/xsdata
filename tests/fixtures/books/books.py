from dataclasses import dataclass, field
from typing import List, Optional
from xsdata.models.datatype import XmlDate

__NAMESPACE__ = "urn:books"


@dataclass
class BookForm:
    """
    Book Definition.

    Attributes
        author: Writer's name
        title: Book Title
        genre: Book Genre
        price: Amount in USD
        pub_date: Publication date
        review: Sticky Review
        id: International Standard Book Number
        lang: Language ISO Code
    """
    author: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    genre: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    price: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    pub_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    review: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    lang: str = field(
        init=False,
        default="en",
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class BooksForm:
    book: List[BookForm] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )


@dataclass
class Books(BooksForm):
    """
    Το βιβλίο.
    """
    class Meta:
        name = "books"
        namespace = "urn:books"
