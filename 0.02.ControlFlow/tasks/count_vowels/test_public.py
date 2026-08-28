from count_vowels import count_vowels


def test_latin() -> None:
    assert count_vowels("hello") == 2


def test_cyrillic() -> None:
    assert count_vowels("Привет") == 2


def test_no_vowels() -> None:
    assert count_vowels("XYZ") == 0
