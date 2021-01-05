from tests.fixtures.books import Books, BookForm
from xsdata.models.datatype import XmlDate

books = Books(
    book=[
        BookForm(
            id="bk001",
            author="Hightower, Kim",
            title="The First Book",
            genre="Fiction",
            price=44.95,
            pub_date=XmlDate(2000, 10, 1),
            review="An amazing story of nothing.",
        ),
        BookForm(
            id="bk002",
            author="Nagata, Suanne",
            title="Becoming Somebody",
            genre="Biography",
            price=33.95,
            pub_date=XmlDate(2001, 1, 10),
            review="A masterpiece of the fine art of gossiping.",
        ),
    ]
)
events = [
    ('start-ns', 'brk', 'urn:books'),
    ('start', '{urn:books}books', {}, {'brk': 'urn:books'}),
    ('start', 'book', {'id': 'bk001', 'lang': 'en'}, {'brk': 'urn:books'}),
    ('start', 'author', {}, {'brk': 'urn:books'}),
    ('end', 'author', 'Hightower, Kim', '\n    '),
    ('start', 'title', {}, {'brk': 'urn:books'}),
    ('end', 'title', 'The First Book', '\n    '),
    ('start', 'genre', {}, {'brk': 'urn:books'}),
    ('end', 'genre', 'Fiction', '\n    '),
    ('start', 'price', {}, {'brk': 'urn:books'}),
    ('end', 'price', '44.95', '\n    '),
    ('start', 'pub_date', {}, {'brk': 'urn:books'}),
    ('end', 'pub_date', '2000-10-01', '\n    '),
    ('start', 'review', {}, {'brk': 'urn:books'}),
    ('end', 'review', 'An amazing story of nothing.', '\n  '),
    ('end', 'book', '\n    ', '\n  '),
    ('start', 'book', {'id': 'bk002', 'lang': 'en'}, {'brk': 'urn:books'}),
    ('start', 'author', {}, {'brk': 'urn:books'}),
    ('end', 'author', 'Nagata, Suanne', '\n    '),
    ('start', 'title', {}, {'brk': 'urn:books'}),
    ('end', 'title', 'Becoming Somebody', '\n    '),
    ('start', 'genre', {}, {'brk': 'urn:books'}),
    ('end', 'genre', 'Biography', '\n    '),
    ('start', 'price', {}, {'brk': 'urn:books'}),
    ('end', 'price', '33.95', '\n    '),
    ('start', 'pub_date', {}, {'brk': 'urn:books'}),
    ('end', 'pub_date', '2001-01-10', '\n    '),
    ('start', 'review', {}, {'brk': 'urn:books'}),
    ('end', 'review', 'A masterpiece of the fine art of gossiping.', '\n  '),
    ('end', 'book', '\n    ', '\n'),
    ('end', '{urn:books}books', '\n  ', None)
]
