from collections import Counter

from letters import can_build, is_anagram, letter_counts, missing, top


def test_letter_counts() -> None:
    assert letter_counts("абракадабра") == Counter({"а": 5, "б": 2, "р": 2, "к": 1, "д": 1})
    assert letter_counts("") == Counter()


def test_letter_counts_ignores_case_and_punctuation() -> None:
    assert letter_counts("Ало, Алё!") == letter_counts("алоалё")
    assert letter_counts("а б\tв\n") == Counter({"а": 1, "б": 1, "в": 1})
    assert letter_counts("123 ...") == Counter()


def test_top() -> None:
    assert top("абракадабра", 2) == [("а", 5), ("б", 2)]
    assert top("абракадабра", 0) == []
    assert len(top("абракадабра", 100)) == 5


def test_is_anagram() -> None:
    assert is_anagram("апельсин", "спаниель") is True
    assert is_anagram("Ток", "кот") is True
    assert is_anagram("кот", "код") is False
    assert is_anagram("", "") is True


def test_can_build() -> None:
    assert can_build("кот", "тыкво") is True
    assert can_build("кот", "кто") is True
    assert can_build("коток", "кот") is False
    assert can_build("", "что угодно") is True


def test_missing() -> None:
    assert missing("коток", "кот") == Counter({"к": 1, "о": 1})
    assert missing("кот", "тыкво") == Counter()
    assert missing("кот", "") == Counter({"к": 1, "о": 1, "т": 1})
