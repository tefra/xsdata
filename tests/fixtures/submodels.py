from dataclasses import dataclass

from tests.fixtures.models import ChoiceType


@dataclass
class ChoiceTypeChild(ChoiceType):
    pass
