import random

import pytest

from tests import xsdata_temp_dir
from tests.integration.benchmarks.conftest import make_books
from tests.integration.benchmarks.conftest import parse
from tests.integration.benchmarks.conftest import write
from xsdata.formats.dataclass.context import XmlContext
from xsdata.formats.dataclass.parsers import handlers as readers
from xsdata.formats.dataclass.serializers import writers

context = XmlContext()
readers_list = list(readers.__all__)
writers_list = list(writers.__all__)

random.shuffle(readers_list)
random.shuffle(writers_list)

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
