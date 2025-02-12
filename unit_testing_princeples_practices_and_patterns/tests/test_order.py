from app.price import Product, Order

def test_adding_a_product_to_an_order():
    # 状態テスト例
    product = Product("Hand wash")
    sut = Order()

    sut.add_product(product)

    assert 1 == len(sut.products)
    assert product == sut.products[0]
