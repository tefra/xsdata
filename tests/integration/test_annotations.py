import os

import pytest
from click.testing import CliRunner

from tests import fixtures_dir
from tests import root
from xsdata.cli import cli
from xsdata.formats.dataclass.context import XmlContext
from xsdata.formats.dataclass.parsers.xml import XmlParser
from xsdata.utils.testing import load_class

os.chdir(root)


def test_annotations():
    filepath = fixtures_dir.joinpath("annotations")
    schema = filepath.joinpath("model.xsd")
    runner = CliRunner()
    result = runner.invoke(
        cli, [str(schema), f"--config={str(filepath.joinpath('xsdata.xml'))}"]
    )

    if result.exception:
        raise result.exception

    try:
        Measurement = load_class(result.output, "Measurement")
        unit = load_class(result.output, "unit")
    except Exception:
        pytest.fail("Could not load class with member having the same name as type")

    filename = str(filepath.joinpath("sample.xml"))
    parser = XmlParser(context=XmlContext())
    measurement = parser.parse(filename, Measurement)
    assert measurement.value == 2.0
    assert measurement.unit == unit.KG
