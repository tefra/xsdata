from dataclasses import asdict
from typing import Callable, Dict, List, Tuple


class DictSerializer:
    def render(self, obj: object, dict_factory: Callable = dict) -> Dict:
        return asdict(obj, dict_factory=dict_factory)

    @staticmethod
    def filter(data: List[Tuple], filter: Callable):
        return dict((key, value) for key, value in data if filter(value))

    @staticmethod
    def filter_none(data):
        return DictSerializer.filter(data, filter=lambda x: x is not None)
