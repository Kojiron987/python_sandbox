from collections.abc import Iterable
from dataclasses import dataclass
from decimal import Decimal

@dataclass
class Product:
    name: str


class PriceEngine:

    def calculate_discount(self, products: Iterable[Product]) -> Decimal:
        discount = Decimal(len(products) * 0.01)

        return min(discount, Decimal(0.2))

