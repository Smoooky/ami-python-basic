from collections import deque

import pytest
from lineup import is_palindrome, last, serve, shift

PEOPLE = ["Аня", "Боря", "Вера", "Гоша"]


def test_shift() -> None:
    assert shift(PEOPLE, 1) == ["Гоша", "Аня", "Боря", "Вера"]
    assert shift(PEOPLE, -1) == ["Боря", "Вера", "Гоша", "Аня"]
    assert shift(PEOPLE, 0) == PEOPLE
    assert shift([], 3) == []


def test_serve() -> None:
    assert serve(["Аня", "Боря", "Вера"], 2) == ["Боря", "Аня", "Вера"]
    assert serve(PEOPLE, 1) == PEOPLE
    assert serve([], 2) == []


def test_serve_checks_the_step() -> None:
    with pytest.raises(ValueError):
        serve(PEOPLE, 0)
    with pytest.raises(ValueError):
        serve(PEOPLE, -1)


def test_last() -> None:
    tape = last(["а", "б", "в", "г"], 2)
    assert list(tape) == ["в", "г"]
    assert isinstance(tape, deque)
    assert tape.maxlen == 2

    assert list(last(["а"], 5)) == ["а"]
    assert list(last(["а", "б"], 0)) == []


def test_last_keeps_the_length_while_being_filled() -> None:
    tape = last(["а", "б"], 2)
    tape.append("в")
    assert list(tape) == ["б", "в"]


def test_is_palindrome() -> None:
    assert is_palindrome("шалаш") is True
    assert is_palindrome("А роза упала на лапу Азора") is True
    assert is_palindrome("привет") is False
    assert is_palindrome("") is True
