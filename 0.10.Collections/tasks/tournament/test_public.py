import pytest
from tournament import Match, missing, podium, schedule, standings

PLAYERS = ["Аня", "Боря", "Вера"]
PLAYED = [
    Match("Аня", "Боря", "Аня"),
    Match("Аня", "Вера", None),
]


def test_match_is_a_named_tuple() -> None:
    match = Match("Аня", "Боря", "Аня")
    assert match.left == "Аня"
    assert match.winner == "Аня"
    assert repr(match) == "Match(left='Аня', right='Боря', winner='Аня')"
    assert standings(["Аня", "Боря"], [match]) == {"Аня": 3, "Боря": 0}
    assert match == ("Аня", "Боря", "Аня")


def test_schedule() -> None:
    assert schedule(PLAYERS) == [
        ("Аня", "Боря"),
        ("Аня", "Вера"),
        ("Боря", "Вера"),
    ]
    assert schedule(["Аня"]) == []
    assert schedule([]) == []


def test_missing() -> None:
    assert missing(PLAYERS, PLAYED) == [("Боря", "Вера")]
    assert missing(PLAYERS, []) == schedule(PLAYERS)


def test_missing_ignores_the_order_inside_a_pair() -> None:
    played = [Match("Боря", "Аня", None)]
    assert ("Аня", "Боря") not in missing(PLAYERS, played)


def test_standings() -> None:
    assert standings(PLAYERS, PLAYED) == {"Аня": 4, "Боря": 0, "Вера": 1}
    assert standings(PLAYERS, []) == {"Аня": 0, "Боря": 0, "Вера": 0}


def test_podium() -> None:
    assert podium(PLAYERS, PLAYED, 2) == [("Аня", 4), ("Вера", 1)]
    assert podium(PLAYERS, PLAYED, 100) == [("Аня", 4), ("Вера", 1), ("Боря", 0)]
    assert podium(PLAYERS, PLAYED, 0) == []


def test_bad_matches_are_rejected() -> None:
    with pytest.raises(ValueError):
        standings(PLAYERS, [Match("Аня", "Боря", "Вера")])
    with pytest.raises(ValueError):
        standings(PLAYERS, [Match("Аня", "Дима", None)])
