from unique_sorted import unique_sorted


def test_with_duplicates() -> None:
    assert unique_sorted([3, 1, 2, 3, 1]) == [1, 2, 3]


def test_single() -> None:
    assert unique_sorted([5]) == [5]


def test_empty() -> None:
    assert unique_sorted([]) == []
