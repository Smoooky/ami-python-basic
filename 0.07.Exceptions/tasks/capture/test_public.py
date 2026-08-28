import sys

import pytest
from capture import Captured


def print_report(rows: list[tuple[str, int]]) -> None:
    print("Отчёт")
    for name, count in rows:
        print(f"{name}: {count}")


def test_captures_text_and_lines() -> None:
    with Captured() as out:
        print_report([("книги", 3), ("ручки", 12)])

    assert out.text == "Отчёт\nкниги: 3\nручки: 12\n"
    assert out.lines == ["Отчёт", "книги: 3", "ручки: 12"]


def test_empty_block() -> None:
    with Captured() as out:
        pass

    assert out.text == ""
    assert out.lines == []


def test_stdout_is_restored_after_an_error() -> None:
    before = sys.stdout
    out = Captured()

    with pytest.raises(ValueError), out:
        print("успело напечататься")
        raise ValueError("а тут всё сломалось")

    assert sys.stdout is before
    assert out.lines == ["успело напечататься"]


def test_nested_blocks() -> None:
    with Captured() as outer:
        print("наружное")
        with Captured() as inner:
            print("внутреннее")
        print("снова наружное")

    assert inner.lines == ["внутреннее"]
    assert outer.lines == ["наружное", "снова наружное"]
