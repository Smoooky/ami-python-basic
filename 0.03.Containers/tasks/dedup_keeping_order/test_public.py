from dedup_keeping_order import dedup_keeping_order


def test_keeps_first_occurrence() -> None:
    assert dedup_keeping_order(["b", "a", "b", "c"]) == ["b", "a", "c"]


def test_all_equal() -> None:
    assert dedup_keeping_order(["a", "a", "a"]) == ["a"]


def test_empty() -> None:
    assert dedup_keeping_order([]) == []
