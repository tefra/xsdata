from typing import Any
from typing import Dict
from typing import Sequence

EMPTY_MAP: Dict = {}
EMPTY_SEQUENCE: Sequence = []


def return_true(*_: Any) -> bool:
    """A dummy function that always returns true."""
    return True


def return_input(obj: Any) -> Any:
    """A dummy function that always returns input."""
    return obj


class DateFormat:
    DATE = "%Y-%m-%d%z"
    TIME = "%H:%M:%S%z"
    DATE_TIME = "%Y-%m-%dT%H:%M:%S%z"
    G_DAY = "---%d%z"
    G_MONTH = "--%m%z"
    G_MONTH_DAY = "--%m-%d%z"
    G_YEAR = "%Y%z"
    G_YEAR_MONTH = "%Y-%m%z"
