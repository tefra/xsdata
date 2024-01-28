from dataclasses import dataclass, field
from typing import TYPE_CHECKING, List, Optional

if TYPE_CHECKING:
    from tests.fixtures.typemapping.city import City
    from tests.fixtures.typemapping.house import House


@dataclass
class Street:
    class Meta:
        global_type = False

    name: str
    city: Optional["City"] = None
    houses: List["House"] = field(default_factory=list)
