from copies import deep, is_independent, shallow


def test_shallow_copies_the_outer_list() -> None:
    rows = [[1, 2], [3]]
    result = shallow(rows)
    assert result == [[1, 2], [3]]
    assert result is not rows


def test_shallow_shares_the_rows() -> None:
    rows = [[1, 2], [3]]
    result = shallow(rows)
    assert result[0] is rows[0]
    result[0].append(9)
    assert rows[0] == [1, 2, 9]


def test_shallow_of_an_empty_table() -> None:
    assert shallow([]) == []


def test_deep_copies_everything() -> None:
    rows = [[1, 2], [3]]
    result = deep(rows)
    assert result == [[1, 2], [3]]
    assert result is not rows
    assert result[0] is not rows[0]


def test_deep_change_does_not_reach_the_source() -> None:
    rows = [[1, 2], [3]]
    result = deep(rows)
    result[0].append(9)
    assert rows == [[1, 2], [3]]


def test_deep_of_an_empty_table() -> None:
    assert deep([]) == []


def test_is_independent() -> None:
    rows = [[1, 2], [3]]
    assert is_independent(rows, deep(rows)) is True
    assert is_independent(rows, shallow(rows)) is False


def test_is_independent_compares_objects_not_values() -> None:
    assert is_independent([[1, 2]], [[1, 2]]) is True


def test_is_independent_with_an_empty_table() -> None:
    assert is_independent([], [[1]]) is True
    assert is_independent([], []) is True
