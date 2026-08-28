import inspect
from collections.abc import Iterator

from pipeline import Row, average, first, only, passing, scores

JOURNAL: list[Row] = [
    ("матан", 78),
    ("питон", 91),
    ("матан", 45),
    ("история", 60),
    ("матан", 88),
]


def test_only_and_scores() -> None:
    assert list(only(JOURNAL, "матан")) == [("матан", 78), ("матан", 45), ("матан", 88)]
    assert list(only(JOURNAL, "физра")) == []
    assert list(scores(JOURNAL)) == [78, 91, 45, 60, 88]


def test_passing_and_first() -> None:
    assert list(passing([78, 45, 88, 60], 60)) == [78, 88, 60]
    assert list(first([1, 2, 3, 4], 2)) == [1, 2]
    assert list(first([1, 2], 10)) == [1, 2]
    assert list(first([1, 2], 0)) == []


def test_the_whole_pipeline() -> None:
    assert sum(passing(scores(only(JOURNAL, "матан")), 60)) == 166
    assert round(average(scores(only(JOURNAL, "матан"))) or 0, 2) == 70.33


def test_average() -> None:
    assert average([2, 4]) == 3.0
    assert average([5]) == 5.0
    assert average([]) is None


def test_every_step_is_a_generator() -> None:
    assert inspect.isgenerator(only(JOURNAL, "матан"))
    assert inspect.isgenerator(scores(JOURNAL))
    assert inspect.isgenerator(passing([1, 2], 1))
    assert inspect.isgenerator(first([1, 2], 1))


def test_nothing_is_read_until_asked() -> None:
    read: list[int] = []

    def source() -> Iterator[Row]:
        for number in range(1000):
            read.append(number)
            yield ("матан", number)

    pipe = first(passing(scores(only(source(), "матан")), 10), 2)
    assert read == []
    assert list(pipe) == [10, 11]
    assert len(read) == 12
