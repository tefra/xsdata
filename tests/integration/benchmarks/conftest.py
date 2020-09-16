import tempfile
from pathlib import Path


def pytest_unconfigure(config):
    temp_xsdata = Path(tempfile.gettempdir()).joinpath("xsdata")
    for tmp_file in temp_xsdata.glob("*"):
        tmp_file.unlink()

    temp_xsdata.rmdir()
