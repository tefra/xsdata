import tempfile
from pathlib import Path


root = Path(__file__).parent.parent
fixtures_dir = root.joinpath("tests/fixtures")
xsdata_temp_dir = Path(tempfile.gettempdir()).joinpath("xsdata")
