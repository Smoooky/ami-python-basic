from inplace import drop_odd, extend_in_place, extended, replace_contents


def test_extend_in_place() -> None:
    values = [1, 2]
    extend_in_place(values, [3, 4])
    assert values == [1, 2, 3, 4]


def test_extend_in_place_keeps_the_object() -> None:
    values = [1]
    alias = values
    extend_in_place(values, [2])
    assert alias is values
    assert alias == [1, 2]


def test_extend_in_place_with_nothing_to_add() -> None:
    values = [1]
    extend_in_place(values, [])
    assert values == [1]


def test_extended() -> None:
    assert extended([1], [2, 3]) == [1, 2, 3]
    assert extended([], []) == []


def test_extended_does_not_touch_the_source() -> None:
    source = [1, 2]
    result = extended(source, [3])
    assert source == [1, 2]
    assert result is not source


def test_replace_contents() -> None:
    values = [1, 2, 3]
    replace_contents(values, [9])
    assert values == [9]


def test_replace_contents_keeps_the_object() -> None:
    values = [1, 2, 3]
    alias = values
    replace_contents(values, [7, 8])
    assert alias is values
    assert alias == [7, 8]


def test_replace_contents_with_an_empty_list() -> None:
    values = [1, 2]
    replace_contents(values, [])
    assert values == []


def test_drop_odd() -> None:
    values = [1, 2, 3, 4]
    drop_odd(values)
    assert values == [2, 4]


def test_drop_odd_keeps_the_object() -> None:
    values = [1, 2, 3]
    alias = values
    drop_odd(values)
    assert alias is values
    assert alias == [2]


def test_drop_odd_when_nothing_is_left() -> None:
    values = [1, 3]
    drop_odd(values)
    assert values == []
