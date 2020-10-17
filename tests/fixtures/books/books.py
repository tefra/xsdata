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
    pub_date: Optional[str] = field(
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
    """
    :ivar book:
    """
    book: List[BookForm] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )


@dataclass
class Books(BooksForm):
    """Το βιβλίο."""
    class Meta:
        name = "books"
        namespace = "urn:books"
