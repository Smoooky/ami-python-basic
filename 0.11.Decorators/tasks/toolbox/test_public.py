import pytest
from toolbox import Registry, first_line, once


def filled() -> Registry:
    commands = Registry()

    @commands.register("привет", summary="Поздороваться")
    def greet(name: str) -> str:
        return f"привет, {name}"

    @commands.register("сумма")
    def total(*numbers: int) -> int:
        """Сложить числа.

        Складывает всё, что дали.
        """
        return sum(numbers)

    return commands


def test_first_line() -> None:
    assert first_line("Одна строка") == "Одна строка"
    assert first_line("  Первая\n\n  Вторая  ") == "Первая"
    assert first_line(None) == ""
    assert first_line("") == ""


def test_register_leaves_the_function_alone() -> None:
    commands = Registry()

    @commands.register("привет")
    def greet(name: str) -> str:
        """Поздороваться."""
        return f"привет, {name}"

    assert greet("Аня") == "привет, Аня"
    assert greet.__name__ == "greet"
    assert "привет" in commands


def test_run() -> None:
    commands = filled()
    assert commands.run("привет", "Аня") == "привет, Аня"
    assert commands.run("сумма", 1, 2, 3) == 6
    with pytest.raises(KeyError):
        commands.run("нет такой")


def test_names_and_len() -> None:
    commands = filled()
    assert commands.names() == ["привет", "сумма"]
    assert len(commands) == 2
    assert "сумма" in commands
    assert "нет" not in commands


def test_summary_falls_back_to_the_docstring() -> None:
    commands = filled()
    assert commands.summary("привет") == "Поздороваться"
    assert commands.summary("сумма") == "Сложить числа."
    with pytest.raises(KeyError):
        commands.summary("нет такой")


def test_help() -> None:
    assert filled().help() == "привет — Поздороваться\nсумма — Сложить числа."


def test_duplicate_and_empty_names() -> None:
    commands = filled()
    with pytest.raises(ValueError):
        commands.register("привет")
    with pytest.raises(ValueError):
        commands.register("   ")


def test_once() -> None:
    calls: list[int] = []

    @once
    def setup() -> str:
        """Подготовка."""
        calls.append(1)
        return "готово"

    assert setup() == "готово"
    assert setup() == "готово"
    assert calls == [1]
    assert setup.called is True
    assert setup.__name__ == "setup"

    setup.reset()
    assert setup.called is False
    assert setup() == "готово"
    assert calls == [1, 1]
