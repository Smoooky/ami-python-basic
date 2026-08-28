import pytest
from leaderboard import Leaderboard, top, worst

SCORES = [2, 8, 5, 1, 6, 7]


def test_top_and_worst() -> None:
    assert top(SCORES, 3) == [8, 7, 6]
    assert worst(SCORES, 3) == [1, 2, 5]
    assert top(SCORES, 0) == []
    assert top(SCORES, 100) == sorted(SCORES, reverse=True)


def test_top_checks_the_count() -> None:
    with pytest.raises(ValueError):
        top(SCORES, -1)
    with pytest.raises(ValueError):
        worst(SCORES, -1)


def test_board_size_is_checked() -> None:
    with pytest.raises(ValueError):
        Leaderboard(0)


def test_board_keeps_only_the_best() -> None:
    board = Leaderboard(3)
    for score in SCORES:
        board.add(score)

    assert board.best() == [8, 7, 6]
    assert len(board) == 3
    assert board.cutoff() == 6


def test_add_reports_whether_the_score_made_it() -> None:
    board = Leaderboard(2)
    assert board.add(10) is True
    assert board.add(20) is True
    assert board.add(5) is False
    assert board.add(30) is True
    assert board.best() == [30, 20]


def test_empty_board() -> None:
    board = Leaderboard(3)
    assert board.best() == []
    assert len(board) == 0
    assert board.cutoff() is None
