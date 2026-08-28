from cleanup import cut_long, dedup_adjacent, flatten, without_negatives


def test_without_negatives() -> None:
    assert without_negatives([1, -2, 3]) == [1, 3]
    assert without_negatives([0, -1]) == [0]
    assert without_negatives([]) == []
    assert without_negatives([-1, -2]) == []


def test_without_negatives_does_not_touch_the_argument() -> None:
    numbers = [1, -2, 3]
    without_negatives(numbers)
    assert numbers == [1, -2, 3]


def test_dedup_adjacent() -> None:
    assert dedup_adjacent([1, 1, 2, 1]) == [1, 2, 1]
    assert dedup_adjacent([5, 5, 5]) == [5]
    assert dedup_adjacent([1, 2, 3]) == [1, 2, 3]


def test_dedup_adjacent_on_short_lists() -> None:
    assert dedup_adjacent([]) == []
    assert dedup_adjacent([7]) == [7]


def test_dedup_adjacent_does_not_touch_the_argument() -> None:
    numbers = [1, 1, 2]
    dedup_adjacent(numbers)
    assert numbers == [1, 1, 2]


def test_flatten() -> None:
    assert flatten([[1, 2], [3], [4, 5]]) == [1, 2, 3, 4, 5]
    assert flatten([[1], [2]]) == [1, 2]
    assert flatten([]) == []


def test_flatten_skips_empty_rows() -> None:
    assert flatten([[], [1], []]) == [1]
    assert flatten([[], []]) == []


def test_cut_long() -> None:
    assert cut_long(["короткое", "длинное"], 4) == ["коро", "длин"]
    assert cut_long(["да", "нет"], 4) == ["да", "нет"]
    assert cut_long([], 3) == []


def test_cut_long_by_zero() -> None:
    assert cut_long(["слово"], 0) == [""]
