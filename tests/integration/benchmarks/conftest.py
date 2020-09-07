import tempfile
from pathlib import Path

from tests import xsdata_temp_dir
from tests.fixtures.books import BookForm
from tests.fixtures.books import Books
from xsdata.formats.dataclass.serializers import XmlSerializer

bench_fixtures = {
    "small": 100,
    "medium": 1000,
    "large": 10000,
}


def pytest_configure(config):
    xsdata_temp_dir.mkdir(parents=True, exist_ok=True)
    serializer = XmlSerializer()

    for name, items in bench_fixtures.items():
        result = serializer.render(
            Books(
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
                    for _ in range(items)
                ]
            )
        )

        fixture = xsdata_temp_dir.joinpath(f"benchmark_{name}.xml")
        fixture.write_text(result)
        stat = fixture.stat()
        bench_fixtures[name] = f"{stat.st_size / 1024:.2f} KB"


def pytest_unconfigure(config):
    temp_xsdata = Path(tempfile.gettempdir()).joinpath("xsdata")
    for tmp_file in temp_xsdata.glob("*"):
        tmp_file.unlink()

    temp_xsdata.rmdir()
