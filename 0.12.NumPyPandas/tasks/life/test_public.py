import numpy as np
import pytest
from life import from_text, neighbours, run, step, to_text

BLINKER = [
    ".....",
    ".....",
    ".###.",
    ".....",
    ".....",
]
BLOCK = [
    "....",
    ".##.",
    ".##.",
    "....",
]


def test_from_text_and_back() -> None:
    board = from_text(BLINKER)
    assert board.dtype == np.bool_
    assert board.shape == (5, 5)
    assert to_text(board) == BLINKER


def test_from_text_checks_its_input() -> None:
    with pytest.raises(ValueError):
        from_text([])
    with pytest.raises(ValueError):
        from_text(["##", "#"])
    with pytest.raises(ValueError):
        from_text(["#x"])


def test_neighbours() -> None:
    counts = neighbours(from_text(BLINKER))
    assert counts.shape == (5, 5)
    assert counts[2, 2] == 2
    assert counts[1, 2] == 3
    assert counts[0, 0] == 0


def test_blinker_blinks() -> None:
    board = from_text(BLINKER)
    assert to_text(step(board)) == [
        ".....",
        "..#..",
        "..#..",
        "..#..",
        ".....",
    ]
    assert to_text(run(board, 2)) == BLINKER


def test_block_is_still() -> None:
    board = from_text(BLOCK)
    assert to_text(step(board)) == BLOCK
    assert to_text(run(board, 10)) == BLOCK


def test_empty_field_stays_empty() -> None:
    board = from_text(["...", "..."])
    assert not step(board).any()


def test_run_zero_steps() -> None:
    board = from_text(BLINKER)
    assert to_text(run(board, 0)) == BLINKER
    with pytest.raises(ValueError):
        run(board, -1)


def test_glider_moves_diagonally() -> None:
    field: list[str] = [
        ".#........",
        "..#.......",
        "###.......",
    ] + ["." * 10] * 7

    moved = to_text(run(from_text(field), 4))
    expected: list[str] = (
        ["." * 10]
        + [
            "..#.......",
            "...#......",
            ".###......",
        ]
        + ["." * 10] * 6
    )
    assert moved == expected
