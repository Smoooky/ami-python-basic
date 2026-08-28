from orders import has_pair_with_sum, repeated, unique_ordered


def test_unique_ordered() -> None:
    assert unique_ordered(["б", "а", "б", "в"]) == ["б", "а", "в"]
    assert unique_ordered(["а", "а", "а"]) == ["а"]
    assert unique_ordered([]) == []


def test_unique_ordered_does_not_sort() -> None:
    assert unique_ordered(["я", "б", "а"]) == ["я", "б", "а"]


def test_repeated() -> None:
    assert repeated(["б", "а", "б", "в", "а"]) == ["а", "б"]
    assert repeated(["а", "б"]) == []
    assert repeated([]) == []


def test_repeated_counts_a_value_once() -> None:
    assert repeated(["а", "а", "а"]) == ["а"]


def test_has_pair_with_sum() -> None:
    assert has_pair_with_sum([1, 2, 3], 5) is True
    assert has_pair_with_sum([1, 2, 3], 7) is False
    assert has_pair_with_sum([], 0) is False


def test_has_pair_with_sum_needs_two_elements() -> None:
    # Одно число дважды использовать нельзя.
    assert has_pair_with_sum([3], 6) is False
    assert has_pair_with_sum([3, 3], 6) is True


def test_has_pair_with_sum_on_negatives_and_zero() -> None:
    assert has_pair_with_sum([-2, 5, 2], 0) is True
    assert has_pair_with_sum([0, 0], 0) is True
    assert has_pair_with_sum([0, 1], 0) is False
