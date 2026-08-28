import pytest
from rounds import duty, numbered, padded, page

PEOPLE = ["Аня", "Боря", "Вера"]


def test_duty() -> None:
    assert duty(PEOPLE, 5) == ["Аня", "Боря", "Вера", "Аня", "Боря"]
    assert duty(PEOPLE, 3) == PEOPLE
    assert duty(PEOPLE, 0) == []
    assert duty([], 5) == []


def test_duty_checks_the_weeks() -> None:
    with pytest.raises(ValueError):
        duty(PEOPLE, -1)


def test_numbered() -> None:
    assert numbered(["а", "б", "в"]) == [(1, "а"), (2, "б"), (3, "в")]
    assert numbered(["а", "б"], 10) == [(10, "а"), (11, "б")]
    assert numbered(["а", "б", "в"], 0, 2) == [(0, "а"), (2, "б"), (4, "в")]
    assert numbered([]) == []


def test_padded() -> None:
    assert padded(["Аня", "Боря"], 5, "—") == ["Аня", "Боря", "—", "—", "—"]
    assert padded(["Аня", "Боря"], 2, "—") == ["Аня", "Боря"]
    assert padded(["Аня", "Боря", "Вера"], 2, "—") == ["Аня", "Боря"]
    assert padded([], 3, "—") == ["—", "—", "—"]


def test_page() -> None:
    items = ["а", "б", "в", "г", "д"]
    assert page(items, 1, 2) == ["а", "б"]
    assert page(items, 2, 2) == ["в", "г"]
    assert page(items, 3, 2) == ["д"]
    assert page(items, 4, 2) == []


def test_page_checks_its_arguments() -> None:
    with pytest.raises(ValueError):
        page(["а"], 0, 2)
    with pytest.raises(ValueError):
        page(["а"], 1, 0)
