from dataclasses import fields
from dataclasses import is_dataclass
from dataclasses import MISSING
from typing import Any
from typing import Tuple
from typing import Type

from xsdata.formats.dataclass.models.generics import AnyElement
from xsdata.formats.dataclass.models.generics import DerivedElement


class CrossCompat:
    any_element: Type = AnyElement
    derived_element: Type = DerivedElement

    any_keys = {"qname", "text", "tail", "children", "attributes"}
    derived_keys = {"qname", "value", "type"}

    @classmethod
    def is_model(cls, obj: Any) -> bool:
        return is_dataclass(obj)

    @classmethod
    def get_fields(cls, obj: Any) -> Tuple[Any, ...]:
        return fields(obj)

    @classmethod
    def default_value(cls, field: Any) -> Any:
        if field.default_factory is not MISSING:  # type: ignore
            return field.default_factory  # type: ignore

        if field.default is not MISSING:
            return field.default

        return None

    @classmethod
    def score_object(cls, obj: Any) -> float:
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

        if cls.is_model(obj):
            return sum(score(getattr(obj, var.name)) for var in cls.get_fields(obj))

        return score(obj)


cross_compat = CrossCompat()
