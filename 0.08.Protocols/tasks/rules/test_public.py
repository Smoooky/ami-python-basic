from typing import Any

from rules import Longer, NoWords, accepted, broken_rules, is_rule


def not_empty(text: str) -> bool:
    return bool(text.strip())


def make_rules() -> list[Any]:
    return [
        not_empty,
        Longer(10),
        NoWords(["спам", "реклама"]),
        lambda text: not text.isupper(),
    ]


def test_rule_objects_behave_like_functions() -> None:
    assert Longer(10)("короткий") is False
    assert Longer(10)("вполне достаточной длины") is True
    assert NoWords(["спам"])("обычный текст") is True
    assert NoWords(["спам"])("Спамище повсюду") is False


def test_repr() -> None:
    assert repr(Longer(10)) == "Longer(10)"
    assert repr(NoWords(["спам"])) == "NoWords(['спам'])"


def test_broken_rules() -> None:
    checks = make_rules()
    assert broken_rules("Отличный разбор, спасибо!", checks) == []
    assert broken_rules("ок", checks) == [1]
    assert broken_rules("СПАМ СПАМ КУПИ ПРЯМО СЕЙЧАС", checks) == [2, 3]
    assert broken_rules("", checks) == [0, 1]


def test_accepted() -> None:
    checks = make_rules()
    texts = ["ок", "Отличный разбор, спасибо!", "спам-спам-спам-спам"]
    assert accepted(texts, checks) == ["Отличный разбор, спасибо!"]


def test_is_rule() -> None:
    assert is_rule(not_empty) is True
    assert is_rule(Longer(10)) is True
    assert is_rule(Longer) is True
    assert is_rule("Longer(10)") is False
    assert is_rule(42) is False
