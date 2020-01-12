from dataclasses import dataclass, field


@dataclass
class Product:
    """
    :ivar name:
    :ivar size:
    """
    class Meta:
        name = "product"

    name: str = field(
        default="N/A",
        metadata=dict(
            name="name",
            type="Element"
        )
    )
    size: int = field(
        default=12,
        metadata=dict(
            name="size",
            type="Element"
        )
    )
