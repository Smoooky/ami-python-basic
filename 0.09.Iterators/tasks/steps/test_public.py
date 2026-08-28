import inspect

import pytest
from steps import averages, dedupe, runs, windows


def test_windows() -> None:
    assert list(windows([1, 2, 3, 4], 2)) == [(1, 2), (2, 3), (3, 4)]
    assert list(windows([1, 2, 3], 3)) == [(1, 2, 3)]
    assert list(windows([1, 2], 3)) == []
    assert list(windows([], 2)) == []


def test_windows_checks_the_size_right_away() -> None:
    with pytest.raises(ValueError):
        windows([1, 2, 3], 0)
    with pytest.raises(ValueError):
        windows([1, 2, 3], -1)


def test_averages() -> None:
    assert list(averages([0, 10, 20, 30], 2)) == [5.0, 15.0, 25.0]
    assert list(averages([2, 2, 2], 3)) == [2.0]
    assert list(averages([1], 2)) == []


def test_dedupe() -> None:
    assert list(dedupe([0, 0, 0, 5, 5, 0])) == [0, 5, 0]
    assert list(dedupe([1, 2, 3])) == [1, 2, 3]
    assert list(dedupe([])) == []


def test_runs() -> None:
    assert list(runs([0, 0, 0, 5, 5, 0])) == [(0, 3), (5, 2), (0, 1)]
    assert list(runs([7])) == [(7, 1)]
    assert list(runs([])) == []


def test_everything_is_a_generator() -> None:
    assert inspect.isgenerator(windows([1, 2], 2))
    assert inspect.isgenerator(dedupe([1]))
    assert inspect.isgenerator(runs([1]))
