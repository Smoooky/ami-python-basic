from typing import Any

import pytest
from settings import muted, section, temporary


def test_temporary_puts_the_value_back() -> None:
    config: dict[str, Any] = {"режим": "обычный", "порт": 80}

    with temporary(config, "порт", 8080) as draft:
        assert draft is config
        assert config["порт"] == 8080

    assert config == {"режим": "обычный", "порт": 80}


def test_temporary_removes_a_key_that_was_not_there() -> None:
    config: dict[str, Any] = {"режим": "обычный"}

    with temporary(config, "отладка", True):
        assert config["отладка"] is True

    assert config == {"режим": "обычный"}


def test_temporary_puts_the_value_back_after_an_error() -> None:
    config: dict[str, Any] = {"порт": 80}

    with pytest.raises(ValueError), temporary(config, "порт", 8080):
        raise ValueError("что-то пошло не так")

    assert config == {"порт": 80}


def test_section_writes_both_lines() -> None:
    log: list[str] = []

    with section(log, "загрузка"):
        log.append("работаем")

    assert log == ["начало: загрузка", "работаем", "конец: загрузка"]


def test_section_writes_the_end_after_an_error() -> None:
    log: list[str] = []

    with pytest.raises(RuntimeError), section(log, "загрузка"):
        raise RuntimeError("упало")

    assert log == ["начало: загрузка", "конец: загрузка"]


def test_muted_swallows_the_listed_errors() -> None:
    with muted(ValueError) as caught:
        raise ValueError("не страшно")

    assert len(caught) == 1
    assert isinstance(caught[0], ValueError)
    assert str(caught[0]) == "не страшно"


def test_muted_lets_other_errors_out() -> None:
    with pytest.raises(TypeError), muted(ValueError):
        raise TypeError("а вот это страшно")


def test_muted_on_a_quiet_block() -> None:
    with muted(ValueError) as caught:
        pass

    assert caught == []
