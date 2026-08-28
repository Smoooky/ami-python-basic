from rectangle import rectangle


def test_integers() -> None:
    assert rectangle(2, 3) == (6, 10)


def test_square() -> None:
    assert rectangle(1, 1) == (1, 4)


def test_returns_tuple_of_two() -> None:
    result = rectangle(2, 3)
    assert isinstance(result, tuple)
    assert len(result) == 2
