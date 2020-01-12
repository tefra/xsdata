from dataclasses import dataclass, field


@dataclass
class Size:
    """
    :ivar dim:
    """
    class Meta:
        name = "size"

    dim: int = field(
        default=1,
        metadata=dict(
            name="dim",
            type="Attribute"
        )
    )
