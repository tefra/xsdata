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

readers_list.remove("default_handler")
writers_list.remove("default_writer")

random.shuffle(readers_list)
random.shuffle(writers_list)

numbers = [100, 1000, 10000]

fixtures = {number: make_books(number) for number in numbers}


@pytest.mark.benchmark(disable_gc=True, group="Serialize")
@pytest.mark.parametrize("number", numbers)
@pytest.mark.parametrize("writer", writers_list)
def test_serialize(benchmark, writer, number):
    benchmark(write, number, fixtures[number], getattr(writers, writer))


@pytest.mark.benchmark(disable_gc=True, group="Parse")
@pytest.mark.parametrize("number", numbers)
@pytest.mark.parametrize("handler", readers_list)
def test_parse(benchmark, handler, number):
    src = xsdata_temp_dir.joinpath(f"benchmark_{number}.xml").read_bytes()
    benchmark(parse, src, getattr(readers, handler))
