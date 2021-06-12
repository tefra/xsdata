import abc
from dataclasses import fields
from dataclasses import is_dataclass
from dataclasses import MISSING
from typing import Any
from typing import Dict
from typing import Set
from typing import Tuple
from typing import Type

from xsdata.formats.dataclass.models.generics import AnyElement
from xsdata.formats.dataclass.models.generics import DerivedElement


class ClassType(abc.ABC):

    __slots__ = ()

    @property
    @abc.abstractmethod
    def any_element(self) -> Type:
        pass

    @property
    @abc.abstractmethod
    def derived_element(self) -> Type:
        pass

    @property
    def any_keys(self) -> Set[str]:
        return {field.name for field in self.get_fields(self.any_element)}

    @property
    def derived_keys(self) -> Set[str]:
        return {field.name for field in self.get_fields(self.derived_element)}

    @abc.abstractmethod
    def is_model(self, obj: Type) -> bool:
        pass

    @abc.abstractmethod
    def get_fields(self, obj: Type) -> Tuple[Any, ...]:
        pass

    @abc.abstractmethod
    def default_value(self, field: Any) -> Any:
        pass

    def score_object(self, obj: Any) -> float:
        """
        Score a dataclass instance by the field values types.

        Weights:
            1. None: 0
            2. str: 1
            3. *: 1.5
        """

        if not obj:
            return -1.0

        def score(value: Any) -> float:
            if isinstance(value, str):
                return 1.0

            if value is not None:
                return 1.5

            return 0.0

        if self.is_model(obj):
            return sum(score(getattr(obj, var.name)) for var in self.get_fields(obj))

        return score(obj)


class ClassTypes:
    __slots__ = "types"

    def __init__(self):
        self.types: Dict[str, ClassType] = {}

    def register(self, name: str, fmt: ClassType, **_: Any):
        self.types[name] = fmt

    def get_type(self, name: str) -> ClassType:
        return self.types[name]


class Dataclasses(ClassType):

    __slots__ = ()

    @property
    def any_element(self) -> Type:
        return AnyElement

    @property
    def derived_element(self) -> Type:
        return DerivedElement

    def is_model(self, obj: Type) -> bool:
        return is_dataclass(obj)

    def get_fields(self, obj: Type) -> Tuple[Any, ...]:
        return fields(obj)

    def default_value(self, field: Any) -> Any:
        if field.default_factory is not MISSING:  # type: ignore
            return field.default_factory  # type: ignore

        if field.default is not MISSING:
            return field.default

        return None


class_types = ClassTypes()
class_types.register("dataclasses", Dataclasses())
