from dataclasses import dataclass, field
from enum import Enum
from typing import Any, Callable, Dict, Iterator, Optional, Tuple

from xsdata.formats.converter import converter
from xsdata.formats.dataclass.context import XmlContext
from xsdata.formats.dataclass.models.elements import XmlVar
from xsdata.formats.dataclass.serializers.config import SerializerConfig
from xsdata.utils import collections


def filter_none(x: Tuple) -> Dict:
    """Convert a key-value pairs to dict, ignoring None values.

    Args:
        x: Key-value pairs

    Returns:
        The filtered dictionary.
    """
    return {k: v for k, v in x if v is not None}


class DictFactory:
    """Dictionary factory types."""

    FILTER_NONE = filter_none


@dataclass
class DictEncoder:
    """Json serializer for data classes.

    Args:
        config: The serializer config instance
        context: The models context instance
        dict_factory: Dictionary factory
    """

    config: SerializerConfig = field(default_factory=SerializerConfig)
    context: XmlContext = field(default_factory=XmlContext)
    dict_factory: Callable = field(default=dict)

    def encode(self, value: Any, var: Optional[XmlVar] = None) -> Any:
        """Convert a value to a dictionary object.

        Args:
            value: The input value
            var: The xml var instance

        Returns:
            The converted json serializable value.
        """
        if var is None or self.context.class_type.is_model(value):
            if collections.is_array(value):
                return list(map(self.encode, value))

            return self.dict_factory(self.next_value(value))

        if collections.is_array(value):
            return type(value)(self.encode(val, var) for val in value)

        if isinstance(value, (dict, int, float, str, bool)):
            return value

        if isinstance(value, Enum):
            return self.encode(value.value, var)

        return converter.serialize(value, format=var.format)

    def next_value(self, obj: Any) -> Iterator[Tuple[str, Any]]:
        """Fetch the next value of a model instance to convert.

        Args:
            obj: The input model instance

        Yields:
            An iterator of field name and value tuples.
        """
        ignore_optionals = self.config.ignore_default_attributes
        meta = self.context.build(obj.__class__, globalns=self.config.globalns)

        for var in meta.get_all_vars():
            value = getattr(obj, var.name)
            if (
                not var.is_attribute
                or not ignore_optionals
                or not var.is_optional(value)
            ):
                yield var.local_name, self.encode(value, var)
