from dataclasses import dataclass
from typing import Optional
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from tests.models.typemapping.street import Street


@dataclass
class House:
    class Meta:
        global_type = False

    number: int
    street: Optional["Street"] = None
