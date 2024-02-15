# Dict Decoding

The [DictDecoder][xsdata.formats.dataclass.parsers.DictDecoder] can be used to bind a
dictionary or a list of dictionaries to data models. It's the backbone of the
[JsonParser][xsdata.formats.dataclass.parsers.JsonParser] without the loading
entrypoints.

## Single object

```python
>>> from xsdata.formats.dataclass.context import XmlContext
>>> from xsdata.formats.dataclass.parsers import DictDecoder
>>> from xsdata.formats.dataclass.parsers.config import ParserConfig
>>> from tests.fixtures.books.books import BookForm
>>>
>>> config = ParserConfig()
>>> context = XmlContext()
>>> decoder = DictDecoder(context=context, config=config)
>>>
>>> data = {
...     "author": "Hightower, Kim",
...     "title": "The First Book",
...     "genre": "Fiction",
...     "price": 44.95,
...     "pub_date": "2000-10-01",
...     "review": "An amazing story of nothing.",
...     "id": "bk001"
... }
>>> book = decoder.decode(data, BookForm)
>>> book.author
'Hightower, Kim'

```

## List of objects

```python
>>> from typing import List
>>> from tests.fixtures.books.books import BookForm
>>>
>>> data = [
...     {
...       "author": "Hightower, Kim",
...       "title": "The First Book",
...       "genre": "Fiction",
...       "price": 44.95,
...       "pub_date": "2000-10-01",
...       "review": "An amazing story of nothing.",
...       "id": "bk001"
...     },
...     {
...       "author": "Nagata, Suanne",
...       "title": "Becoming Somebody",
...       "genre": "Biography",
...       "price": None,
...       "pub_date": None,
...       "review": "A masterpiece of the fine art of gossiping.",
...       "id": "bk002"
...     }
...   ]
>>> booklist = decoder.decode(data, List[BookForm])
>>> booklist[1].author
'Nagata, Suanne'

```
