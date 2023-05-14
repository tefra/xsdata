============
JSON Binding
============

All binding modules rely on a :class:`~xsdata.formats.dataclass.context.XmlContext`
instance to cache model metadata and binding information.

It's recommended to either reuse the same parser/serializer instance or reuse the
context instance.

.. code-block::

    from xsdata.formats.dataclass.context import XmlContext
    from xsdata.formats.dataclass.parsers import JsonParser
    from xsdata.formats.dataclass.serializers import JsonSerializer

    context = XmlContext()
    parser = JsonParser(context=context)
    serializer = JsonSerializer(context=context)


.. testsetup:: *

    import io
    from pathlib import Path
    from xsdata.formats.dataclass.context import XmlContext
    from xsdata.formats.dataclass.parsers import JsonParser
    from xsdata.models.datatype import XmlDate
    from tests import fixtures_dir
    from tests.fixtures.books.books import Books


Parse from json filename
========================

.. doctest::

    >>> from pathlib import Path
    >>> from xsdata.formats.dataclass.context import XmlContext
    >>> from xsdata.formats.dataclass.parsers import JsonParser
    >>> from tests.fixtures.books.books import Books
    >>> from tests import fixtures_dir # pathlib.Path
    ...
    >>> filename = str(fixtures_dir.joinpath("books/books.json"))
    >>> parser = JsonParser(context=XmlContext())
    >>> books = parser.parse(filename, Books)
    >>> books.book[0]
    BookForm(author='Hightower, Kim', title='The First Book', genre='Fiction', price=44.95, pub_date=XmlDate(2000, 10, 1), review='An amazing story of nothing.', id='bk001', lang='en')


Parse from json file object
===========================

.. doctest::

    >>> json_path = fixtures_dir.joinpath("books/books.json")
    >>> with json_path.open("rb") as fp:
    ...     books = parser.parse(fp, Books)
    >>> books.book[0]
    BookForm(author='Hightower, Kim', title='The First Book', genre='Fiction', price=44.95, pub_date=XmlDate(2000, 10, 1), review='An amazing story of nothing.', id='bk001', lang='en')


Parse from json stream
======================

.. doctest::

    >>> import io
    >>> books = parser.parse(io.BytesIO(json_path.read_bytes()), Books)
    >>> books.book[0]
    BookForm(author='Hightower, Kim', title='The First Book', genre='Fiction', price=44.95, pub_date=XmlDate(2000, 10, 1), review='An amazing story of nothing.', id='bk001', lang='en')


Parse from json string
======================

.. doctest::

    >>> books = parser.from_string(json_path.read_text(), Books)
    >>> books.book[0]
    BookForm(author='Hightower, Kim', title='The First Book', genre='Fiction', price=44.95, pub_date=XmlDate(2000, 10, 1), review='An amazing story of nothing.', id='bk001', lang='en')


Parse from json bytes
=====================

.. doctest::

    >>> books = parser.from_bytes(json_path.read_bytes(), Books)
    >>> books.book[0]
    BookForm(author='Hightower, Kim', title='The First Book', genre='Fiction', price=44.95, pub_date=XmlDate(2000, 10, 1), review='An amazing story of nothing.', id='bk001', lang='en')


Parse from json Path
====================

.. doctest::

    >>> books = parser.from_path(json_path, Books)
    >>> books.book[0]
    BookForm(author='Hightower, Kim', title='The First Book', genre='Fiction', price=44.95, pub_date=XmlDate(2000, 10, 1), review='An amazing story of nothing.', id='bk001', lang='en')


Parse json with unknown properties
==================================

By default the parser will fail on unknown properties, but you can disable these
errors through configuration.


.. doctest::

    >>> from tests.fixtures.books import *  # Import all classes
    >>> from xsdata.formats.dataclass.parsers.config import ParserConfig
    ...
    >>> config = ParserConfig(
    ...     fail_on_unknown_properties=False,
    ...     fail_on_unknown_attributes=False,
    ... )
    >>> json_string = """{
    ...   "author": "Hightower, Kim",
    ...   "unknown_property": "I will fail"
    ... }"""
    >>> parser = JsonParser(config=config)
    >>> parser.from_string(json_string, BookForm)
    BookForm(author='Hightower, Kim', title=None, genre=None, price=None, pub_date=None, review=None, id=None, lang='en')

API :ref:`Reference <ParserConfig>`.


Parse with unknown json target type
===================================

It's optimal to provide the target model but completely optional. The parser can scan
all the imported modules to find a matching dataclass.

.. doctest::

    >>> from tests.fixtures.books import *  # Import all classes
    >>> from xsdata.formats.dataclass.parsers.config import ParserConfig
    >>> json_string = """{
    ...   "author": "Hightower, Kim",
    ...   "title": "The First Book",
    ...   "genre": "Fiction",
    ...   "price": 44.95,
    ...   "pub_date": "2000-10-01",
    ...   "review": "An amazing story of nothing.",
    ...   "id": "bk001"
    ... }"""
    >>> parser = JsonParser()
    >>> parser.from_string(json_string)
    BookForm(author='Hightower, Kim', title='The First Book', genre='Fiction', price=44.95, pub_date=XmlDate(2000, 10, 1), review='An amazing story of nothing.', id='bk001', lang='en')

.. warning::

    The class locator searches for a dataclass that includes all the input object
    properties. This process doesn't work for documents with unknown properties even
    if the configuration option is disabled!


Parser list of objects
======================

Specify the target binding type to ``List[ModelName]``

.. doctest::

    >>> from typing import List
    >>>
    >>> json_string = """[
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
    ...       "price": null,
    ...       "pub_date": null,
    ...       "review": "A masterpiece of the fine art of gossiping.",
    ...       "id": "bk002"
    ...     }
    ...   ]"""
    >>> parser = JsonParser()
    >>> booklist = parser.from_string(json_string, List[BookForm])
    >>> booklist[1].author
    'Nagata, Suanne'


Parser with custom json load factory
====================================

The default factory is python's builtin :func:`python:json.load` but you can use any
other implementation as long as it's has a compatible signature.

.. code-block:: python

    import ujson

    parser = JsonParser(load_factory=ujson.load)


Serialize json to string
========================

.. doctest::

    >>> from xsdata.formats.dataclass.context import XmlContext
    >>> from xsdata.formats.dataclass.serializers import JsonSerializer
    >>> from xsdata.formats.dataclass.serializers.config import SerializerConfig
    >>> from xsdata.models.datatype import XmlDate
    >>> books = Books(
    ...    book=[
    ...        BookForm(
    ...            id="bk001",
    ...            author="Hightower, Kim",
    ...            title="The First Book",
    ...            genre="Fiction",
    ...            price=44.95,
    ...            review="An amazing story of nothing.",
    ...        ),
    ...        BookForm(
    ...            id="bk002",
    ...            author="Nagata, Suanne",
    ...            title="Becoming Somebody",
    ...            price=33.95,
    ...            pub_date=XmlDate(2001, 1, 10),
    ...            review="A masterpiece of the fine art of gossiping.",
    ...        ),
    ...    ]
    ... )
    >>> config = SerializerConfig(pretty_print=True)
    >>> serializer = JsonSerializer(context=XmlContext(), config=config)
    >>> print(serializer.render(books))
    {
      "book": [
        {
          "author": "Hightower, Kim",
          "title": "The First Book",
          "genre": "Fiction",
          "price": 44.95,
          "pub_date": null,
          "review": "An amazing story of nothing.",
          "id": "bk001",
          "lang": "en"
        },
        {
          "author": "Nagata, Suanne",
          "title": "Becoming Somebody",
          "genre": null,
          "price": 33.95,
          "pub_date": "2001-01-10",
          "review": "A masterpiece of the fine art of gossiping.",
          "id": "bk002",
          "lang": "en"
        }
      ]
    }


Serialize json to stream
=========================

.. doctest::

    >>> from pathlib import Path
    ...
    >>> path = Path("output.json")
    >>> with path.open("w") as fp:
    ...     serializer.write(fp, books)
    ...
    >>> print(path.read_text())
    {
      "book": [
        {
          "author": "Hightower, Kim",
          "title": "The First Book",
          "genre": "Fiction",
          "price": 44.95,
          "pub_date": null,
          "review": "An amazing story of nothing.",
          "id": "bk001",
          "lang": "en"
        },
        {
          "author": "Nagata, Suanne",
          "title": "Becoming Somebody",
          "genre": null,
          "price": 33.95,
          "pub_date": "2001-01-10",
          "review": "A masterpiece of the fine art of gossiping.",
          "id": "bk002",
          "lang": "en"
        }
      ]
    }

    >>> path.unlink()


Serialize with custom dict factory
==================================

By using a custom dict factory you can change the output behaviour, like filter out
``None`` values.

.. doctest::

    >>> from typing import Dict, Tuple
    >>>
    >>> def filter_none(x: Tuple) -> Dict:
    ...     return {k: v for k, v in x if v is not None}
    >>>
    >>> books.book[0].genre = None
    >>> config = SerializerConfig(pretty_print=True)
    >>> serializer = JsonSerializer(dict_factory=filter_none, config=config)
    >>> print(serializer.render(books.book[0]))
    {
      "author": "Hightower, Kim",
      "title": "The First Book",
      "price": 44.95,
      "review": "An amazing story of nothing.",
      "id": "bk001",
      "lang": "en"
    }


or conveniently

.. doctest::

    >>> from xsdata.formats.dataclass.serializers.json import DictFactory
    >>>
    >>> serializer = JsonSerializer(dict_factory=DictFactory.FILTER_NONE)


Serialize with custom json dump factory
=======================================

The default factory is python's builtin :func:`python:json.dump` but you can use any
other implementation as long as it's has a compatible signature.

.. code-block:: python

    import ujson

    serializer = JsonSerializer(dump_factory=ujson.dump)


.. meta::
    :keywords: json, parse, serialize, python
