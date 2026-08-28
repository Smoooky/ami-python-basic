from typing import Any

from aliases import describe, distinct_objects, same_object, same_value, shared_positions


def test_assignment_does_not_copy() -> None:
    cookie: dict[str, Any] = {"name": "Cookie", "size": "small"}
    brownie = cookie

    assert same_object(cookie, brownie) is True
    assert same_value(cookie, brownie) is True

    cookie["age"] = 3
    assert brownie["age"] == 3


def test_the_imposter() -> None:
    cookie: dict[str, Any] = {"name": "Cookie", "size": "small"}
    imposter: dict[str, Any] = {"name": "Cookie", "size": "small"}

    assert same_value(cookie, imposter) is True
    assert same_object(cookie, imposter) is False


def test_describe() -> None:
    original = [1, 2, 3]
    alias = original
    twin = [1, 2, 3]
    other = [9]

    assert describe(original, alias) == "один и тот же объект"
    assert describe(original, twin) == "равны, но это разные объекты"
    assert describe(original, other) == "разные"


def test_shared_positions() -> None:
    shared = [10, 20]
    left = [shared, [1], "текст"]
    right = [shared, [1], "текст"]

    assert shared_positions(left, right) == [0, 2]


def test_distinct_objects() -> None:
    row = [0, 0]
    assert distinct_objects([row, row, row]) == 1
    assert distinct_objects([[0, 0], [0, 0], [0, 0]]) == 3
    assert distinct_objects([]) == 0
