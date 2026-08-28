import pytest
from layers import apply, checked, doubled, logged


def test_logged() -> None:
    log: list[str] = []

    @logged(log)
    def score(points: int, bonus: int = 0) -> int:
        """Балл за задачу."""
        return points + bonus

    assert score(5) == 5
    assert score(5, bonus=2) == 7
    assert log == [
        "→ score(5)",
        "← score = 5",
        "→ score(5, bonus=2)",
        "← score = 7",
    ]
    assert score.__name__ == "score"
    assert score.__doc__ == "Балл за задачу."


def test_doubled_and_checked() -> None:
    @doubled
    def score(points: int) -> int:
        return points

    @checked
    def strict(points: int) -> int:
        return points

    assert score(5) == 10
    assert strict(5) == 5
    with pytest.raises(ValueError):
        strict(-1)


def test_order_changes_what_gets_logged() -> None:
    above: list[str] = []
    below: list[str] = []

    @logged(above)
    @doubled
    def first(points: int) -> int:
        return points

    @doubled
    @logged(below)
    def second(points: int) -> int:
        return points

    assert first(5) == 10
    assert second(5) == 10
    assert above == ["→ first(5)", "← first = 10"]
    assert below == ["→ second(5)", "← second = 5"]


def test_apply_matches_the_at_notation() -> None:
    log: list[str] = []

    def score(points: int) -> int:
        return points

    stacked = apply([logged(log), doubled], score)
    assert stacked(5) == 10
    assert log == ["→ score(5)", "← score = 10"]
    assert apply([], score)(5) == 5


def test_failed_call_is_logged_and_let_out() -> None:
    log: list[str] = []

    @logged(log)
    @checked
    def score(points: int) -> int:
        return points

    with pytest.raises(ValueError):
        score(-1)
    assert log == ["→ score(-1)", "× score: ValueError"]
