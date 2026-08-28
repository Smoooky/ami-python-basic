import pytest
from guard import at_most, clamped, default_on_error


def test_at_most() -> None:
    @at_most(2)
    def submit(answer: str) -> str:
        """Сдать лабу."""
        return f"принято: {answer}"

    assert submit("раз") == "принято: раз"
    assert submit("два") == "принято: два"
    with pytest.raises(RuntimeError):
        submit("три")


def test_at_most_keeps_metadata_and_shows_the_rest() -> None:
    @at_most(3)
    def submit() -> None:
        """Сдать лабу."""

    assert submit.__name__ == "submit"
    assert submit.__doc__ == "Сдать лабу."
    assert submit.remaining == 3
    submit()
    assert submit.remaining == 2


def test_at_most_zero() -> None:
    @at_most(0)
    def never() -> int:
        return 1

    with pytest.raises(RuntimeError):
        never()


def test_default_on_error() -> None:
    @default_on_error(0, ValueError)
    def to_int(text: str) -> int:
        """Число из строки."""
        return int(text)

    assert to_int("42") == 42
    assert to_int("не число") == 0
    assert to_int.__name__ == "to_int"


def test_default_on_error_lets_other_errors_out() -> None:
    @default_on_error("нет", KeyError)
    def read(mapping: dict[str, str], key: str) -> str:
        return mapping[key]

    assert read({"а": "б"}, "а") == "б"
    assert read({}, "а") == "нет"
    with pytest.raises(TypeError):
        read(None, "а")


def test_clamped() -> None:
    @clamped(0, 100)
    def score(points: int) -> int:
        """Балл за работу."""
        return points

    assert score(50) == 50
    assert score(150) == 100
    assert score(-20) == 0
    assert score.__name__ == "score"


def test_arguments_are_checked_when_the_decorator_is_made() -> None:
    with pytest.raises(ValueError):
        at_most(-1)
    with pytest.raises(ValueError):
        default_on_error(0)
    with pytest.raises(ValueError):
        clamped(10, 5)
