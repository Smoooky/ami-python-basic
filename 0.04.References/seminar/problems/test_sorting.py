from sorting import reverse_in_place, reversed_copy, sort_in_place, sorted_copy


def test_sort_in_place() -> None:
    values = [3, 1, 2]
    sort_in_place(values)
    assert values == [1, 2, 3]


def test_sort_in_place_keeps_the_object() -> None:
    values = [3, 1, 2]
    alias = values
    sort_in_place(values)
    assert alias is values
    assert alias == [1, 2, 3]


def test_sort_in_place_on_an_empty_list() -> None:
    values: list[int] = []
    sort_in_place(values)
    assert values == []


def test_sorted_copy() -> None:
    assert sorted_copy([3, 1, 2]) == [1, 2, 3]
    assert sorted_copy([]) == []


def test_sorted_copy_does_not_touch_the_source() -> None:
    values = [3, 1, 2]
    result = sorted_copy(values)
    assert values == [3, 1, 2]
    assert result is not values


def test_reverse_in_place() -> None:
    values = [1, 2, 3]
    reverse_in_place(values)
    assert values == [3, 2, 1]


def test_reverse_in_place_keeps_the_object() -> None:
    values = [1, 2, 3]
    alias = values
    reverse_in_place(values)
    assert alias is values
    assert alias == [3, 2, 1]


def test_reversed_copy() -> None:
    assert reversed_copy([1, 2, 3]) == [3, 2, 1]
    assert reversed_copy([]) == []


def test_reversed_copy_does_not_touch_the_source() -> None:
    values = [1, 2, 3]
    result = reversed_copy(values)
    assert values == [1, 2, 3]
    assert result is not values
