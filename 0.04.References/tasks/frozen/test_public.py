from typing import Any

from frozen import freeze, is_frozen, mutable_parts, thaw


def test_is_frozen_on_simple_values() -> None:
    assert is_frozen(42) is True
    assert is_frozen("текст") is True
    assert is_frozen(None) is True
    assert is_frozen([1, 2]) is False
    assert is_frozen({"a": 1}) is False


def test_a_tuple_is_frozen_only_if_everything_inside_is() -> None:
    assert is_frozen((1, 2, 3)) is True
    assert is_frozen((1, (2, 3))) is True
    assert is_frozen((1, 2, [3, 4])) is False


def test_mutable_parts_finds_the_hole_in_a_tuple() -> None:
    assert mutable_parts((1, 2, [3, 4])) == [(2,)]
    assert mutable_parts((1, 2, 3)) == []
    assert mutable_parts((1, (2, [3]))) == [(1, 1)]


def test_mutable_parts_of_a_mutable_value_itself() -> None:
    assert mutable_parts([1, 2]) == [()]
    assert mutable_parts({"a": 1}) == [()]


def test_freeze() -> None:
    assert freeze([1, [2, 3]]) == (1, (2, 3))
    assert is_frozen(freeze([1, [2, 3]])) is True
    assert freeze(42) == 42


def test_thaw() -> None:
    assert thaw((1, (2, 3))) == [1, [2, 3]]
    assert thaw(42) == 42


def test_freeze_and_thaw_are_opposites() -> None:
    data: Any = [1, [2, [3, 4]], 5]
    assert thaw(freeze(data)) == data
