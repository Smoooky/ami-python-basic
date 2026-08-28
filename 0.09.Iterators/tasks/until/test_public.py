import io
from collections.abc import Callable
from typing import Any

import pytest
from until import collect, first_hit, read_chunks


def rolls(values: list[Any]) -> Callable[[], Any]:
    """Кубик с заранее известными бросками."""
    source = iter(values)
    return lambda: next(source)


def test_collect_stops_before_the_sentinel() -> None:
    assert collect(rolls([3, 5, 2, 6, 4]), 6) == [3, 5, 2]
    assert collect(rolls([6, 1, 2]), 6) == []
    assert collect(rolls([1, 2, 3, 6]), 6) == [1, 2, 3]


def test_read_chunks() -> None:
    text = io.StringIO("абвгдеж")
    assert read_chunks(text.read, 3) == ["абв", "где", "ж"]

    assert read_chunks(io.StringIO("").read, 3) == []
    assert read_chunks(io.StringIO("абвгд").read, 5) == ["абвгд"]


def test_read_chunks_checks_the_size() -> None:
    with pytest.raises(ValueError):
        read_chunks(io.StringIO("абв").read, 0)
    with pytest.raises(ValueError):
        read_chunks(io.StringIO("абв").read, -2)


def test_first_hit() -> None:
    assert first_hit(rolls([3, 5, 1, 6]), 6, 1) == 3
    assert first_hit(rolls([3, 5, 6, 1]), 6, 1) is None
    assert first_hit(rolls([1, 2, 3, 6]), 6, 1) == 1
    assert first_hit(rolls([6]), 6, 6) is None
