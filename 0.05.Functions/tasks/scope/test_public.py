import scope
from scope import add, extend_copy, extend_in_place, rebind, reset


def test_add_remembers_between_calls() -> None:
    reset()
    assert add(3) == 3
    assert add(4) == 7
    assert scope.total == 7


def test_reset() -> None:
    reset()
    add(10)
    reset()
    assert scope.total == 0
    assert add(1) == 1


def test_extend_in_place_changes_the_callers_list() -> None:
    reset()
    values = [1, 2]
    extend_in_place(values, [3])
    assert values == [1, 2, 3]


def test_rebind_does_not_change_the_callers_list() -> None:
    values = [1, 2]
    result = rebind(values, [3])

    assert result == [1, 2, 3]
    assert values == [1, 2]


def test_extend_copy_returns_a_new_list() -> None:
    values = [1, 2]
    result = extend_copy(values, [3])

    assert result == [1, 2, 3]
    assert values == [1, 2]
    assert result is not values
