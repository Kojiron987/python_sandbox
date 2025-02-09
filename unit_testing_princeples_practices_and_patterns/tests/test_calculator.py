from app.calculator import Calculator

def test_sum():
    calculator = Calculator()

    assert 4 == calculator.sum(3, 1)
