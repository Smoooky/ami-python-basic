import numpy as np
import pytest
from sudoku import Grid, blocks, columns, has_repeats, is_complete, is_valid, mistakes, rows

SOLVED: Grid = np.array(
    [
        [5, 3, 4, 6, 7, 8, 9, 1, 2],
        [6, 7, 2, 1, 9, 5, 3, 4, 8],
        [1, 9, 8, 3, 4, 2, 5, 6, 7],
        [8, 5, 9, 7, 6, 1, 4, 2, 3],
        [4, 2, 6, 8, 5, 3, 7, 9, 1],
        [7, 1, 3, 9, 2, 4, 8, 5, 6],
        [9, 6, 1, 5, 3, 7, 2, 8, 4],
        [2, 8, 7, 4, 1, 9, 6, 3, 5],
        [3, 4, 5, 2, 8, 6, 1, 7, 9],
    ],
    dtype=np.int8,
)


def test_rows_and_columns() -> None:
    assert np.array_equal(rows(SOLVED), SOLVED)
    assert columns(SOLVED)[0].tolist() == [5, 6, 1, 8, 4, 7, 9, 2, 3]
    assert columns(SOLVED).shape == (9, 9)


def test_blocks() -> None:
    result = blocks(SOLVED)
    assert result.shape == (9, 9)
    assert result[0].tolist() == [5, 3, 4, 6, 7, 2, 1, 9, 8]
    assert result[1].tolist() == [6, 7, 8, 1, 9, 5, 3, 4, 2]
    assert result[8].tolist() == [2, 8, 4, 6, 3, 5, 1, 7, 9]


def test_has_repeats() -> None:
    full = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9], dtype=np.int8)
    twice = np.array([1, 1, 3, 4, 5, 6, 7, 8, 9], dtype=np.int8)
    empty = np.zeros(9, dtype=np.int8)

    assert has_repeats(full) is False
    assert has_repeats(twice) is True
    assert has_repeats(empty) is False


def test_solved_grid() -> None:
    assert is_complete(SOLVED)
    assert mistakes(SOLVED) == []
    assert is_valid(SOLVED)


def test_a_grid_with_a_mistake() -> None:
    broken = SOLVED.copy()
    broken[0, 0] = 3
    assert mistakes(broken) == ["строка 1", "столбец 1", "блок 1"]
    assert not is_valid(broken)


def test_an_unfinished_grid() -> None:
    unfinished = SOLVED.copy()
    unfinished[4, 4] = 0
    assert not is_complete(unfinished)
    assert mistakes(unfinished) == []
    assert not is_valid(unfinished)


def test_bad_grids_are_rejected() -> None:
    with pytest.raises(ValueError):
        rows(np.zeros((3, 3), dtype=np.int8))
    with pytest.raises(ValueError):
        rows(np.full((9, 9), 10, dtype=np.int8))
