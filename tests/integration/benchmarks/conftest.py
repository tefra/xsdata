from tests import xsdata_temp_dir
from xsdata.formats.dataclass.context import XmlContext

xsdata_temp_dir.mkdir(parents=True, exist_ok=True)
context = XmlContext()


def pytest_unconfigure(config):
    for tmp_file in xsdata_temp_dir.glob("*"):
        tmp_file.unlink()

    xsdata_temp_dir.rmdir()
