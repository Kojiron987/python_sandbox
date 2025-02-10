from decimal import Decimal

from app.price import Product, PriceEngine

def test_discount_of_two_products():
    p1 = Product("Hand wash")
    p2 = Product("Shampoo")

    sut = PriceEngine()

    discount = sut.calculate_discount((
        p1, p2))

    assert discount == Decimal(0.02)
