from dataclasses import dataclass
from dataclasses import field
from typing import List
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from tests.models.typemapping.street import Street


@dataclass
class City:
    class Meta:
        global_type = False

    name: str
    streets: List["Street"] = field(default_factory=list)
