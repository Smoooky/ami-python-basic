import pytest
from pointer import escape, exists, parse, pointers, resolve, set_value, unescape

DOCUMENT: dict[str, object] = {
    "название": "Отчёт",
    "авторы": [{"имя": "Иванов", "теги": []}, {"имя": "Петрова", "теги": ["физика"]}],
    "страниц": 12,
    "": "пустой ключ",
    "a/b": "косая черта",
    "c~d": "тильда",
}


def test_escape() -> None:
    assert escape("имя") == "имя"
    assert escape("a/b") == "a~1b"
    assert escape("c~d") == "c~0d"
    assert escape("~1") == "~01"


def test_unescape() -> None:
    assert unescape("имя") == "имя"
    assert unescape("a~1b") == "a/b"
    assert unescape("c~0d") == "c~d"
    assert unescape("~01") == "~1"


def test_escape_and_unescape_are_inverse() -> None:
    for token in ["", "имя", "a/b", "c~d", "~1", "~0", "//~~", "0"]:
        assert unescape(escape(token)) == token


def test_parse() -> None:
    assert parse("") == []
    assert parse("/") == [""]
    assert parse("/авторы/0/имя") == ["авторы", "0", "имя"]
    assert parse("/a~1b") == ["a/b"]


def test_parse_rejects_bad_pointer() -> None:
    with pytest.raises(ValueError):
        parse("авторы")
    with pytest.raises(ValueError):
        parse("/a~2b")


def test_resolve() -> None:
    assert resolve(DOCUMENT, "") is DOCUMENT
    assert resolve(DOCUMENT, "/название") == "Отчёт"
    assert resolve(DOCUMENT, "/авторы/1/имя") == "Петрова"
    assert resolve(DOCUMENT, "/") == "пустой ключ"
    assert resolve(DOCUMENT, "/a~1b") == "косая черта"
    assert resolve(DOCUMENT, "/c~0d") == "тильда"


def test_resolve_reports_absence_and_nonsense_differently() -> None:
    with pytest.raises(KeyError):
        resolve(DOCUMENT, "/нет")
    with pytest.raises(KeyError):
        resolve(DOCUMENT, "/авторы/9")
    with pytest.raises(ValueError):
        resolve(DOCUMENT, "/авторы/01")
    with pytest.raises(ValueError):
        resolve(DOCUMENT, "/авторы/-")
    with pytest.raises(ValueError):
        resolve(DOCUMENT, "/страниц/0")


def test_exists() -> None:
    assert exists(DOCUMENT, "") is True
    assert exists(DOCUMENT, "/авторы/0/имя") is True
    assert exists(DOCUMENT, "/авторы/9/имя") is False
    assert exists(DOCUMENT, "/страниц/0") is False


def test_exists_still_raises_on_broken_pointer() -> None:
    with pytest.raises(ValueError):
        exists(DOCUMENT, "авторы")


def test_set_value_does_not_touch_the_original() -> None:
    changed = set_value(DOCUMENT, "/авторы/0/имя", "Сидоров")
    assert resolve(changed, "/авторы/0/имя") == "Сидоров"
    assert resolve(DOCUMENT, "/авторы/0/имя") == "Иванов"


def test_set_value_adds_a_key_but_not_an_index() -> None:
    changed = set_value(DOCUMENT, "/новый", 1)
    assert resolve(changed, "/новый") == 1
    with pytest.raises(KeyError):
        set_value(DOCUMENT, "/авторы/9", 1)
    with pytest.raises(ValueError):
        set_value(DOCUMENT, "", 1)


def test_pointers() -> None:
    assert pointers({"a": [1]}) == ["", "/a", "/a/0"]
    assert pointers(7) == [""]
    assert pointers({"a/b": 1}) == ["", "/a~1b"]


def test_every_pointer_resolves() -> None:
    for pointer in pointers(DOCUMENT):
        assert exists(DOCUMENT, pointer)
