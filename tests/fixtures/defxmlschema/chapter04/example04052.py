from dataclasses import dataclass


@dataclass
class OrderSummary:
    class Meta:
        name = "orderSummary"
        namespace = "http://datypic.com/ord"
