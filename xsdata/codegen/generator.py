from abc import ABC, abstractmethod
from pathlib import Path
from typing import Iterator, List, Tuple

from xsdata.models.codegen import Class
from xsdata.models.elements import Schema


class AbstractGenerator(ABC):
    @abstractmethod
    def render(
        self, schema: Schema, classes: List[Class], package: str
    ) -> Iterator[Tuple[Path, str]]:
        pass

    @abstractmethod
    def print(
        self, schema: Schema, classes: List[Class], package: str
    ) -> Iterator[Tuple[str, Class]]:
        pass
