import pytest
from counter import make_adder, make_counter, make_multiplier, multipliers, shared_counter


def test_make_counter() -> None:
    step = make_counter()
    assert step() == 1
    assert step() == 2
    assert step() == 3


def test_make_counter_starts_where_asked() -> None:
    step = make_counter(10)
    assert step() == 11
    assert step() == 12


def test_counters_are_independent() -> None:
    first = make_counter()
    second = make_counter()
    assert first() == 1
    assert first() == 2
    assert second() == 1


def test_make_adder() -> None:
    add_two = make_adder(2)
    add_five = make_adder(5)
    assert add_two(7) == 9
    assert add_five(10) == 15
    assert add_two(7) == 9


def test_make_multiplier() -> None:
    assert make_multiplier(3)(4) == 12
    assert make_multiplier(0)(4) == 0


def test_multipliers_each_have_their_own_number() -> None:
    funcs = multipliers(4)
    assert [func(10) for func in funcs] == [0, 10, 20, 30]
    assert multipliers(0) == []


def test_shared_counter_shares_one_number() -> None:
    funcs = shared_counter(3)
    assert funcs[0]() == 1
    assert funcs[1]() == 2
    assert funcs[2]() == 3
    assert funcs[0]() == 4


def test_arguments_are_checked() -> None:
    with pytest.raises(ValueError):
        multipliers(-1)
    with pytest.raises(ValueError):
        shared_counter(-1)
