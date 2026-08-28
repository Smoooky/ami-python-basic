from text_wrap import text_wrap


def test_example() -> None:
    assert text_wrap("один два три четыре", 9) == ["один два", "три", "четыре"]


def test_fits_in_one_line() -> None:
    assert text_wrap("a b c", 5) == ["a b c"]


def test_empty_text() -> None:
    assert text_wrap("", 10) == []
