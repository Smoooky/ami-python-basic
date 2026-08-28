from typing import Any

from board import Note, Pinnable, broken_pins, pin_all, render


class Schedule:
    """Чужой класс: про Pinnable ничего не знает, а подходит."""

    def title(self) -> str:
        return "расписание"

    def lines(self) -> list[str]:
        return ["9:00 матан", "10:40 питон"]


class Sticker:
    """Притворщик: имена на месте, но это поля, а не методы."""

    title = "распродажа"
    lines = ["всё по рублю"]


def test_note() -> None:
    note = Note("домашка", "прочитать главу 3\n\n  сдать лабу  ")
    assert note.title() == "домашка"
    assert note.lines() == ["прочитать главу 3", "сдать лабу"]


def test_render() -> None:
    assert render(Note("домашка", "глава 3")) == "домашка\n- глава 3"
    assert render(Note("пусто", "")) == "пусто"


def test_protocol_needs_no_inheritance() -> None:
    assert Pinnable not in Note.__mro__
    assert isinstance(Note("а", "б"), Pinnable) is True
    assert isinstance(Schedule(), Pinnable) is True
    assert isinstance(42, Pinnable) is False


def test_pin_all_keeps_only_the_suitable() -> None:
    items: list[Any] = [Note("домашка", "глава 3"), 42, "строка", Schedule()]
    assert pin_all(items) == [
        "домашка\n- глава 3",
        "расписание\n- 9:00 матан\n- 10:40 питон",
    ]


def test_broken_pins_finds_the_pretender() -> None:
    items: list[Any] = [Note("а", "б"), Sticker(), 42]
    assert isinstance(Sticker(), Pinnable) is True
    assert broken_pins(items) == [1]
