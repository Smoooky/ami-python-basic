from collections import abc

import pytest
from route import Route


def test_creation_and_cleanup() -> None:
    route = Route(["  Москва ", "Тверь"])
    assert list(route) == ["Москва", "Тверь"]
    assert len(route) == 2
    assert repr(route) == "Route(['Москва', 'Тверь'])"


def test_empty_stop_is_rejected() -> None:
    with pytest.raises(ValueError):
        Route(["Москва", "   "])
    with pytest.raises(ValueError):
        Route().append("")


def test_free_methods_work() -> None:
    route = Route(["Москва", "Тверь"])

    route.append("  Новгород  ")
    assert route[-1] == "Новгород"

    route.insert(1, "Клин")
    assert list(route) == ["Москва", "Клин", "Тверь", "Новгород"]

    assert "Тверь" in route
    assert route.index("Тверь") == 2
    assert route.count("Москва") == 1
    assert list(reversed(route)) == ["Новгород", "Тверь", "Клин", "Москва"]

    route[0] = " Химки "
    assert route[0] == "Химки"
    del route[0]
    assert route.pop() == "Новгород"
    route.remove("Клин")
    assert list(route) == ["Тверь"]


def test_it_is_a_real_sequence_now() -> None:
    route = Route(["Москва"])
    assert isinstance(route, abc.Sequence)
    assert isinstance(route, abc.MutableSequence)
    assert isinstance(route, abc.Iterable)
