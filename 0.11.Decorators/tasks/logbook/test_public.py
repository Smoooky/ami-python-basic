from typing import Any

import pytest
from logbook import describe, traced


def add(a: int, b: int = 0) -> int:
    """Складывает два числа."""
    return a + b


def make_add() -> Any:
    return traced(add)


def test_describe() -> None:
    assert describe(1, 2) == "1, 2"
    assert describe("текст") == "'текст'"
    assert describe(1, b=2) == "1, b=2"
    assert describe(b=2, c="три") == "b=2, c='три'"
    assert describe() == ""


def test_metadata_is_kept() -> None:
    traced_add = make_add()
    assert traced_add.__name__ == "add"
    assert traced_add.__doc__ == "Складывает два числа."


def test_the_function_still_works() -> None:
    traced_add = make_add()
    assert traced_add(1, 2) == 3
    assert traced_add(5) == 5
    assert traced_add(1, b=2) == 3


def test_calls_are_counted() -> None:
    traced_add = make_add()
    assert traced_add.calls == 0
    traced_add(1, 2)
    traced_add(3, 4)
    assert traced_add.calls == 2


def test_history() -> None:
    traced_add = make_add()
    traced_add(1, 2)
    traced_add(5)
    traced_add(1, b=2)
    assert traced_add.history == [
        "add(1, 2) -> 3",
        "add(5) -> 5",
        "add(1, b=2) -> 3",
    ]


def test_reset() -> None:
    traced_add = make_add()
    traced_add(1, 2)
    traced_add.reset()
    assert traced_add.calls == 0
    assert traced_add.history == []


def test_errors_are_recorded_and_let_out() -> None:
    traced_add = make_add()
    with pytest.raises(TypeError):
        traced_add(1, "два")
    assert traced_add.calls == 1
    assert traced_add.history == ["add(1, 'два') -> TypeError"]


def test_the_at_sign_works_too() -> None:
    @traced
    def greet(name: str) -> str:
        """Здоровается."""
        return f"привет, {name}"

    assert greet("Аня") == "привет, Аня"
    assert greet.__name__ == "greet"
    assert greet.history == ["greet('Аня') -> 'привет, Аня'"]
