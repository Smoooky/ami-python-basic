from checks import all_even, any_starts_with, has_negative, is_sorted, no_blanks


def test_has_negative() -> None:
    assert has_negative([1, -2, 3]) is True
    assert has_negative([1, 2, 3]) is False
    assert has_negative([0]) is False
    assert has_negative([]) is False


def test_all_even() -> None:
    assert all_even([2, 4, 6]) is True
    assert all_even([2, 3]) is False
    assert all_even([0]) is True


def test_all_even_on_an_empty_list() -> None:
    # Ни одного нечётного не нашлось, значит утверждение верно.
    assert all_even([]) is True


def test_any_starts_with() -> None:
    assert any_starts_with(["кот", "пёс"], "к") is True
    assert any_starts_with(["кот", "пёс"], "с") is False
    assert any_starts_with([], "к") is False
    assert any_starts_with(["кот"], "") is True


def test_is_sorted() -> None:
    assert is_sorted([1, 2, 3]) is True
    assert is_sorted([1, 1, 2]) is True
    assert is_sorted([3, 1, 2]) is False
    assert is_sorted([2, 1]) is False


def test_is_sorted_on_short_lists() -> None:
    assert is_sorted([]) is True
    assert is_sorted([5]) is True


def test_no_blanks() -> None:
    assert no_blanks(["раз", "два"]) is True
    assert no_blanks(["раз", ""]) is False
    assert no_blanks(["раз", "   "]) is False
    assert no_blanks([]) is True
