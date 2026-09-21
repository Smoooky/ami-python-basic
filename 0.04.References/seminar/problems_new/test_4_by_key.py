from importlib import import_module

by_key = import_module("4_by_key")


def test_by_length_then_alpha() -> None:
    words = ["як", "кот", "а", "аб"]

    assert by_key.by_length_then_alpha(words) == ["а", "аб", "як", "кот"]


def test_by_length_then_alpha_returns_a_new_list() -> None:
    words = ["б", "а"]

    assert by_key.by_length_then_alpha(words) is not words
    assert words == ["б", "а"]


def test_by_grade_desc() -> None:
    pairs = [("анна", 3), ("борис", 5), ("вера", 4)]

    assert by_key.by_grade_desc(pairs) == [("борис", 5), ("вера", 4), ("анна", 3)]


def test_best_word() -> None:
    assert by_key.best_word(["як", "кот", "аб"], key=len) == "кот"


def test_best_word_first_wins_ties() -> None:
    assert by_key.best_word(["аб", "як"], key=len) == "аб"


def test_ranked() -> None:
    words = ["а", "як", "аб"]

    ranked = by_key.ranked(words, key=len)

    assert ranked == ["як", "аб", "а"]
    assert ranked is not words
    assert words == ["а", "як", "аб"]
