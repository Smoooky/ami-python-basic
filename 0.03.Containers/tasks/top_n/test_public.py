from top_n import top_n


def test_by_count() -> None:
    assert top_n({"a": 3, "b": 1, "c": 2}, 2) == [("a", 3), ("c", 2)]


def test_tie_is_broken_alphabetically() -> None:
    assert top_n({"b": 2, "a": 2}, 2) == [("a", 2), ("b", 2)]


def test_empty() -> None:
    assert top_n({}, 3) == []
