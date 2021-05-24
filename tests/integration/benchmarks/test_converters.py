import pytest

from xsdata.models.datatype import XmlDate
from xsdata.models.datatype import XmlDateTime
from xsdata.models.datatype import XmlDuration
from xsdata.models.datatype import XmlTime


@pytest.mark.benchmark(disable_gc=True, group="converters", min_rounds=100000)
def test_xml_date_time(benchmark):
    benchmark(XmlDateTime.from_string, "2010-09-20T13:00:00.000+01:00")


@pytest.mark.benchmark(disable_gc=True, group="converters", min_rounds=100000)
def test_xml_time(benchmark):
    benchmark(XmlTime.from_string, "13:00:00.000+01:00")


@pytest.mark.benchmark(disable_gc=True, group="converters", min_rounds=100000)
def test_xml_date(benchmark):
    benchmark(XmlDate.from_string, "2010-09-20")


@pytest.mark.benchmark(disable_gc=True, group="converters", min_rounds=100000)
def test_xml_duration(benchmark):
    benchmark(XmlDuration, "P2Y6M5DT12H35M30.5S")
