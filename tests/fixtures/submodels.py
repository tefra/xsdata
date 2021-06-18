from dataclasses import dataclass
from dataclasses import field
from typing import Dict
from typing import List
from typing import Optional
from typing import Union
from xml.etree.ElementTree import QName

from tests.fixtures.models import ChoiceType


@dataclass
class ChoiceTypeChild(ChoiceType):
    pass