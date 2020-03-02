from dataclasses import dataclass
from dataclasses import field
from typing import Dict
from typing import List
from typing import Optional


@dataclass
class AnyElement:
    qname: Optional[str] = field(default=None)
    text: Optional[str] = field(default=None)
    tail: Optional[str] = field(default=None)
    children: List[object] = field(default_factory=list)
    attributes: Dict[str, str] = field(
        default_factory=dict, metadata=dict(name="attributes", type="AnyAttribute")
    )
