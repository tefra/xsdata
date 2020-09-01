import random

import pytest

from tests import xsdata_temp_dir
from tests.fixtures.books import Books
from tests.integration.conftest import bench_fixtures
from xsdata.formats.dataclass.context import XmlContext
from xsdata.formats.dataclass.parsers import handlers
from xsdata.formats.dataclass.parsers import XmlParser

context = XmlContext()
handlers_list = list(handlers.__all__)
ids = [f"{key}-{size}" for key, size in bench_fixtures.items()]

random.shuffle(handlers_list)


@pytest.mark.benchmark(disable_gc=True, group=f"size: {bench_fixtures['small']}")
@pytest.mark.parametrize("handler", handlers_list)
def test_small(benchmark, handler):
    src = xsdata_temp_dir.joinpath("benchmark_small.xml").read_bytes()
    benchmark(parse, src, getattr(handlers, handler))


@pytest.mark.benchmark(disable_gc=True, group=f"size: {bench_fixtures['medium']}")
@pytest.mark.parametrize("handler", handlers_list)
def test_medium(benchmark, handler):
    src = xsdata_temp_dir.joinpath("benchmark_medium.xml").read_bytes()
    benchmark(parse, src, getattr(handlers, handler))


@pytest.mark.benchmark(disable_gc=True, group=f"size: {bench_fixtures['large']}")
@pytest.mark.parametrize("handler", handlers_list)
def test_large(benchmark, handler):
    src = xsdata_temp_dir.joinpath("benchmark_large.xml").read_bytes()
    benchmark(parse, src, getattr(handlers, handler))


def parse(source, handler):
    parser = XmlParser(context=context, handler=handler)
    parser.from_bytes(source, Books)
