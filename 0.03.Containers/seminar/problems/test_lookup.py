from lookup import first_present, is_set, missing, value_or

SETTINGS: dict[str, int | None] = {"прокси": None, "порт": 8080, "таймаут": 0}


def test_is_set() -> None:
    assert is_set(SETTINGS, "порт") is True
    assert is_set(SETTINGS, "шрифт") is False


def test_is_set_counts_a_none_value_as_set() -> None:
    assert is_set(SETTINGS, "прокси") is True


def test_value_or() -> None:
    assert value_or(SETTINGS, "порт", 80) == 8080
    assert value_or(SETTINGS, "шрифт", 12) == 12


def test_value_or_keeps_a_none_value() -> None:
    assert value_or(SETTINGS, "прокси", 3128) is None


def test_value_or_keeps_a_zero() -> None:
    assert value_or(SETTINGS, "таймаут", 30) == 0


def test_first_present() -> None:
    assert first_present(SETTINGS, ["шрифт", "порт"], 80) == 8080
    assert first_present(SETTINGS, ["шрифт", "цвет"], 80) == 80
    assert first_present(SETTINGS, [], 80) == 80


def test_first_present_stops_at_a_none_value() -> None:
    assert first_present(SETTINGS, ["прокси", "порт"], 80) is None


def test_missing() -> None:
    assert missing(SETTINGS, ["шрифт", "порт", "цвет"]) == ["цвет", "шрифт"]
    assert missing(SETTINGS, ["порт"]) == []
    assert missing(SETTINGS, []) == []


def test_missing_drops_duplicates() -> None:
    assert missing(SETTINGS, ["шрифт", "шрифт"]) == ["шрифт"]
