from collections import defaultdict

import pytest
from groups import by_club, known, plain, tally

SIGNUPS = [
    ("Аня", "робототехника"),
    ("Боря", "театр"),
    ("Вера", "робототехника"),
    ("Гоша", "театр"),
    ("Аня", "театр"),
]


def test_by_club() -> None:
    clubs = by_club(SIGNUPS)
    assert clubs == {
        "робототехника": ["Аня", "Вера"],
        "театр": ["Боря", "Гоша", "Аня"],
    }
    assert isinstance(clubs, defaultdict)


def test_by_club_gives_an_empty_list_for_a_new_club() -> None:
    clubs = by_club(SIGNUPS)
    assert clubs["вязание"] == []
    clubs["вязание"].append("Дима")
    assert clubs["вязание"] == ["Дима"]
    assert clubs["робототехника"] == ["Аня", "Вера"]


def test_tally() -> None:
    counts = tally(["яблоко", "банан", "яблоко"])
    assert counts == {"яблоко": 2, "банан": 1}
    assert isinstance(counts, defaultdict)
    assert counts["груша"] == 0


def test_known_does_not_create_anything() -> None:
    counts = tally(["яблоко"])
    assert known(counts, "яблоко") is True
    assert known(counts, "груша") is False
    assert len(counts) == 1


def test_plain() -> None:
    counts = tally(["яблоко"])
    result = plain(counts)
    assert result == {"яблоко": 1}
    assert type(result) is dict
    with pytest.raises(KeyError):
        result["груша"]
