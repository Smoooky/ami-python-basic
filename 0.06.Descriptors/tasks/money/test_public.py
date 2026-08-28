import pytest
from money import Money


def test_str_and_arithmetic() -> None:
    a = Money(10000, "RUB")
    b = Money(2550, "RUB")
    assert str(a) == "100.00 RUB"
    assert a + b == Money(12550, "RUB")
    assert a - b == Money(7450, "RUB")
    assert a == Money(10000, "RUB")


def test_currencies_do_not_mix() -> None:
    assert (Money(100, "RUB") == Money(100, "USD")) is False
    with pytest.raises(TypeError):
        Money(100, "RUB") + Money(100, "USD")


def test_multiplication_by_integer_only() -> None:
    assert Money(100, "USD") * 3 == Money(300, "USD")
    assert 3 * Money(100, "USD") == Money(300, "USD")
    with pytest.raises(TypeError):
        Money(100, "RUB") * 1.5
