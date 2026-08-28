import pytest
from recent import Recent


def filled() -> Recent:
    chats = Recent(3)
    chats.put("Аня", "привет")
    chats.put("Боря", "ты где")
    chats.put("Вера", "скинь конспект")
    return chats


def test_capacity_is_checked() -> None:
    with pytest.raises(ValueError):
        Recent(0)
    with pytest.raises(ValueError):
        Recent(-2)


def test_keys_go_from_the_oldest_to_the_newest() -> None:
    chats = filled()
    assert chats.keys() == ["Аня", "Боря", "Вера"]
    assert len(chats) == 3


def test_the_oldest_is_pushed_out() -> None:
    chats = filled()
    assert chats.put("Гоша", "го в столовую") == "Аня"
    assert chats.keys() == ["Боря", "Вера", "Гоша"]
    assert "Аня" not in chats


def test_get_moves_the_key_to_the_end() -> None:
    chats = filled()
    assert chats.get("Аня") == "привет"
    assert chats.keys() == ["Боря", "Вера", "Аня"]
    assert chats.put("Гоша", "го") == "Боря"


def test_get_of_a_missing_key() -> None:
    chats = filled()
    assert chats.get("Дима") is None
    assert chats.get("Дима", "нет такого") == "нет такого"
    assert chats.keys() == ["Аня", "Боря", "Вера"]


def test_membership_is_not_an_access() -> None:
    chats = filled()
    assert "Аня" in chats
    assert len(chats) == 3
    assert chats.keys() == ["Аня", "Боря", "Вера"]


def test_put_of_a_known_key_updates_and_promotes() -> None:
    chats = filled()
    assert chats.put("Аня", "уже иду") is None
    assert chats.get("Аня") == "уже иду"
    assert chats.keys() == ["Боря", "Вера", "Аня"]
    assert len(chats) == 3


def test_forget() -> None:
    chats = filled()
    chats.forget("Боря")
    assert chats.keys() == ["Аня", "Вера"]
    with pytest.raises(KeyError):
        chats.forget("Боря")
