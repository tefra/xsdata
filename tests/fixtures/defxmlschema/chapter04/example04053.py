from dataclasses import dataclass


@dataclass
class OrderDetails:
    class Meta:
        name = "orderDetails"
        namespace = "http://datypic.com/ord"
