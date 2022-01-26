import sys
from typing import Any
from typing import Dict
from typing import Sequence
from typing import Tuple

EMPTY_MAP: Dict = {}
EMPTY_SEQUENCE: Sequence = []
EMPTY_TUPLE: Tuple = ()

XML_FALSE = sys.intern("false")
XML_TRUE = sys.intern("true")
DEFAULT_ATTR_NAME = "value"


def return_true(*_: Any) -> bool:
    """A dummy function that always returns true."""
    return True


def return_input(obj: Any) -> Any:
    """A dummy function that always returns input."""
    return obj
