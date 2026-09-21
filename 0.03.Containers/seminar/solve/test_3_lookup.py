from importlib import import_module

lookup = import_module("3_lookup")

SETTINGS: dict[str, int | None] = {"прокси": None, "порт": 8080, "таймаут": 0}


def test_fetch() -> None:
    assert lookup.fetch(SETTINGS, "порт") == (True, 8080)
    assert lookup.fetch(SETTINGS, "таймаут") == (True, 0)


def test_fetch_tells_a_none_value_from_a_missing_key() -> None:
    assert lookup.fetch(SETTINGS, "прокси") == (True, None)
    assert lookup.fetch(SETTINGS, "шрифт") == (False, None)


def test_picked() -> None:
    assert lookup.picked(SETTINGS, ["порт", "шрифт", "таймаут"]) == {"порт": 8080, "таймаут": 0}
    assert lookup.picked(SETTINGS, []) == {}
    assert lookup.picked(SETTINGS, ["шрифт"]) == {}


def test_picked_keeps_the_names_order() -> None:
    assert list(lookup.picked(SETTINGS, ["таймаут", "порт"])) == ["таймаут", "порт"]


def test_picked_drops_duplicate_names() -> None:
    assert lookup.picked(SETTINGS, ["порт", "порт"]) == {"порт": 8080}


def test_count_missing() -> None:
    assert lookup.count_missing(SETTINGS, ["шрифт", "порт", "цвет"]) == 2
    assert lookup.count_missing(SETTINGS, ["порт"]) == 0


def test_count_missing_counts_unique_names() -> None:
    assert lookup.count_missing(SETTINGS, ["шрифт", "шрифт"]) == 1


def test_first_unset() -> None:
    assert lookup.first_unset(SETTINGS, ["порт", "цвет", "шрифт"]) == "цвет"
    assert lookup.first_unset(SETTINGS, ["порт", "прокси"]) is None
    assert lookup.first_unset(SETTINGS, []) is None
