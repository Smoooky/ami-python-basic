import pytest
from memo import Memo


def test_key_tells_positional_from_keyword() -> None:
    assert Memo.key(1, 2) != Memo.key(1, b=2)
    assert Memo.key(1, 2) == Memo.key(1, 2)
    assert Memo.key(a=1, b=2) == Memo.key(b=2, a=1)
    assert Memo.key() == Memo.key()


def test_result_is_computed_once() -> None:
    calls: list[int] = []

    @Memo()
    def square(number: int) -> int:
        """Квадрат числа."""
        calls.append(number)
        return number * number

    assert square(4) == 16
    assert square(4) == 16
    assert calls == [4]
    assert square.hits == 1
    assert square.misses == 1


def test_metadata_is_kept() -> None:
    @Memo()
    def square(number: int) -> int:
        """Квадрат числа."""
        return number * number

    assert square.__name__ == "square"
    assert square.__doc__ == "Квадрат числа."


def test_different_arguments_are_different_entries() -> None:
    @Memo()
    def square(number: int) -> int:
        return number * number

    assert [square(number) for number in (1, 2, 1, 3)] == [1, 4, 1, 9]
    assert square.misses == 3
    assert square.hits == 1
    assert square.cache_size() == 3


def test_cache_clear() -> None:
    @Memo()
    def square(number: int) -> int:
        return number * number

    square(2)
    square(2)
    square.cache_clear()
    assert square.cache_size() == 0
    assert square.hits == 0
    assert square.misses == 0


def test_size_limits_the_cache() -> None:
    calls: list[int] = []

    @Memo(size=2)
    def square(number: int) -> int:
        calls.append(number)
        return number * number

    square(1)
    square(2)
    square(3)
    assert square.cache_size() == 2
    square(1)
    assert calls == [1, 2, 3, 1]


def test_size_is_checked() -> None:
    with pytest.raises(ValueError):
        Memo(size=0)
    with pytest.raises(ValueError):
        Memo(size=-3)
