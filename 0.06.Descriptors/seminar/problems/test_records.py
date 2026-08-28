from records import Measurement, distinct, in_order, latest


def test_latest() -> None:
    rows = [Measurement(1, 10), Measurement(5, 3), Measurement(2, 99)]
    assert latest(rows) == Measurement(5, 3)


def test_latest_on_an_empty_list() -> None:
    assert latest([]) is None


def test_latest_on_a_single_row() -> None:
    assert latest([Measurement(7, 0)]) == Measurement(7, 0)


def test_distinct() -> None:
    # Датакласс с frozen хешируем, поэтому множество схлопнет одинаковые.
    assert distinct([Measurement(1, 10), Measurement(1, 10), Measurement(2, 0)]) == 2
    assert distinct([]) == 0


def test_distinct_counts_by_value_not_by_object() -> None:
    assert distinct([Measurement(1, 1), Measurement(1, 1)]) == 1


def test_in_order() -> None:
    rows = [Measurement(5, 3), Measurement(1, 10)]
    assert in_order(rows) == [Measurement(1, 10), Measurement(5, 3)]


def test_in_order_does_not_touch_the_source() -> None:
    rows = [Measurement(5, 3), Measurement(1, 10)]
    in_order(rows)
    assert rows == [Measurement(5, 3), Measurement(1, 10)]


def test_in_order_compares_by_moment_first() -> None:
    rows = [Measurement(2, 0), Measurement(1, 999)]
    assert in_order(rows)[0] == Measurement(1, 999)


def test_in_order_on_an_empty_list() -> None:
    assert in_order([]) == []
