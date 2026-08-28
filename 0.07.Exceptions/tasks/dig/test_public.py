from typing import Any

from dig import dig, flatten, has_path

RESPONSE: dict[str, Any] = {
    "user": {"name": "Алиса", "address": {"city": "Москва"}},
    "items": [{"title": "книга", "price": 500}, {"title": "ручка"}],
    "note": None,
}


def test_reaches_nested_values() -> None:
    assert dig(RESPONSE, ["user", "name"]) == "Алиса"
    assert dig(RESPONSE, ["user", "address", "city"]) == "Москва"
    assert dig(RESPONSE, ["items", 0, "price"]) == 500
    assert dig(RESPONSE, ["items", -1, "title"]) == "ручка"
    assert dig(RESPONSE, []) is RESPONSE


def test_missing_pieces_give_the_default() -> None:
    assert dig(RESPONSE, ["user", "phone"]) is None
    assert dig(RESPONSE, ["items", 99, "title"]) is None
    assert dig(RESPONSE, ["user", "name", "first"]) is None
    assert dig(RESPONSE, ["user", "phone"], default="—") == "—"


def test_has_path_sees_the_difference_between_none_and_missing() -> None:
    assert has_path(RESPONSE, ["note"]) is True
    assert has_path(RESPONSE, ["missing"]) is False
    assert has_path(RESPONSE, ["items", 1, "price"]) is False


def test_flatten() -> None:
    assert flatten(
        RESPONSE,
        {
            "имя": ["user", "name"],
            "город": ["user", "address", "city"],
            "телефон": ["user", "phone"],
            "заметка": ["note"],
        },
    ) == {"имя": "Алиса", "город": "Москва", "заметка": None}
