import random

import pytest

from tests import xsdata_temp_dir
from tests.fixtures.books import BookForm
from tests.fixtures.books import Books
from xsdata.formats.dataclass.context import XmlContext
from xsdata.formats.dataclass.parsers import handlers as readers
from xsdata.formats.dataclass.parsers import XmlParser
from xsdata.formats.dataclass.serializers import writers
from xsdata.formats.dataclass.serializers import XmlSerializer

context = XmlContext()
readers_list = list(readers.__all__)
writers_list = list(writers.__all__)

random.shuffle(readers_list)
random.shuffle(writers_list)

xsdata_temp_dir.mkdir(parents=True, exist_ok=True)


def make_books(how_many: int):
    return Books(
        book=[
            BookForm(
                author="Arne Dahl",
                title="Misterioso: A Crime Novel",
                genre="Thrillers & Suspense",
                price=15.95,
                pub_date="1999-10-05",
                review=(
                    "Lorem ipsum dolor sit amet, consectetur adipiscing elit. "
                    "Integer at erat sagittis, accumsan mauris eu, egestas "
                    "quam. Nam tristique felis justo, vel iaculis ipsum cursus "
                    "at. Praesent varius enim ac nunc interdum placerat. "
                    "Integer porttitor, nibh at viverra vehicula, leo dui "
                    "suscipit nisi, ornare laoreet eros neque nec mi. Proin."
                ),
                id="9788831796781",
            )
            for _ in range(how_many)
        ]
    )


small_books = make_books(100)
medium_books = make_books(1000)
large_books = make_books(10000)


@pytest.mark.benchmark(disable_gc=True, group="Serialize: 100 books")
@pytest.mark.parametrize("writer", writers_list)
def test_serialize_small(benchmark, writer):
    benchmark(write, "small", small_books, getattr(writers, writer))


@pytest.mark.benchmark(disable_gc=True, group="Serialize: 1000 books")
@pytest.mark.parametrize("writer", writers_list)
def test_serialize_medium(benchmark, writer):
    benchmark(write, "medium", medium_books, getattr(writers, writer))


@pytest.mark.benchmark(disable_gc=True, group="Serialize: 10000 books")
@pytest.mark.parametrize("writer", writers_list)
def test_serialize_large(benchmark, writer):
    benchmark(write, "large", large_books, getattr(writers, writer))


@pytest.mark.benchmark(disable_gc=True, group="Parse: 100 books")
@pytest.mark.parametrize("handler", readers_list)
def test_parse_small(benchmark, handler):
    src = xsdata_temp_dir.joinpath("benchmark_small.xml").read_bytes()
    benchmark(parse, src, getattr(readers, handler))


@pytest.mark.benchmark(disable_gc=True, group="Parse: 1000 books")
@pytest.mark.parametrize("handler", readers_list)
def test_parse_medium(benchmark, handler):
    src = xsdata_temp_dir.joinpath("benchmark_medium.xml").read_bytes()
    benchmark(parse, src, getattr(readers, handler))


@pytest.mark.benchmark(disable_gc=True, group="Parse: 10000 books")
@pytest.mark.parametrize("handler", readers_list)
def test_parse_large(benchmark, handler):
    src = xsdata_temp_dir.joinpath("benchmark_large.xml").read_bytes()
    benchmark(parse, src, getattr(readers, handler))


def parse(source, handler):
    parser = XmlParser(context=context, handler=handler)
    parser.from_bytes(source, Books)


def write(size, obj, writer):
    with xsdata_temp_dir.joinpath(f"benchmark_{size}.xml").open("w") as f:
        serializer = XmlSerializer(writer=writer)
        serializer.write(f, obj)
