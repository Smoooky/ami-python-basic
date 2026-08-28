import pytest
from vocabulary import Vocabulary


def test_normalize() -> None:
    assert Vocabulary.normalize("  Apple  ") == "apple"
    assert Vocabulary.normalize("APPLE") == "apple"


def test_lookup_ignores_case_and_spaces() -> None:
    words = Vocabulary({"Apple": "яблоко", "  BOOK ": "  книга  "})
    assert words["apple"] == "яблоко"
    assert words["APPLE"] == "яблоко"
    assert words["book"] == "книга"
    assert list(words) == ["apple", "book"]
    assert repr(words) == "Vocabulary({'apple': 'яблоко', 'book': 'книга'})"


def test_free_methods_work() -> None:
    words = Vocabulary({"Apple": "яблоко", "book": "книга"})

    assert "APPLE" in words
    assert words.get("nope", "не знаю") == "не знаю"
    assert words.pop("Apple") == "яблоко"
    assert len(words) == 1

    words.update({"Cat": "кот", "DOG": "собака"})
    assert sorted(words.keys()) == ["book", "cat", "dog"]

    assert words.setdefault("cat", "кошка") == "кот"
    assert words["CAT"] == "кот"


def test_equality_and_errors() -> None:
    assert Vocabulary({"a": "1"}) == Vocabulary({"A": "1"})

    words = Vocabulary()
    with pytest.raises(ValueError):
        words[""] = "перевод"
    with pytest.raises(KeyError):
        _ = words["нет такого"]
