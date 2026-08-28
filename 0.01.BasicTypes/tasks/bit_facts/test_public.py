from bit_facts import bit_facts


def test_even_number() -> None:
    assert bit_facts(10, 1) == (True, 20, 2)


def test_odd_number() -> None:
    assert bit_facts(7, 3) == (False, 56, 3)


def test_zero() -> None:
    assert bit_facts(0, 5) == (True, 0, 0)
