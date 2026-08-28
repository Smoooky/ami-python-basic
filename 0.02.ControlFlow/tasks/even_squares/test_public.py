from even_squares import even_squares


def test_ten() -> None:
    assert even_squares(10) == [0, 4, 16, 36, 64]


def test_one() -> None:
    assert even_squares(1) == [0]


def test_zero_is_empty() -> None:
    assert even_squares(0) == []
