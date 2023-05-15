import abc
from dataclasses import Field
from dataclasses import fields
from dataclasses import is_dataclass
from dataclasses import MISSING
from typing import Any
from typing import Dict
from typing import Optional
from typing import Set
from typing import Tuple
from typing import Type

from xsdata.exceptions import XmlContextError
from xsdata.formats.dataclass.models.generics import AnyElement
from xsdata.formats.dataclass.models.generics import DerivedElement
from xsdata.utils.hooks import load_entry_points


class ClassType(abc.ABC):
    __slots__ = ()

    @property
    @abc.abstractmethod
    def any_element(self) -> Type:
        """Return the any type used to bind wildcard element nodes."""

    @property
    @abc.abstractmethod
    def derived_element(self) -> Type:
        """Return the derived type used to bind ambiguous element nodes."""

    @property
    def any_keys(self) -> Set[str]:
        """Return the field names of the any type."""
        return {field.name for field in self.get_fields(self.any_element)}

    @property
    def derived_keys(self) -> Set[str]:
        """Return the field names of the derived type."""
        return {field.name for field in self.get_fields(self.derived_element)}

    @abc.abstractmethod
    def is_model(self, obj: Any) -> bool:
        """Return whether the given value is binding model."""

    @abc.abstractmethod
    def verify_model(self, obj: Any):
        """
        Verify the given value is a binding model.

        :raises xsdata.exceptions.XmlContextError: if not supported
        """

    @abc.abstractmethod
    def get_fields(self, obj: Any) -> Tuple[Any, ...]:
        """Return the models fields in the correct mro ordering."""

    @abc.abstractmethod
    def default_value(self, field: Any, default: Optional[Any] = None) -> Any:
        """Return the default value or factory of the given model field."""

    @abc.abstractmethod
    def default_choice_value(self, choice: Dict) -> Any:
        """Return the default value or factory of the given model field
        choice."""

    def score_object(self, obj: Any) -> float:
        """
        Score a binding model instance by its field values types.

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

    def is_model(self, obj: Any) -> bool:
        return is_dataclass(obj)

    def verify_model(self, obj: Any):
        if not self.is_model(obj):
            raise XmlContextError(f"Type '{obj}' is not a dataclass.")

    def get_fields(self, obj: Any) -> Tuple[Any, ...]:
        return fields(obj)

    def default_value(self, field: Field, default: Optional[Any] = None) -> Any:
        if field.default_factory is not MISSING:
            return field.default_factory

        if field.default is not MISSING:
            return field.default

        return default

    def default_choice_value(self, choice: Dict) -> Any:
        factory = choice.get("default_factory")
        if callable(factory):
            return factory

        return choice.get("default")


class_types = ClassTypes()
class_types.register("dataclasses", Dataclasses())

load_entry_points("xsdata.plugins.class_types")
