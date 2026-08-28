from typing import Any

from nested import count_lists, depth, find, flatten, total

DATA = [1, [2, [3, 4]], 5]


def test_total() -> None:
    assert total(DATA) == 15
    assert total([]) == 0
    assert total(7) == 7


def test_depth() -> None:
    assert depth(7) == 0
    assert depth([1, 2]) == 1
    assert depth(DATA) == 3
    assert depth([]) == 1


def test_flatten() -> None:
    assert flatten(DATA) == [1, 2, 3, 4, 5]
    assert flatten([]) == []
    assert flatten(7) == [7]


def test_count_lists() -> None:
    assert count_lists(DATA) == 3
    assert count_lists(7) == 0
    assert count_lists([]) == 1


def test_find() -> None:
    assert find(DATA, 1) == [0]
    assert find(DATA, 3) == [1, 1, 0]
    assert find(DATA, 5) == [2]
    assert find(DATA, 99) is None


def test_find_path_leads_to_the_value() -> None:
    path = find(DATA, 4)
    assert path == [1, 1, 1]

    place: Any = DATA
    for step in path:
        place = place[step]
    assert place == 4
