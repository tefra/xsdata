from typing import List

from xsdata.codegen.models import Class
from xsdata.formats.dataclass.models.generics import AnyElement


class ElementMapper:
    @classmethod
    def map(cls, element: AnyElement) -> List[Class]:
        return []
