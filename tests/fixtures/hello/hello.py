from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://hello/"


@dataclass
class HelloByeError:
    class Meta:
        namespace = "http://hello/"

    message: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )


@dataclass
class HelloError1:
    class Meta:
        name = "HelloError"

    message: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
