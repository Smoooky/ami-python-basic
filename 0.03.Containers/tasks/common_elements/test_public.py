from common_elements import common_elements


def test_overlap() -> None:
    assert common_elements([1, 2, 3], [2, 3, 4]) == [2, 3]


def test_no_overlap() -> None:
    assert common_elements([1, 2], [3, 4]) == []


def test_empty() -> None:
    assert common_elements([], [1]) == []
